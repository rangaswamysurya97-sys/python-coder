from flask import Flask, render_template_string

app = Flask(__name__)

attempts = [
    ("surya", "Failed"),
    ("admin", "Success"),
    ("guest", "Failed")
]

HTML = """
<h1>Login Attempts</h1>

<table border="1">
<tr>
<th>User</th>
<th>Status</th>
</tr>

{% for user, status in attempts %}
<tr>
<td>{{ user }}</td>
<td>{{ status }}</td>
</tr>
{% endfor %}
</table>
"""

@app.route("/")
def home():
    return render_template_string(HTML, attempts=attempts)

app.run(debug=True)
