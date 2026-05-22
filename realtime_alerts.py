import time

attempts = 0

while True:
    attempts += 1

    print(f"Monitoring... Attempt {attempts}")

    if attempts == 5:
        print("⚠ ALERT: Suspicious activity detected!")

    time.sleep(2)
