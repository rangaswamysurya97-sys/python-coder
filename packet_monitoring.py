from flask import Flask, render_template_string

app = Flask(__name__)

packets = [
    ("192.168.1.1", "192.168.1.10"),
    ("10.0.0.1", "10.0.0.2")
]

HTML = """
<h1>Packet Monitoring Dashboard</h1>

<table border="1">

<tr>
<th>Source</th>
<th>Destination</th>
</tr>

{% for src, dst in packets %}
<tr>
<td>{{ src }}</td>
<td>{{ dst }}</td>
</tr>
{% endfor %}

</table>
"""

@app.route("/")
def home():
    return render_template_string(HTML, packets=packets)

app.run(debug=True)
