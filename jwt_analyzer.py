import jwt

token = input("Enter JWT Token: ")

decoded = jwt.decode(
    token,
    options={"verify_signature": False}
)

print(decoded)
