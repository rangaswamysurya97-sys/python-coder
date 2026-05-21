import requests

ip = input("Enter IP address: ")

url = f"https://ipinfo.io/{ip}/json"

try:

    response = requests.get(url)

    data = response.json()

    print("\nThreat Intelligence Result")
    print("--------------------------")

    print("IP:", data.get("ip"))
    print("City:", data.get("city"))
    print("Region:", data.get("region"))
    print("Country:", data.get("country"))
    print("Organization:", data.get("org"))

except Exception as e:

    print("Error:", e)
