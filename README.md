🛡️ Neural Gate v3.1 — AI Crowd Intelligence & Autonomous Incident Capture

AI-powered surveillance dashboard with real-time crowd analysis, threat detection, and autonomous recording. Designed for high-tech security monitoring and advanced behavioral metrics.


⚡ Features

• Real-Time Detection: YOLOv8 multi-object tracking optimized for live CPU/GPU feeds.
• Behavioral Metrics: Calculates Velocity, Coherence, Panic Index, and Threat Level on-the-fly.
• Autonomous Recording: Automatically records video when threat level is HIGH or CRITICAL.
• Interactive Dashboard: Glassmorphic panels, neon glow metrics, animated cyber particles, velocity charts, live “LIVE” indicator, and flashing threat badge.
• Infrastructure-Ready: Fully containerized for deployment via Docker with minimal setup.

## 🤖 Smart Input Auto-Detection
This project is built with *Environment Awareness*:
- *Local Mode*: When run normally, the system automatically binds to your hardware webcam (/dev/video0).
- *Docker Mode*: When containerized, the system automatically switches to a high-fidelity video simulation (demo_video.mp4) to ensure portability across Windows/Linux without hardware driver errors.


🛠️ Tech Stack

• AI Engine: YOLOv8 (Ultralytics)
• Backend: Python 3.10 / Flask / Flask-SocketIO / Eventlet
• Frontend: HTML5 / CSS3 / JavaScript / Chart.js / Cyberpunk styling
• Infrastructure: Docker / WSL2


📦 Getting Started

🚀 Installation & Launch

1️⃣ Local Mode (Webcam)
Ideal for real-time testing on your laptop.

```bash
git clone https://github.com/ahmedxzarai/Neural-Gate-v3.1
cd Neural-Gate-v3.1
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  
# On Windows use:
.\venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Access at: http://localhost:5000

2️⃣ Docker Mode (Simulation)
Ideal for deployment, portfolios, and servers.

```bash
docker build -t neural-gate:3.1 .
docker run -p 5000:5000 neural-gate:3.1
```
Access at: http://localhost:5000

**💡 Note:** To persist recordings to your host machine, run with a volume:
`docker run -p 5000:5000 -v ${PWD}/recordings:/app/recordings neural-gate:3.1`

🎛️ System Architecture

[Input Source] -> [YOLOv8 AI Engine] -> [Tracking & Metrics]
      |                |                         |
   Webcam / MP4   Object Detection        Velocity / Threat / Panic
      |________________|_______________________|
                       |
                  [WebSocket Server]
                       |
             [Premium Neural Gate Dashboard]


📊 Metrics

| Metric           | Description                                     |
| ---------------- | ----------------------------------------------- |
| **People**       | Number of detected individuals                  |
| **Velocity**     | Average movement speed of the crowd             |
| **Coherence**    | Alignment of crowd movement vectors             |
| **Panic**        | Derived from acceleration, spread, and entropy  |
| **Threat**       | Risk assessment: `STABLE` → `HIGH` → `CRITICAL` |
| **FPS / Uptime** | Live frame rate and system runtime              |


🚨 Auto-recording triggers when Threat ≥ HIGH

🖥️ Dashboard Highlights

• Live Red “LIVE” Indicator: Always shows streaming status
• Auto Recording Badge: Blinks when system is recording
• Threat-Level Flashing: High → red flash, Critical → neon red blink
• Neon / Cyberpunk Design: Glassmorphic panels, smooth glow, animated particle background
• Dynamic Charts: Velocity trend over the last 20 frames

📦 Project Structure

Neural-Gate-v3.1/
├─ app.py                # Flask server + SocketIO streaming
├─ engine.py             # YOLOv8 crowd detection & metrics
├─ metrics.py            # Behavioral metric computations
├─ config.py             # Global constants / frame size / FPS
├─ static/
│  ├─ demo_video.mp4     # Demo video for Docker mode
│  └─ ...                # Any additional assets
├─ templates/
│  └─ index.html         # Premium dashboard UI
├─ Dockerfile            # Container setup
├─ requirements.txt      # Python dependencies
├─ LICENSE               # MIT License file
├─ .dockerignore
├─ .gitignore
└─ README.md             # This file



👤 Author
AHMED ZARAI — AI Systems & Biometric Intelligence Developer
⚡ “Powered by Neural Gate v3.1 — real-time AI crowd intelligence for security and analytics”


📜 License \& Copyright
Copyright © 2026 AHMED ZARAI. Distributed under the MIT License. See LICENSE for more information.

