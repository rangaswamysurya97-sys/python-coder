logs = [
    "Login Success",
    "Failed Login",
    "Access Denied",
    "Failed Login"
]

for log in logs:

    if "Failed" in log or "Denied" in log:

        print("ALERT:", log)
