---
id: da354a-ht21
title: "Modul 6 - Webbapplikationer"
---

# Modul 6 - Webbapplikationer

## Föreläsning (extra)

<div class="video-frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.25%;"><iframe src="https://www.youtube.com/embed/ctGAG0U4V3s?rel=0" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture;"></iframe></div>
</div>

---

## Dagens exempel

[Ni kan ladda ner hela exemplet som ZIP-fil här](../zip/wish.zip)

### my_app.py

```python
from bottle import redirect, run, route, template, static_file, request
import json

def read_wishes_from_file():
    try:
        my_file = open("wishes.json", "r")
        wishes = json.loads(my_file.read())
        my_file.close()

        return wishes
    except FileNotFoundError:
        my_file = open("wishes.json", "w")
        my_file.write(json.dumps([]))
        my_file.close()

        return []

def create_id(wishes):
    highest_id = 1
    for wish in wishes:
        if wish["id"] >= highest_id:
            highest_id = wish["id"] + 1
    
    return highest_id

@route('/')
def index():
    return template("index", wishes=read_wishes_from_file())

@route('/new-wish', method="post")
def create_wish():
    title = getattr(request.forms, "title")
    price = getattr(request.forms, "price")
    link = getattr(request.forms, "link")
    prio = getattr(request.forms, "prio")

    wishes = read_wishes_from_file()
    id = create_id(wishes)

    wishes.append({
        "title": title,
        "price": price,
        "link": link,
        "prio": prio,
        "id": id
    })

    try:
        my_file = open("wishes.json", "w")
        my_file.write(json.dumps(wishes, indent=4))
        my_file.close()
    except:
        print("Det gick inte att spara önskningarna")

    redirect("/")

@route('/static/<filename>')
def static_files(filename):
    return static_file(filename, root="static")

run(host="127.0.0.1", port=8080, reloader=True)
```

### index.html (OBS - ska ligga i mappen "views")
```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Min önskelista</title>
        <link href="/static/style.css" rel="stylesheet">
        <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Mountains+of+Christmas&display=swap" rel="stylesheet">
    </head>
    <body>
        <h1>Min önskelista</h1>
        <article id="wish">
            <img src="/static/hat.png" alt="Tomteluva" id="hat">
            <img src="/static/santa.png" alt="Jultomte" id="santa">
            <h2>Mina önskningar</h2>
            % for wish in wishes:
                <a href="{{ wish['link'] }}" class="prio-{{ wish['prio'] }}">{{ wish['title'] }} ({{ wish['price'] }})</a>
            % end
            <h2>Lägg till en önskning</h2>
            <form action="/new-wish" method="post">
                <label for="title">Titel: </label>
                <input type="text" id="title" name="title">
                <label for="price">Pris: </label>
                <input type="number" id="price" name="price">
                <label for="link">Länk: </label>
                <input type="url" id="link" name="link">
                <label for="prio">Prioritering</label>
                <select name="prio" id="prio">
                    <option value="1">1 - Högsta prio</option>
                    <option value="2">2 - Medel prio</option>
                    <option value="3">3 - Lägsta prio</option>
                </select>
                <input type="submit" value="Skapa önskning">
            </form>
        </article>

        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
        <script src="/static/jquery.snowfall.js"></script>
        <script>
            $(document).snowfall({
                flakeCount : 100,
                maxSpeed : 5,
                collection: "#wish"
            });
        </script>
    </body>
</html>
```

### wishes.json

```json
[
    {
        "id": 1,
        "title": "Vinterskor",
        "price": "2499",
        "link": "https://www.naturkompaniet.se/icebug-vinterkangor-herr-detour-m-bugrip-gtx-black-2064542/?sku=7310710215216",
        "prio": "1"
    },
    {
        "title": "Vinterhandskar",
        "price": "349",
        "link": "https://www.naturkompaniet.se/hestra-handskar-unisex-work-glove-iii-naturgul-2091941/?sku=7332904087980",
        "prio": "1",
        "id": 2
    },
    {
        "title": "M\u00f6ssa",
        "price": "399",
        "link": "https://www.naturkompaniet.se/fjallraven-mossa-unisex-keb-fleece-hat-dark-grey-f77374/?sku=7323450347352",
        "prio": "2",
        "id": 3
    },
    {
        "title": "Strumpor",
        "price": "199",
        "link": "https://www.naturkompaniet.se/bola-ullstrumpor-unisex-raggsocka-grey-ex0003067/?sku=7331407077771",
        "prio": "3",
        "id": 4
    }
]
```
