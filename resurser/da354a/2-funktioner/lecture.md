---
id: da354a
title: "Modul 2 - Funktioner"
---

# Modul 2 - Funktioner

## Föreläsning - Funktioner

<div class="frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.1972%;"><iframe src="https://speakerdeck.com/player/2ca9be91d5d5431db672d9b3d3e23c03" style="border: 0; top: 0; left: 0; width: 100%; height: 100%; position: absolute;" allowfullscreen scrolling="no" allow="encrypted-media"></iframe></div>
</div>

---

<div class="video-frame">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/rHP8Kt83OVQ" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

---

### Dagens exempel

#### Lunchexempel

```python
def heading(message):
    '''
    Skriver ut en rubrik
    '''
    print("************************************")
    print(message)
    print("************************************")

def today_lunch(day, lunch):
    '''
    Skriver ut lunch för en given dag
    '''
    print("Lunch " + day + " is: " + lunch)

def menu():
    '''
    Skriver ut veckans meny
    '''
    today_lunch("Monday", "Spagetti Bolognaise")
    today_lunch("Tuesday", "Fish and chips")
    today_lunch("Wednesday", "Hamburger")
    today_lunch("Thursday", "Soup")
    today_lunch("Friday", "Pizza")

heading("Welcome!")
menu()
heading("Goodbye!")
```

#### Parametrar & argument

```python
def calculate(a, b):
    return a + b


nr_1 = input("Ange tal 1: ")
nr_2 = input("Ange tal 2: ")
result = calculate(int(nr_1), int(nr_2))


def meters_to_yards(meters):
    yards_per_meter = 0.9144
    result = meters/yards_per_meter
    return result

m = input("Hur många meter vill du omvandla till yards? ")
x = meters_to_yards(int(m))
print(x)
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

Ni kan även ladda ner PDF-versionen av presentationen [här](../pdf/2020-funktioner.pdf).