from flask import Flask, jsonify, request

app = Flask(__name__)

API_KEY = "secret123"

@app.route("/data")
def secure_data():
    key = request.headers.get("API-KEY")

    if key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    return jsonify({"message": "Secure Data Accessed"})

app.run(debug=True)
