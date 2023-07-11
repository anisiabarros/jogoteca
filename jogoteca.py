# flask-2.3.2
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/inicio')
def ola():
    return render_template('lista.html')

app.run()
