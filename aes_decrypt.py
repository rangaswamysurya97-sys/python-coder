from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

key = b'1234567890123456'

encrypted_text = input(
    "Enter encrypted text: "
).strip()

try:

    cipher = AES.new(key, AES.MODE_ECB)

    decoded = base64.b64decode(encrypted_text)

    decrypted = unpad(
        cipher.decrypt(decoded),
        AES.block_size
    )

    print("Decrypted Text:")
    print(decrypted.decode())

except Exception as e:

    print("Invalid encrypted text")
    print(e)
