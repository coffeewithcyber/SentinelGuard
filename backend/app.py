from flask import Flask, jsonify
from flask_cors import CORS
from log_monitor import LogMonitor
from network_monitor import NetworkMonitor
from database import Database
import threading

app = Flask(__name__)
CORS(app)

db = Database()
log_monitor = LogMonitor(db)
network_monitor = NetworkMonitor(db)

@app.route("/api/incidents", methods=["GET"])
def get_incidents():
    return jsonify(db.get_incidents())

if __name__ == "__main__":
    # Start monitoring in separate threads
    threading.Thread(target=log_monitor.monitor_logs).start()
    threading.Thread(target=network_monitor.start_sniffing).start()
    app.run(host="0.0.0.0", port=5000)
