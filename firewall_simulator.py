blocked_ports = [21, 23]

port = int(input("Enter port number: "))

if port in blocked_ports:

    print("Connection Blocked")

else:

    print("Connection Allowed")
