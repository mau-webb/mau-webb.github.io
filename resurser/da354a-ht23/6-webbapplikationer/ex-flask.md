---
id: da354a-ht23
title: "Modul 6 - Webbapplikationer - Flask"
---

# Övningsuppgifter - Flask

## Introduktion

I dessa övningar kommer du att få prova på grunderna i att bygga en enkel webbapplikation med hjälp av [Flask](https://flask.palletsprojects.com/en/3.0.x/). Flask är ett kraftfullt och flexibelt ramverk som ger en bra förståelse för hur webbapplikationer fungerar.

## Övning 1: Installera Flask och skapa din första webbsida

### Mål

Kom igång med Flask genom att installera ramverket och skapa en enkel webbsida.

### Instruktioner

1. Öppna terminalen.
2. Installera Flask genom att köra följande kommando:
   ```bash
   pip install Flask
   ```
   **OBS!** Det ska vara `Flask`, och inte `flask`.

3. Skapa en ny Python-fil som du kan kalla `app.py` och lägg in följande kod:
```python
   from flask import Flask

   app = Flask(__name__)

   @app.route("/")
   def index():
       return "Välkommen till din första Flask-app!"

   if __name__ == "__main__":
       app.run(debug=True)
   ```

3. Kör din applikation genom att köra följande kommando:
   ```bash
   python app.py
   ```
4. Öppna din webbläsare och navigera till [`http://localhost:5000`](http://localhost:5000). Du borde nu se texten "Välkommen till din första Flask-app!".

### Utmaningar

- Prova att ändra texten som returneras i index-funktionen och se att ändringarna syns i webbläsaren.
- Prova att lägga till en ny route som returnerar en annan text när du navigerar till en annan URL.

## Övning 2: Lägg till en route med parametrar

### Mål

Lär dig att hantera dynamiska URL genom att lägga till en route som tar emot en parameter.

### Instruktioner

1. Utöka din app.py-fil med följande kod:
   ```python
   @app.route("/hello/<name>")
   def hello(name):
       return f"Hej {name}!"
   ```
2. Spara filen. Om servern har krashat kan du behöva starta den igen.
3. Gå till [`http://localhost:5000/hello/DittNamn`](http://localhost:5000/hello/DittNamn)) i din webbläsare och ersätt DittNamn med ditt namn.

### Utmaningar

- Experimentera med att lägga till fler rutter som tar emot olika typer av parametrar, som till exempel siffror eller datum.
- Prova att skapa en route som tar emot två parametrar och returnerar en text baserat på dessa.

## Övning 3: Skapa ett enkelt formulär

### Mål

Lär dig att hantera användarinmatning genom att skapa ett enkelt formulär och hantera POST-begäran.

### Instruktioner

1. Lägg till följande rutt i din app.py-fil för att skapa ett formulär:
```python
   from flask import request

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
   ```

2. Spara filen. Om servern har krashat kan du behöva starta den igen.
3. Gå till [`http://localhost:5000/form`](http://localhost:5000/form) och fyll i formuläret med ditt namn.

### Utmaning

- Lägg till ett fält för ålder och visa ett meddelande som innehåller både namn och ålder.

## Övning 4: Hantera fel och skapa en 404-sida

### Mål

Lär dig att hantera fel genom att skapa en enkel 404-sida.

### Instruktioner

1. Lägg till följande kod för att fånga upp icke-existerande sidor:
```python
   @app.errorhandler(404)
   def page_not_found(e):
       return "404 - Sidan kunde inte hittas.", 404
```

2. Spara filen, starta servern vid behov.
3. Testa att besöka en sida som inte finns, till exempel [`http://localhost:5000/ingensida`](http://localhost:5000/ingensida).

### Utmaning

- Försök att göra din 404-sida mer användarvänlig, kanske med en länk tillbaka till startsidan eller en enkel navigationsmeny.

## Övning 5: Leverera HTML-templates

### Mål

Lär dig att använda Jinja2-templates för att skapa dynamiska HTML-sidor.

### Instruktioner

_Flask kommer med Jinja2 som standard, så du behöver inte installera det separat._

1. Skapa en ny mapp i din projektmapp som heter `templates`.
2. Inuti `templates`-mappen, skapa en fil som heter `good_morning.html` med följande innehåll:
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
3. Uppdatera din app.py för att använda detta template med Flask:
```python
   from flask import render_template

   @app.route('/good-morning')
   def good_morning():
       return render_template('good_morning.html')
   ```

4. Spara filen, starta servern vid behov.
5. Gå till [`http://localhost:5000/good-morning`](http://localhost:5000/good-morning) för att se din nya sida.

## Övning 6: Leverera HTML-templates med variabler

### Mål

Lär dig att skicka variabler till Jinja2-templates för att skapa dynamiska sidor.

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
2. Uppdatera din app.py-fil för att skicka en variabel till ditt template:
   ```python
   @app.route("/goodbye/<name>")
   def goodbye(name):
       return render_template("goodbye.html", name=name)
   ```

3. Spara filerna.
4. Gå till [`http://localhost:5000/goodbye/DittNamn`](http://localhost:5000/goodbye/DittNamn) och se hur variabeln `name` används i HTML-templaten. Testa att byta ut `DittNamn` mot ditt eget namn.

### Utmaning

- Prova att skapa ett nytt template för formuläret i övning 3 och uppdatera din kod så att formuläret levereras via templaten istället.
- Prova även att använd variabler för att skicka olika meddelanden beroende på användarens inmatning.

## Avslutning

Grattis! Du har nu kommit igång med att bygga en enkel webbapplikation med Flask. Genom att experimentera med olika rutter/routes, formulär och templates har du fått en bra grundförståelse för hur du kan skapa dynamiska webbsidor med hjälp av Flask. Fortsätt att experimentera och bygg vidare på dina kunskaper för att skapa mer avancerade applikationer.
