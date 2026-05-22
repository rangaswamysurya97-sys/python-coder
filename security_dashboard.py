from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<h1>System Security Dashboard</h1>

<ul>
<li>Firewall : Active</li>
<li>Antivirus : Running</li>
<li>Threat Level : Low</li>
</ul>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

app.run(debug=True)
