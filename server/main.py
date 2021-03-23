from flask import Flask

app = Flask(__name__)


@app.route('/command/<name>')
def command(name):
    return f"command is {name}"
