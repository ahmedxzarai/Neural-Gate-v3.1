
# ---------------------------------------------------------------------------
# Project: 🛡️ Neural Gate v3.1 — AI Crowd Intelligence & Autonomous Incident Capture
# File:    metrics.py
# Author:  AHMED ZARAI
# ---------------------------------------------------------------------------

import numpy as np

def compute_spread(centers):
    if not centers:
        return 0
    centroid = np.mean(centers, axis=0)
    distances = [np.linalg.norm(np.array(c) - centroid) for c in centers]
    return float(np.mean(distances))

def compute_flow_coherence(flow_vectors):
    if not flow_vectors:
        return 0
    avg_vector = np.mean(flow_vectors, axis=0)
    return float(np.linalg.norm(avg_vector))

def compute_panic(acceleration, entropy, spread, w, h):
    panic = abs(acceleration)*0.4 + entropy*100*0.3 + (spread/(w+h))*100*0.3
    return float(min(panic, 100))

def classify_threat(panic):
    if panic < 20:
        return "STABLE"
    elif panic < 50:
        return "ELEVATED"
    elif panic < 75:
        return "HIGH RISK"
    else:
        return "CRITICAL"
