import time
from monitor import collect_metrics
from predictor import AnomalyDetector, get_data
from auto_heal import heal
from database import init_db

def rmm():
    print("\n Running RMM...\n")
    collect_metrics()

    data, latest = get_data()
    if len(data) < 10:
        print("Not enough data. Waiting...")
        return

    detector = AnomalyDetector()
    result = detector.check(data, latest)

    print("Latest:", latest)
    if result == -1:
        print("Anomaly! Healing...")
        heal()
    else:
        print("System OK.")

if __name__ == "__main__":
    print("Smart RMM Starting...")
    init_db()

    try:
        while True:
            rmm()
            time.sleep(10)
    except KeyboardInterrupt:
        print("\n Stopped.")
