logs = [
    "Login Success",
    "Failed Login",
    "Access Denied"
]

for log in logs:

    if "Failed" in log or "Denied" in log:

        print("Suspicious Activity:", log)
