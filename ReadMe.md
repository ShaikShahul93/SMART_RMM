# 🛠️ Smart RMM Tool (Remote Monitoring & Management)

A beginner-friendly Python tool to **monitor**, **detect anomalies**, and **auto-heal** system issues using live and historical data. Built with `psutil`, `SQLite`, and `scikit-learn`.

---

## 🚀 Features

- 📊 **System Monitoring**  
  Collects CPU, Memory, and Disk usage every 10 seconds.

- 🤖 **Anomaly Detection**  
  Uses `IsolationForest` to detect unusual behavior based on past metrics.

- 🔧 **Auto-Healing**  
  If an anomaly is detected, the tool:
  - Checks for high CPU-consuming processes
  - Tries to kill them (if safe)
  - Restarts a dummy service as fallback

- 🗃️ **Historical Metrics**  
  All system metrics are stored in a local SQLite database.

---

## 📂 Project Structure
Smart_Rmm/
├── main.py # Main script to run the RMM cycle
├── monitor.py # Collects and stores system metrics
├── predictor.py # ML model for anomaly detection
├── auto_heal.py # Healing logic
├── database.py # SQLite operations
├── system_metrics.db # SQLite database (auto-created)
└── README.md # This file

---

## 🧰 Requirements

Install dependencies via pip:

```bash
pip install psutil scikit-learn numpy

## 📘 How to Run
1. Clone the project:
   ```bash
   git clone https://github.com/your-username/smart-rmm.git
   cd smart-rmm

Run the main script:

bash
python main.py
Stop the tool any time with CTRL + C.

🧪 Sample Output:

✅ Saved: {'cpu': 7.7, 'memory': 58.9, 'disk': 18.7}
📊 Latest: [ 7.7 58.9 18.7]
🚨 Anomaly Detected! Initiating auto-healing...

🛠️ Checking for high CPU usage...
⚠️ No high CPU process found.
🔄 Restarting dummy service...
✅ Dummy service restarted successfully.

And here’s another example when the system is normal:
✅ Saved: {'cpu': 4.2, 'memory': 58.8, 'disk': 18.7}
📊 Latest: [ 4.2 58.8 18.7]
✅ System OK. No action needed.

💡 Future Improvements (Next Steps):

📝 Save all results into a log file or show on a simple dashboard
📧 Send alerts using email or Slack when problems are found
🧠 Check for memory and disk problems, not just CPU
🔧 Replace fake healing steps with real system fixes



👨‍💻 Author
SHAIK SHAHUL



