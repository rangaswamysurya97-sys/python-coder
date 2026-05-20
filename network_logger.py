from datetime import datetime

log_file = "network_logs.txt"

event = input("Enter network event: ")

with open(log_file, "a") as file:

    file.write(
        f"{datetime.now()} : {event}\n"
    )

print("Event Logged")
