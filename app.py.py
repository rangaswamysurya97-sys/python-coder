from flask import Flask, render_template
from routes.chat_routes import chat_bp

app = Flask(__name__)

app.register_blueprint(chat_bp)

@app.route("/")
def home():

    return render_template("index.html")

if __name__ == "__main__":

    app.run(debug=True)
