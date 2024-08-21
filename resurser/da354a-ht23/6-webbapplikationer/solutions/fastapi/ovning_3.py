from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
def root():
    return "Välkommen till din första FastAPI-app!"


@app.get("/hello/{name}")
def hello(name: str):
    return f"Hej {name}!"


@app.get("/form", response_class=HTMLResponse)
def form():
    return """
        <form action="/form" method="post">
            <label for="name">Skriv ditt namn:</label>
            <input id="name" name="name" type="text" required />
            <button type="submit">Skicka</button>
        </form>
    """


@app.post("/form", response_class=HTMLResponse)
async def form_submit(request: Request):
    form_data = await request.form()
    name = form_data.get("name")
    return f"Hej {name}!"
