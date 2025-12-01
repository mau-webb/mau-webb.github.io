---
id: da354b-ht25
title: "Modul 4 - Listor & Lexikon"
---

# Modul 4 - Listor & Lexikon

## Föreläsning

<div class="frame">
    <embed
        src="../pdf/2025-listor.pdf"
        type="application/pdf"
        frameBorder="0"
        scrolling="auto"
        style="width: 100%; height: 55vh;"
    >
</div>

<!--

Inspelad föreläsning (från föregående år).

<div class="video-frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.25%;"><iframe src="https://www.youtube.com/embed/ts1OZoalLMM?rel=0" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share;"></iframe></div>
</div>


## Föreläsning

<div class="frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.1972%;"><iframe src="https://speakerdeck.com/player/0e9773ea9dd8419a915698bbf3afbca1" style="border: 0; top: 0; left: 0; width: 100%; height: 100%; position: absolute;" allowfullscreen scrolling="no" allow="encrypted-media"></iframe></div>
</div>

-->

[Ni kan ladda ner föreläsningen i PDF här](../pdf/2025-listor.pdf)

## Dagens exempel

### Strängar som sekvens av data

```python
# Låter användaren ange en sträng
text = input("Ange en text: ")

# Kontrollerar av strängen *bara* innehåller siffror
if text.isdigit():
    print("Innehåller bara siffror")
else:
    print("Innehåller inte bara siffror")

# Kontrollerar av strängen *bara* innehåller siffror
if text.isalpha():
    print("Innehåller bara bokstäver")
else:
    print("innehåller inte bara bokstäver")

# Skriver ut strängen i stora bokstäver (versaler)
print(text.upper())

# Skriver ut strängen i små bokstäver (gemener)
print(text.lower())

def get_first_and_last_character(text):
    '''
    Funktionen skriver ut den första & sista bokstaven i en sträng

    Args:
        text (str) : Texten som vi använder i funktionen
    '''
    print(f"Texten: {text} börjar på {text[0]} och slutar på {text[-1]}")

# Frågar användaren efter hens namn
user_text = input("Ange en text: ")

# Kör funktionen "get_first_and_last_character" och med användarens namn
get_first_and_last_character(user_text)
```

### Listor

```python
# En lista med siffror
numbers = [5, 10, 20, 17, 18, 200]

# Frågar användaren efter ett nummer, och gör om det till ett tal
user_number = int(input("Ange nummer: "))

# Lägger in talet först i listan
numbers.insert(0, user_number)

# Tar bort värdet 17 från listan
numbers.remove(17)

# Skriver ut alla tal i listan
for nr in numbers:
    print(nr, end=" ")
```

### En boklista

```python
def print_books(books):
    """Skriver ut en lista med boktitlar

    Args:
        books (str) : En lista med boktitlar
    """
    print("Att läsa-lista")
    print("--------------")
    for book in books:
        print(f"- {book}")

# En lista med 5 st boktitlar
books = [
    "Pride and prejudice",
    "It ends with us",
    "Jaktsäsong",
    "Morgon i Jenin",
    "Divine comedy"
]

# Skriver ut boktitlarna
print_books(books)

# Tar bort den sista boktiteln (Divine comedy) ur listan och sparar i variabeln: last_book
last_book = books.pop()

# Skriver ut vilken bok vi tog bort
print(f"Vi tog bort {last_book}")

# Skriver ut boktitlarna
print_books(books)

# Skapar boktiteln "If"
new_book = "If"

# Lägger till boktiteln "If" sist i listan av böcker
books.append(new_book)

# En loop som frågar användaren om man vill lägga till fler böcker (ända tills man svarar något annat än "ja")
while input("Vill du lägga till en ny bok? ").lower() == "ja":
    # Frågar användaren efter en boktitel
    user_book = input("Ange titel på bok: ")
    # Lägger till boktiteln sist i listan
    books.append(user_book)

# Skriver ut boktitlarna
print_books(books)

# Frågar användaren om vilken boktitel vi ska ta bort
delete_book = input("Vilken bok vill du ta bort? ")

# Kontrollerar om boktiteln finns i listan
if delete_book in books:
    # Boktiteln finns - tar bort den
    books.remove(delete_book)
else:
    # Boktiteln finns inte - skriver ut felmeddelande
    print("Boken du försöker ta bort finns inte i listan")

# Sorterar böckerna i alfabetisk ordning
books.sort()

# Skriver ut boktitlarna
print_books(books)
```

### Listor & Lexikon

```python
'''
Ett husdjur har följande:
    - namn
    - djur
    - ålder
    - färger
'''

def print_pet(pet):
    """Skriver ut ett hurdjur

    Args:
        pet (dict) : Ett lexikon som representerar ett husdjur
    """
    print(pet["name"])
    print("*"*10)
    print(f"Djur: {pet['animal']}")
    print(f"Ålder: {pet['age']}")
    print(f"Färger: {", ".join(pet['colors'])}")


# Skapar en lista med två husdjur (varje husdjur är ett lexikon) 
pets = [{
    "name": "Pigge",
    "animal": "Blåsfisk",
    "age": 21,
    "colors": ["grå"]
}, {
    "name": "Tiger",
    "animal": "Katt",
    "age": 7,
    "colors": ["vit", "brun", "svart"]
}]

# Skapar ett tredje husdjur
pet = {}
pet["name"] = "Malte"
pet["animal"] = "Hund"
pet["age"] = 3
pet["colors"] = ["vit", "svart"]

# Lägger till husdjuret sist i listan
pets.append(pet)

# Skriver ut husdjuren
for p in pets:
    print_pet(p)
```