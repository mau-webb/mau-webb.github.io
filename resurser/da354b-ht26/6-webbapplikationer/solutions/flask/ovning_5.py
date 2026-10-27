from flask import Flask, request, render_template


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


@app.errorhandler(404)
def page_not_found(e):
    return "404 - Sidan kunde inte hittas.", 404


@app.route("/good-morning")
def good_morning():
    return render_template("good_morning.html")


if __name__ == "__main__":
    app.run(debug=True)
