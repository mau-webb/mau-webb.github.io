---
id: da354a-ht23
title: "Modul 6 - Webbapplikationer"
---

# Modul 6 - Webbapplikationer

## Föreläsning

<div class="frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.1972%;"><iframe src="https://speakerdeck.com/player/677ce9d2303b48d4a1d8805810f3f45b" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="encrypted-media;"></iframe></div>
</div>

[Ni kan ladda ner föreläsningen i PDF här](../pdf/Episode X-2021.pdf)

<!--

<div class="video-frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.25%;"><iframe src="https://www.youtube.com/embed/_6wmXRLPWXM?rel=0" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture;"></iframe></div>
</div>

-->

---

## Dagens exempel

### Bottle - Grunder: Routes & Templates

#### my_app.py

```python
from bottle import route, run, error, template

@route('/')
def index():
    return template("index")

@route('/hello')
def hello():
    return "Hello there!"

@route('/hello/<name>')
def hello_name(name):
    return template("hello", username=name)

@error(404)
def error404(error):
    return "This page do not exist"

run(host="127.0.0.1", port=8080)
```

#### index.html (OBS - ska ligga i mappen "views")
```html
<h1>Hello World</h1>
<p>Welcome to my website</p>
```

#### hello.html (OBS - ska ligga i mappen "views")
```html
<h1>Hello {{username}}</h1>
<p>Vad kul att du ville besöka vår webbplats, {{username}}</p>
```
### Star Wars-sida

I exemplet nedan har jag kommenterat koden lite mer utförligt för bättre förståelse av den.

[Ni kan ladda ner hela exemplet här](../zip/starwars.zip)

#### my_app.py

```python
from bottle import route, get, post, run, template, error, static_file, request, response, redirect
import json
import datetime	

def get_votes():
	'''Returns an object (dictionary) with the results from file: "staic/standings.json"
	
	The result is in JSON format, ex.
	{
		"empire": 13,
		"rebels": 9
	}
	
	Returns:
		dict : The results
	'''
	try:
		# Opens the file "static/standings.json" in "read" mode
		votes_file = open('static/standings.json', 'r')
		# Reads and converts the file content (JSON) to Python datatype (dictionary)
		votes = json.loads(votes_file.read())
		# Closes the file
		votes_file.close()
		# Return the votes
		return votes
	except:
		# Creates a new file called "standings.json"
		votes_file = open("static/standings.json", "w")
		# Writes the basic structure in JSON-format
		votes_file.write(json.dumps({"empire": 0, "rebels": 0}))
		# Returns the basic structure as a dictionary
		return {"empire": 0, "rebels": 0}

def get_disqus():
	'''Returns a list of comments,  from file: "staic/disqus.json"
	
	Example result:
	[
        {
            "name": "Darth Vader",
            "message": "Join the dark side, we got cookies!",
            "datetime": "2021-12-14, 18:48:43"
        },
        {
            "name": "Yoda",
            "message": "Join the light side, we got wookies!",
            "datetime": "2021-12-14, 18:49:02"
        }
    ]
	
	Returns:
		list : The results
	'''
	try:
		# Opens the file "static/disqus.json" in "read" mode
		disqus_file = open('static/disqus.json', 'r')
		# Reads and converts the file content (JSON) to Python datatype (list)
		disqusions = json.loads(disqus_file.read())
		# Closes the file
		disqus_file.close()
		# Returns the list of every posts in file
		return disqusions
	except:
		# Creates a new file called "disqus.json"
		disqus_file = open("static/disqus.json", "w")
		# Writes the basic structure in JSON-format
		disqus_file.write(json.dumps([]))
		# Returns the basic structure as an empty list
		return []

@route('/')
def index():
	'''Returns the start page
	
	Returns:
		template : index
	'''
	# Creates and returns the template "index" (views/index.html) with the current standings (votes)
	return template("index", votes=get_votes() )
	
@route('/vote', method='POST')
def vote():
	'''Register a vote, and then redirects to the start page
	
	Notes:
		- The vote is sent by a from (method = POST) with the key "vote"
		- The vote is added to the file "static/standings.json"
	'''
	# Recives the vote send from a from (method=POST) by the key "vote"
	vote = request.forms.get("vote")
	# Get the current standing (votes)
	current_votes = get_votes()
	# If the vote is for empire
	if vote == "empire":
		# Add one vote to the empire
		current_votes["empire"] = current_votes["empire"] + 1
	# If the vote is for rebels
	else:
		# Add one vote to the empire
		current_votes["rebels"] = current_votes["rebels"] + 1
	# Opens the file "static/standings.txt" in "write" mode
	votes_file = open('static/standings.json', 'w')
	# Converts the standings dictionary (current_votes) to JSON-format and saves it to text file
	votes_file.write(json.dumps(current_votes))
	# Closes the file
	votes_file.close()
	# Redirects to the start page
	redirect("/")

@route('/disqus')
def disqus():
	'''Returns the disqus page
	
	Returns:
		template : disqus
	'''
	return template("disqus", posts=get_disqus())

@post('/disqus-post', method='POST')
def save_post():
	'''Register a new disqus post, and then redirects to the disqus route
	
	Notes:
		- The disqus post is sent by a from (method = POST) with following keys
			name 	=> the author
			message => the disqus post
		- The disqus post is added to the file "static/disqus.json"
		- We also add the date/time when the post is created
	'''
	# Recives the name send from a from (method=POST) by the key "name"
	name = getattr(request.forms, "name")
	# Recives the message send from a from (method=POST) by the key "message"
	message = getattr(request.forms, "message")
	# Create a timestamp - when the post is created (i.e. 2015-12-15 14:37:31)
	date_time = datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S")

	posts = get_disqus()
	posts.append({
		"name": name,
		"message": message,
		"datetime": date_time
	})

	# Opens the file "static/disqus.json" in "write" mode
	disqus_file = open('static/disqus.json', 'w')

	disqus_file.write(json.dumps(posts, indent=4))
	# Closes the file
	disqus_file.close()
	# Creates and returns the template "disqus" (views/disqus.html) with the current disqus posts
	redirect("/disqus")

@route('/static/<filename:path>')
def server_static(filename):
	'''Handles the routes to our static files
	
	Returns:
		file : the static file requested by URL	
	'''
	return static_file(filename, root='static')


@error(404)
def error404(error):
	'''Makes a pretty error page, when page is not found (error 404)
	
	Returns:
		template : error
	'''
	return template("error")

# Start our web server
run(host='127.0.0.1', port=8080, debug=False, reloader=True)
```

#### index.html

```html
<!doctype html>
<html>
	<head>
		<title>Vote for freedom</title>
		<meta charset="utf-8">
		<link href="/static/style.css" rel="stylesheet" type="text/css">
		<script src="//code.jquery.com/jquery-1.11.3.min.js"></script>
		<script src="//code.jquery.com/jquery-migrate-1.2.1.min.js"></script>
		<script src="/static/script.js"></script>
	</head>
	<body>
		<header>
			<h1><a href="/" class="black-link">star wars  - vote</a></h1>
		</header>
		<div id="content">
			<h2>Please choose side</h2>
			<form action="/vote" method="post">
				<figure>
					<h3>Empire</h3>
					<label for="empire-radio">
						<img src="static/empire.png" alt="The empire" id="empire-logo">
					</label>
					<input type="radio" name="vote" value="empire" id="empire-radio">
				</figure>
				<figure>
					<h3>Rebels</h3>
					<label for="rebels-radio">
						<img src="static/rebels.png" alt="The rebels" id="rebels-logo">
					</label>
					<input type="radio" name="vote" value="rebels" id="rebels-radio">
				</figure>
				<input type="submit" value="Vote">
			</form>
			
			<hr>
			
			<h2>Current standing</h2>
			<figure>
				<h3>Empire</h3>
				<div class="vote-count">
					{{votes["empire"]}}
				</div>
			</figure>
			<figure>
				<h3>Rebels</h3>
				<div class="vote-count">
					{{votes["rebels"]}}
				</div>
			</figure>
			<h3><a href="/disqus" class="center">Disqus the results</a></h3>
		</div>
		<footer>
			Made by the force
		</footer>
	</body>
</html>
```

#### disqus.html

```html
<!doctype html>
<html>
	<head>
		<title>Vote for freedom</title>
		<meta charset="utf-8">
		<link href="/static/style.css" rel="stylesheet" type="text/css">
		<script src="//code.jquery.com/jquery-1.11.3.min.js"></script>
		<script src="//code.jquery.com/jquery-migrate-1.2.1.min.js"></script>
		<script src="/static/script.js"></script>
	</head>
	<body>
		<header>
			<h1><a href="/" class="black-link">star wars  - vote</a></h1>
		</header>
		<div id="content">
			<h2>Disqus the results here</h2>
			<form action="/disqus-post" method="post" id="new-post-form">
				<fieldset>
					<legend>Join the disqusion!</legend>
					<label for="name">Name:</label>
					<input type="text" id="name" name="name">
					<label for="message">Message:</label>
					<textarea name="message" id="message"></textarea>
					<input type="submit" value="Submit post">
				</fieldset>
			</form>
			% for post in posts:
				<div class="post">
					<div class="name"><strong>Name:</strong> {{ post["name"]}} <small>({{ post["datetime"] }})</small></div>
					<div class="message"><strong>Message:</strong> {{ post["message"] }}</div>
				</div>
			% end
		</div>
		<footer>
			Made by the force
		</footer>
	</body>
</html>
```

#### error.html

```html
<!doctype html>
<html>
	<head>
		<title>Vote for freedom</title>
		<meta charset="utf-8">
		<link href="/static/style.css" rel="stylesheet" type="text/css">
		<script src="//code.jquery.com/jquery-1.11.3.min.js"></script>
		<script src="//code.jquery.com/jquery-migrate-1.2.1.min.js"></script>
		<script src="/static/script.js"></script>
	</head>
	<body>
		<header>
			<h1>this is not the page you are looking for...<br><a href="/">Return to start page</a></h1>
		</header>
	</body>
</html>
```

#### style.css

```css
@font-face {
     font-family: starwars;
     src: url(/static/Starjedi.ttf);
 }

body{
	margin:0px;
	background-image:url(wall4.png);
	font-family: cambria, arial, sans-serif;
}

h1{
	font-family: starwars, Arial, sans-serif;
	font-size: 40px;
	margin:0px;
	padding:0px;
	margin:auto;
}

h2{
	text-align: center;
	font-size: 30px;
}

body > header{
	text-align: center;
	height:200px;
	line-height: 200px;
}

input[type="submit"]{
	width: 100%;
	clear:both;
	height: 40px;
	margin-bottom: 20px;
}
input[type="radio"]{
	text-align:center;
	margin:auto;
	display:block;
	margin-top:10px;
}

#content{
	width: 600px;
	margin:0 auto 25px auto;
	overflow: hidden;
	background-color: rgba(0,0,0,0.3);
	padding: 0 50px;
	border-radius:25px;
	box-shadow: 0 0 10px #000;
}

#content figure{
	width:40%;
	padding:2.5%;
	margin: 2.5%;
	float:left;
	text-align:center;
	background-color: rgba(255, 255, 255, 0.4);
	transition: all 500ms;
	border-radius: 25px;
}

#content figure.chosen{
	background-color: rgba(255, 255, 255, 1);
}

#content figure.chosen:hover{
	background-color: rgba(255, 255, 255, 1);
}

#content figure img{
	width:80%;
	cursor: pointer;
}

#content figure:hover{
	background-color: rgba(255, 255, 255, 0.6);
}

.vote-count{
	font-size: 50px;
}

.black-link{
	color: #000;
	text-decoration:none;
}

.center{
	text-align: center;
	display: block;
}

footer{
	text-align:center;
	margin-bottom:25px;
}

.post{
	background-color: rgba(255, 255, 255, 0.8);
	padding: 10px;
	border-radius: 10px;
	box-shadow: 0 0 5px #666;
	margin-bottom: 10px;
}

#new-post-form{
	margin-bottom:20px;
}

#new-post-form textarea{
	height: 50px;
}

#new-post-form label, #new-post-form input, #new-post-form textarea{
	clear: both;
	display: block;
	font-weight: bold;
	width: 100%;
	margin-bottom: 5px;
}
```

#### script.js

```js
$(document).on("ready", function(){
	$("input[type='radio']").on("change", function(){
		$("input[type='radio']").parent().removeClass("chosen");
		if($(this).prop("checked") == true){
			$(this).parent().addClass("chosen");
		}
	})
});
```