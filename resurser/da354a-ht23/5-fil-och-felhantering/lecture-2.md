---
id: da354a-ht23
title: "Modul 5 - Fil- och felhantering i Python"
---

# Modul 5 - Fil- och felhantering i Python

Presentation & kod presenteras efter tillfället den 6:e december.

<!--

Dagens föreläsning hade ingen presentation. Se bild och kod nedan.

![Bild på tabeller](../images/20221206_151422.jpg)


**OBS - dagens tillfälle spelades inte in**, detta då det var mycket ritande på tavlan och det var svårt att spela in det på ett bra och pedagogiskt sätt. Istället lägger jag upp extratillfället från förra året, där vi går igenom samma principer som vi gjorde på plats idag.

Vill ni ha dagens exempelkod så hittar ni den [på denna länk](https://github.com/mau-webb/mau-webb.github.io/raw/master/resurser/da354a-ht23/5-fil-och-felhantering/files/extra-files.zip).

## Föreläsning - Extra

<div class="video-frame">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/j0h_zr0ecos" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

---

![Bild på tabeller](../images/DA354A-tabell-produkter.png)

---

## Dagens exempel

### Shop - CSV-format

#### shop.py

```python
def main():
    '''
    Huvudfunktionen i programmet som hantera välkomnande av användaren,
    inläsning av produkter från vår fil "products.csv" samt menyn i programmet.
    '''
    # 1. Skriva ut en välkomstfras
    welcome()

    # 2. Läsa in alla produkter från en text-fil
    products = read_products_from_file("products.csv")

    # 3. Skriver ut menyn - och beroende på vad användaren väljer - visar/lägger till/tar bort produkter (eller avslutar programmet)
    while True:
        print_menu()
        user_choice = input("Ange val: ")

        if user_choice == "1":
            print_products(products)
        elif user_choice == "2":
            add_product(products)
        elif user_choice == "3":
            remove_product(products)
        elif user_choice == "4":
            save_products_to_file("products.csv",products)
        elif user_choice == "5":
            search_product(products)
        elif user_choice == "0":
            break
        else:
            print("Du valde inte ett giltigt alternativ, försök igen.")

def save_products_to_file(file_name, products):
    '''
    Sparar våra produkter till given fil

    Args:
        file_name (str) : Sökvägen till den fil som ska användas
        products (list) : En lista innehållandes listor (produkter) som ska sparas
    '''
    my_file = open(file_name, "w")
    for product in products:
        my_file.write("{}\n".format(";".join(product)))
    my_file.close()
    print("\nProdukterna är nu sparade i filen!")
    
def remove_product(products):
    """
    Tar bort en produkt (som användaren väljer genom id)

    Args:
        products (list) : En lista innehållandes listor (produkter)
    """
    print("\nTa bort en produkt")
    print("-------------------")
    product_id = input("Id: ")
    for product in products:
        if product[0] == product_id:
            products.remove(product)
            print("Produkten har tagit bort!")
            return
            
def add_product(products):
    '''
    Lägger till en produkt i vår produktlista

    Args:
        products (list) : En lista innehållandes listor (produkter)
    '''
    print("\nLägg till en produkt")
    print("-"*40)
    product_id = input("Ange id: ")
    product_name = input("Ange produkt: ")
    product_brand = input("Ange märke: ")
    product_price = input("Ange pris: ")
    
    products.append([
        product_id,
        product_name,
        product_brand,
        product_price
    ])

def search_product(products):
    '''
    Frågar efter en söksträng och skriver ut sökresultaten för given söksträng

    Args:
        products (list) : En lista innehållandes listor (produkter)
    '''
    print("\nSök efter en produkt")
    print("-------------------")
    product_name = input("Produktnamn: ")

    print("\nSökträffar:")
    for product in products:
        if product_name in product[1]:
            print(f"- {product[0]}: {product[1]} ({product[2]}) - {product[3]}")
    


def print_products(products):
    '''
    Skriver ut alla produkterna i vår produktlista

    Args:
        products (list) : En lista innehållandes listor (produkter)
    '''
    print("\nProdukter")
    print("{:<10}{:<10}{:<10}{:<10}".format("Id", "Produkt", "Märke", "Pris"))
    print("-"*40)
    for product in products:
        if len(product) == 4:
            for item in product:
                print(f"{item:<10}", end="")
            print("")
          

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
    print("5) Sök efter produkt")
    print("0) Avsluta")

def read_products_from_file(file_name):
    '''
    Läsa in filen (file_name) och returnera produkterna som en lista:
    t.ex.
    [
        [
            "1",
            "iPhone 14",
            "Apple",
            "14000"
        ],
        [
            "2",
            "Pixel 7",
            "Google",
            "7900"
        ]
    ]

    Args:
        file_name (str) : Namnet på filen vi vill öppna

    Return:
        list : En lista på produkterna som finns i filen
    '''
    try:
        my_file = open(filename, "r")
        data = my_file.read()
        my_file.close()

        products = []

        for row in data.split("\n"):
            if len(row.split(";")) == 4:
                products.append(row.split(";"))

        return products
        
    except FileNotFoundError:
        my_file = open(filename, "w")
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

#### products.csv

```
1;iPhone 14;Apple;14000
3;AX-3000;Asus;1900
4;WH1000XM3;Sony;3000
5;Pixel 7;Google;7900
6;Active 7;Jabra;1800

```

### Shop - JSON-format

#### shop.py

```python
def main():
    '''
    Huvudfunktionen i programmet som hantera välkomnande av användaren,
    inläsning av produkter från vår json-fil "products.json" samt menyn i programmet.
    '''
    # 1. Skriva ut en välkomstfras
    welcome()

    # 2. Läsa in alla produkter från en text-fil
    products = read_products_from_file("products.csv")

    # 3. Skriver ut menyn - och beroende på vad användaren väljer - visar/lägger till/tar bort produkter (eller avslutar programmet)
    while True:
        print_menu()
        user_choice = input("Ange val: ")

        if user_choice == "1":
            print_products(products)
        elif user_choice == "2":
            add_product(products)
        elif user_choice == "3":
            remove_product(products)
        elif user_choice == "4":
            save_products_to_file("products.csv",products)
        elif user_choice == "5":
            search_product(products)
        elif user_choice == "0":
            break
        else:
            print("Du valde inte ett giltigt alternativ, försök igen.")

def save_products_to_file(file_name, products):
    '''
    Sparar våra produkter till given fil

    Args:
        file_name (str) : Sökvägen till den fil som ska användas
        products (list) : En lista innehållandes listor (produkter) som ska sparas
    '''
    my_file = open(file_name, "w")
    my_file.write(json.dumps(products, indent=4))
    my_file.close()
    print("\nProdukterna är nu sparade i filen!")

def remove_product(products):
    """
    Tar bort en produkt (som användaren väljer genom id)

    Args:
        products (list) : En lista innehållandes listor (produkter)
    """
    print("\nTa bort en produkt")
    print("-------------------")
    product_id = input("Id: ")
    for product in products:
        if product[0] == product_id:
            products.remove(product)
            print("Produkten har tagit bort!")
            return

def add_product(products):
    '''
    Lägger till en produkt i vår produktlista

    Args:
        products (list) : En lista innehållandes listor (produkter)
    '''
    print("\nLägg till en produkt")
    print("-"*40)
    product_id = input("Ange id: ")
    product_name = input("Ange produkt: ")
    product_brand = input("Ange märke: ")
    product_price = input("Ange pris: ")
    
    products.append([
        product_id,
        product_name,
        product_brand,
        product_price
    ])

def search_product(products):
    '''
    Frågar efter en söksträng och skriver ut sökresultaten för given söksträng

    Args:
        products (list) : En lista innehållandes listor (produkter)
    '''
    print("\nSök efter en produkt")
    print("-------------------")
    product_name = input("Produktnamn: ")

    print("\nSökträffar:")
    for product in products:
        if product_name in product[1]:
            print(f"- {product[0]}: {product[1]} ({product[2]}) - {product[3]}")
    


def print_products(products):
    '''
    Skriver ut alla produkterna i vår produktlista

    Args:
        products (list) : En lista innehållandes listor (produkter)
    '''
    print("\nProdukter")
    print("{:<10}{:<10}{:<10}{:<10}".format("Id", "Produkt", "Märke", "Pris"))
    print("-"*40)
    for product in products:
        if len(product) == 4:
            for item in product:
                print(f"{item:<10}", end="")
            print("")
          

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
    print("5) Sök efter produkt")
    print("0) Avsluta")

def read_products_from_file(file_name):
    '''
    Läsa in filen (file_name) och returnera produkterna som en lista:
    t.ex.
    [
        [
            "1",
            "iPhone 14",
            "Apple",
            "14000"
        ],
        [
            "2",
            "Pixel 7",
            "Google",
            "7900"
        ]
    ]

    Args:
        file_name (str) : Namnet på filen vi vill öppna

    Return:
        list : En lista på produkterna (listor) som finns i filen
    '''
    try:
        my_file = open(file_name, "r")
        data = my_file.read()
        products = json.loads(data)

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

#### products.json

```json
[
    [
        "1",
        "iPhone 14",
        "Apple",
        "14000"
    ],
    [
        "2",
        "Mini",
        "DAWOO",
        "13000"
    ],
    [
        "3",
        "AX-3000",
        "Asus",
        "1900"
    ],
    [
        "4",
        "WH1000XM3",
        "Sony",
        "3000"
    ]
]
```