import requests

ip = input("🌍 Enter IP Address: ").strip()
api = f"http://ip-api.com/json/{ip}"
res = requests.get(api).json()

if res['status'] == 'success':
    print(f"🌦️ Location: {res['city']}, {res['country']}")
    print(f"📡 ISP: {res['isp']}")
    print(f"🕒 Timezone: {res['timezone']}")
    print(f"🌐 IP: {res['query']}")
    print(f"🧭 Lat, Lon: {res['lat']}, {res['lon']}")
else:
    print("❌ IP not found.")
