payloads = [
    "<script>",
    "javascript:"
]

text = input("Enter input: ")

for payload in payloads:

    if payload.lower() in text.lower():

        print("Possible XSS Detected")
