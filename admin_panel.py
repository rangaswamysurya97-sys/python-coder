from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<h1>Admin Panel</h1>

<button>View Logs</button><br><br>
<button>Manage Users</button><br><br>
<button>System Settings</button>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

app.run(debug=True)
