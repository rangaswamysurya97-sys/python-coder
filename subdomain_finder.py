import socket

# Common subdomains list
subdomains = [
    "www",
    "mail",
    "ftp",
    "webmail",
    "admin",
    "blog",
    "test",
    "dev",
    "api",
    "shop",
    "portal",
    "ns1",
    "ns2"
]

# Get domain from user
domain = input("Enter domain (example: google.com): ")

print("\n===== Subdomain Finder =====\n")

found = 0

# Check each subdomain
for sub in subdomains:
    subdomain = f"{sub}.{domain}"

    try:
        # Resolve subdomain
        ip = socket.gethostbyname(subdomain)

        print(f"[FOUND] {subdomain} --> {ip}")
        found += 1

    except socket.gaierror:
        # Subdomain not found
        pass

# Final result
print(f"\nTotal Subdomains Found: {found}")
