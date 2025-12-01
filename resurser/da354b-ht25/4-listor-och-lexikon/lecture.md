---
id: da354b-ht25
title: "Modul 4 - Listor & Lexikon"
---

# Modul 4 - Listor & Lexikon

## Föreläsning

Ej publicerad ännu.

<!--

Inspelad föreläsning (från föregående år).

<div class="video-frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.25%;"><iframe src="https://www.youtube.com/embed/ts1OZoalLMM?rel=0" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share;"></iframe></div>
</div>


## Föreläsning

<div class="frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.1972%;"><iframe src="https://speakerdeck.com/player/0e9773ea9dd8419a915698bbf3afbca1" style="border: 0; top: 0; left: 0; width: 100%; height: 100%; position: absolute;" allowfullscreen scrolling="no" allow="encrypted-media"></iframe></div>
</div>

[Ni kan ladda ner föreläsningen i PDF här](../pdf/2020-listor.pdf)

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
user_text = input("Ange ditt namn: ")

# Kör funktionen "get_first_and_last_character" och med användarens namn
get_first_and_last_character(user_text)
```

### Listor

```python
# En lista med siffror
numbers = [1, 5, 10, 20, 50, 2, 100, 7]

total_sum = 0

# Räknar ut summan av alla siffrorna i listan och sparar resultatet i "total_sum"
for nr in numbers:
    total_sum += nr

# Skriver ut medelvärdet av sifforna i listan
print(total_sum/len(numbers))
```

### En boklista

```python
# En lista med 4st böcker
books = [
    "Dune",
    "Name of the Wind",
    "Think Python",
    "Alkemisten"    
]

# Frågar användaren efter en boktitel
new_book = input("Ange bok: ")
# Lägger till boktiteln sist i vår lista
books.append(new_book)


# Skriver ut alla böckerna i listan "books"
for book in books:
    print(book, end=", ") # end=", " gör att böckerna skrivs ut horisontellt med ett , mellan sig

# Skriver ut en blank rad
print()

# Lägger till boken "Mio min Mio" sist i listan "books"
books.append("Mio min Mio")
# Lägger till boken "Omgiven av idioter" sist i listan "books"
books.append("Omgiven av idioter")

# Tar bort boken "Think Python" från vår lista "books"
books.remove("Think Python")

# Skriver ut alla böckerna i listan "books"
for book in books:
    print(book, end=", ") # end=", " gör att böckerna skrivs ut horisontellt med ett , mellan sig

# Skriver ut en blank rad
print()

# Tar bort den sista bokentiteln och sparar den i variabeln "removed_book"
removed_book = books.pop()
# Skriver ut titeln på boken vi tog bort
print(f"Vi tar bort boken {removed_book}")

# Skriver ut alla böckerna i listan "books"
for book in books:
    print(book, end=", ") # end=", " gör att böckerna skrivs ut horisontellt med ett , mellan sig
```

### Listor & Lexikon

```python
'''
Ett husdjur har följande:
    - namn
    - djur
    - ålder
'''

# En lista med två husdjur
pets = [
    {
        "name": "Doug",
        "animal": "hund",
        "age": 3
    },
    {
        "name": "Pigge",
        "animal": "fisk",
        "age": 1
    }
]

# Skapar ett nytt husdjur
new_pet = {}
new_pet["name"] = input("Namn: ")
new_pet["animal"] = input("Djur: ")
new_pet["age"] = input("Ålder: ")

# Lägger till det nya husdjuret i listan "pets"
pets.append(new_pet)

# Skriver ut alla våra husdjur i listan "pets"
for pet in pets:
    print(f"{pet['name']} är en {pet['animal']} och är {pet['age']}år")
```
-->