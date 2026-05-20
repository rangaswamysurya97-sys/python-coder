import socket

target = input("Enter IP address: ")
port = int(input("Enter port: "))

sock = socket.socket()

sock.settimeout(2)

sock.connect((target, port))

banner = sock.recv(1024)

print("Banner:")
print(banner.decode())

sock.close()
