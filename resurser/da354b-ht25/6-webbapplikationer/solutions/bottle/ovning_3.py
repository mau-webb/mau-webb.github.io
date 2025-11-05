from bottle import route, run, request


@route("/")
def index():
    return "Välkommen till din första Bottle-app!"


@route("/hello/<name>")
def hello(name):
    return f"Hej {name}!"


@route("/form")
def form():
    return """
        <form action="/form" method="post">
            <label for="name">Skriv ditt namn:</label>
            <input id="name" name="name" type="text" required />
            <button type="submit">Skicka</button>
        </form>
    """


@route("/form", method="POST")
def form_submit():
    name = request.forms.get("name")
    return f"Hej, {name}!"


run(host="localhost", port=8080, debug=True)
