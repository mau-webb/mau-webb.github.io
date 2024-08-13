---
id: da354a-ht23
title: "Modul 6 - Webbapplikationer - FastAPI"
---

# Övningsuppgifter - FastAPI

## Introduktion

I dessa övningar kommer du att få prova på grunderna i att bygga en enkel webbapplikation med hjälp av [FastAPI](https://fastapi.tiangolo.com/). FastAPI är ett modernt och snabbt ramverk för att bygga webbtjänster med Python.

## Övning 1: Installera FastAPI och skapa din första route

### Mål

Kom igång med FastAPI genom att installera ramverket och skapa en enkel endpoint.

### Instruktioner

1. Öppna terminalen.
2. Installera FastAPI och en Uvicorn genom att köra följande kommando:
   ```bash
   pip install fastapi uvicorn
   ```
3. Skapa en ny Python-fil som du kan kalla `main.py` och lägg in följande kod:

   ```python
    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/")
    def root():
        return "Välkommen till din första FastAPI-app!"
   ```

4. Kör din applikation genom att köra följande kommando:
   ```bash
    uvicorn main:app --reload
   ```
5. Öppna din webbläsare och navigera till [`http://localhost:8000`](http://localhost:8000). Du borde nu se texten `"Välkommen till din första FastAPI-app!"`.

### Utmaningar

- Prova att ändra texten som returneras i read_root-funktionen och se att ändringarna syns i webbläsaren.
- Prova att lägga till en ny route som returnerar en annan text när du navigerar till en annan URL, t.ex. `/mau` som returnerar `"Malmö universitet"`.

## Övning 2: Lägg till en route med parametrar

### Mål

Lär dig att hantera dynamiska URL genom att lägga till en route som tar emot en parameter.

### Instruktioner

1. Utöka din `main.py`-fil med följande kod:

   ```python
     @app.get("/hello/{name}")
    def hello(name: str):
        return f"Hej {name}!"
   ```

2. Spara filen. Servern uppdateras automatiskt om du körde kommmandot `uvicorn main:app --reload`. (Det är `--reload` som gör att servern uppdateras automatiskt när du sparar filen.)
3. Gå till [`http://localhost:8000/hello/DittNamn`](http://localhost:8000/hello/DittNamn) i din webbläsare och ersätt DittNamn med ditt namn.

### Utmaningar

- Experimentera med att lägga till fler routes som tar emot olika typer av parametrar, som till exempel siffror eller datum.
- Prova att skapa en route som tar emot två parametrar, till exempel namn och ålder, och returnerar en text baserat på dessa.

## Övning 3: Skapa en route som hanterar formulärdata

### Mål

Lär dig att hantera användarinmatning genom att skapa en route som tar emot data från ett formulär.

### Instruktioner

1. Installera det nödvändiga biblioteket för att hantera formulärdata:

   ```bash
   pip install python-multipart
   ```

2. Lägg till följande kod i din main.py-fil för att skapa ett enkelt formulär:

   ```python
   from fastapi import Request
   from fastapi.responses import HTMLResponse

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
      return f"Hej {name}"
   ```

3. Spara filen.
4. Öppna din webbläsare och navigera till [`http://localhost:8000/form`](http://localhost:8000/form). Fyll i formuläret och skicka det för att se resultatet.

### Utmaningar

- Lägg till ålder i formuläret och returnera en text som inkluderar både namn och ålder. Tips: använd `form_data.get("ID")` för att hämta åldern från formuläret.
- Returnera en anpassad hälsningsfras om användaren heter "Bob".
- Överkurs - Kolla på [dokumentationen för FastAPI](https://fastapi.tiangolo.com/tutorial/request-forms/) och hitta ett bättre sätt att hämta data från formulär.

## Övning 4: Skapa en anpassad 404-sida

### Mål

Lär dig att hantera fel genom att skapa en anpassad 404-sida för att visa ett meddelande när användaren försöker navigera till en route som inte finns.

### Instruktioner

1. Använd FastAPI inbyggda funktion för att hantera icke-existerande routes genom att lägga till följande kod i din main.py-fil:

   ```python
   from fastapi.responses import PlainTextResponse

   @app.exception_handler(404)
   async def custom_404_handler(request, exc):
     return PlainTextResponse("404 - Sidan kunde inte hittas.", status_code=404)
   ```

2. Spara filen.
3. Testa att besöka en route som inte finns, till exempel [`http://localhost:8000/ingensida`](http://localhost:8000/ingensida), för att se din 404-sida.

### Utmaningar

- Prova att lägga till en anpassad 404-sida.

## Övning 5: Leverera HTML-sidor med FastAPI

### Mål

Lär dig att leverera HTML-sidor med FastAPI genom att använda templates.

### Instruktioner

1. Installera Jinja2 för att kunna använda templating-motorn:
   ```bash
    pip install jinja2
   ```
2. Skapa en ny mapp i din projektmapp som heter `templates`.
3. Inuti `templates`-mappen, skapa en fil som heter `good-morning.html` med följande innehåll:
   ```html
   <!DOCTYPE html>
   <html lang="sv">
     <head>
       <meta charset="UTF-8" />
       <meta name="viewport" content="width=device-width, initial-scale=1.0" />
       <title>Godmorgon!</title>
     </head>
     <body>
       <h1>Godmorgon!</h1>
       <p>Kul att du ville titta in.</p>
     </body>
   </html>
   ```
4. Uppdatera din `main.py` för att använda detta template med FastAPI:

   ```python
   from fastapi.templating import Jinja2Templates
   from fastapi import Request

   templates = Jinja2Templates(directory="templates")

   @app.get("/good-morning")
   def good_morning(request: Request):
       return templates.TemplateResponse("good-morning.html", {"request": request})
   ```

5. Spara filen.
6. Öppna din webbläsare och navigera till [`http://localhost:8000/good-morning`](http://localhost:8000/good-morning) för att se din HTML-sida.

### Utmaningar

- Skapa fler HTML-sidor och leverera dem via FastAPI.

## Övning 6: Använda variabler i HTML-sidor

### Mål

Lär dig att skicka variabler till templates för att skapa dynamiska HTML-sidor.

### Instruktioner

1. Skapa en ny fil i `templates`-mappen som heter `goodbye.html` med följande innehåll:
   ```html
   <!DOCTYPE html>
   <html lang="sv">
     <head>
       <meta charset="UTF-8" />
       <meta name="viewport" content="width=device-width, initial-scale=1.0" />
       <title>Hej då, {{ name }}!</title>
     </head>
     <body>
       <h1>Hej då, {{ name }}!</h1>
     </body>
   </html>
   ```
2. Uppdatera din main.py-fil för att skicka en variabel till ditt template:
   ```python
    @app.get("/goodbye/{name}")
    def goodbye(name, request: Request):
        return templates.TemplateResponse("goodbye.html", {"request": request, "name": name})
   ```
3. Spara filen.
4. Gå till [`http://localhost:8000/goodbye/DittNamn`](http://localhost:8000/goodbye/DittNamn) och se hur variabeln `name` används i HTML-templaten. Testa att byta ut `DittNamn` mot ditt eget namn.

### Utmaningar

- Skapa ett nytt template för formuläret i övning 3 och uppdatera din kod så att formuläret levereras via templaten istället.
- Använd variabler för att skicka olika meddelanden beroende på användarens inmatning.

## Avslutning

Grattis! Du har nu kommit igång med att bygga en enkel webbapplikation med FastAPI. Genom att experimentera med olika routes, formulär och templates har du fått en bra grundförståelse för hur du kan skapa dynamiska webbsidor och applikationer med hjälp av FastAPI. Fortsätt att experimentera och bygg vidare på dina kunskaper för att skapa mer avancerade applikationer.

### Kul att veta (Överkurs)

Visste du att du faktiskt har byggt ett webb-API nu? FastAPI genererar automatiskt dokumentation för ditt API, som du kan se på [`http://localhost:8000/docs`](http://localhost:8000/docs). Där kan du utforska och testa dina routes direkt i webbläsaren. Webb-API:er är något som vi kommer lära oss mer om i kursen [Webbtjänster (DA109A)](https://utbildningsinfo.mau.se/kurs/da109a) som ni kommer att läsa längre fram i utbildningen.
