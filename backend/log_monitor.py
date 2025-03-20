import re
import time
from collections import defaultdict

class LogMonitor:
    def __init__(self, db):
        self.db = db
        self.failed_attempts = defaultdict(int)

    def monitor_logs(self, log_file="/var/log/auth.log"):
        try:
            with open(log_file, "r") as f:
                f.seek(0, 2)  # Move to end of file
                while True:
                    line = f.readline()
                    if not line:
                        time.sleep(0.1)
                        continue
                    self.analyze_log(line)
        except PermissionError:
            print("Error: Need root privileges to read logs.")
            exit(1)

    def analyze_log(self, line):
        failed_login = re.search(r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)", line)
        if failed_login:
            ip = failed_login.group(1)
            self.failed_attempts[ip] += 1
            if self.failed_attempts[ip] > 3:  # Threshold for brute-force
                self.db.log_incident(ip, "Brute-force attempt detected", "High")
                self.failed_attempts[ip] = 0  # Reset counter
