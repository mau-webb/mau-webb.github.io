from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return "Välkommen till din första FastAPI-app!"
