from bottle import route, run


@route("/")
def index():
    return "Välkommen till din första Bottle-app!"


@route("/hello/<name>")
def hello(name):
    return f"Hej {name}!"


run(host="localhost", port=8080, debug=True)
