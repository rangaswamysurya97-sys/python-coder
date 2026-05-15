import urllib.request
import urllib.error

# List of important security headers
SECURITY_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy"
]

def check_security_headers(url):
    try:
        # Create request
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        # Open URL
        response = urllib.request.urlopen(request, timeout=5)

        # Get headers
        headers = response.headers

        print("\n===== Security Header Report =====\n")

        score = 0

        # HTTPS check
        if url.startswith("https://"):
            print("[+] HTTPS Enabled")
        else:
            print("[-] HTTPS NOT Enabled")

        print()

        # Check each header
        for header in SECURITY_HEADERS:
            if header in headers:
                print(f"[FOUND] {header}")
                score += 1
            else:
                print(f"[MISSING] {header}")

        print(f"\nSecurity Score: {score}/{len(SECURITY_HEADERS)}")

    except urllib.error.URLError as e:
        print("Error:", e)

# User input
url = input("Enter Website URL: ")

# Run checker
check_security_headers(url)
