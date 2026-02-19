<p align="center">
  <img src="https://img.icons8.com/nolan/128/artificial-intelligence.png" width="110"/>
</p>

<h1 align="center">NEURAL GATE v3.1</h1>
<h3 align="center">
Behavioral Intelligence Engine for Real-Time Crowd Instability Detection
</h3>

<p align="center">
  <img src="https://img.shields.io/badge/YOLOv8-Real--Time%20Inference-00F0FF?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Flask--SocketIO-Low%20Latency-black?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Docker-Production%20Ready-2496ED?style=for-the-badge"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square"/>
  <img src="https://img.shields.io/badge/License-MIT-FFD700?style=flat-square"/>
  <img src="https://img.shields.io/badge/Status-Active%20Development-00C853?style=flat-square"/>
</p>

---

## Executive Summary

Neural Gate v3.1 is a deterministic behavioral intelligence engine designed to detect, quantify, and anticipate abnormal crowd dynamics in real time.

Traditional video analytics systems stop at object detection.

Neural Gate models collective motion behavior.

It transforms raw video streams into structured instability metrics through vector calculus, density modeling, and entropy-based analysis.

The system does not classify isolated anomalies.

It evaluates emergent system-level instability.

---

## Problem Statement

Conventional surveillance pipelines focus on:

- Object presence
- Identity recognition
- Static anomaly classification

However, large-scale instability events (panic waves, crowd surges, density collapses) emerge from collective dynamics — not individual detections.

These events require:

- Motion vector aggregation
- Acceleration modeling
- Spatial entropy measurement
- Deterministic escalation logic

Neural Gate addresses this gap.

---

## Core Capabilities

- Real-time multi-object tracking  
- Frame-to-frame vector displacement modeling  
- Acceleration-based instability detection  
- Density-weighted motion aggregation  
- Entropy-informed dispersion analysis  
- Deterministic threat state transitions  
- Autonomous incident recording  

---

## System Architecture

<p align="center">
  <img src="assets/architecture.svg" width="100%">
</p>

Streaming-first modular architecture built for edge-to-cloud scalability.

Pipeline flow:

```
Video Stream → Detection Engine → Vector Engine → Analytics Core → Threat Engine → Dashboard + DVR
```
Each layer is isolated, testable, and independently extensible.

---

## Intelligence Modules

### 1. Multi-Object Vector Engine

- Bounding box tracking  
- Displacement vector computation  
- Velocity and acceleration modeling  
- Crowd centroid calculation  
- Real-time state propagation  

Transforms pixel movement into structured physical dynamics.

---

### 2. Behavioral Calculus Engine

| Metric | Description |
|--------|-------------|
| Velocity (v) | Mean displacement over Δt |
| Acceleration (a) | Rate of directional change |
| Density (ρ) | Local spatial clustering intensity |
| Coherence (C) | Directional alignment consistency |
| Panic Index (P) | Composite instability metric |

The engine continuously updates these metrics under sub-100ms latency.

---

## Mathematical Threat Modeling

The Panic Index is defined as:

$begin:math:display$
P \= \\sum \(a\_i \\cdot \\rho\_i\) \+ S
$end:math:display$

Where:

- $begin:math:text$ a\_i $end:math:text$ = acceleration vectors  
- $begin:math:text$ \\rho\_i $end:math:text$ = local density weight  
- $begin:math:text$ S $end:math:text$ = spatial entropy  

This formulation enables nonlinear instability detection rather than static anomaly thresholds.

The result is deterministic escalation logic with explainable transitions.

---

## Deterministic Threat Escalation

State transitions are governed by the Panic Index:

| Current State | Threshold ($P$) | System Action | Dash Indicator | DVR Status |
| :--- | :--- | :--- | :--- | :--- |
| *STABLE* | $P < 0.4$ | Standard Monitoring | 🟢 Solid Green | IDLE |
| *HIGH* | $0.4 \leq P < 0.8$ | Analytics Warning | 🟠 Pulsing Orange | *ARMED* |
| *CRITICAL* | $P \geq 0.8$ | Autonomous Response | 🔴 Flashing Red | *RECORDING* |

When threat level ≥ 75%:

- DVR recording initiates automatically  
- Timestamped footage is stored  
- Event metadata is logged  
- Dashboard visual alerts activate  

No operator intervention required.

---

## Dashboard Interface

Designed for command-center environments:

- Glassmorphic panels  
- Real-time velocity graphs  
- Threat state indicators  
- Autonomous recording banner  
- Low-latency WebSocket updates  

The interface reflects deterministic system state in real time.

---

## Deployment

### Local Mode (Webcam)
```bash
git clone https://github.com/ahmedxzarai/Neural-Gate-v3.1
cd Neural-Gate-v3.1

python -m venv venv
source venv/bin/activate
# Windows: .\venv\Scripts\activate

pip install -r requirements.txt
python app.py
```
Live at:

```
http://localhost:5000
```

---

### Docker Mode (Simulation)
```bash
docker build -t neural-gate:3.1 .
docker run -p 5000:5000 neural-gate:3.1
```
Hardware-agnostic, containerized deployment.

---

## Performance Profile

| Metric | Value |
|--------|--------|
| Inference | Real-time YOLOv8 |
| Latency | <100ms metric update |
| State Transition | Deterministic |
| CPU Compatible | Yes |
| GPU Optional | Yes |
| Containerized | Yes |

---

## Privacy & Ethical Design

Neural Gate is designed for behavioral modeling, not identity surveillance.

- No facial recognition  
- No biometric storage  
- No identity persistence  
- Motion-vector-based analysis only  
- Compatible with anonymized footage  

System design prioritizes explainability and operational transparency.

---

## Operational Deployment Scenarios

- Smart city crowd monitoring  
- Stadium and event risk detection  
- Airport congestion analysis  
- Industrial perimeter intelligence  
- Behavioral anomaly research environments  

---

## Advanced Research Extensions

- Multi-camera distributed inference  
- Edge optimization (Jetson-class hardware)  
- Cloud-based aggregation layer  
- Reinforcement-adaptive thresholds  
- Privacy-preserving vector anonymization  

---

## Project Structure
```
Neural-Gate-v3.1/
│
├── app.py              # Flask-SocketIO server
├── engine.py           # YOLOv8 inference & tracking
├── metrics.py          # Behavioral calculus engine
├── config.py           # Threshold configuration
│
├── static/
│   ├── recordings/     # Autonomous incident capture
│   └── assets/
│
├── templates/
│   └── dashboard.html  # Frontend interface
│
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Author

**Ahmed Zarai**  
AI Systems & Behavioral Intelligence Developer  

Neural Gate v3.1 represents applied research in deterministic crowd instability modeling and real-time behavioral analytics.

---

## License

Distributed under the MIT License.  
Copyright © 2026 Ahmed Zarai.