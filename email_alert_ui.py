from flask import Flask, render_template_string

app = Flask(__name__)

emails = [
    ("admin@gmail.com", "Threat Alert"),
    ("security@gmail.com", "Failed Login Alert")
]

HTML = """
<h1>Email Alerts</h1>

<table border="1">

<tr>
<th>Email</th>
<th>Subject</th>
</tr>

{% for email, subject in emails %}
<tr>
<td>{{ email }}</td>
<td>{{ subject }}</td>
</tr>
{% endfor %}

</table>
"""

@app.route("/")
def home():
    return render_template_string(HTML, emails=emails)

app.run(debug=True)
