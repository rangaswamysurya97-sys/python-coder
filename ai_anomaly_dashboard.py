from flask import Flask, render_template_string

app = Flask(__name__)

results = [
    ("192.168.1.10", "Normal"),
    ("192.168.1.99", "Anomaly")
]

HTML = """
<h1>AI Anomaly Dashboard</h1>

<table border="1">

<tr>
<th>IP Address</th>
<th>Status</th>
</tr>

{% for ip, status in results %}
<tr>
<td>{{ ip }}</td>
<td>{{ status }}</td>
</tr>
{% endfor %}

</table>
"""

@app.route("/")
def home():
    return render_template_string(HTML, results=results)

app.run(debug=True)
