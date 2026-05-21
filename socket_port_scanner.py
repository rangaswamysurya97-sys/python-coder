import socket

target = input("Enter IP address: ")

start_port = 1
end_port = 100

for port in range(start_port, end_port + 1):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")

    sock.close()
