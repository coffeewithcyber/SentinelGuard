# SentinelGuard - Intrusion Detection and Response System

## Requirements
- **OS**: Linux (e.g., Ubuntu/Kali)
- **Privileges**: Root access (for log monitoring and packet capture)
- **Tools**: Python 3.8+, Node.js 16+, Scapy, tcpdump

## Setup Instructions

1. **Install Dependencies**:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip tcpdump
   cd backend && pip3 install -r requirements.txt
   cd ../frontend && npm install
