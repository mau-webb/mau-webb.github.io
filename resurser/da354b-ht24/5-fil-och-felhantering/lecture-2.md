---
id: da354b-ht24
title: "Modul 5 - Fil- och felhantering i Python"
---

# Modul 5 - Fil- och felhantering i Python

Dagens föreläsning hade ingen presentation. Se bild och kod nedan.

![Bild på tabell](../images/20241211_120416.jpg)
![Bild på tabell](../images/20241211_120428.jpg)
![Bild på tabell](../images/20241211_120433.jpg)

<!--
![Bild på tabeller](https://lh3.googleusercontent.com/pw/ADCreHeHNyWwP4uig9-XJ30WvVm4J4H_YedopfRUxoyFU1USDwSKmeo_NmFi07POjfEpa5mIxRl5YmniudhYjh21m-46WG434SusqZOBe2ATlCwAzQ3xlydXNc778YsnWC9GQ-_DnuqM0uNxFWqumPrRJnMWE-KFyUhLQBQ-eLEz6ZTR_kbqNekMK9S6AalTrFMjVEXb55PUtFQTMEhgAC8wigYAqHNK_-cS8oVYRD4TzopNle5LQH7JvWXahUPxUiTV3Pk8YAQR-P-bLBGKxA0FBSkY6BtoFY3nvui8f0mI2Mb1Bm6UGfi8PnjdwxDp_6avJNWwdPiN1-dp6fRu7NCMKdB221sZSlwadiUWi-EHvw3eObfOKm9smpW7KnL6_CW_Y6DpdQdPxstCrNIrOWZD-9mZCQPDzAJPWsWr-x2UvmehkYbohNlSYurrKtg_rhVdED4R-nK595BJZXIvRKvi4xqq9KA16PWEiBElMtMBAMVpb7-PRo2UyvBeurw_B0AJWTvaA8hSTtu0j2cPonacxJt0KRyf4XazYecD3dMghDu6myeyqyAcjNKAtNKppQeQPZo3O5BILljMmhjpiRMbqqzsOpQ2c-N7-FF_aYtktzNnbtEsoFLNyldlE-y0hsZJUw729T5zlYw8JAs1kVmGK-hJVHSX1QgtdCFQN9N8I-N0utOE1pJ0c7IL0FB6eJ5IDeBhuXZa9G4XTeOKCwc2ABrMTJkFQn3wZPmv9Wa7QExL9IenfPekWlOVKoP-73Qnygfal50K-ODS9QHhAGoR22RdzD07BryNL3B_UtP6z6zzlkYAHUt-vn-VqX2qhCuP3BRS-Y0LtCVivxgJt0B2HxsOWWZYM4oXYYc0mmJMDgV1kBgAKTy3RSQa3280H9-AZZtdES992xJpOBOe4BF_L1rR6mvcrjNmZEw9qoLtmg=w1696-h955-s-no-gm?authuser=0)
-->

**OBS - dagens tillfälle spelades inte in**, detta då det var mycket ritande på tavlan och det var svårt att spela in det på ett bra och pedagogiskt sätt. Istället lägger jag upp extratillfället från förra året, där vi går igenom samma principer som vi gjorde på plats idag.

Vill ni ha dagens exempelkod så hittar ni den [på denna länk](https://github.com/mau-webb/mau-webb.github.io/raw/master/resurser/da354b-ht24/5-fil-och-felhantering/files/extra-files.zip).

## Föreläsning - Extra

**OM NI TITTAR PÅ FÖRELÄSNINGEN NEDAN** Tänk på att det är från tidigare version av kursen och att ev. kursinfor **INTE ÄR AKTUELL** (t.ex. deadlines, information om inlämningsuppgifter, etc.).

<div class="video-frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.25%;"><iframe src="https://www.youtube.com/embed/j0h_zr0ecos?rel=0" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share;"></iframe></div>
</div>

---

![Bild på tabeller](../images/DA354A-tabell-produkter.png)

---


## Dagens exempel

### Shop - CSV-format

#### shop.py

```python
def main():
    """Vår huvudfunktion som startar upp och kör vårt program"""

    FILE_NAME = "products.csv"

    products = read_products_from_file(FILE_NAME)

    print(products)
    
    while True:

        print_menu()

        choice = input("Val: ")

        if choice == "1":
            print_products(products)
        elif choice == "2":
            add_product(products)
        elif choice == "3":
            remove_product(products)
        elif choice == "4":
            search_for_products(products)
        elif choice == "5":
            save_products_to_file(products, FILE_NAME)
        elif choice == "0":
            break # Avsluta programmet
        else:
            print("Du valde inte ett giltligt alternativ, försök igen")

def search_for_products(product_list):
    """Söker efter produkter
    
    Args:
        product_list (list): Lista på produkterna
    """
    print("="*50)
    print("Sök efter produkter")
    print("="*50)
    search_string = input("Söksträng: ")
    search_results = []

    for product in product_list:
        if search_string in product[1]:
            search_results.append(product)

    if len(search_results) == 0:
        print("Det finns inga produkter för den söksträngen")
    else:
        print_products(search_results)


def remove_product(product_list):
    """Tar bort en product
    
    Args:
        product_list (list): Lista på produkterna
    """
    print("="*50)
    print("Ta bort en product")
    print("="*50)
    remove_id = input("Id: ")
    product_removed = False

    for product in product_list:
        if product[0] == remove_id:
            product_list.remove(product)
            product_removed = True

    if product_removed == True:
        print("Produkt borttagen!")
    else:
        print("Det finns ingen produkt med det id:t")

def save_products_to_file(product_list, file_name):
    """Sparar producterna i angiven fil
    
    Args:
        product_list (list): Lista på produkterna
        file_name (str): Namnet på filen
    """
    # Öppnar filen i skrivläge (write)
    my_file = open(file_name, "w")
    # Går igenom varje produkt i produktlistan (för varje produkt i listan av produkter)
    for product in product_list:
        # Slår ihop listan av en produkt till en sträng, t.ex. ["1", "iPhone 15",  "Apple", "15000"] till "1;iPhone 15;Apple;15000"
        product_as_a_string = ";".join(product)
        # Skriver nuvarande produkt (t.ex. "1;iPhone 15;Apple;15000") till filen
        my_file.write(f"{product_as_a_string}\n")
    # Stänger filen
    my_file.close()
    

def add_product(product_list):
    """Lägger till en produkt i listan
    
    Args:
        product_list (list): Lista på produkterna
    """
    print("="*50)
    print("Lägg till en product")
    print("="*50)
    product_id = input("Id: ")
    title = input("Titel: ")
    brand = input("Tillverkare: ")
    price = input("Pris: ")

    product = [product_id, title, brand, price]
    product_list.append(product)
    

def print_products(product_list):
    """Skriver ut produkterna
    
    Args:
        product_list (list): Lista på produkterna
    """
    print("="*50)
    print("Produkter")
    print("="*50)
    print(f"{'Id':<15}{'Produkt':<15}{'Tillverkare':<15}{'Pris':<15}")
    print("-"*50)
    for product in product_list:
        for item in product:
            print(f"{item:<15}", end="")
        print("")

def print_menu():
    """Skriver ut programmets meny"""
    print("="*25)
    print("Meny")
    print("="*25)
    print("1) Visa produkter")
    print("2) Lägg till en produkt")
    print("3) Ta bort en produkt")
    print("4) Sök efter en produkt")
    print("5) Spara produkter till fil")
    print("0) Avsluta")

def read_products_from_file(file_name):
    """Läser in en fil och returnerar produkterna som en nästlad lista, t.ex.
    
    [
        [
            "1",
            "iPhone 16",
            "Apple",
            "16000"
        ],
        [
            "2",
            "Pixel 9",
            "Google",
            "10000"
        ]
    ]
    
    Args:   
        file_name (str): Namnet på filen där produkterna finns sparade i CSV

    Returns
        list: En nästlad lista på våra produkter
    """
    try:
        my_file = open(file_name, "r")
        data = my_file.read()
        my_file.close()

        products = []

        for product in data.split("\n"):
            item = product.split(";")
            if len(item) == 4:
                products.append(item)

        return products
    except FileNotFoundError:
        my_file = open(file_name, "w")
        my_file.close()

        return []


main()
```

#### products.csv

```
1;iPhone 16;Apple;16000
2;Pixel 9;Google;10000
4;Apple;Bonderna;5
5;Penna;Bic;100

```

<!--
### Shop - JSON-format

#### shop.py

```python
def main():
    """Huvudfunktionen i programmet som hantera välkomnande av användaren,
    inläsning av produkter från vår json-fil "products.json" samt menyn i programmet.
    """
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
    """Sparar våra produkter till given fil

    Args:
        file_name (str) : Sökvägen till den fil som ska användas
        products (list) : En lista innehållandes listor (produkter) som ska sparas
    """
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
    """Lägger till en produkt i vår produktlista

    Args:
        products (list) : En lista innehållandes listor (produkter)
    """
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
    """Frågar efter en söksträng och skriver ut sökresultaten för given söksträng

    Args:
        products (list) : En lista innehållandes listor (produkter)
    """
    print("\nSök efter en produkt")
    print("-------------------")
    product_name = input("Produktnamn: ")

    print("\nSökträffar:")
    for product in products:
        if product_name in product[1]:
            print(f"- {product[0]}: {product[1]} ({product[2]}) - {product[3]}")
    


def print_products(products):
    """Skriver ut alla produkterna i vår produktlista

    Args:
        products (list) : En lista innehållandes listor (produkter)
    """
    print("\nProdukter")
    print("{:<10}{:<10}{:<10}{:<10}".format("Id", "Produkt", "Märke", "Pris"))
    print("-"*40)
    for product in products:
        if len(product) == 4:
            for item in product:
                print(f"{item:<10}", end="")
            print("")
          

def print_menu():
    """Skriver ut programmets meny"""
    print("\nMenu")
    print("-"*40)
    print("1) Skriv ut alla produkter")
    print("2) Lägg till en produkt")
    print("3) Ta bort en produkt")
    print("4) Spara produkterna till filen")
    print("5) Sök efter produkt")
    print("0) Avsluta")

def read_products_from_file(file_name):
    """Läsa in filen (file_name) och returnera produkterna som en lista:
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
    """
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
    """Skriver ut välkomstmeddelande"""
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
-->