from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    title = {'titulo': 'Página principal'}
    return render_template('index.html', **title)
