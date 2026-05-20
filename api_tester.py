import requests

url = input("Enter API URL: ")

response = requests.get(url)

print("Status Code:", response.status_code)

print(response.headers)
