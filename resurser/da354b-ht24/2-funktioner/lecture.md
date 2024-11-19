---
id: da354b-ht24
title: "Modul 2 - Funktioner"
---

# Modul 2 - Funktioner

## Föreläsning - Funktioner


<div class="frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.2696%; padding-top: 58px;"><iframe src="https://www.slideshare.net/slideshow/embed_code/key/JjfudWDsepck6o" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no"></iframe></div>
</div>
---

Ni kan även ladda ner PDF-versionen av presentationen [här](../pdf/2024-Funktioner.pdf).

---

<!--
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

def lunch_day(day, dish):
    """Skriver ut lunch för en given dag
    
    Args:
        day: Dagen (t.ex. måndag)
        dish: Maträtten (t.ex. Spagetti Bolognaise)
    """
    print(day + ": " + dish)

def weeks_lunch():
    """Skriver ut veckans luncher"""
    lunch_day("Monday", "Spagetti Bolognaise")
    lunch_day("Tuesday", "Fish and chips")
    lunch_day("Wednesday", "Hamburger")
    lunch_day("Thursday", "Soup")
    lunch_day("Friday", "Pizza")
    lunch_day("Saturday", "Tacos")


def main():
    heading("Welcome!")
    weeks_lunch()
    heading("Goodbye!")

main()
```

#### Parametrar & argument

```python
def shout(text):
    """
    Gör om en textsträng till stora bokstäver, och skriver ut strängen

    Args:
        text: Den sträng som ska göras om till stora bokstäver och skrivas ut
    """
    result = text.upper()
    print(result)

shout("Anton är bäst!")
shout("Python är roligt!")
input_text = input("Ange text du vill skriva ut i stora bokstäver: ")
shout(input_text)

name = input("Vad heter du? ")
print(name + " innehåller " + str(len(name)) + " tecken")
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