text = input("Enter text: ")
shift = 3

encrypted = ""

for char in text:

    if char.isalpha():

        encrypted += chr(ord(char) + shift)

    else:
        encrypted += char

print("Encrypted Text:")
print(encrypted)
