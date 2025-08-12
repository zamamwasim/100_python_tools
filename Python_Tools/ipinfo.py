import socket
import ipaddress
import requests

ip = input("Please enter your IP Address: ")

# Validate IP format
try:
    ipaddress.ip_address(ip)
except ValueError:
    print("❌ Invalid IP address format.")
    exit()

# Get hostname
try:
    hostname = socket.gethostbyaddr(ip)[0]
except socket.herror:
    hostname = "Hostname not found"

# API request
url = f"http://ip-api.com/json/{ip}"
try:
    response = requests.get(url, timeout=5)
    data = response.json()
except requests.RequestException:
    print("❌ Could not connect to IP API service.")
    exit()

# Check if API succeeded
if data.get("status") != "success":
    print("❌ API request failed:", data.get("message", "Unknown error"))
    exit()

# Print results
print("\n--- IP INFO ---")
print(f"IP Address: {ip}")
print(f"Hostname: {hostname}")
print(f"Country: {data.get('country', 'N/A')}")
print(f"City: {data.get('city', 'N/A')}")
print(f"ISP: {data.get('isp', 'N/A')}")
print(f"Location: {data.get('lat', 'N/A')}, {data.get('lon', 'N/A')}")
