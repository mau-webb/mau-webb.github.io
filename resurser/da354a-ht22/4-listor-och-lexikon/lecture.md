---
id: da354a-ht22
title: "Modul 4 - Listor & Lexikon"
---

# Modul 4 - Listor & Lexikon

## Föreläsning

<div class="frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.2696%; padding-top: 58px;"><iframe src="https://www.slideshare.net/slideshow/embed_code/key/14PuX1SgBjEYgm" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="encrypted-media;"></iframe></div>
</div>

[Ni kan ladda ner föreläsningen i PDF här](../pdf/2022-listor.pdf)

---
<!--
<div class="video-frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.25%;"><iframe src="https://www.youtube.com/embed/LE7bjJ_0zHA?rel=0" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture;"></iframe></div>
</div>
-->

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
def print_books(book_list):
    print("\nBöcker")
    print("*"*25)
    for i, book in enumerate(book_list, start=1):
        print(f"{i}: {book}")


books = [
    "Ondskan",
    "Utvandrarna",
    "Clean code"
]

book = input("Ange boken du vill ta bort: ")
if book in books:
    # Boken finns
    books.remove(book)
else:
    print("Boken finns inte i listan")

# Skriv ut alla böckerna
print_books(books)

# Fråga användaren efter en bok
new_book = input("Ange en titel: ")

# Lägg till boken sist i listan
books.append(new_book)

# Skriv ut alla böckerna
print_books(books)

# Fråga användaren efter en ny bok
new_book_2 = input("Ang en titel som ska hamna först i listan: ")

# Lägg boken först i listan
books.insert(0, new_book_2)

# Skriv ut alla böckerna
print_books(books)

# Ta bort den sista boken
removed_book = books.pop()
print(f"Nu tog vi bort: {removed_book}")

# Be användaren om att ta bort en bok
book_to_be_removed = input("Ange titeln på boken du vill ta bort: ")
books.remove(book_to_be_removed)

# Skriv ut alla böckerna
print_books(books)

```

### Listor & Lexikon

```python
users = [{
        "id": 1,
        "name": "Anton",
        "email": "anton.tibblin@mau.se"
    },{
        "id": 2,
        "name": "Johan",
        "email": "johan.holmberg@mau.se"
    }, {
        "id": 3,
        "name": "Dipak",
        "email": "dipak.surie@mau.se"
    }
]

for user in users:
    print(f"Id: {user['id']}")
    print(f"Namn: {user['name']}")
    print(f"Email: {user['email']}")
    print("")

```
