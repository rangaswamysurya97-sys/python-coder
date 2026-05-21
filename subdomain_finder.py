import socket

domain = input("Enter domain: ")

subdomains = [
    "www",
    "mail",
    "ftp",
    "blog",
    "api"
]

for sub in subdomains:

    url = sub + "." + domain

    try:
        ip = socket.gethostbyname(url)

        print(url, "->", ip)

    except:
        pass
