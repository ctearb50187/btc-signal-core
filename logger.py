import sqlite3
from datetime import datetime

def log_action(action):
    conn = sqlite3.connect("signals.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS actions (timestamp TEXT, action TEXT)")
    c.execute("INSERT INTO actions (timestamp, action) VALUES (?, ?)", (datetime.now().isoformat(), action))
    conn.commit()
    conn.close()