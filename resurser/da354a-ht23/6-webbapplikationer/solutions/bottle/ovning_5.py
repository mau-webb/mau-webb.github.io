from os import error
from bottle import route, run, request, error
from bottle import jinja2_template as template, TEMPLATE_PATH
import os

# Ställ in relativ väg för templates
template_path = os.path.join(os.path.dirname(__file__), "views")
TEMPLATE_PATH.insert(0, template_path)


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


@error(404)
def error404(error):
    return "404 - Sidan kunde inte hittas."


@route("/good-morning")
def good_morning():
    return template("good_morning_template.html")


run(host="localhost", port=8080, debug=True)
