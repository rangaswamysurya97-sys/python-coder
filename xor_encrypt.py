text = input("Enter text: ")
key = 5

encrypted = ""

for char in text:

    encrypted += chr(ord(char) ^ key)

print("Encrypted:")
print(encrypted)

decrypted = ""

for char in encrypted:

    decrypted += chr(ord(char) ^ key)

print("Decrypted:")
print(decrypted)
