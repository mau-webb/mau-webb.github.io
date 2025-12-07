---
id: da354b-ht25
title: "Modul 5 - Fil- och felhantering i Python"
---

# Modul 5 - Fil- och felhantering i Python

## Föreläsning

Publiceras när föreläsningen ägt rum.

<!--

<div class="frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.2696%; padding-top: 58px;"><iframe src="https://www.slideshare.net/slideshow/embed_code/key/CTVbLIArSDCXKr" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no"></iframe></div>
</div>

[Ni kan ladda ner föreläsningen i PDF här](../pdf/2024-try-except.pdf)

---

## Föreläsning från tidigare år

**OM NI TITTAR PÅ FÖRELÄSNINGEN NEDAN** Tänk på att det är från tidigare version av kursen och att ev. kursinfor **INTE ÄR AKTUELL** (t.ex. deadlines, information om inlämningsuppgifter, etc.).

<div class="video-frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.25%;"><iframe src="https://www.youtube.com/embed/5ITue0swW_U?rel=0" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture;"></iframe></div>
</div>


---


## Dagens exempel

### Exempel med try och except

```python
movies = ["Star Wars", "Titanic", "Fight club"]

# Alt 1.
index = input("Ange index: ")

if index.isdigit():
    # Användaren angett en siffra
    index_as_int = int(index)

    if index_as_int >= 0 and index_as_int < len(movies):
        print(movies[index_as_int])
    else:
        print("Du valde ett index som inte finns!")
else:
    print("Du angav inte en siffra!")


# Alt 2.
while True:
    try:
        index = int(input("Ange index: "))
        print(movies[index])
        break
    except IndexError:
        print("Du valde ett index som inte finns!")
    except ValueError:
        print("Du angav inte en siffra!")


# Bonus: Fråga efter ett nummer (tills användaren anger ett nummer)
while True:
    try:
        number = int(input("Ange ett nummer: "))
        break
    except:
        print("Du angav inte ett nummer, försök igen!")

print(f"Du valde: {number}")
```

### Läsa in en fil och skirv ut innehållet

```python
# Öppna filen
my_file = open("lyrics/goliat.txt")
# Läs in innehållet till en lista (varje rad i textfilen är en sak i listan)
lyric = my_file.readlines()
# Gå igenom listan med alla rader text
for i, line in enumerate(lyric, start=1):
    # Skriv ut aktuell rad, tillsammans med radnummer
    print(f"{i:<2}: {line}", end="")
# Stäng filen
my_file.close()
```

Filen som användes i exemplet ovan hittar ni [här](../files/Laleh-Goliat.txt)

### Try & except med filer

```python
try:
    # Öppnar filen "demo.txt" i läsläge
    my_file = open("demo.txt", "r")
    # Skriver ut innehåller i filen
    print(my_file.read())
    # Stänger vår användning av filen
    my_file.close()
except FileNotFoundError: # FileNotFoundError - Detta innebär att filen vi försöker öppna inte finns
    # Skriver ut att filen inte finns
    print("Filen finns inte!")
    # Skapar filen "demo.txt" genom att öppna den i skrivläge ("w")
    my_file = open("demo.txt", "w")
    # Skriver texten "Varsågod! =)" i filen
    my_file.write("Varsågod! =)")
    # Stänger vår användning av filen
    my_file.close()
    # Skriver ut ett snällt meddelande till användaren
    print("... men det gör inget - jag är så snäll och har skapa filen till dig! =)")


# Öppnar filen "demo.txt" i append-läge
my_file = open("demo.txt", "a")
# Lägger till texten "Kaffe är gott" som en rad sist i text-filen
my_file.write("\nKaffe är gott")
# Stänger vår användning av filen
my_file.close()
```

### Önskelista genom att skriva till fil genom *append*

```py
def main():
    """Huvudfunktion som styr vår önskelista"""

    # Vilken fil vi ska använda för att spara våra önskningar
    FILE_NAME = "wishes.txt"

    wishes = get_wishes_from_file(FILE_NAME)

    print("*"*30)
    print("Önskelista")
    print("*"*30)

    while True:
        print_menu()

        choice = input("Val: ")

        if choice == "1":
            print_wish_list(wishes)
        elif choice == "2":
            add_wish(wishes, FILE_NAME)
        elif choice == "3":
            break
        else:
            print("Du angav inte ett giltligt alternativ, försök igen")

def print_menu():
    """Skriver ut programmets menu"""
    print("\nMeny")
    print("----")
    print("1) Visa önskelista")
    print("2) Lägg till en önskning")
    print("3) Avsluta programmet")

def print_wish_list(wish_list):
    """Skriver ut önskelistan
    
    Args:
        wish_list: lista med önskningar
    """
    print("\nÖnskelista")
    print("--------------")
    for wish in wish_list:
        print(f"- {wish}", end="")

def add_wish(wish_list, file_name):
    """Skapar en ny önskning och sparar den i filen
    
    Args:
        wish_list: Lista med önskningar
        file_name: Namnet på filen där önskningen ska läggas till
    """
    print("\nNy önskning")
    print("---------------")
    new_item = input("Vad önskar du dig? ")
    # Lägger till den nya önskningen i listan som används i programmet
    wish_list.append(new_item)

    # Lägger till önskningen sist i text-filen 
    my_file = open(file_name, "a")
    my_file.write(f"{new_item}\n")
    my_file.close()


def get_wishes_from_file(file_name):
    """Hämtar önskningarna från angiven fil, om filen inte finns så skapar vi den
    
    Args:
        file_name: Namnet på filen som ska läsas in

    Returns:
        Lista med önskningar
    """
    try:
        my_file = open(file_name, "r")
        content = my_file.readlines()
        my_file.close()
        return content
    except FileNotFoundError:
        print("Filen finns inte, så jag är supersnäll och skapar den till dig =)")
        my_file = open(file_name, "w")
        my_file.close()
        return []

main()
```

<!--

```python
def main():
    FILE_NAME = "wishes.txt"
    wishes = get_wishes_from_file(FILE_NAME)

    print("*"*30)
    print("Önskelista")
    print("*"*30)

    while True:
        print_menu()

        choice = input("Ange val: ")

        if choice == "1":
            print_wish_list(wishes)
        elif choice == "2":
            add_wish(wishes, FILE_NAME)
        elif choice == "3":
            remove_wish(wishes, FILE_NAME)
        elif choice == "4":
            break # Avsluta programmet
        else:
            print("Du valde ett felaktigt alternativ, försök igen.")

def remove_wish(wish_list, filename):
    print("\nTa bort en önskning")
    print("---------------")
    remove_item = input("Ange önskning att ta bort: ")
    try:
        wish_list.remove(remove_item)

        my_file = open(filename, "w")
        for wish in wish_list:
            my_file.write(f"{wish}\n")
        my_file.close()
    except ValueError:
        print("Saken du försökte ta bort finns inte i önskelistan")

def add_wish(wish_list, filename):
    print("\nNy önskning")
    print("---------------")
    new_item = input("Ange ny önskning: ")
    wish_list.append(new_item)
    # Lägg till önskningen i textfilen
    my_file = open(filename, "a")
    my_file.write(f"{new_item}\n")
    my_file.close()

def print_wish_list(wish_list):
    print("\nÖnskelista")
    print("---------------")
    for wish in wish_list:
        print(f"- {wish}")

def print_menu():
    print("\nMeny")
    print("1) Visa önskelista")
    print("2) Lägg till en sak i önskelistan")
    print("3) Ta bort en önskning")
    print("4) Avsluta")

def get_wishes_from_file(filename):
    try:
        my_file = open(filename, "r")
        wishes = []
        file_data = my_file.read()
        for wish in file_data.split("\n"):
            if wish != "":
                wishes.append(wish)
        my_file.close()

        return wishes
    except FileNotFoundError:
        print("Filen finns inte, men oroa dig inte - vi skapar den till dig! =)")
        my_file = open(filename, "w")
        my_file.close()
        return []
    
main()
```



### Önskelista genom att skriva till fil genom *write*

```python
def main():

    wishes = get_wishes_from_file("wishes.txt")

    print("*"*30)
    print("Önskelista")
    print("*"*30)

    while True:
        print_menu()

        choice = input("Val: ")

        if choice == "1":
            print_wish_list(wishes)
        elif choice == "2":
            add_wish(wishes, "wishes.txt")
        elif choice == "3":
            break
        else:
            print("Du angav inte ett giltigt val, försök igen")

def add_wish(wish_list, filename):
    print("\nNy önskning")
    print("-----------")
    new_item = input("Ange ny önskning: ")
    while True:
        try:
            place = int(input("Ange plats som du vill lägga in din önskning på: "))
            break
        except:
            print("Du måste ange en siffra!")


    wish_list.insert(place, new_item)

    # Spara önskelistan i filen
    my_file = open(filename, "w")
    for wish in wish_list:
        my_file.write(f"{wish}\n")

def print_wish_list(wish_list):
    print("\nÖnskelista")
    print("-----------")
    for item in wish_list:
        print(item)

def print_menu():
    print("\nMeny")
    print("----")
    print("1) Visa önskelista")
    print("2) Lägg till sak")
    print("3) Avsluta programmet")

def get_wishes_from_file(filename):
    try:
        my_file = open(filename, "r")
        data = my_file.read()
        items = data.split("\n")
        for item in items:
            if item == "":
                items.remove(item)
        my_file.close()
        return items
    except:
        print("Filen finns inte, men jag är ett snällt program, så jag skapar den till dig =)")
        my_file = open(filename, "w")
        my_file.close()
        return []
        


main()
```

### Exempel från videoinspelningen: Ett program som hanterar produkter

```python
def main():
    """Huvudfunktionen i programmet som hantera välkomnande av användaren,
    inläsning av produkter från vår textfil "products.text" samt menyn i programmet.
    """
    # 1. Skriva ut en välkomstfras
    welcome()

    # 2. Läsa in alla produkter från en text-fil
    products = read_products_from_file("products.txt")

    # 3. Skriver ut menyn - och beroende på vad användaren väljer - visar/lägger till/tar bort produkter (eller avslutar programmet)
    while True:
        print_menu()
        user_choice = input("Ange val: ")

        if user_choice == "1":
            print_products(products)
        elif user_choice == "2":
            add_product(products)
        elif user_choice == "3":
            pass # Inte implementerad än
        elif user_choice == "4":
            save_products_to_file("products.txt",products)
        elif user_choice == "0":
            break
        else:
            print("Du valde inte ett giltigt alternativ, försök igen.")

def save_products_to_file(file_name, products):
    """Sparar våra produkter till given fil

    Args:
        file_name (str) : Sökvägen till den fil som ska användas
        products (list) : En lista innehållandes strängar (produkter) som ska sparas
    """
    my_file = open(file_name, "w")
    for product in products:
        my_file.write(f"{product}\n")
    my_file.close()
    print("\nProdukterna är nu sparade i filen!")
    

def add_product(products):
    """Lägger till en produkt i vår produktlista

    Args:
        products (list) : En lista innehållandes strängar (produkter)
    """
    print("\nLägg till en produkt")
    print("-"*40)
    product = input("Ange produkt: ")
    products.append(product)


def print_products(products):
    """Skriver ut alla produkterna i vår produktlista

    Args:
        products (list) : En lista innehållandes strängar (produkter)
    """
    print("\nProdukter")
    print("-"*40)
    for i, product in enumerate(products, start=1):
        if product != "":
            print(f"{i}: {product}")
          

def print_menu():
    """Skriver ut programmets meny"""
    print("\nMenu")
    print("-"*40)
    print("1) Skriv ut alla produkter")
    print("2) Lägg till en produkt")
    print("3) Ta bort en produkt")
    print("4) Spara produkterna till filen")
    print("0) Avsluta")

def read_products_from_file(file_name):
    """Läsa in filen (file_name) och returnera produkterna som en lista:
    t.ex. ["iPhone", "Kabelsamlare", "iPad", "Tangentbord"]

    Args:
        file_name (str) : Namnet på filen vi vill öppna

    Return:
        list : En lista på produkterna som finns i filen
    """
    try:
        my_file = open(file_name, "r")
        products = my_file.read().split("\n")

        return products
    except FileNotFoundError:
        my_file = open(file_name, "w")
        my_file.close()

        return []
    

def welcome():
    """Skriver ut välkomstmeddelande"""
    print("-"*40)
    print("Antons teknikbutik")
    print("-"*40)

# Kör vårt program genom funktionen "main"
main()
```

Text-filen "products.txt" ser ut något i stil med:
```
iPhone
Kabelsamlare
iPad
Tangentbord
Bärbar dator

```
-->