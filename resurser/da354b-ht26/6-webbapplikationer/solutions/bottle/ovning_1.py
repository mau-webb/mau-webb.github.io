from bottle import route, run


@route("/")
def index():
    return "Välkommen till din första Bottle-app!"


run(host="localhost", port=8080, debug=True)
