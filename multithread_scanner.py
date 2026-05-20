import socket
import threading

target = input("Enter IP address: ")

def scan(port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} OPEN")

    sock.close()

for port in range(1, 101):

    thread = threading.Thread(target=scan, args=(port,))

    thread.start()
