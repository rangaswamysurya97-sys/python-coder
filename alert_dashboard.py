from flask import Flask, render_template_string

app = Flask(__name__)

alerts = [
    "⚠ Malware Detected",
    "⚠ Failed Login Attempts",
    "✓ Firewall Active"
]

HTML = """
<h1>Security Alerts</h1>

<ul>
{% for alert in alerts %}
<li>{{ alert }}</li>
{% endfor %}
</ul>
"""

@app.route("/")
def home():
    return render_template_string(HTML, alerts=alerts)

app.run(debug=True)
