import urllib.request
import urllib.error

# Common directories to check
directories = [
    "admin",
    "login",
    "dashboard",
    "uploads",
    "images",
    "backup",
    "test",
    "api"
]

# Get target website
target = input("Enter Target URL (Example: https://example.com): ")

print("\n===== Directory Finder =====\n")

# Loop through directories
for directory in directories:

    # Create full URL
    url = target.rstrip("/") + "/" + directory

    try:
        # Send request
        response = urllib.request.urlopen(url)

        # If page exists
        print(f"[FOUND] {url}  | Status Code: {response.status}")

    except urllib.error.HTTPError as e:

        # Handle common errors
        if e.code == 404:
            print(f"[NOT FOUND] {url}")

        else:
            print(f"[{e.code}] {url}")

    except urllib.error.URLError:
        print(f"[ERROR] Could not connect to {url}")

print("\nScan Completed.")
