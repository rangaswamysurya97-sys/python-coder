failed_ips = {}

with open(r"C:\Users\ELCOT\Desktop\TASKS\python programms\server.log", "r") as file:

    for line in file:

        if "FAILED LOGIN" in line:

            ip = line.split()[-1]

            if ip in failed_ips:
                failed_ips[ip] += 1
            else:
                failed_ips[ip] = 1

print("\n--- Correlated Logs ---")

for ip, count in failed_ips.items():
    print(f"{ip} -> {count} failed attempts")
