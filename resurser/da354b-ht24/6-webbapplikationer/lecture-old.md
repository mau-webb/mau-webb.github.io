---
id: da354b-ht24
title: "Modul 6 - Webbapplikationer"
---

# Modul 6 - Webbapplikationer

## Föreläsning

<div class="frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.1972%;"><iframe src="https://speakerdeck.com/player/9641e0877d124cb699cf5c568eec9d10" style="border: 0; top: 0; left: 0; width: 100%; height: 100%; position: absolute;" allowfullscreen scrolling="no" allow="encrypted-media"></iframe></div>
</div>

[Ni kan ladda ner föreläsningen i PDF här](../pdf/Presentation.pdf)

---

<div class="video-frame">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/v0imFcQHZVc" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

---

## Dagens exempel

### Bottle - Grunder: Routes & Templates

#### my_app.py

```python
from bottle import run, route, template

@route("/")
def index():
    my_name = "Anton"
    return template("index", name=my_name)

@route("/about")
def about():
    return "Här kommer om-mig sidan att finnas"

@route("/contact")
def contact():
    return "Här kommer kontakt-sidan att finnas"

run(host="127.0.0.1", port=8080)
```

### Önskelista

[Ni kan ladda ner hela exemplet här](../zip/wishes.zip)

#### my_app.py

```python
import json
from bottle import run, route, template, static_file, request, redirect

def read_wishes_from_file():
    """Läser in våra önskningar från filen "storage/wishes.json" och returnerar
    en lista enligt följande struktur:
    [
        {
            "title": "Nitro Snowboardboots Venture Tls Brown",
            "link": "https://www.standtall.se/snowboard/snowboard-boots/kille/nitro-snowboardboots-venture-tls-brown",
            "price": "2999"
        },
        {
            "title": "Appertiff Sqt Goggle Goldtooth Black",
            "link": "https://www.standtall.se/snowboard/goggles/appertiff-sqt-goggle-goldtooth-black",
            "price": "899"
        }
    ]

    Returns:
        list : En lista med önskningar (varje önskning är ett lexikon)
    """
    try:
        my_file = open("storage/wishes.json", "r")
        wishes = json.loads(my_file.read())
        my_file.close()

        return wishes
    except:
        my_file = open("storage/wishes.json", "w")
        my_file.write(json.dumps([]))
        my_file.close()

        return []

@route("/")
def index():
    """Hanterar vår startsida, genom att skicka tillbaka template: index.html

    Returns:
        str : Källkoden till vår webbsida
    """
    return template("index", wishes=read_wishes_from_file())

@route("/new-wish", method="POST")
def new_wish():
    """Sparar en önskning och skickar sedan vidare användaren till startisdan"""
    wish = getattr(request.forms, "wish")
    link = getattr(request.forms, "link")
    price = getattr(request.forms, "price")

    wishes = read_wishes_from_file()
    wishes.append({
        "title": wish,
        "link": link,
        "price": price
    })

    my_file = open("storage/wishes.json", "w")
    my_file.write(json.dumps(wishes, indent=4))
    my_file.close()

    return redirect("/")

@route("/static/<filename>")
def static_files(filename):
    """Returnerar efterfrågad fil i mappen "static""""
    return static_file(filename, "static")

run(host="127.0.0.1", port=8000)
```

#### index.html

```html
<!doctype html>
<html>
	<head>
		<title>Min önskelista</title>
		<meta charset="utf-8">
		<!-- CSS only -->
		<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
		<link href="/static/style.css" rel="stylesheet">
	</head>
	<body>
		<main>
			<article>
				<img src="/static/santa.png" alt="Jultomten" id="santa">
                <img src="/static/hat.png" alt="Tomteluva" id="hat">
				<h1>Önskelista!</h1>
				<ul id="wishes">
					% for wish in wishes:
						<li>
							<a href="{{ wish['link'] }}" target="_blank">{{ wish['title'] }} ({{ wish['price'] }})</a>
						</li>
					% end
				</ul>
			</article>
			<form action="/new-wish" method="POST">
				<label for="wish">Önskning</label>
				<input type="text" id="wish" name="wish">
				<label for="link">Länk</label>
				<input type="url" id="link" name="link">
				<label for="price">Pris</label>
				<input type="text" id="price" name="price">
				<input type="submit" value="Spara önskning">
			</form>
		</main>
		
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
		<script src="/static/snowfall.jquery.js"></script>
		<script src="/static/script.js"></script>
	</body>
</html>
```

#### style.css

```css
body {
    background-image: url("background.jpg");
}

main {
    width: 500px;
    margin: 200px auto 10px auto;
    background-color: #fff;
    overflow: hidden;
    border-radius: 10px;
    box-shadow: 0 0  10px #000;
}

main > article > h1 {
    background-color: #000;
    color: #fff;
    text-align: center;
}

main > article li, main > article ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

main > article a {
    display: block;
    padding: 10px;
    margin: 5px;
    box-shadow: 0 0 3px #999;
}

main > form {
    background-color: #000;
    color: #fff;
    padding: 10px;
}

main > form > input, main > form > label {
    display: block;
    width: 100%;
    margin-bottom: 5px;
}

#hat {
    position: absolute;
    z-index: 10;
    height: 100px;
    margin-top: -50px;
    margin-left: -75px;
}

#santa {
    position: absolute;
	z-index: 10;
    height: 150px;
    margin-top: -125px;
    margin-left: 400px;
}
```

#### script.js

```js
// https://github.com/loktar00/JQuery-Snowfall

$(document).snowfall({
    flakeCount : 100,
    maxSpeed : 5,
    maxSize: 5,
    round: true,
    collection: 'main'
});
```