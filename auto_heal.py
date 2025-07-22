import psutil
import os
import platform

def kill_high_cpu(threshold=90):
    print("Checking for high CPU usage...")
    for p in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            if p.info['cpu_percent'] > threshold:
                print(f"Killing {p.info['name']} (PID: {p.info['pid']}) - {p.info['cpu_percent']}%")
                psutil.Process(p.info['pid']).terminate()
                return
        except:
            pass
    print("No high CPU process found.")

def restart_service():
    print("Restarting dummy service...")
    os.system("echo Dummy service restarted")

def heal():
    kill_high_cpu()
    restart_service()

if __name__ == "__main__":
    heal()
