from flask import Flask, render_template_string
import os

app = Flask(__name__)

folder = "."

files = os.listdir(folder)

HTML = """
<h1>File Monitoring Dashboard</h1>

<ul>
{% for file in files %}
<li>{{ file }}</li>
{% endfor %}
</ul>
"""

@app.route("/")
def home():
    return render_template_string(HTML, files=files)

app.run(debug=True)
