from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64

key = b'1234567890123456'

text = input("Enter text: ")

cipher = AES.new(key, AES.MODE_ECB)

encrypted = cipher.encrypt(
    pad(text.encode(), AES.block_size)
)

encoded = base64.b64encode(encrypted)

print("Encrypted:")
print(encoded.decode())
