from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Välkommen till din första Flask-app!"


@app.route("/hello/<name>")
def hello(name):
    return f"Hej {name}!"


if __name__ == "__main__":
    app.run(debug=True)
