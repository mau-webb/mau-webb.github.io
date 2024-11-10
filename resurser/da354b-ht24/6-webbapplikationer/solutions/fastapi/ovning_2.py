from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return "Välkommen till din första FastAPI-app!"


@app.get("/hello/{name}")
def hello(name: str):
    return f"Hej {name}!"
