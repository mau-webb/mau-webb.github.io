---
id: da354a-ht22
title: "Modul 2 - Funktioner"
---

# Modul 2 - Funktioner

## Föreläsning - Funktioner

Publiceras efter föreläsningen den 14/11.

<!--

<div class="frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.1972%;"><iframe src="https://speakerdeck.com/player/68272bdc57ab45b59c47d444c8565722" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="encrypted-media;"></iframe></div>
</div>

---

<div class="video-frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.25%;"><iframe src="https://www.youtube.com/embed/zHm_sBNdaI0?rel=0" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture;"></iframe></div>
</div>

---

### Dagens exempel

#### Lunchexempel

```python
def todays_lunch(day, lunch):
    print(day + ": " + lunch)

def heading(message):
    '''
    Prints a heading
    '''
    print("*"*40)
    print(message)
    print("*"*40)

def weeks_lunch():
    '''
    Presents the lunches to the user
    '''
    todays_lunch("Monday", "Pizza")
    todays_lunch("Tuesday", "Fish and chips")
    todays_lunch("Wednesday", "Hamburger")
    todays_lunch("Thursday", "Soup")
    todays_lunch("Friday", "Taco")

def main():
    heading("Welcome")
    weeks_lunch()
    heading("Goodbye")

main()
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

Ni kan även ladda ner PDF-versionen av presentationen [här](../pdf/2021-Funktioner.pdf).

-->