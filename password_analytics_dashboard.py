from flask import Flask, render_template, request
import math
import re

app = Flask(__name__)


def calculate_entropy(password):
    charset = 0

    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[^a-zA-Z0-9]", password):
        charset += 32

    if charset == 0:
        return 0

    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)


def password_strength(password):
    score = 0
    remarks = []

    if len(password) >= 8:
        score += 1
    else:
        remarks.append("Use at least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        remarks.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        remarks.append("Add lowercase letters")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        remarks.append("Add numbers")

    if re.search(r"[^a-zA-Z0-9]", password):
        score += 1
    else:
        remarks.append("Add special characters")

    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, remarks


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        password = request.form["password"]

        entropy = calculate_entropy(password)
        strength, remarks = password_strength(password)

        result = {
            "password": password,
            "length": len(password),
            "entropy": entropy,
            "strength": strength,
            "remarks": remarks
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
