blocked_ips = [
    "192.168.1.100",
    "10.0.0.50"
]

ip = input("Enter IP address: ")

if ip in blocked_ips:

    print("Suspicious IP Detected")

else:

    print("IP Looks Safe")
