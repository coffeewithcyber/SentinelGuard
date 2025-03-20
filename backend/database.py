import sqlite3
import time

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("incidents.db", check_same_thread=False)
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS incidents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip TEXT,
                event TEXT,
                timestamp TEXT,
                severity TEXT
            )
        """)
        self.conn.commit()

    def log_incident(self, ip, event, severity):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.conn.execute(
            "INSERT INTO incidents (ip, event, timestamp, severity) VALUES (?, ?, ?, ?)",
            (ip, event, timestamp, severity)
        )
        self.conn.commit()

    def get_incidents(self):
        cursor = self.conn.execute("SELECT * FROM incidents ORDER BY timestamp DESC")
        return [{"id": row[0], "ip": row[1], "event": row[2], "timestamp": row[3], "severity": row[4]} for row in cursor.fetchall()]
