<div align="center">

<img src="https://img.icons8.com/nolan/128/artificial-intelligence.png" width="90"/>

# 🚨 NEURAL GATE v3.1
### **Crowd Intelligence • Autonomous Threat Detection • Real-Time Behavioral Analytics**

<p>
<img src="https://img.shields.io/badge/YOLOv8-Real--Time%20Inference-00F0FF?style=for-the-badge&logo=ai&logoColor=white"/>
<img src="https://img.shields.io/badge/Flask--SocketIO-Low%20Latency-black?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Docker-Production%20Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/License-MIT-FFD700?style=for-the-badge"/>
</p>

### ⚡ Next-Generation AI Surveillance Engine  
*From Detection to Behavioral Intelligence*

</div>

---

### 🚀 Overview
*Neural Gate v3.1* is a high-performance surveillance dashboard designed for automated security monitoring. It utilizes *YOLOv8* for multi-object tracking and an custom *Inference Engine* to quantify crowd behavior in real-time.



### ⚡ Core Capabilities
* *Behavioral Metrics:* On-the-fly calculation of Velocity, Coherence, and the *Panic Index*.
* *Autonomous Incident Capture:* Triggers DVR-style recording automatically when the Threat Level reaches HIGH or CRITICAL.
* *Cyberpunk UI:* Glassmorphic panels, neon-glow metrics, and animated particle backgrounds.
* *Smart Input Auto-Detection:* 
    * *Local:* Binds to hardware /dev/video0 (Webcam).
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
*AI Systems & Biometric Intelligence Developer*<br>
⚡Powered by Neural Gate v3.1 — Anticipating threats through crowd intelligence.
<br><br><br>

<div align="center">
<p>Copyright © 2026 AHMED ZARAI. Distributed under the MIT License.</p>
</div>