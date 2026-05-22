import matplotlib.pyplot as plt

ports = [21, 22, 80, 443]
status = [1, 0, 1, 1]

plt.bar(ports, status)

plt.xlabel("Ports")
plt.ylabel("Status")
plt.title("Port Scan Results")

plt.show()
