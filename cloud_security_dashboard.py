from flask import Flask, render_template_string

app = Flask(__name__)

cloud = [
    ("AWS", "Secure"),
    ("Azure", "Secure"),
    ("GCP", "Warning")
]

HTML = """
<h1>Cloud Security Dashboard</h1>

<table border="1">

<tr>
<th>Cloud</th>
<th>Status</th>
</tr>

{% for name, status in cloud %}
<tr>
<td>{{ name }}</td>
<td>{{ status }}</td>
</tr>
{% endfor %}

</table>
"""

@app.route("/")
def home():
    return render_template_string(HTML, cloud=cloud)

app.run(debug=True)
