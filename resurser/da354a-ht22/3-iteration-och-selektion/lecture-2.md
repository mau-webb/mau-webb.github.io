---
id: da354a-ht22
title: "Modul 3 - Iteration & Selektion"
---

# Modul 3 - Iteration & Selektion

## Föreläsning - Extra

Presentation & kod presenteras här efter föreläsningen.
<!--
---

<div class="video-frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.25%;"><iframe src="https://www.youtube.com/embed/gdk4JeFTgrA?rel=0" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture;"></iframe></div>
</div>

---

## Dagens exempel

### Sten, sax, påse (eller grävskopa)

```python
import random

win = 0
lose = 0
tie = 0

def main():
    """Huvudfunktionen som styr programmet"""

    welcome()

    while True:
        print_menu()
        user_choice = input("Val: ")

        if user_choice == "1":
            # 1. Användarens val (sten, sax, påse)
            user_pick = get_user_pick()
            # 2. Datorns val (sten, sax, påse)
            cpu_pick = get_cpu_pick()
            # 3. Utse vinnare
            get_result(user_pick, cpu_pick)
        elif user_choice == "2":
            # Visa statistik
            view_statistics()
        elif user_choice == "0":
            break
        else:
            print("Felaktigt alternativ, försök igen")

def view_statistics():
    """Skriver ut aktuell poänställning"""
    print("\nStatistik")
    print("-----------")
    print(f"Vinster: {win}")
    print(f"Förluster: {lose}")
    print(f"Lika: {tie}")

def get_user_pick():
    """Funktionen hämtar ett giltigt val av användaren

    Ett giltigt val är: sten, sax, påse eller grävskopa

    Return
        str : Användarens val
    """
    choice = input("Vad gissar du på? ").lower()

    while choice != "sten" and choice != "sax" and choice != "påse" and choice != "grävskopa":
        choice = input("Vad gissar du på? ").lower()

    return choice

def get_cpu_pick():
    """Funktionen slumpar fram en gissning åt datorn

    En giltig gissning är: sten, sax eller påse

    Return
        str : Datorns val
    """
    choice = random.randint(0, 2)

    if choice == 0:
        return "sten"
    elif choice == 1:
        return "sax"
    else:
        return "påse"

def get_result(user_choice, cpu_choice):
    """Utser vinnare i spelet

    Regler för spelet:
        sten > sax
        sax > påse
        påse > sten

    Args:
        user_choice (str) : Användarens gissning (sten, sax, påse)
        cpu_choice (str) : Datorns gissning (sten, sax, påse)
    """
    global win
    global lose
    global tie
    
    print(f"Du valde: {user_choice}")
    print(f"Datorn valde: {cpu_choice}")

    if user_choice == cpu_choice:
        print("Lika!")
        tie += 1
    elif user_choice == "grävskopa":
        print("Du vann! Snyggt! Datorn hade inte en chans! ;)")
        win += 1
    elif user_choice == "sten" and cpu_choice == "sax":
        print("Du vann!")
        win += 1
    elif user_choice == "sax" and cpu_choice == "påse":
        print("Du vann!")
        win += 1
    elif user_choice == "påse" and cpu_choice == "sten":
        print("Du vann!")
        win += 1
    else:
        print("Datorn vann!")
        lose += 1

def welcome():
    """Skriver ut rubriken för programmet"""
    print("*"*40)
    print("Sten, sax, påse")
    print("*"*40)

def print_menu():
    """Skriver ut programmets menu"""
    print("\nMeny")
    print("--------")
    print("1) Spela")
    print("2) Statistik")
    print("0) Avsluta")

main()
```
-->