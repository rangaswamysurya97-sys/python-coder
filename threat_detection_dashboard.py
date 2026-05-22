from flask import Flask, render_template_string

app = Flask(__name__)

threats = [
    "SQL Injection",
    "XSS Attack",
    "Brute Force Attempt"
]

HTML = """
<h1>Threat Detection Dashboard</h1>

<ul>
{% for threat in threats %}
<li>{{ threat }}</li>
{% endfor %}
</ul>
"""

@app.route("/")
def home():
    return render_template_string(HTML, threats=threats)

app.run(debug=True)
