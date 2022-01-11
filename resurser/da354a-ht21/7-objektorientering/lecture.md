---
id: da354a
title: "Modul 7 - Objektorientering"
---

# Modul 7 - Objektorientering

## Föreläsning

<div class="frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.1972%;"><iframe src="https://speakerdeck.com/player/61b652078b074fe2867e8dafc3875a19" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="encrypted-media;"></iframe></div>
</div>

[Ni kan ladda ner föreläsningen i PDF här](../pdf/lecture.pdf)

---

Videon laddas upp så fort den är färdigredigerad.

<!--
<div class="video-frame">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/rpHAU_yqtY0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
-->
---

## Dagens exempel

### MovieCollection.py

Detta är en något utökad version av den kod som vi gick igenom på dagens föreläsning.

```python
from Movie import Movie

class MovieCollection:

    def __init__(self):
        self.movies = []
        self.menu()

    def menu(self):
        while True:
            print("Meny")
            print("----")
            print("1) Visa alla filmer")
            print("2) Lägg till en film")
            print("3) Avsluta")
            user_choice = input("Ange val: ")

            if user_choice == "1":
                self.print_movies()
            elif user_choice == "2":
                self.add_movie()
            elif user_choice == "3":
                break
            else:
                print("Du angav ett felaktigt val, försök igen")
        

    def add_movie(self):
        print("\nLägg till en ny film")
        title = input("Ange titel: ")
        year = input("Ange år: ")
        self.movies.append(Movie(title, year))

    def print_movies(self):
        print("\nFilmer")
        print("-----------------")
        for movie in self.movies:
            print(movie)

MovieCollection()
```

### Movie.py

```python
class Movie:

    def __init__(self, title, year):
        self.title = title
        self.year = year
        self.actors = []
        self.time = 0

    def add_actor(self, actor):
        self.actors.append(actor)

    def get_actor(self):
        return self.actors

    def __str__(self):
        return f"{self.title} ({self.year})"
```