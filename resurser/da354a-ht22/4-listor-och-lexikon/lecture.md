---
id: da354a-ht22
title: "Modul 4 - Listor & Lexikon"
---

# Modul 4 - Listor & Lexikon

## Föreläsning

<div class="frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.1972%;"><iframe src="https://speakerdeck.com/player/63c76f062b684143857e84a26925dd42" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="encrypted-media;"></iframe></div>
</div>

[Ni kan ladda ner föreläsningen i PDF här](../pdf/2021-listor.pdf)

---

<div class="video-frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.25%;"><iframe src="https://www.youtube.com/embed/LE7bjJ_0zHA?rel=0" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture;"></iframe></div>
</div>

---

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
numbers = [5, 10, 27, 85, 16, 21, 4, 3, 13, 100]

total_sum = 0

numbers.append(69)

print(numbers)

for number in numbers:
    total_sum += number

print(total_sum/len(numbers))
```

### En boklista

```python
def print_books(books):
    print("\nBooks")
    print("*"*30)
    for i, book in enumerate(books, start=1):
        print(f"{i}: {book}")

books = [
    "12 rules of life",
    "Vindens skugga",
    "Wheele of time",
    "Harry Potter",
    "Forgotten Valentine"
]

print_books(books)

books.append("Sapiens")
books.insert(0, "Alkemisten")

while input("Vill du lägga till en ny bok? ").lower() == "ja":
    book = input("Ange en bok: ")
    books.append(book)

print_books(books)

remove_book = input("Vilken bok vill du ta bort? ")
if remove_book in books:
    books.remove(remove_book)
else:
    print("Boken finns inte i listan")

print_books(books)

```

### Listor & Lexikon

```python
pets = [
    {
        "name": "Malte",
        "animal": "Hund",
        "size": "Liten",
        "age": 1,
        "color": ["Vit"]
    },
    {
        "name": "Tiger",
        "animal": "Katt",
        "size": "Stor",
        "age": 11,
        "color": ["Orange", "Vit"]
    }
]

for pet in pets:
    print(f"{pet['name']} är en {pet['size'].lower()} {pet['animal'].lower()} och har färgerna {', '.join(pet['color'])}")

```