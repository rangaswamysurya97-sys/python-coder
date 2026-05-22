from flask import Flask, render_template_string

app = Flask(__name__)

users = [
    ("Admin", "Online"),
    ("Analyst", "Online"),
    ("Security Officer", "Offline")
]

HTML = """
<h1>Multi User SOC</h1>

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
"""

@app.route("/")
def home():
    return render_template_string(HTML, users=users)

app.run(debug=True)
