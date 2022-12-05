---
id: da354a-ht22
title: "Modul 5 - Fil- och felhantering i Python"
---

# Modul 5 - Fil- och felhantering i Python

## Föreläsning

Presentation & kod presenteras efter tillfället den 5:e december.

<!--

<div class="frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.1972%;"><iframe src="https://speakerdeck.com/player/cff4fae3a76f42508adacffc29763862" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="encrypted-media;"></iframe></div>
</div>

[Ni kan ladda ner föreläsningen i PDF här](../pdf/Presentation-2021.pdf)

---

<div class="video-frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.25%;"><iframe src="https://www.youtube.com/embed/5ITue0swW_U?rel=0" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture;"></iframe></div>
</div>

---

## Dagens exempel

### Läsa in text från en fil, och skriva ut den radvis

```python
# Öppnar filen "Laleh-Goliat.txt" i läsläge
my_file = open("Laleh-Goliat.txt", "r")

# Läser in all text från filen, och splittar den till en lista vid varje radbrytning
lyric = my_file.read().split("\n")

# Loopar igenom varje sträng i listan lyric, samt skapar ett index i loopen som börjar på 1
for i, line in enumerate(lyric, start=1):
    # Skriver ut aktuell rad, tillsammans med radnummer
    print(f"{i}: {line}")
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

### Ett program som hanterar produkter

```python
def main():
    '''
    Huvudfunktionen i programmet som hantera välkomnande av användaren,
    inläsning av produkter från vår textfil "products.text" samt menyn i programmet.
    '''
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
    '''
    Sparar våra produkter till given fil

    Args:
        file_name (str) : Sökvägen till den fil som ska användas
        products (list) : En lista innehållandes strängar (produkter) som ska sparas
    '''
    my_file = open(file_name, "w")
    for product in products:
        my_file.write(f"{product}\n")
    my_file.close()
    print("\nProdukterna är nu sparade i filen!")
    

def add_product(products):
    '''
    Lägger till en produkt i vår produktlista

    Args:
        products (list) : En lista innehållandes strängar (produkter)
    '''
    print("\nLägg till en produkt")
    print("-"*40)
    product = input("Ange produkt: ")
    products.append(product)


def print_products(products):
    '''
    Skriver ut alla produkterna i vår produktlista

    Args:
        products (list) : En lista innehållandes strängar (produkter)
    '''
    print("\nProdukter")
    print("-"*40)
    for i, product in enumerate(products, start=1):
        if product != "":
            print(f"{i}: {product}")
          

def print_menu():
    '''
    Skriver ut programmets meny
    '''
    print("\nMenu")
    print("-"*40)
    print("1) Skriv ut alla produkter")
    print("2) Lägg till en produkt")
    print("3) Ta bort en produkt")
    print("4) Spara produkterna till filen")
    print("0) Avsluta")

def read_products_from_file(file_name):
    '''
    Läsa in filen (file_name) och returnera produkterna som en lista:
    t.ex. ["iPhone", "Kabelsamlare", "iPad", "Tangentbord"]

    Args:
        file_name (str) : Namnet på filen vi vill öppna

    Return:
        list : En lista på produkterna som finns i filen
    '''
    try:
        my_file = open(file_name, "r")
        products = my_file.read().split("\n")

        return products
    except FileNotFoundError:
        my_file = open(file_name, "w")
        my_file.close()

        return []
    

def welcome():
    '''
    Skriver ut välkomstmeddelande
    '''
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