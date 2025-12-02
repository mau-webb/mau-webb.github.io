---
id: da354b-ht25
title: "Modul 4 - Listor & Lexikon"
---

# Modul 4 - Listor & Lexikon

## Föreläsning - Nästlade listor & bussbokningsprogram

Inga presentationsslides finns från föreläsningen - se bilder och kod nedan.

![Idle](../images/table.jpg)

![Idle](../images/bus-2025.jpg)

<!--

Inspelad föreläsning (från tidigare år).

<div class="video-frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.25%;"><iframe src="https://www.youtube.com/embed/fTdLe3XKbQw?rel=0" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture;"></iframe></div>
</div>

-->

### Nästlade listor som tabeller

```python
movies = [
    ["Star Wars", 1977, "George Lucas"],
    ["Pulp fiction", 1994, "Quentin Tarantino"],
    ["Alien", 1979, "Ridly Scott"]
]


headings = ["Film", "År", "Regissör"]
for heading in headings:
    print(f"{heading : <20}", end="")
print("\n------------------------------------")

for row in movies:
    for column in row:
        print(f"{column : <20}", end="")
    print("")
```

### Bussprogram

```python
def main():
    """Huvudfunktionen i programmet som ägen bussen och sköter menyn"""
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
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None]
    ]

    user_choice = False

    while user_choice != "0":
        print_menu()

        user_choice = input("Ange val: ")
        if user_choice == "1":
            print_bus(bus)
        elif user_choice == "2":
            book(bus)
        elif user_choice == "3":
            un_book(bus)
        elif user_choice == "4":
            view_booking(bus)
        elif user_choice != "0":
            print("Du valde inte ett giltigt alternativ, försök igen!")

def view_booking(bus):
    """Visar upp en specifik bokning (vem som bokat platsen)

    Args:
        bus (list): En nästlad lista som representerar en buss
    """ 
    print("\nSe en bokning")
    print("*"*25)
    row = get_row(bus)
    seat = get_seat(bus)
    if bus[row][seat] == None:
        print("Ingen har bokat sätet")
    else:
        print(f"Sätet är bokat av: {bus[row][seat]}")

def book(bus):
    """Bokar en plats i bussen

    Args:
        bus (list): En nästlad lista som representerar en buss
    """
    while True:
        print("\nBoka plats")
        print("*"*25)
        name = input("Namn: ")
        row = get_row(bus)
        col = get_seat(bus)
        if bus[row][col] == None:
            bus[row][col] = name
            break
        else:
            print("Platsen är bokad, välj en ny plats")

def un_book(bus):
    """Avbokar en plats i bussen

    Args:
        bus (list): En nästlad lista som representerar en buss
    """
    print("\nAvboka plats")
    print("*"*25)
    row = get_row(bus)
    col = get_seat(bus)
    if bus[row][col] != None:
        bus[row][col] = None
        print("Platsen är nu avbokad")
    else:
        print("Platsen är inte bokad, går inte att avboka")


def get_row(bus):
    """Returnerar ett giltigt val för en rad i bussen

    Args:
        bus (list): En nästlad lista som representerar en buss

    Returns:
        int : Vald rad
    """
    while True:
        row = input("Rad: ")
        if row.isdigit() == False:
            print("Du måste ange raden i siffror")
            continue

        if int(row) <= 0 or int(row) > len(bus):
            print("Du måste ange en korrekt rad")
            continue

        return int(row)-1
    
def get_seat(bus):
    """Returnerar ett giltigt val för ett säte i bussen

    Args:
        bus (list): En nästlad lista som representerar en buss

    Returns:
        int : Valt säte
    """
    while True:
        seat = input("Säte: ")
        if seat.isdigit() == False:
            print("Du måste ange plats i siffror")
            continue

        if int(seat) <= 0 or int(seat) > len(bus[0]):
            print("Du måste ange en korrekt plats")
            continue

        return int(seat)-1


def print_menu():
    """Skriver ut menyn i programmet"""
    print("\nMeny")
    print("*"*25)
    print("1) Visa bussen")
    print("2) Boka en plats")
    print("3) Avboka en plats")
    print("4) Se bokning på en plats")
    print("0) Avsluta programmet")

def print_bus(bus):
    """Skriver ut en representation av bussen

    Args:
        bus (list): En nästlad lista som representerar en buss
    """
    print("\nBussen")
    print("-"*30)
    
    for i, row in enumerate(bus, start=1):
        print(f"{i:<2}: ", end="")
        for seat in row:
            if seat == None:
                print(" - ", end="")
            else:
                print(" x ", end="")
        print("")

main()
```