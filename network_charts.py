import matplotlib.pyplot as plt

devices = ["PC1", "PC2", "Server", "Router"]
traffic = [30, 50, 90, 40]

plt.plot(devices, traffic)

plt.xlabel("Devices")
plt.ylabel("Traffic")

plt.title("Network Traffic")

plt.show()
