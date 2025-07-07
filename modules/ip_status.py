import os, requests

ip = input("🌐 Enter IP or domain to check: ").strip()
try:
    res = requests.get(f"http://{ip}", timeout=5)
    print(f"✅ {ip} is UP [Status: {res.status_code}]")
except:
    print(f"❌ {ip} is DOWN or Unreachable.")
