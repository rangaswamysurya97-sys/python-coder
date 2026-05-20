filename = "form.html"

with open(filename, "r") as file:

    html = file.read()

if "csrf_token" in html:

    print("CSRF Protection Present")

else:

    print("Possible CSRF Risk")
