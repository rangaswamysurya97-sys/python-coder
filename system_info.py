import platform
import socket

# Operating System
os_name = platform.system()
os_version = platform.version()

# Hostname
hostname = socket.gethostname()

# IP Address
ip_address = socket.gethostbyname(hostname)

# Processor
processor = platform.processor()

# Python Version
python_version = platform.python_version()

print("===== SYSTEM INFORMATION =====")
print("Operating System :", os_name)
print("OS Version       :", os_version)
print("Hostname         :", hostname)
print("IP Address       :", ip_address)
print("Processor        :", processor)
print("Python Version   :", python_version)
