---
id: da354a-ht23
title: "Modul 4 - Listor & Lexikon"
---

# Modul 4 - Listor & Lexikon

## Föreläsning - Extra

<!--
**Kommer när videon är färdigrenderad**

<div class="video-frame">
<div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.25%;"><iframe src="https://www.youtube.com/embed/fTdLe3XKbQw?rel=0" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture;"></iframe></div>
</div>
--->

### Nästlade listor som tabeller

```python
courses = [
    [1, "LP2", "Introd prog", "Anton Tibblin"],
    [1, "LP2", "ID för IA", "Dipak Surie"],
    [2, "LP1", "OOP för IA", "Anton Tibblin"]    
]

for row in courses:
    for col in row:
        print(f"{col : <20} ", end="")
    print("")


```

### Bussprogram

```python
def main():
    # Representation av vår buss
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
        [None, None, None, None]
    ]

    user_choice = False

    while user_choice != "0":
        # Skriva ut menyn
        print_menu()

        # Fråga användaren efter ett val
        user_choice = input("Ange val: ")

        # Beroende på användarens val, kör vald funktion
        if user_choice == "1":
            print_bus(bus) # Visa bussen
        elif user_choice == "2":
            book(bus) # Boka en plats i bussen
        elif user_choice == "3":
            unbook(bus) # Avboka en plats i bussen
        elif user_choice == "4":
            show_booking(bus) # Visa vem som bokat en plats
        elif user_choice == "0":
            pass
        else:
            print("Du valde inte ett giltigt alternativ, försöka igen")

def show_booking(bus):
    print("\nSe detaljer kring en bokning")
    print("-"*30)
    row = get_row(bus)-1
    seat = get_seat(bus)-1
    if bus[row][seat] == None:
        print("Platsen är ej bokad")
    else:
        print(f"Platsen är bokad av: {bus[row][seat]}")

def book(bus):
    print("\nBoka en plats")
    print("-"*30)
    while True:
        # 1. Vilken rad
        row = get_row(bus)-1
        # 2. Vilket säte på den raden
        seat = get_seat(bus)-1
        # 3. Kontroller att platsen är ledig
        if bus[row][seat] == None:
            break
        else:
            print("Platsen du har valt är upptagen, försök igen")

    # Här är efter att loopen är bruten
    name = input("Vad heter du? ")
    bus[row][seat] = name

def unbook(bus):
    print("\nAvboka en plats")
    print("-"*30)
    while True:
        # 1. Vilken rad
        row = get_row(bus)-1
        # 2. Vilket säte på den raden
        seat = get_seat(bus)-1
        # 3. Kontrollera att platsen är bokad
        if bus[row][seat] != None:
            name = input("Ange namnet på personen som bokat platsen: ")
            if name == bus[row][seat]:
                break
            else:
                print("Du angav fel namn")
        else:
            print("Platsen är inte bokad, så du kan inte avboka den")

    bus[row][seat] = None
    

def get_seat(bus):
    while True:
        seat = input("Plats: ")
        if seat.isdigit() == False:
            print("Platsen måste anges i siffror")
            continue

        if int(seat) < 1 or int(seat) > len(bus[0]): # Istället för len(bus[0]) kunna skriva 4
            print("Den platsen finns inte i bussen")
            continue

        return int(seat)
        
def get_row(bus):
    while True:
        row = input("Rad: ")
        if row.isdigit() == False:
            print("Raden måste anges i siffror")
            continue

        if int(row) < 1 or int(row) > len(bus):
            print("Den raden finns inte i bussen")
            continue

        return int(row)

def print_bus(bus):
    print("\nBussen")
    print("-"*30)
    print("     1  2   3  4")
    for i, row in enumerate(bus, start=1):
        print(f"{i:<2}"+": ", end="")
        for j, seat in enumerate(row, start=0):
            if seat == None:
                print(f"{'-' : ^3}", end="")
            else:
                print(f"{'x' : ^3}", end="")

            if j == 1:
                print(" ", end="")
        print("")

def print_menu():
    print("\nMeny")
    print("****")
    print("1) Visa bussen")
    print("2) Boka en plats i bussen")
    print("3) Avboka en plats i bussen")
    print("4) Se vem som bokat plats")
    print("0) Avsluta")

main()

```