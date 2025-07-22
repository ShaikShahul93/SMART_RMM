import sqlite3
from datetime import datetime

DB = "rmm.db"

def connect():
    return sqlite3.connect(DB)

def init_db():
    with connect() as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS metrics (
            timestamp TEXT, cpu REAL, memory REAL, disk REAL)""")

def insert_metric(data):
    with connect() as conn:
        conn.execute("INSERT INTO metrics VALUES (?, ?, ?, ?)", (
            datetime.now().isoformat(), data['cpu'], data['memory'], data['disk']))

def fetch_metrics(limit=100):
    with connect() as conn:
        return conn.execute(
            "SELECT * FROM metrics ORDER BY timestamp DESC LIMIT ?", (limit,)
        ).fetchall()

if __name__ == "__main__":
    init_db()
    print("Database ready.")
