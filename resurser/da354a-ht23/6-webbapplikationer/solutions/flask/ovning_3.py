from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def index():
    return "Välkommen till din första Flask-app!"


@app.route("/hello/<name>")
def hello(name):
    return f"Hej {name}!"


@app.route("/form")
def form():
    return """
        <form action="/form" method="post">
            <label for="name">Skriv ditt namn:</label>
            <input id="name" name="name" type="text" required />
            <button type="submit">Skicka</button>
        </form>
    """


@app.route("/form", methods=["POST"])
def form_submit():
    name = request.form.get("name")
    return f"Hej, {name}!"


if __name__ == "__main__":
    app.run(debug=True)
