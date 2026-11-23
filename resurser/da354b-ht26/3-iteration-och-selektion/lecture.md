---
id: da354b-ht26
title: "Modul 3 - Iteration & Selektion"
---

# Modul 3 - Iteration & Selektion

<div class="frame">
    <embed src="../pdf/ht-26-Presentation.pdf" type="application/pdf" width="100%" height="485px">
</div>

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

Andra exempel:

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
