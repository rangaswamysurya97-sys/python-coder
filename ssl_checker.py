import ssl
import socket
from urllib.parse import urlparse
from datetime import datetime

def check_ssl_certificate(url):
    try:
        # Add https if missing
        if not url.startswith("https://"):
            url = "https://" + url

        # Extract hostname
        hostname = urlparse(url).hostname

        # Create SSL context
        context = ssl.create_default_context()

        # Connect to server
        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:

                # Get certificate
                cert = ssock.getpeercert()

                print("\n===== SSL Certificate Report =====\n")

                # Subject
                subject = dict(x[0] for x in cert['subject'])
                print("Domain Name :", subject.get('commonName'))

                # Issuer
                issuer = dict(x[0] for x in cert['issuer'])
                print("Issued By   :", issuer.get('commonName'))

                # Validity
                valid_from = cert['notBefore']
                valid_to = cert['notAfter']

                print("Valid From  :", valid_from)
                print("Valid Until :", valid_to)

                # Expiry check
                expiry_date = datetime.strptime(
                    valid_to,
                    "%b %d %H:%M:%S %Y %Z"
                )

                days_left = (expiry_date - datetime.utcnow()).days

                print("Days Left   :", days_left)

                # Security status
                if days_left > 30:
                    print("\n[+] SSL Certificate is Valid")
                elif days_left > 0:
                    print("\n[WARNING] SSL Certificate will expire soon")
                else:
                    print("\n[-] SSL Certificate has expired")

    except Exception as e:
        print("Error:", e)

# User input
website = input("Enter Website URL: ")

# Run checker
check_ssl_certificate(website)
