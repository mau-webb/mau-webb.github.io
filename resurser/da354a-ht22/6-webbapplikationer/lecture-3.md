---
id: da354a-ht22
title: "Modul 6 - Webbapplikationer"
---

# Modul 6 - Webbapplikationer

## Föreläsning (extra)

<div class="video-frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.25%;"><iframe src="https://www.youtube.com/embed/vV-QGKb2xN8?rel=0" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture;"></iframe></div>
</div>

---

## Dagens exempel

[Ni kan ladda ner hela exemplet genom github här](https://github.com/Tibbelit/Wishlist-for-christmas)

### my_app.py

```python
from bottle import run, template, route, request, redirect, static_file
import json

def read_wishes_from_file():
    '''
    Returns a list of wishes,  from file: "wishes.json"
	
	Example result:
	[
        {
            "id": 1,
            "name": "iPhone",
            "price": 14000,
            "link": "https://www.apple.com/se/iphone-14/",
            "prio": 1
        },
        {
            "name": "Pixel 7 Pro",
            "price": "9990",
            "link": "https://store.google.com/se/product/pixel_7_pro?hl=sv&pli=1",
            "prio": "1",
            "id": 2
        }
	]

	Returns:
		list : The wishes
	'''
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
    """
    Returns an integer representing the current highest id + 1
    
    Returns
        int : the current highest id + 1
    """
    highest_id = 1
    for wish in wishes:
        if wish["id"] >= highest_id:
            highest_id = wish["id"] + 1

    return highest_id

@route("/")
def index():
    '''Returns the start page
	
	Returns:
		template : index
	'''
    wishes = read_wishes_from_file()
    return template("index", wishes= wishes)

@route("/new-wish", method="post")
def new_wish():
    '''
    Registers a new wish, then redirects the user to the start page
	'''
    name = getattr(request.forms, "name")
    price = getattr(request.forms, "price")
    link = getattr(request.forms, "link")
    prio = getattr(request.forms, "prio")

    wishes = read_wishes_from_file()
    id = create_id(wishes)

    wishes.append({
        "name": name,
        "price": price,
        "link": link,
        "prio": prio,
        "id": id
    })

    my_file = open("wishes.json", "w")
    my_file.write(json.dumps(wishes, indent=4))
    my_file.close()

    redirect("/")

@route("/static/<filename>")
def static_files(filename):
    '''
    Handles the routes to our static files
	
	Returns:
		file : the static file requested by URL	
	'''
    return static_file(filename, root="static")

# Start our web server
run(host="127.0.0.1", port=8080, reloader=True)
```

### index.html (OBS - ska ligga i mappen "views")
```html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Min önskelista</title>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Mountains+of+Christmas&display=swap" rel="stylesheet">
        <link href="static/style.css" rel="stylesheet" type="text/css">
    </head>
    <body>
        <h1>Min önskelista</h1>

        <article id="wishes">
            <img src="/static/hat.png" alt="Tomteluva" id="hat"> 
            <img src="/static/santa.png" alt="Jultomte" id="santa">
            <h2>Mina önskningar</h2>
            % for wish in wishes:
                <a href="{{ wish['link'] }}" target="_blank" class="prio-{{ wish['prio'] }}">{{ wish["name"] }} ({{ wish["price"] }})</a>
            % end
            <h2 id="add-wish">Lägg till en önskning</h2>
            <form action="/new-wish" method="post">
                <label for="name">Sak:</label>
                <input type="text" id="name" name="name">
                <label for="price">Pris:</label>
                <input type="number" id="price" name="price">
                <label for="link">Länk:</label>
                <input type="url" id="link" name="link">
                <label for="prio">Prio:</label>
                <select name="prio" id="prio">
                    <option value="1">1 - Högsta prio</option>
                    <option value="2">2 - Medel prio</option>
                    <option value="3">3 - Lägsta prio</option>
                </select>
                <input type="submit" value="Spara önskning">
            </form>
        </article>

        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
        <script src="/static/jquery.snowfall.js"></script>
        <script>
            $(document).snowfall({
                flakeCount: 100,
                maxSpeed: 5,
                collection: "#wishes"
            });

            $("form").hide();
            $("#add-wish").on("click", function() {
                $("form").slideToggle();
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
        "name": "iPhone",
        "price": 14000,
        "link": "https://www.apple.com/se/iphone-14/",
        "prio": 1
    },
    {
        "name": "Pixel 7 Pro",
        "price": "9990",
        "link": "https://store.google.com/se/product/pixel_7_pro?hl=sv&pli=1",
        "prio": "1",
        "id": 2
    },
    {
        "name": "Samsung Galaxy Tab S6",
        "price": "2790",
        "link": "https://www.mediamarkt.se/sv/product/_samsung-galaxy-tab-s6-lite-wifi-64gb-surfplatta-oxford-gray-1347824.html?utm_source=google&utm_medium=cpc&utm_campaign=bb-shopping-generic&utm_term=&utm_content=1347824&gclid=CjwKCAiAheacBhB8EiwAItVO2zbXtsnm6GvWnOuehZnA4UMvdRF0iYzF-fS-OkkmQrbMS717BCp-qRoCNp8QAvD_BwE",
        "prio": "2",
        "id": 3
    },
    {
        "name": "Strumpor",
        "price": "99",
        "link": "https://www.happysocks.com/se/product/XNCG09-9300?gclid=CjwKCAiAheacBhB8EiwAItVO27prVzc3EvvWghp2WGbEEhtQrQErZrExOaqxCXyeeMY4UFn5XkSnCRoCEwkQAvD_BwE",
        "prio": "3",
        "id": 4
    }
]
```