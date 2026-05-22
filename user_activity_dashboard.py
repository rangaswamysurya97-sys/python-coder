from flask import Flask, render_template_string

app = Flask(__name__)

activities = [
    ("surya", "Logged In"),
    ("admin", "Downloaded File"),
    ("guest", "Failed Login")
]

HTML = """
<h1>User Activity Dashboard</h1>

<table border="1">

<tr>
<th>User</th>
<th>Activity</th>
</tr>

{% for user, activity in activities %}
<tr>
<td>{{ user }}</td>
<td>{{ activity }}</td>
</tr>
{% endfor %}

</table>
"""

@app.route("/")
def home():
    return render_template_string(HTML, activities=activities)

app.run(debug=True)
