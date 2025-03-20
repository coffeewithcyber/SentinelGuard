from scapy.all import sniff
from collections import defaultdict

class NetworkMonitor:
    def __init__(self, db):
        self.db = db
        self.port_attempts = defaultdict(set)

    def start_sniffing(self):
        try:
            sniff(prn=self.analyze_packet, store=False, count=100)  # Limit for demo
        except PermissionError:
            print("Error: Need root privileges to capture packets.")
            exit(1)

    def analyze_packet(self, packet):
        if packet.haslayer("IP"):
            ip = packet["IP"].src
            if packet.haslayer("TCP"):
                port = packet["TCP"].dport
                self.port_attempts[ip].add(port)
                if len(self.port_attempts[ip]) > 5:  # Multiple ports scanned
                    self.db.log_incident(ip, "Port scan detected", "Medium")
                    self.port_attempts[ip].clear()
