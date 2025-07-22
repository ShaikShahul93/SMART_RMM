import psutil
from database import insert_metric

def collect_metrics():
    data = {
        'cpu': psutil.cpu_percent(1),
        'memory': psutil.virtual_memory().percent,
        'disk': psutil.disk_usage('/').percent
    }
    insert_metric(data)
    print("✅ Saved:", data)

if __name__ == "__main__":
    collect_metrics()
