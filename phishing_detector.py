url = input("Enter URL: ")

suspicious_words = [
    "login",
    "verify",
    "banking",
    "free",
    "bonus"
]

for word in suspicious_words:

    if word in url.lower():

        print("Possible Phishing URL")
        break

else:

    print("URL Looks Safer")
