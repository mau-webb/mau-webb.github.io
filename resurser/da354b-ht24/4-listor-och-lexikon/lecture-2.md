---
id: da354b-ht24
title: "Modul 4 - Listor & Lexikon"
---

# Modul 4 - Listor & Lexikon

## Föreläsning - Extra

Ingen presentation finns, men koden från dagens exempel hittar ni nedan.

<!--
<div class="video-frame">
<div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.25%;"><iframe src="https://www.youtube.com/embed/fTdLe3XKbQw?rel=0" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture;"></iframe></div>
</div>
-->

### Nästlade listor som tabeller

![Idle](../images/lists.png)

```python
# En lista på 4 personer, som råkar vara lärare
people = ["Anton", "Kristina", "Åse", "Johan"]
# Skriv ut varje lärare, numrerat genom index med start 1
for i, teacher in enumerate(people, start=1):
    print(f"{i}: {teacher}")

# En nästlad lista med kurser inom IA-programmet, kan liknas med följande tabellstruktur:
# 
# DA106A | Introduktion till webbutveckling               | Anton
# ---------------------------------------------------------------
# DA211A | Introduktion till studier inom datavetenskap   | Steve
# ---------------------------------------------------------------
# DA354A | Introduktion till programmering                | Anton
courses = [
    ["DA106A", "Introduktion till webbutveckling", "Anton"],
    ["DA211A", "Introduktion till datavetenskap", "Steve"],
    ["DA354A", "Introduktion till programmering", "Anton"]
]

# För varje kurs (rad) i den nästlade listan
for row in courses:
    # För varje kolumn i raden
    for col in row:
        # Skriv ut kolumnens värde, end="" innebär att print-funktionen inte radbryter
        print(col, end=" ")
    # Skriv ut en radbrytning
    print("")
```

### Bussprogram

![Idle](../images/bus.png)

```python
def main():
    """Huvudfunktionen för vårt bussprogram"""
    # Represenation av vår buss: 12 rader med 4 säte på varje rad
    bus = [
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None]
    ]

    while True:
        print_menu()

        user_choice = input("Ange val: ")

        if user_choice == "1":
            print_bus(bus)
        elif user_choice == "2":
            book(bus)
        elif user_choice == "3":
            unbook(bus)
        elif user_choice == "4":
            show_booking(bus)
        elif user_choice == "0":
            break
        else:
            print("Du valde inte ett giltigt alternativ, försök igen\n")

def show_booking(bus):
    """Visar upp vem som bokat en plats (eller om den är obokad)
    
    Args
        bus(list) : En nästlad lista som representerar en buss
    """
    row = get_row(bus)-1
    seat = get_seat(bus)-1
    if bus[row][seat] == None:
        print("Platsen är ej bokad")
    else:
        print(f"Platsen är bokad av: {bus[row][seat]}")


def book(bus):
    """Bokar en plats i bussen
    
    Args
        bus(list) : En nästlad lista som representerar en buss
    """
    print("\nBoka plats")
    print("************")
    while True:
        # 1. Välj rad
        row = get_row(bus)-1
        # 2. Välj säte
        seat = get_seat(bus)-1
        # 3. Kontrollera att vald plats är ledig
        if bus[row][seat] == None:
            # Platsen är ledig
            name = input("Vad heter du? ")
            bus[row][seat] = name
            break
        else:
            print("Platsen är upptagen, försök igen")

def unbook(bus):
    """Avbokar en plats i bussen
    
    Args
        bus(list) : En nästlad lista som representerar en buss
    """
    print("\nAvoka plats")
    print("************")
    while True:
        # 1. Välj rad
        row = get_row(bus)-1
        # 2. Välj säte
        seat = get_seat(bus)-1
        # 3. Kontrollera att sätet är bokat
        if bus[row][seat] != None:
            # Platsen är bokad
            bus[row][seat] = None
            break
        else:
            print("Platsen är inte bokad, du kan inte avboka en icke-bokad plats")


def get_seat(bus):
    """Låter användaren välja ett säte i bussen
    
    Args
        bus(list) : En nästlad lista som representerar en buss

    Returns
        int : Sätesnumret som användaren valt
    """
    while True:
        seat = input("Säte: ")
        if seat.isdigit() == False:
            print("Sätet måste anges som en siffra")
            continue

        # Gör om användarens valda säta till datatypen siffra
        seat = int(seat)

        if seat < 1 or seat > len(bus[0]):
            print("Den platsen finns inte i bussen")
            continue

        return seat

def get_row(bus):
    """Låter användaren välja en rad i bussen
    
    Args
        bus(list) : En nästlad lista som representerar en buss

    Returns
        int : Radsnumret som användaren valt
    """
    while True:
        row = input("Rad: ")
        if row.isdigit() == False:
            print("Raden måste anges som en siffra")
            continue

        # Gör om användarens rad till datatypen siffra
        row = int(row)

        if row < 1 or row > len(bus):
            print("Raden finns inte i denna buss")
            continue

        return row



def print_bus(bus):
    """Skriver ut en översikt över bussens bokningar
    
    Args
        bus(list) : En nästlad lista som representerar en buss
    """"
    print("\nBussen")
    print("****************")
    print("   1 2  3 4")
    for i, row in enumerate(bus, start=1):
        print(f"{i:>2} ", end="")
        for j, seat in enumerate(row, start=0):
            if seat == None:
                print("- ", end="")
            else:
                print("x ", end="")

            if j == 1:
                print(" ", end="")
        print("")


def print_menu():
    """Skriver ut menyn för programmet"""
    print("\nMeny")
    print("**********")
    print("1) Visa bussen")
    print("2) Boka plats")
    print("3) Avboka plats")
    print("4) Se vem som bokat en plats")
    print("0) Avsluta")

main()

```