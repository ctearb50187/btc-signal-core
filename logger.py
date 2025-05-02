import sqlite3
from datetime import datetime
import os

def log_action(action):
    db_path = os.path.join(os.path.dirname(__file__), "signals.db")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS actions (timestamp TEXT, action TEXT)")
    c.execute("INSERT INTO actions (timestamp, action) VALUES (?, ?)", (datetime.now().isoformat(), action))
    conn.commit()
    conn.close()