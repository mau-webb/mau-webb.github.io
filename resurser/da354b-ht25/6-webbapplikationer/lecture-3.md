---
id: da354b-ht25
title: "Modul 6 - Webbapplikationer"
---

# Modul 6 - Webbapplikationer

## Föreläsning - Önskelista

### Video från tidigare kursversioner

<div class="video-frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.25%;"><iframe src="https://www.youtube.com/embed/vV-QGKb2xN8?rel=0" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture;"></iframe></div>
</div>

[Ni kan ladda ner hela exemplet genom github här](https://github.com/Tibbelit/Wishlist-for-christmas)

---

## Exempellösning av önskelistan

### my_app.py

```python
from bottle import run, route, template, static_file, request, redirect
import json

def read_wishes_from_file():
    """Returns a list of wishes, from file: "wishes.json"
	
	Example result:
	[
        {
            "id": 1,
            "title": "iPhone",
            "link": "https://www.apple.com/se/iphone-14/",
            "prio": 1
        },
        {
            "title": "Pixel 7 Pro",
            "link": "https://store.google.com/se/product/pixel_7_pro?hl=sv&pli=1",
            "prio": "1",
            "id": 2
        }
	]

	Returns:
		list : The wishes
	"""
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

def create_id(wish_list):
    """Returns an integer representing the current highest id + 1
    
    Returns
        int : the current highest id + 1
    """
    highest_id = 1
    for wish in wish_list:
        if wish["id"] >= highest_id:
            highest_id = wish["id"] + 1 

    return highest_id

@route("/")
def index():
    """Returns the start page
	
	Returns:
		template : index
	"""
    wishes = read_wishes_from_file()
    return template("index", wishes=wishes)

@route("/new-wish", method="post")
def new_wish():
    """Registers a new wish, then redirects the user to the start page"""
    wish_title = getattr(request.forms, "title")
    wish_link = getattr(request.forms, "link")
    wish_prio = getattr(request.forms, "prio")

    wishes = read_wishes_from_file()
    wish_id = create_id(wishes)

    wishes.append({
        "title": wish_title,
        "link": wish_link,
        "prio": wish_prio,
        "id": wish_id
    })

    my_file = open("wishes.json", "w")
    my_file.write(json.dumps(wishes, indent=4))
    my_file.close()

    redirect("/")

@route("/delete-wish/<id>")
def delete_wish(id):
    """Deletes a wish with, using the id of the wish
    
    Args:
        id (str): The id of the wish that should be deleted
    """
    id_to_delete = int(id)

    wishes = read_wishes_from_file()

    for wish in wishes:
        if wish["id"] == id_to_delete:
            wishes.remove(wish)

    my_file = open("wishes.json", "w")
    my_file.write(json.dumps(wishes, indent=4))
    my_file.close()

    redirect("/")

@route("/static/<filename>")
def static_files(filename):
    """Handles the routes to our static files
	
	Returns:
		file : the static file requested by URL	
	"""
    return static_file(filename, root="static")

# Start our web server
run(host="127.0.0.1", port=8080, reloader=True)
```

### index.html (OBS - ska ligga i mappen "views")
```html
<!DOCTYPE html>
<html lang="sv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Önskelista</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Mountains+of+Christmas:wght@400;700&family=Quicksand:wght@300..700&display=swap" rel="stylesheet">
    <link href="/static/style.css" rel="stylesheet">
</head>
<body>
    <h1>Min Önskelista</h1>
    <article id="wish">
        <h2>Önskningar</h2>
        % for wish in wishes:
        <div class="wish-item">
            <a href="{% raw %}{{ wish["link"] }}{% endraw %}" target="_blank" class="wish-a prio-{% raw %}{{ wish["prio"] }}{% endraw %}">{% raw %}{{ wish["title"] }}{% endraw %}</a>
            <a href="/delete-wish/{% raw %}{{ wish["id"] }}{% endraw %}" class="delete-a">Radera</a>
        </div>
        % end
        
        <h2>Lägg till en önskning</h2>

        <form id="add-wish-form" action="/new-wish" method="post">
            <label for="wish-title">Titel</label>
            <input type="text" id="wish-title" name="title" required>
            <label for="wish-link">Länk</label>
            <input type="url" id="wish-link" name="link" required>
            <label for="wish-prio">Prio</label>
            <select id="wish-prio" name="prio" required>
                <option>Välj prio här</option>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
            </select>
            <input type="submit" value="Spara önskning">
        </form>
    </article>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
    <script src="/static/jquery.snowfall.js"></script>
    <script>
        $("body").snowfall($("#wish"));
    </script>
</body>
</html>
```

### wishes.json

```json
[
    {
        "title": "Radiostyrd bil",
        "link": "https://www.webhallen.com/se/product/337361-Gear4Play-360-Stunt-Car-V2?utm_source=google&utm_medium=cpc&utm_campaign=Pmax%20%7C%20Bestsellers&gad_source=1&gclid=CjwKCAiAgoq7BhBxEiwAVcW0LDgBCffDM2RU2vrE8JE5FRHdsNVg5RvQy-NK_PgRxoxAQmD2MWIX6hoCLCwQAvD_BwE",
        "prio": "1",
        "id": 1
    },
    {
        "title": "Moccamaster",
        "link": "https://www.elgiganten.se/product/hem-hushall-tradgard/kaffemaskiner-te/kaffebryggare/moccamaster-one-switch-kaffebryggare-53751-svart/789125?utm_source=google&utm_medium=cpc&utm_campaign=PLA%20-%20Shopping%20Campaign%20PLA%20-%20Kaffemaskiner%20%26%20Te&utm_id=16005606872&gad_source=1&gclid=CjwKCAiAgoq7BhBxEiwAVcW0LIkczsVu3m54xhrp4J0pgnQh8EmWy2m4uVHrp-9Dc1OzCTRUUTjrdRoCkOoQAvD_BwE",
        "prio": "1",
        "id": 3
    },
    {
        "title": "Resevoarpenna",
        "link": "https://penstore.se/platinum/desk-fountain-pen?utm_source=google&utm_medium=cpc&utm_campaign=18216731403&gad_source=1&gclid=CjwKCAiAgoq7BhBxEiwAVcW0LHRwEAw9fiGx_RQviQ8ws1UHJfR1PnS3g6Dh5Pa4R429gV_-Zx8nbBoCjQAQAvD_BwE",
        "prio": "3",
        "id": 4
    }
]
```