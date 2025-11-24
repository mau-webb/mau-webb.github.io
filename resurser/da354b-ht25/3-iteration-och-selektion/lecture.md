---
id: da354b-ht25
title: "Modul 3 - Iteration & Selektion"
---

# Modul 3 - Iteration & Selektion

## Föreläsning

<div class="frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.2696%; padding-top: 58px;"><iframe src="https://www.slideshare.net/slideshow/embed_code/key/ydf5eYjCMzSmXn" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no"></iframe></div>
</div>

<!--

Videoföreläsning (från tidigare år).

<div class="video-frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.25%;"><iframe src="https://www.youtube.com/embed/eThWwiyfN_A?rel=0" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share;"></iframe></div>
</div>

---

<div class="frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.1972%;"><iframe src="https://speakerdeck.com/player/a641102ea36d48d69143e06850b0ce1b" style="border: 0; top: 0; left: 0; width: 100%; height: 100%; position: absolute;" allowfullscreen scrolling="no" allow="encrypted-media"></iframe></div>
</div>
-->

[Ni kan ladda ner föreläsningen i PDF här](../pdf/2025-Presentation.pdf)

---

## Dagens exempel

### Exempel på if-satser

```python
def check_password(password):
    if len(password) < 8:
        print("Osäkert lösenord - Det är för kort")
    elif password.isdigit():
        print("Osäkert lösenord - Du har enbart siffror i ditt lösenord")
    else:
        print("Du har ett säkert lösenord")

check_password("123456789a")
```

```python
password = "secret"
user = "Anton"

user_user = input("Användarnamn: ")
user_password = input("Lösenord: ")


if user_password == password and user == user_user:
    print("Inloggad!")
else:
    print("Du angav fel användarnamn eller lösenord")
```

### Systembolagetkoll

```python
age = input("Hur gammal är du? ")

if age.isdigit():
    age = int(age)

    if age < 18:
        print("Du är en ungdom")
    else:
        print("Du är vuxen")
else:
    print("Du angav inte en siffra! =(")
```

### Exempel: loopar

```python
for i in range(100):
    print("I will never do anything stupid again...")

question = "ja"
while question == "ja":
    print("=====")
    print("Vi kör ett varv till i loopen")
    print("=====")
    question = input("Vill du göra igen?")
```
<!--
### Exempel - bonus: Meny

```python
def menu():
    print("************")
    print("Välkommen")
    print("************")

    user_choice = None

    while user_choice != "0":
        print("\n******")
        print("Menu")
        print("******")
        print("1) Test")
        print("2) Hej")
        print("3) Hoppsan")
        print("0) Avsluta")
        user_choice = input("Ange val: ")

        if user_choice == "1":
            print("Du valde altenativ 1: Test")
        elif user_choice == "2":
            print("Du valde alternativ 2: Hej")
        elif user_choice == "3":
            print("Du valde alternativ 3: Hoppsan")
        elif user_choice == "0":
            pass
        else:
            print("Du valde inte ett korrekt alternativ")            
        
              
menu()
```

### Exempel: for-loop

```python
name = input("Vad heter du? ")
times = input("Hur många gånger vill du skriva ut ditt namn? ")

for i in range(int(times)):
    print(f"{i}: {name}")

for i in range(1000):
    print("Anton är bäst!")

for i in range(12): # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    print(i)
```
-->

### Rövarspråket

```python
def is_vowel(char):
    """Controlls if a character is a vowel

    Args:
      char (str): The character to test

    Returns:
        bool: True if vowel, False otherwise
    """
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
    """Asks the user for a text

    Returns:
        str: The text the user entered
    """
    return input("Ange text: ")

def translate_to_rovarspraket(text):
    """Translates a given text to "rövarspråk"

    Args:
        text (str): The string to translate

    Returns:
        str: The translated text
    """
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
    """Controlls if a character is a vowel

    Args:
      char (str): The character to test

    Returns:
        bool: True if vowel, False otherwise
    """
    return char.lower() in 'aeiouyåäö'

def get_user_text():
    """Asks the user for a text

    Returns:
        str: The text the user entered
    """
    return input("Ange text: ")

def translate_to_rovarspraket(text):
    """Translates a given text to "rövarspråk"

    Args:
        text (str): The string to translate

    Returns:
        str: The translated text
    """
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