---
id: da354b-ht25
title: "Modul 6 - Webbapplikationer - Bottle"
---

# Övningsuppgifter - Bottle

## Introduktion

I dessa övningar kommer du att få prova på grunderna i att bygga en enkel webbapplikation med hjälp av [Bottle](https://bottlepy.org/docs/dev/index.html). Bottle är enkelt att komma igång med och ger en bra grundförståelse för hur webbapplikationer fungerar.

## Övning 1: Installera Bottle och skapa din första webbsida

### Mål

Kom igång med Bottle genom att installera ramverket och skapa en enkel webbsida.

### Instruktioner

1. Öppna terminalen.
2. Installera Bottle genom att köra följande kommando:
   ```bash
   pip install bottle
   ```
3. Skapa en ny Python-fil som du kan kalla `app.py` och lägg in följande kod:

   ```python
   from bottle import route, run

   @route("/")
   def index():
       return "Välkommen till din första Bottle-app!"

   run(host="localhost", port=8080, debug=True)
   ```

4. Kör din applikation genom att köra följande kommando:
   ```bash
   python app.py
   ```
5. Öppna din webbläsare och navigera till [`http://localhost:8080`](http://localhost:8080). Du borde nu se texten "Välkommen till din första Bottle-app!".

#### Utmaningar

- Prova att ändra texten som returneras i `index`-funktionen och se att ändringarna syns i webbläsaren.
- Prova att lägga till en ny route som returnerar en annan text när du navigerar till en annan URL (route visar på vilken URL som ska användas för att nå en viss funktion).

## Övning 2: Lägg till en route med parametrar

### Mål

Lär dig att hantera dynamiska URL genom att lägga till en rutt som tar emot en parameter.

### Instruktioner

1. Utöka din app.py-fil med följande kod:
   ```python
   @route("/hello/<name>")
   def hello(name):
       return f"Hej {name}!"
   ```
2. Spara filen och starta om din server om den redan körs.
3. Gå till [`http://localhost:8080/hello/DittNamn`](http://localhost:8080/hello/DittNamn) i din webbläsare och ersätt DittNamn med ditt namn.

#### Utmaningar

- Experimentera med att lägga till fler rutter som tar emot olika typer av parametrar, som till exempel siffror eller datum.
- Prova att skapa en route som tar emot två parametrar och returnerar en text baserat på dessa.

## Övning 3: Skapa ett enkelt formulär

### Mål

Lär dig att hantera användarinmatning genom att skapa ett enkelt formulär och hantera POST-begäran.

### Instruktioner

1. Lägg till följande rutt i din app.py-fil för att skapa ett formulär:
```python
   from bottle import request

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
   ```

2. Spara filen och starta om din server.
3. Gå till [`http://localhost:8080/form`](http://localhost:8080/form) och fyll i formuläret med ditt namn.

### Utmaning

- Lägg till ett fält för ålder och visa ett meddelande som innehåller både namn och ålder.

## Övning 4: Hantera fel och skapa en 404-sida

### Mål

Lär dig att hantera fel genom att skapa en enkel 404-sida.

### Instruktioner

1. Lägg till följande kod för att fånga upp icke-existerande sidor:
```python
   from bottle import error

   @error(404)
   def error404(error):
       return "404 - Sidan kunde inte hittas."
   ```
2. Spara filen och starta om din server.
3. Testa att besöka en sida som inte finns, till exempel [`http://localhost:8080/ingensida`](http://localhost:8080/ingensida).

### Utmaning

- Försök att göra din 404-sida mer användarvänlig, kanske med en länk tillbaka till startsidan eller en enkel navigationsmeny.

## Övning 5: Leverera HTML-templates

### Mål

Lär dig att använda Jinja2-templates för att skapa dynamiska HTML-sidor.

### Instruktioner

1. Installera Jinja2 genom att köra:
   ```bash
   pip install jinja2
   ```
2. Skapa en ny mapp i din projektmapp som heter `views`.
3. Inuti `views`-mappen, skapa en fil som heter `good_morning_template.html` med följande innehåll:
   ```html
   <!DOCTYPE html>
   <html lang="sv">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Godmorgon!</title>
   </head>
   <body>
       <h1>Godmorgon!</h1>
       <p>Kul att du ville titta in.</p>
   </body>
   </html>
   ```
4. Uppdatera din app.py för att använda detta template med Jinja2:
   ```python
   from bottle import jinja2_template as template, TEMPLATE_PATH

   # Ställ in relativ väg för templates
   template_path = os.path.join(os.path.dirname(__file__), "views")
   TEMPLATE_PATH.insert(0, template_path)

   @route("/good-morning")
   def good_morning():
       return template("good_morning_template.html")

    ```
5. Spara filen och starta om din server.
6. Gå till [`http://localhost:8080/good-morning`](http://localhost:8080/good-morning) och se hur HTML-templaten används för att visa hälsningen.

## Övning 6: Leverera HTML-templates med variabler

### Mål

Lär dig att skicka variabler till Jinja2-templates för att skapa dynamiska sidor.

### Instruktioner

1. Skapa en ny fil i `views`-mappen som heter `goodbye_template.html` med följande innehåll:
   ```html
   <!DOCTYPE html>
   <html lang="sv">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Hej då,{% raw %}{{name}}{% endraw %}!</title>
   </head>
   <body>
       <h1>Hej då,{% raw %}{{name}}{% endraw %}!</h1>
   </body>
   </html>
   ```
2. Uppdatera din app.py-fil för att skicka en variabel till ditt template:
   ```python
   @route("/goodbye/<name>")
   def goodbye(name):
       return template("goodbye_template.html", name=name)
   ```
3. Spara filen och starta om din server.
4. Gå till [`http://localhost:8080/goodbye/DittNamn`](http://localhost:8080/goodbye/DittNamn) och se hur variabeln `name` används i HTML-templaten.

### Utmaning
- Skapa ett nytt template för formuläret i övning 3 och uppdatera din kod så att formuläret levereras via templaten istället.

## Avslutning

Grattis! Du har nu kommit igång med att bygga en enkel webbapplikation med Bottle. Genom att experimentera med olika rutter/routes, formulär och templates har du fått en bra grundförståelse för hur du kan skapa dynamiska webbsidor med hjälp av Bottle. Fortsätt att experimentera och bygg vidare på dina kunskaper för att skapa mer avancerade applikationer.
