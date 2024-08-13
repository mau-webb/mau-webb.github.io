from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates


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


@app.exception_handler(404)
async def custom_404_handler(request, exc):
    return PlainTextResponse("404 - Sidan kunde inte hittas.", status_code=404)


templates = Jinja2Templates(directory="templates")


@app.get("/good-morning")
def good_morning(request: Request):
    return templates.TemplateResponse("good-morning.html", {"request": request})
