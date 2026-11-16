---
id: da354b-ht26
title: "Modul 2 - Funktioner"
---

# Modul 2 - Funktioner

## Föreläsning - Funktioner

Publiceras när tillfället ägt rum.

<!--

### Dagens exempel

#### Lunchexempel

```python
def heading(message):
    """Skriver ut en rubrik

    Args:
        message: Titeln i rubriken som ska skrivas ut
    """
    print("="*40)
    print(message)
    print("="*40)

def day_lunch(day, dish):
    """Skriver ut lunch för en given dag

    Args:
        day: Dagen (t.ex. måndag)
        dish: Maträtten (t.ex. Spagetti Bolognaise)

    """
    print(f"Lunch {day}: {dish}")

def weeks_lunches():
    """Skriver ut en veckas matmeny"""
    day_lunch("måndag", "Pasta Bolognaise")
    day_lunch("tisdag", "Hamburgare")
    day_lunch("onsdag", "Pizza")
    day_lunch("torsdag", "Soppa")
    day_lunch("fredag", "Tacos")

heading("Välkommen!")
weeks_lunches()
heading("Tack och hejdå!")
```

#### Parametrar & argument

```python
def sek_to_dollar(sek):
    """Omvanldar sek till dollar

    Args:
        sek: Antal kronor vi vill omvandla
    """
    dollar = 9.45
    result = sek/dollar
    return result

user_sek = int(input("Hur många SEK vill du omvandla till dollar? "))
x = sek_to_dollar(user_sek)
print(round(x, 2))
```

<!--
#### Använda modulen random

```python
import random

# Slumpa fram ett tal (1-10)
rand_nr = random.randint(1,10)
# Skriv ut det slumpade talet
print(rand_nr)
```

---

-->
