from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Välkommen till din första Flask-app!"


if __name__ == "__main__":
    app.run(debug=True)
