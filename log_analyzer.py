filename = "system_logs.txt"

with open(filename, "r") as file:

    logs = file.readlines()

failed = 0

for log in logs:

    if "Failed" in log:

        failed += 1

print("Failed Events:", failed)
