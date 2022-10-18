---
id: da354a-ht22
title: "Modul 2 - Funktioner"
---

# Modul 2 - Funktioner

## Föreläsning - Funktioner (extra)

Här kommer dagens exempelkod:

### Enkla funktioner

```python
def hello_world():
    '''
    En funktion som skriver ut: Hello World!
    '''
    print("Hello World!")

def god_morgon():
    '''
    En funktion som säger god morgon på ett uppmuntrande sätt
    '''
    print("God morgon! Vilket fint väder det är idag! =)")
```

### Funktioner med parametrar

```python
def print_three_times(x):
    '''
    Skriver ut x tre gånger

    Args:
        x (str): Strängen som ska skrivas ut
    '''
    print(x)
    print(x)
    print(x)

def hej(name):
    '''
    Välkomnar en användare

    Args:
        name (str) : Namnet på användaren
    '''
    print(f"Hej {name}!")

# Kör funktionerna
name = input("Vad heter du? ")
hej(name)

text = input("Vad vill du skriva ut tre gånger? ")
print_three_times(text)
```

### Funktioner med returvärden
```python
def kr_to_dollar(kr):
    '''
    Konverterar kronor till dollar

    Args:
        kr (int) : Antal kronor som ska omvandlas till dollar

    Return:
        int : Antal dollar
    '''
    usd = 8.65 # En dollar är 8.65kr
    result = round(kr / usd, 2)
    return result

def get_user_int(question):
    '''
    Hämta ett nummer från användaren

    Args:
        question (string) : Frågan som ska skrivas ut

    Returns:
        int : Användarens angivna nummer
    '''
    user_input = input(question)
    return int(user_input)

def main():
    '''
    Valutakonverteringsprogram som växlar antal kronor
    som användaren anger till dollar och skriver ut resultatet.
    '''
    user_kr = get_user_int("Ange antal kr: ")
    dollar = kr_to_dollar(user_kr)
    print(f"För {user_kr}kr får man ${dollar}")

# Kör vårt program
main()
```