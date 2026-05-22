from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<h1>Login Dashboard</h1>
<form>
Username: <input><br><br>
Password: <input type='password'><br><br>
<button>Login</button>
</form>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

app.run(debug=True)
