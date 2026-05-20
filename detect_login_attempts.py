logins = [
    "success",
    "failed",
    "failed",
    "success",
    "failed"
]

failed_count = logins.count("failed")

print("Failed Login Attempts:", failed_count)

if failed_count >= 3:
    print("Warning: Multiple Failed Logins")
