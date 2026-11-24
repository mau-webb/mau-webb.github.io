---
id: da354b-ht26
title: "Modul 3 - Iteration & Selektion"
---

# Modul 3 - Iteration & Selektion

## Föreläsning - Sten, sax, påse

Dagens föreläsning har ingen presentation, se koden nedan.

Bonus - Videoföreläsning (från tidigare år) på sten, sax, påse-spelet (+ lite extra).

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
    """Huvudfunktionen som styr spelet Sten, Sax, Påse"""
    # 1. Välkomna användaren
    welcome()

    # 2. Köra en loop för menyvalen
    while True:
        print_menu()
        user_choice = input("Val: ")

        if user_choice == "1":
            # 1) Spela sten, sax, påse

            # a) Hämta användarens val
            user_pick = get_user_choice()

            # b) Hämta datorns val
            cpu_pick = get_cpu_choice()

            # c) Presentera vinnare
            get_result(user_pick, cpu_pick)

        elif user_choice == "2":
            # 2) Visa statistik
            view_statistics()
        elif user_choice == "3":
            # 3) Visa regler
            view_rules()
        elif user_choice == "4":
            # 4) Avsluta spelet
            break
        else:
            print("\nDu valde ett ogiltligt alternativ, försök igen!\n")

    print("Tack för den här gången - hoppas vi spelar snart igen!")


def view_rules():
    """Skriver ut reglerna till Sten, Sax, Påse"""
    print("-"*40)
    print("Regler")
    print("-"*40)
    print("- Sten vinner över sax")
    print("- Sax vinner över påse")
    print("- Påse vinner över sten")

def view_statistics():
    """Skriver ut spelarstatistiken till Sten, Sax, Påse"""
    print("-"*40)
    print("Statistik")
    print("-"*40)
    print(f"Vinster: {win}")
    print(f"Förluster: {lose}")
    print(f"Lika: {tie}")

def get_result(user_choice, cpu_choice):
    """Beräknar vinnaren (användren eller datorn)

    Args:
        user_choice (str) : Spelarens val: sten, sax, påse eller grävskopa
        cpu_choice (str) : Datorns val: sten, sax, påse

    """
    global win
    global lose
    global tie

    print(f"Du valde: {user_choice}")
    print(f"Datorn valde: {cpu_choice}")

    if user_choice == cpu_choice:
        print("Lika!")
        tie = tie + 1
    elif user_choice == "grävskopa":
        print("BOOOM - Snyggt jobbat!")
        win = win + 100
    elif user_choice == "sten" and cpu_choice == "sax":
        print("Du vann!")
        win = win + 1
    elif user_choice == "sax" and cpu_choice == "påse":
        print("Du vann!")
        win = win + 1
    elif user_choice == "påse" and cpu_choice == "sten":
        print("Du vann!")
        win = win + 1
    else:
        print("Datorn vann!")
        lose = lose + 1

def get_cpu_choice():
    """Genererar en gissning från datorn, antingen: sten, sax eller påse

    Returns
        str : Gissningen: sten, sax eller påse
    """
    random_number = random.randint(0, 2)

    if random_number == 0:
        return "sten"
    elif random_number == 1:
        return "sax"
    elif random_number == 2:
        return "påse"

def get_user_choice():
    """Hämtar användarens gissning: sten, sax, påse eller grävskopa

    Returns
        str : Användarens gissning: sten, sax, påse, grävskopa
    """
    choice = input("Vad gissar du på? ").lower()

    while choice != "sten" and choice != "sax" and choice != "påse" and choice != "grävskopa":
        print("Du valde inte ett giltigt alternativ, försök igen")
        choice = input("Vad gissar du på? ")
    return choice

def print_menu():
    """Skriver ut spelets menu"""
    print("-"*40)
    print("Meny")
    print("-"*40)
    print("1) Spela")
    print("2) Visa statistik")
    print("3) Visa regler")
    print("4) Avsluta")

def welcome():
    """Skriver ut ett välkomstmeddelande / rubrik för spelet"""
    print("*"*40)
    print("Sten, sax, påse")
    print("*"*40)

main()
```

<!--
```python
import random

win = 0
lose = 0
tie = 0

def main():
    """Huvudfunktionen som styr programmet"""

    # 1. Välkomna användaren
    welcome()

    # 2. Köra en loop som visar en meny, där användaren väljer ett val (ända till användaren väljer att stänga av programmet)
    while True:
        print_menu()
        user_choice = input("Val: ")

        if user_choice == "1":
            # 1. Användarens val (sten, sax, påse)
            user_pick = get_user_pick()
            # 2. Datorns val (sten, sax, påse)
            cpu_pick = get_cpu_pick()
            # 3. Utse (och skriva ut) vinnare
            get_result(user_pick, cpu_pick)

        elif user_choice == "2":
            # Visa statistik
            view_statistics()
        elif user_choice == "0":
            break
        else:
            print("Felaktivt alternativ valt, försök igen!")

def view_statistics():
    """Skriver ut aktuell statistik för spelet"""
    print("\nStatistik")
    print("--------------")
    print(f"Vinster: {win}")
    print(f"Förluster: {lose}")
    print(f"Lika: {tie}")

def get_result(user_choice, cpu_choice):
    """Utser vinnare i spelet, och uppdaterar statistiken

    Regler för spelet:
        sten > sax
        sax > påse
        påse > sten

    Args:
        user_choice (str) : Användarens gissning (sten, sax, påse)
        cpu_choice (str) : Datorn gissning (sten, sax, påse)
    """
    global win
    global tie
    global lose

    print(f"Du valde: {user_choice}")
    print(f"Datorn valde: {cpu_choice}")

    if user_choice == "grävskopa":
        print("Snyggt jobbbat! Du får 100 extra poäng!!!")
        win = win + 100
    elif user_choice == cpu_choice:
        print("Lika!")
        tie += 1
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


def get_cpu_pick():
    """Funktionen slumpar fram en gissning åt användaren

    En giltig gissning är: sten, sax eller på

    Returns
        str : Datorns val
    """
    random_number = random.randint(0,2)

    if random_number == 0:
        return "sten"
    elif random_number == 1:
        return "sax"
    else:
        return "påse"

def get_user_pick():
    """Funktionen hämtar en giltig gissning från användaren

    En giltig gissning är: sten, sax, påse

    Returns
        str : Användarens val
    """
    choice = input("Vad gissar du på? ").lower()

    while choice != "sten" and choice != "sax" and choice != "påse" and choice != "grävskopa":
        print("Du valde ett felaktigt alternativ, välj något av: sten, sax, påse")
        choice = input("Vad gissar du på? ").lower()

    return choice



def print_menu():
    """Skriver ut programmets meny"""
    print("\nMeny")
    print("1) Spela")
    print("2) Statistik")
    print("0) Avsluta programmet")

def welcome():
    """Skriver ut välkomstfram still användaren"""
    print("*"*30)
    print("Sten, sax, påse")
    print("*"*30)

main()
```


### Rövarspråket

```python
def is_vowel(char):
    '''Controlls if a character is a vowel

    Args:
      char (str): The character to test

    Returns:
        bool: True if vowel, False otherwise
    '''
    char = char.lower()
    if char == "a":
        return True
    elif char == "e":
        return True
    elif char == "i":
        return True
    elif char == "o":
        return True
    elif char == "u":
        return True
    elif char == "y":
        return True
    elif char == "å":
        return True
    elif char == "ä":
        return True
    elif char == "ö":
        return True
    else:
        return False

def get_user_text():
    '''Asks the user for a text

    Returns
        str
    '''
    return input("Ange text: ")

def translate_to_rovarspraket(text):
    '''Translates a given text to "rövarspråk"

    Args:
        text (str): The string to translate

    Returns:
        str: The translated text
    '''
    result = ""

    # Loops through every character in the variable "text"
    for character in text:
        if character.isalpha() and not is_vowel(character):
            # Character is a consonant
            result = result + character + "o" + character.lower()
        else:
            result =  result + character

    return result


def main():
    print("*"*30)
    print("Rövarspråksöversättaren")
    print("*"*30)

    # Asks the user for a text
    text = get_user_text()

    # Translates and prints the text to "rövarspråk"
    rovarsprak = translate_to_rovarspraket(text)

    # Prints the translated text
    print(rovarsprak)

main()
```

### Rövarspråket (annan lösning)

```python
def is_vowel(char):
    '''Controlls if a character is a vowel

    Args:
      char (str): The character to test

    Returns:
        bool: True if vowel, False otherwise
    '''
    return char.lower() in 'aeiouyåäö'

def get_user_text():
    '''Asks the user for a text

    Returns
        str
    '''
    return input("Ange text: ")

def translate_to_rovarspraket(text):
    '''Translates a given text to "rövarspråk"

    Args:
        text (str): The string to translate

    Returns:
        str: The translated text
    '''
    result = ""

    # Loops through every character in the variable "text"
    for character in text:
        if character.isalpha() and not is_vowel(character):
            # Character is a consonant
            result = result + character + "o" + character.lower()
        else:
            result =  result + character

    return result


def main():
    print("*"*30)
    print("Rövarspråksöversättaren")
    print("*"*30)

    # Asks the user for a text
    text = get_user_text()

    # Translates and prints the text to "rövarspråk"
    rovarsprak = translate_to_rovarspraket(text)

    # Prints the translated text
    print(rovarsprak)

main()
```
-->
