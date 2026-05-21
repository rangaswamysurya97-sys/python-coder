services = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS"
}

for port, service in services.items():

    print(f"Port {port} -> {service}")
