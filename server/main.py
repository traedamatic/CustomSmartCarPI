from flask import Flask

app = Flask(__name__)


@app.route('/command/<name>')
def command(name):
    return f"command is {name}"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
