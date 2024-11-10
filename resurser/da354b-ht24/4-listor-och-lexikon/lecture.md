---
id: da354b-ht24
title: "Modul 4 - Listor & Lexikon"
---

# Modul 4 - Listor & Lexikon

## Föreläsning

Publiceras efter att föreläsningen ägt rum.


<div class="frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.2696%; padding-top: 58px;"><iframe src="https://www.slideshare.net/slideshow/embed_code/key/HEz8QScQLRdQgA" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no"></iframe></div>
</div>

[Ni kan ladda ner föreläsningen i PDF här](../pdf/2023-listor.pdf)

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
    """Funktionen skriver ut den första & sista bokstaven i en sträng

    Args:
        text (str) : Texten som vi använder i funktionen
    """
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
    """Skriver ut böckerna från en given lista
    
    Args
        book_list (list): En lista med strängar som representerar boktitlar
    """
    print("\nBöcker:")
    print("--------")
    for book in book_list:
        print(f"- {book}")

def main():
    # Skapar en lista, och lägger till två böcker i den
    books = ["Harry Potter och de vises sten", "Sagan om ringen"]
    # Lägger till boken "Liftarens guide till galaxen" sist i listan
    books.append("Liftarens guide till galaxen")

    # Frågar användaren om en boktitel
    new_book = input("Vilken bok vill du lägga till? ")
    # Frågar användaren efter vilken plats i listan den ska läggas på
    new_book_position = int(input("På vilken plats vill du att boken ska ligga? "))
    # Lägger in boken på angiven plats
    books.insert(new_book_position, new_book)

    # Skriver ut listan på böcker
    print_books(books)

    # Frågar användaren om en boktitel som ska tas bort
    remove_book_title = input("Ange titeln på den bok du vill ta bort: ")

    # Kontrollerar om angiven boktitel finns listan
    if remove_book_title in books:
        # Om ja: Ta bort boktiteln
        books.remove(remove_book_title)
    else:
        # Om nej: Skriv ut att boktiteln inte fanns med i listan
        print(f"Boken: {remove_book_title} finns inte i listan av böcker!")
    
    # Skriver ut listan på böcker
    print_books(books)

    # Tar bort den sista boken i listan, och sparar den i variabeln "last_book"
    last_book = books.pop()
    print(f"Vi har tagit bort boken {last_book}")

    # Sorterar listan i alfabetisk ordning
    books.sort()

    # Skriver ut listan på böcker
    print_books(books)

# Kör huvudfunktionen
main()

```

### Listor & Lexikon

```python
teachers = [{
    "id": 2,
    "name": "Johan",
    "email": "johan.holmberg@mau.se"
}, {
    "id": 3,
    "name": "Dipak",
    "email": "dipak.surie@mau.se"
}]

person = {}
person["id"] = 1
person["name"] = "Anton"
person["email"] = "anton.tibblin@mau.se"

teachers.append(person)

# Bonus: Sortera lärarna efter deras id (stigande)
teachers.sort(key=lambda teacher: teacher["id"])


for teacher in teachers:
    id = teacher["id"]
    name = teacher["name"]
    email = teacher["email"]
    print(f"{id}: {name} ({email})")


```

-->