<div align="center">
  <img src="https://img.icons8.com/nolan/128/artificial-intelligence.png" width="80">
  <h1>🚨 Neural Gate v3.1</h1>
  <p><b>AI Crowd Intelligence & Autonomous Incident Capture</b></p>

  ![YOLOv8](https://img.shields.io/badge/YOLOv8-Inference-00FF00?style=for-the-badge&logo=ai&logoColor=white)
  ![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white)
  ![Python 3.10](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

  <p><i>Real-time AI surveillance dashboard with autonomous threat detection and behavioral analytics.</i></p>
</div>

---

### 🚀 Overview
*Neural Gate v3.1* is a high-performance surveillance dashboard designed for automated security monitoring. It utilizes *YOLOv8* for multi-object tracking and an custom *Inference Engine* to quantify crowd behavior in real-time.



### ⚡ Core Capabilities
* *Behavioral Metrics:* On-the-fly calculation of Velocity, Coherence, and the *Panic Index*.
* *Autonomous Incident Capture:* Triggers DVR-style recording automatically when the Threat Level reaches HIGH or CRITICAL.
* *Cyberpunk UI:* Glassmorphic panels, neon-glow metrics, and animated particle backgrounds.
* *Smart Input Auto-Detection:* * *Local:* Binds to hardware /dev/video0 (Webcam).
    * *Docker:* Switches to a high-fidelity MP4 simulation for zero-driver portable deployment.

---

### 🧠 Mathematical Modeling
The system goes beyond simple detection by analyzing crowd dynamics through vector calculus:

* *Panic Index ($P$):* Calculated as a function of average acceleration ($a$), crowd density ($\rho$), and spatial entropy ($S$):
  $$P = \sum (a \cdot \rho) + S$$
* *Threat Assessment:* A weighted state-machine that evaluates cumulative risk factors to transition between STABLE → HIGH → CRITICAL.

---

### 📊 Metric Intelligence Matrix

| Metric | logic / Description |
| :--- | :--- |
| *Velocity* | Average displacement of crowd vectors over $\Delta t$ |
| *Coherence* | Alignment coefficient of movement trajectories |
| *Panic Index* | Derived from sudden acceleration and chaotic spread |
| *Auto-Record* | Triggered immediately when *Threat ≥ 75%* |

🚨 Auto-recording triggers when Threat ≥ HIGH

---

### 📦 Project Structure
```text
Neural-Gate-v3.1/
├── app.py                # Flask-SocketIO Core Server
├── engine.py             # YOLOv8 Inference Logic
├── metrics.py            # Behavioral Calculus Engine
├── config.py             # Hyperparameters & Constants
├── static/               # Assets & Recordings
├── templates/            # Cyberpunk Dashboard UI
├── Dockerfile            # Container Orchestration
└── requirements.txt      # Dependency Stack
```
---

### 🖥️ Installation & Deployment
<details>
<summary><b>1. Local Development (Webcam Mode)</b></summary>
Ideal for real-time testing on your laptop.

```bash
git clone https://github.com/ahmedxzarai/Neural-Gate-v3.1
cd Neural-Gate-v3.1
python -m venv venv
# Activate & Install
source venv/bin/activate  # Windows: .\venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Live at: http://localhost:5000
</details>
<details>
<summary><b>2. Docker Deployment (Simulation Mode)</b></summary>
Ideal for deployment, portfolios, and servers.

```bash
docker build -t neural-gate:3.1 .
docker run -p 5000:5000 neural-gate:3.1
```
Live at: http://localhost:5000
</details>

---

### 🔥 Dashboard Highlights
* Live "LIVE" Indicator: Pulse-animation for active stream monitoring.
* Dynamic Charts: Real-time velocity trends rendered via Chart.js.
* Visual Alerts: Neon-red flashing overlays triggered by critical threat detection.

---

### 👤 Author
**AHMED ZARAI**<br>
*AI Systems & Biometric Intelligence Developer*
"⚡Powered by Neural Gate v3.1 — Anticipating threats through crowd intelligence."
<br><br><br>

<div align="center">
<p>Copyright © 2026 AHMED ZARAI. Distributed under the MIT License.</p>
</div>