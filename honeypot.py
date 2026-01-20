import socket
from datetime import datetime

HOST = "0.0.0.0"
PORT = 2222   # Fake SSH Port
LOG_FILE = "attacks.log"

def log_attack(ip, data):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} | Attacker IP: {ip} | Data: {data}\n")

def start_honeypot():
    print("[+] Honeypot started on port 2222")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)

    while True:
        client, addr = s.accept()
        ip = addr[0]
        print(f"[!] Connection from {ip}")

        client.send(b"SSH-2.0-OpenSSH_7.4\r\n")
        data = client.recv(1024).decode(errors="ignore")

        log_attack(ip, data)
        client.close()

if __name__ == "__main__":
    start_honeypot()
