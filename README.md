🕵️‍♂️ Python-Based Honeypot

A lightweight Python-based Honeypot designed to simulate a vulnerable network service and capture malicious connection attempts.  
This project helps in understanding attacker behavior, threat intelligence, and SOC-level monitoring.

📌 Project Objective

The goal of this project is to:
- Simulate a fake vulnerable service (SSH-like)
- Attract malicious connections
- Capture attacker IP addresses and payloads
- Log attack attempts for security analysis

🛠 Tools & Technologies

- Python 3
- Socket Programming
- Windows / Linux
- File-based logging system

🧠 Key Cybersecurity Concepts

- Honeypots & Deception Technology
- Threat Intelligence Collection
- SOC Monitoring
- Blue-Team Security
- Attack Surface Analysis

📂 Project Structure
honeypot/
│
├── honeypot.py # Honeypot server logic
├── attacks.log # Captured attacker logs
└── README.md

⚙️ How the Honeypot Works

1. Listens on a fake vulnerable port (default: 2222)
2. Simulates an SSH service banner
3. Accepts incoming connections
4. Logs attacker IP addresses and data
5. Closes the connection safely

⚙️ Installation & Setup

1️⃣ Clone the Repository
git clone https://github.com/your-username/python-honeypot.git
cd python-honeypot

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv

3️⃣ Activate Virtual Environment
Windows (PowerShell):
.\venv\Scripts\Activate.ps1

Windows (CMD):
venv\Scripts\activate

Linux / macOS:
source venv/bin/activate

▶️ Running the Honeypot
python honeypot.py

You should see:
[+] Honeypot started on port 2222

🧪 Testing the Honeypot (Safe & Legal)
From another terminal:
telnet localhost 2222

Or:
nc localhost 2222

📝 Log File Example (attacks.log)
2026-01-20 | Attacker IP: 127.0.0.1 | Data: root

⚠️ This project is strictly for educational and defensive security purposes.
Do NOT deploy on unauthorized networks
Use only on systems you own or have permission to test

🚀 Future Enhancements
Multiple fake services (FTP, HTTP, Telnet)
Real-time alerting
Dashboard integration
SIEM integration (Splunk / ELK)
Machine learning-based attack classification

📄 License
This project is released for educational and ethical cybersecurity learning only.

👨‍💻 Author
@dishank12
Cybersecurity Student | SOC & Blue-Team Enthusiast
