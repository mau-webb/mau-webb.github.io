---
id: da354a-ht23
title: "Modul 2 - Funktioner"
---

# Modul 2 - Funktioner

Publiceras efter att föreläsningen ägt rum.

<!--

## Föreläsning - Funktioner

<div class="frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.2696%; padding-top: 58px;"><iframe src="https://www.slideshare.net/slideshow/embed_code/key/qS3BJ1XTMPEldJ" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="encrypted-media;"></iframe></div>
</div>
-->
<!--

<div class="video-frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.25%;"><iframe src="https://www.youtube.com/embed/zHm_sBNdaI0?rel=0" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture;"></iframe></div>
</div>

-->
<!--
### Dagens exempel

#### Lunchexempel

```python
def heading(message):
    """
    Skriver ut en rubrik

    Args:
        message: str - Texten på rubriken
    """
    print("="*40)
    print(message)
    print("="*40)

def weeks_lunch():
    """
    Skriver ut veckans luncher
    """
    print("Lunch måndag: Spagetti med köttfärssås")
    print("Lunch tisdag: Fish and chips")
    print("Lunch onsdag: Hamburgare")
    print("Lunch torsdag: Kantarellsoppa")
    print("Lunch fredag: Pizza")


# Här finns koden som kör programmet
heading("Välkommen")
weeks_lunch()
heading("Hejdå")

```

#### Parametrar & argument

```python
def meter_to_feet(meter):
    """
    Omvandlar meter till foot

    Args:
        meter: int - Antal meter som vi vill omvandla

    Return:
        int - Antal feet
    """
    foot = 3.28
    result = int(meter) * foot
    return result


user_meter = input("Hur många meter vill du omvandla till foot: ")
feet = meter_to_feet(user_meter)
print("För " + user_meter + "meter får du " + str(feet) + "feet")

```

#### Använda modulen random

```python
import random

# Slumpa fram ett tal (1-10)
rand_nr = random.randint(1,10)
# Skriv ut det slumpade talet
print(rand_nr)
```

---

Ni kan även ladda ner PDF-versionen av presentationen [här](../pdf/2022-Funktioner.pdf).
-->