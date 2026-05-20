import socket

target = input("Enter IP: ")

for port in range(75, 85):

    sock = socket.socket()

    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))

    if result == 0:

        print(f"Port {port} OPEN")

    sock.close()
