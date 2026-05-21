import psutil

cpu = psutil.cpu_percent()

memory = psutil.virtual_memory().percent

print("CPU Usage:", cpu)
print("Memory Usage:", memory)

if cpu > 80:

    print("High CPU Usage Detected")

if memory > 80:

    print("High Memory Usage Detected")
