---
id: da354a-ht22
title: "Modul 4 - Listor & Lexikon"
---

# Modul 4 - Listor & Lexikon

## Föreläsning - Extra

**Kommer när videon är färdigrenderad**

<div class="video-frame">
<div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.25%;"><iframe src="https://www.youtube.com/embed/fTdLe3XKbQw?rel=0" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture;"></iframe></div>
</div>

### Nästlade listor som tabeller

```python
movies = [
    ["Star Wars", 1977, "George Lucas"],
    ["Pulp fiction", 1994, "Quentin Tarantino"],
    ["Alien", 1979, "Ridley Scott"],
    ["The intouchebles", 2011, "Eric Toledans"],
    ["Annabelle", 2019, "Gary Dauberman"]
]

for row in movies:
    for col in row:
        print(f"{col : <20}", end="")
    print("")

```

### Bussprogram

```python
def main():
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
            unbook(bus)
        elif user_choice == "4":
            see_booking(bus)
        elif user_choice != "0":
            print("Du valde ett felaktigt alternativ!")

def see_booking(bus):
    print("\nSe detaljer om en plats")
    print("*"*30)
    row = get_row(bus)-1
    col = get_seat(bus)-1
    seat = bus[row][col]
    if seat is None:
        print("Platsen är ej bokad")
    else:
        print(f"Platsen är bokad av {seat}")

def get_row(bus):
    while True:
        row = input("Rad: ")
        if row.isdigit() == False:
            print("Raden måste anges i en siffra")
            continue
        
        if int(row) < 0 or int(row) > len(bus):
            print("Du måste ange en korrekt rad")
            continue

        return int(row)
    
def get_seat(bus):
    while True:
        seat = input("Säte: ")
        if seat.isdigit() == False:
            print("Platsen måste anges i en siffra")
            continue
        
        if int(seat) < 0 or int(seat) > len(bus[0]):
            print("Du måste ange en korrekt rad")
            continue

        return int(seat)

def book(bus):
    print("\nBoka en plats")
    print("*"*30)
    while True:
        row = get_row(bus)-1
        col = get_seat(bus)-1
        if bus[row][col] is None:
            break

        print("Platsen är redan bokad, ange en ny plats!\n")
    name = input("Vem bokar? ")
    bus[row][col] = name

def unbook(bus):
    print("\nAvboka en plats")
    print("*"*30)
    while True:
        row = get_row(bus)-1
        col = get_seat(bus)-1
        if bus[row][col] is not None:
            break

        print("Platsen är inte bokad, ange en ny plats!\n")

    bus[row][col] = None

def print_menu():
    print("\nMeny")
    print("-"*30)
    print("1) Visa bussen")
    print("2) Boka en plats i bussen")
    print("3) Avboka en plats i bussen")
    print("4) Se bokning på en plats")
    print("0) Avsluta")

def print_bus(bus):
    print("\nBussen")
    print("-"*30)
    for i, row in enumerate(bus, start=1):
        print(f"{i}: ", end="")
        for spot in row:
            if spot is None:
                print(f"{'-' :^3}", end="")
            else:
                print(f"{'x' :^3}", end="")
        print("")

main()
```