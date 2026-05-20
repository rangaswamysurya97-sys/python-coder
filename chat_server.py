import socket

server = socket.socket()

server.bind(("0.0.0.0", 5000))

server.listen(1)

print("Waiting for connection...")

client, addr = server.accept()

print("Connected:", addr)

while True:

    message = client.recv(1024).decode()

    print("Client:", message)

    reply = input("You: ")

    client.send(reply.encode())
