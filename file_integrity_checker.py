import hashlib

filename = input("Enter file name: ")

with open(filename, "rb") as file:

    data = file.read()

    file_hash = hashlib.sha256(data).hexdigest()

print("SHA256 File Hash:")
print(file_hash)
