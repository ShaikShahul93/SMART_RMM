import numpy as np
from sklearn.ensemble import IsolationForest
from database import fetch_metrics

def get_data():
    data = fetch_metrics(100)
    if not data:
        return [], []
    arr = np.array([[cpu, mem, disk] for _, cpu, mem, disk in reversed(data)])
    return arr, arr[-1]

class AnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1)

    def check(self, data, latest):
        self.model.fit(data)
        return self.model.predict([latest])[0]

if __name__ == "__main__":
    print("Checking for anomalies...")
    data, latest = get_data()
    if len(data) > 0 :
        result = AnomalyDetector().check(data, latest)
        print("📊 Latest:", latest)
        print("🚨 Anomaly!" if result == -1 else "✅ Normal")
    else:
        print("⚠️ Not enough data.")
