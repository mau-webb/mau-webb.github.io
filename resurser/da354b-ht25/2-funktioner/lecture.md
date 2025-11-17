---
id: da354b-ht25
title: "Modul 2 - Funktioner"
---

# Modul 2 - Funktioner

## Föreläsning - Funktioner

<div class="frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.2696%; padding-top: 58px;"><iframe src="https://www.slideshare.net/slideshow/embed_code/key/87aYGG8cYtd50B" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no"></iframe></div>
</div>
---

Ni kan även ladda ner PDF-versionen av presentationen [här](../pdf/2025-Funktioner.pdf).

<!--
---

<div class="video-frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.25%;"><iframe src="https://www.youtube.com/embed/rcOXDhwLc4Y?rel=0" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share;"></iframe></div>
</div>

---
-->

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