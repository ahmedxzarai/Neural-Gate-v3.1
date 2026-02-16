
# ---------------------------------------------------------------------------
# Project: 🛡️ Neural Gate v3.1 — AI Crowd Intelligence & Autonomous Incident Capture
# File:    engine.py
# Author:  AHMED ZARAI
# ---------------------------------------------------------------------------

import cv2
import numpy as np
from collections import defaultdict, deque
from ultralytics import YOLO
from config import *
from core.metrics import *

class CrowdEngine:
    def __init__(self):
        self.model = YOLO("models/yolov8n.pt")
        self.model.fuse()

        self.track_history = defaultdict(lambda: deque(maxlen=TRAJECTORY_LENGTH))
        self.heatmap = np.zeros((FRAME_HEIGHT, FRAME_WIDTH), dtype=np.float32)
        self.prev_velocity = 0

    def process(self, frame):
        frame = cv2.resize(frame, (FRAME_WIDTH, FRAME_HEIGHT))
        h, w, _ = frame.shape

        results = self.model.track(
            frame,
            persist=True,
            classes=[0],
            conf=0.5,
            verbose=False
        )

        velocities = []
        centers = []
        flow_vectors = []

        if results and results[0].boxes.id is not None:
            boxes = results[0].boxes.xywh.cpu().numpy()
            ids = results[0].boxes.id.cpu().numpy()

            for box, track_id in zip(boxes, ids):
                x, y, bw, bh = box
                center = (int(x), int(y))
                centers.append(center)

                # --- Gaussian density heatmap ---
                cv2.circle(self.heatmap, center, 15, 1, -1)

                x1, y1 = int(x - bw/2), int(y - bh/2)
                x2, y2 = int(x + bw/2), int(y + bh/2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f"ID: {int(track_id)}",
                            (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.5,
                            (0, 255, 0),
                            2)

                history = self.track_history[int(track_id)]
                history.append(center)

                if len(history) >= 2:
                    dx = history[-1][0] - history[-2][0]
                    dy = history[-1][1] - history[-2][1]
                    velocity = np.sqrt(dx**2 + dy**2)
                    velocities.append(velocity)

                    magnitude = np.sqrt(dx**2 + dy**2)
                    if magnitude > 0:
                        flow_vectors.append([dx/magnitude, dy/magnitude])

        avg_velocity = np.mean(velocities) if velocities else 0
        acceleration = avg_velocity - self.prev_velocity
        self.prev_velocity = avg_velocity

        spread = compute_spread(centers)
        coherence = compute_flow_coherence(flow_vectors)
        entropy = 1 - coherence
        panic = compute_panic(acceleration, entropy, spread, w, h)
        threat_state = classify_threat(panic)

        # Heatmap smoothing
        self.heatmap *= HEATMAP_DECAY
        self.heatmap = cv2.GaussianBlur(self.heatmap, (25, 25), 0)

        if self.heatmap.max() > 0:
            heatmap_norm = self.heatmap / self.heatmap.max()
        else:
            heatmap_norm = self.heatmap

        heatmap_colored = cv2.applyColorMap(
            (heatmap_norm * 255).astype(np.uint8),
            cv2.COLORMAP_JET
        )

        frame = cv2.addWeighted(frame, 0.7, heatmap_colored, 0.3, 0)

        metrics = {
            "people": len(centers),
            "velocity": round(float(avg_velocity), 2),
            "coherence": round(float(coherence), 2),
            "entropy": round(float(entropy), 2),
            "panic": round(float(panic), 1),
            "threat_state": threat_state
        }

        return frame, metrics
