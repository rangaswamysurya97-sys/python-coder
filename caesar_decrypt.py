text = input("Enter encrypted text: ")
shift = 3

decrypted = ""

for char in text:

    if char.isalpha():

        decrypted += chr(ord(char) - shift)

    else:
        decrypted += char

print("Decrypted Text:")
print(decrypted)
