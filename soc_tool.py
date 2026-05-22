logs = [
    "INFO User login",
    "WARNING Multiple failed logins",
    "CRITICAL Malware detected"
]

print("\n--- SOC Dashboard ---")

for log in logs:
    if "CRITICAL" in log:
        print(f"🚨 {log}")
    elif "WARNING" in log:
        print(f"⚠ {log}")
    else:
        print(f"✓ {log}")
