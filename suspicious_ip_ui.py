from flask import Flask, render_template_string

app = Flask(__name__)

ips = [
    "192.168.1.10",
    "45.33.22.10",
    "201.20.10.5"
]

HTML = """
<h1>Suspicious IP List</h1>

<ul>
{% for ip in ips %}
<li>{{ ip }}</li>
{% endfor %}
</ul>
"""

@app.route("/")
def home():
    return render_template_string(HTML, ips=ips)

app.run(debug=True)
