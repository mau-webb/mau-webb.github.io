---
id: da354a-ht23
title: "Modul 3 - Iteration & Selektion"
---

# Modul 3 - Iteration & Selektion

## Föreläsning

Presentation & kod presenteras här efter föreläsningen.


<div class="frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.2696%; padding-top: 58px;"><iframe src="https://www.slideshare.net/slideshow/embed_code/key/493Aovdvq5D2s8" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="encrypted-media;"></iframe></div>
</div>

[Ni kan ladda ner föreläsningen i PDF här](../pdf/2022-Presentation.pdf)

---

<!--
<p><strong>Eftersom att dagens ljudinspelning var horibel, så får ni istället förra årets inspelade föreläsning (typ samma)</strong></p>

<div class="video-frame">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/CU-MHLZ-zSU" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

---
-->

## Dagens exempel

### Systembolagetkoll

```python
user_age = input("Hur gammal är du? ")

# Alt. 1 - med else if
if user_age.isdigit() == False:
    print("Ditt dumhuvud, hur svårt är det att skriva in en siffra egentligen?")
elif int(user_age) < 20:
    print("Välkommen tillbaka när du fyllt 20 år")
else:
    print("Välkommen in!")

# Alt. 2 - med nästlade if-satset
if user_age.isdigit():
    if int(user_age) < 20:
        print("Välkommen tillbaka när du fyllt 20 år")
    else:
        print("Välkommen in!")
else:
    print("Ditt dumhuvud, hur svårt är det att skriva in en siffra egentligen?")
```

### Exempel: while-loop

```python
user_nr = int(input("Gissa korrekt nummer: "))
CORRECT_NUMBER = randint(1, 20)

while user_nr != CORRECT_NUMBER:
    print("FEL NUMMER! Försök igen")
    user_nr = int(input("Gissa korrekt nummer: "))

print("Snyggt jobbat!")
```

<!--
### Exempel: Meny (bonus!)

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
-->

### "Log in"-funktion

```python
print("*"*30)
print("Logga in")
print("*"*30)
username = input("Epost: ")
password = input("Lösenord: ")

MASTER_USER = "anton.tibblin@mau.se"
MASTER_PASSWORD = "Secret@123"

if username == MASTER_USER and password == MASTER_PASSWORD:
    print("Du är inloggad")
else:
    print("Du angav fel kombination av användarnamn & lösenord")
```

### Exempel: for-loop

```python
for i in range(200):
    print(i)
```

<!--
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