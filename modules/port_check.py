import socket

target = input("🌐 Enter IP/domain: ").strip()
ports = [21, 22, 23, 25, 53, 80, 110, 443, 445, 3306, 8080]

print(f"🔍 Scanning ports on {target}...")
for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"✅ Port {port} is OPEN")
    sock.close()
