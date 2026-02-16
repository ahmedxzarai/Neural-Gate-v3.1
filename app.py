
# ---------------------------------------------------------------------------
# Project: 🛡️ Neural Gate v3.1 — AI Crowd Intelligence & Autonomous Incident Capture
# File:    app.py
# Author:  AHMED ZARAI
# ---------------------------------------------------------------------------

import os
import time
import base64
import cv2
from flask import Flask, render_template
from flask_socketio import SocketIO
from core.engine import CrowdEngine
from config import *

# Initialize Flask and SocketIO
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

# --- SMART INPUT AUTO-DETECTION ---
if os.path.exists("/.dockerenv") or os.getenv("RUNNING_IN_DOCKER", "false").lower() == "true":
    is_docker = True
    source = "static/demo_video.mp4"
    print("> SYSTEM MODE: DOCKER (SIMULATION ON)")
else:
    is_docker = False
    source = 0
    print("> SYSTEM MODE: LOCAL (WEBCAM ACTIVE)")

cap = cv2.VideoCapture(source)
engine = CrowdEngine()

# --- Recording Setup ---
recording = False
video_writer = None
os.makedirs("recordings", exist_ok=True)

# --- Helper Functions ---
def threat_to_state(panic):
    if panic < 30:
        return "STABLE"
    elif panic < 60:
        return "ELEVATED"
    elif panic < 80:
        return "HIGH"
    else:
        return "CRITICAL"

# --- Main Streaming Loop ---
def stream():
    global recording, video_writer
    last_time = 0
    start_time = time.time()

    while True:
        now = time.time()
        if now - last_time < 1 / TARGET_FPS:
            socketio.sleep(0.01)
            continue
        last_time = now

        ret, frame = cap.read()
        if not ret:
            if is_docker:
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            socketio.sleep(0.5)
            continue

        frame, metrics = engine.process(frame)
        metrics['threat_state'] = threat_to_state(metrics['panic'])
        metrics['auto_mode'] = False

        # --- Auto-record logic ---
        if metrics['threat_state'] in ["HIGH", "CRITICAL"]:
            if not recording:
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                video_writer = cv2.VideoWriter(
                    f"recordings/incident_{timestamp}.mp4",
                    cv2.VideoWriter_fourcc(*'mp4v'),
                    TARGET_FPS,
                    (FRAME_WIDTH, FRAME_HEIGHT)
                )
                recording = True
            metrics['recording'] = True
            metrics['auto_mode'] = True
            video_writer.write(frame)
        else:
            metrics['recording'] = False
            metrics['auto_mode'] = False
            if recording:
                recording = False
                video_writer.release()
                video_writer = None

        _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
        frame_bytes = base64.b64encode(buffer).decode('utf-8')

        metrics['uptime'] = int(now - start_time)
        metrics['fps'] = round(1 / (time.time() - last_time + 1e-6), 2)

        socketio.emit("frame", {
            "image": frame_bytes,
            "metrics": metrics
        })

        socketio.sleep(0)

# --- Routes ---
@app.route("/")
def index():
    return render_template("index.html")

@socketio.on('connect')
def handle_connect():
    print("> CLIENT CONNECTED: INITIALIZING STREAM")
    socketio.start_background_task(stream)

# --- Main ---
if __name__ == "__main__":
    try:
        socketio.run(app, host="0.0.0.0", port=5000, debug=False)
    finally:
        cap.release()
        if video_writer:
            video_writer.release()
        print("> SYSTEM SHUTDOWN: HARDWARE RELEASED")