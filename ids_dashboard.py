from flask import Flask, render_template_string

app = Flask(__name__)

intrusions = [
    "Port Scan Detected",
    "Brute Force Attack",
    "Malicious Traffic"
]

HTML = """
<h1>IDS Dashboard</h1>

<ul>
{% for item in intrusions %}
<li>{{ item }}</li>
{% endfor %}
</ul>
"""

@app.route("/")
def home():
    return render_template_string(HTML, intrusions=intrusions)

app.run(debug=True)
