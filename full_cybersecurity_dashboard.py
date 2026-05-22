from flask import Flask, render_template_string

app = Flask(__name__)

alerts = [
    "Malware Detected",
    "Suspicious Login",
    "Firewall Active"
]

users = [
    ("surya", "Online"),
    ("admin", "Offline")
]

threats = [
    "SQL Injection",
    "Brute Force"
]

HTML = """

<h1>Full Cybersecurity Dashboard</h1>

<h2>Alerts</h2>
<ul>
{% for alert in alerts %}
<li>{{ alert }}</li>
{% endfor %}
</ul>

<h2>Users</h2>
<table border="1">

<tr>
<th>User</th>
<th>Status</th>
</tr>

{% for user, status in users %}
<tr>
<td>{{ user }}</td>
<td>{{ status }}</td>
</tr>
{% endfor %}

</table>

<h2>Threats</h2>

<ul>
{% for threat in threats %}
<li>{{ threat }}</li>
{% endfor %}
</ul>

"""

@app.route("/")
def home():
    return render_template_string(
        HTML,
        alerts=alerts,
        users=users,
        threats=threats
    )

app.run(debug=True)
