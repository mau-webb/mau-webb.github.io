---
id: da354b-ht25
title: "Modul 2 - Funktioner"
---

# Modul 2 - Funktioner

## Föreläsning - Funktioner (2)

<div class="frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.2696%; padding-top: 58px;"><iframe src="https://www.slideshare.net/slideshow/embed_code/key/rVQLjMPbPfDZkd" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no"></iframe></div>
</div>

---

Ni kan även ladda ner PDF-versionen av presentationen [här](../pdf/2025-Funktioner-2.pdf).

---

Här kommer dagens exempelkod:

### Moduler i Python

```python
import random
from math import pi

# Generera ett tal mellan 1-10
random_number = random.randint(1,10)

print(random_number)
print(pi)
```

### Moduler - Låtar

#### main.py
```python
import mr_brightside
import let_it_be

# Skriv ut låttexten till sången Mr. Brightside
mr_brightside.song()
```

#### mr_brightside.py
```python
def song():
    verse()
    print("")
    chours()
    print("")
    verse()
    print("")
    chours()
    print("")
    outro()

def verse():
    print("I'm coming out of my cage")
    print("And I've been doing just fine")
    print("Gotta gotta be down")
    print("Because I want it all")
    print("It started out with a kiss")
    print("How did it end up like this")
    print("It was only a kiss, it was only a kiss")
    print("Now I'm falling asleep")
    print("And she's calling a cab")
    print("While he's having a smoke")
    print("And she's taking a drag")
    print("Now they're going to bed")
    print("And my stomach is sick")
    print("And it's all in my head")
    print("But she's touching his-chest")
    print("Now, he takes off her dress")
    print("Now, letting me go")
    print("Cause I can't look its killing me")

def chours():
    print("And taking control")
    print("Jealousy, turning saints into the sea")
    print("Swimming through sick lullabies")
    print("Choking on your alibis")
    print("But it's just the price I pay")
    print("Destiny is calling me")
    print("Open up my eager eyes")
    print("'Cause I'm Mr Brightside")

def outro():
    for i in range(5):
        print("I never...")

if __name__ == "__main__":
    song()
```


#### let_it_be.py

```python
def song():
    '''
        Prints the full song
    '''
    verse_1()
    print("")
    verse_2()
    print("")
    chours()
    print("")
    verse_3()
    print("")
    verse_4()
    print("")
    chours_2()
    print("")
    chours()
    print("")
    chours()
    print("")
    verse_5()
    print("")
    verse_6()
    print("")
    chours_2()
    print("")
    chours()

def chours():
    print("Let it be, let it be")
    print("Let it be, let it be")
    print("Whisper words of wisdom")
    print("Let it be")

def chours_2():
    print("Let it be, let it be")
    print("Let it be, let it be")
    print("Yeah, there will be an answer let it be")

def verse_1():
    print("When I find myself in times of trouble")
    print("Mother Mary comes to me")
    print("Speaking words of wisdom, let it be")

def verse_2():
    print("And in my hour of darkness")
    print("She is standing right in front of me")
    print("Speaking words of wisdom, let it be")

def verse_3():
    print("And when all the brokenhearted people")
    print("Living in the world agree")
    print("There will be an answer, let it be")

def verse_4():
    print("For though they may be parted")
    print("There is still a chance that they will see")
    print("There will be an answer, let it be")

def verse_5():
    print("And when the night is cloudy")
    print("There is still a light that shines on me")
    print("Shine on until tomorrow, let it be")

def verse_6():
    print("I wake up to the sound of music")
    print("Mother Mary comes to me")
    print("Speaking words of wisdom, let it be")


if __name__=="__main__":
    song()
```

### Fler funktioner (i exten modul)

#### christmas.py
```python
from datetime import date

def dagar_till_julafton(year, month, day):
    """Räknar ut hur många dagar det är kvar till julafton (2025) från ett givet datum

    Args:
        year (int): Årtal, t.ex. 2025
        month (int): Månad, t.ex. 7
        day (int): Datum, t.ex. 23

    Returns
        int : Antal dagar kvar till julafton 2025
    """
    idag = date(year, month, day)
    julafton = date(2025, 12, 24)

    dagar_kvar = (julafton - idag).days

    return dagar_kvar

print("Välkommen! Räkna ut dagar kvar till julafton!")
user_year = int(input("År: "))
user_month = int(input("Månad: "))
user_date = int(input("Datum: "))

dagar_kvar = dagar_till_julafton(user_year, user_month, user_date)
print(f"Det är {dagar_kvar} dagar kvar till julafton")
```

#### game.py
```python
from random import randint
from time import sleep, time

def play_reaction_game():
    """Ett spel som mäter din reaktionstid"""
    print("="*30)
    print("Reaktionsspel")
    print("="*30)
    print("När det står 'GO!' ska du trycka Enter så snabbt du kan.")
    input("Tryck enter för att starta")

    waiting_time = randint(1, 5)
    sleep(waiting_time)

    print("GO!")
    start = time()
    input()
    stop = time()

    result = stop - start

    print(f"Din reaktionstid: {result:.3f} sekunder")

play_reaction_game()
```

#### units.py
```python
def american_units_to_meter(mile=0, yard=0, foot=0, inch=0, dec=2):
    """Omvandlar amerkanska enheter till meter
    
    Args:
        mile (int): Antal miles (frivillig)
        yard (int): Antal yards (frivillig)
        foot (int): Antal foot (frivillig)
        inch (int): Antal inch (frivillig)
        dec (int): Antal decimaler (frivillig)

    Returns
        int : Summa i meter
    """
    mile_to_meter = 1609.344
    yard_to_meter = 0.9144
    foot_to_meter = 0.3048
    inch_to_meter = 0.0254

    total = mile*mile_to_meter + yard*yard_to_meter + foot*foot_to_meter + inch*inch_to_meter

    return round(total, dec)

# Kör funktionen: amerikan_units_to_meter
km = american_units_to_meter(mile=1, yard=17, dec=1)/1000
print(km)

```


<!--

```python
def print_three_times(x):
    """
    Funktionen skriver ut en text 3 gånger

    Args:
        x(str) : Texten som ska skrivas ut
    """
    print(x)
    print(x)
    print(x)

print_three_times("Python är galet roligt!")
print_three_times("Så mycket kul det är idag!")



def goodmorning():
    """Funktion som säger god morgon"""
    print("Godmorgon!")


def get_teacher_name():
    """Funktion som returnerar kursens lärare"""
    return "Anton", "Johan"

def get_nrs():
    """Frågar användaren efter två nummer och returnerar dessa"""
    nr_1 = int(input("Ange tal 1: "))
    nr_2 = int(input("Ange tal 2: "))
    return nr_1, nr_2

print(get_nrs())

teacher_1, teacher_2 = get_teacher_name()

print(f"{teacher_1} & {teacher_2}")
```

### Funktioner med parametrar

```python
def print_three_times(x):
    """Skriver ut x tre gånger
    Args:
        x (str): Strängen som ska skrivas ut
    """
    print(x)
    print(x)
    print(x)

def hej(name):
    """Välkomnar en användare
    Args:
        name (str) : Namnet på användaren
    """
    print(f"Hej {name}!")

# Kör funktionerna
name = input("Vad heter du? ")
hej(name)

text = input("Vad vill du skriva ut tre gånger? ")
print_three_times(text)
```

### Funktioner med datum
```python
from datetime import date, datetime

def days_to_christmas():
    today = date.today()
    xmas = date(2022, 12, 24)
    days_left = xmas - today
    return days_left.days

def days_to_date(user_date):
    today = date.today()
    days_left = user_date - today
    return days_left.days

def days_between_dates(date_1, date_2):
    days_left = date_2 - date_1
    return days_left.days

def get_date_from_user():
    year = int(input("År: "))
    month = int(input("Månad: "))
    day = int(input("Dag: "))
    future_date = date(year, month, day)
    return future_date

def main():
    d_1 = get_date_from_user()
    d_2 = get_date_from_user()
    days = days_between_dates(d_1, d_2)
    print(f"Det är {days} mellan dina datum")

main()
```

### Egna moduler

#### song.py
```py
import let_it_be

let_it_be.song()
```

#### let_it_be.py
```py
"""This module presents the lyrics to the song: Let it be, by Beatles"""

def song():
    """Prints the full song"""
    vers_1()
    print("")
    vers_2()
    print("")
    chours()
    print("")
    vers_3()
    print("")
    vers_4()
    print("")
    chours_2()
    print("")
    chours()
    print("")
    chours()
    print("")
    vers_5()
    print("")
    vers_6()
    print("")
    chours_2()
    print("")
    chours()

def chours():
    print("Let it be, let it be")
    print("Let it be, let it be")
    print("Whisper words of wisdom")
    print("Let it be")

def chours_2():
    print("Let it be, let it be")
    print("Let it be, let it be")
    print("Yeah, there will be an answer let it be")

def vers_1():
    print("When I find myself in times of trouble")
    print("Mother Mary comes to me")
    print("Speaking words of wisdom, let it be")

def vers_2():
    print("And in my hour of darkness")
    print("She is standing right in front of me")
    print("Speaking words of wisdom, let it be")

def vers_3():
    print("And when all the brokenhearted people")
    print("Living in the world agree")
    print("There will be an answer, let it be")

def vers_4():
    print("For though they may be parted")
    print("There is still a chance that they will see")
    print("There will be an answer, let it be")

def vers_5():
    print("And when the night is cloudy")
    print("There is still a light that shines on me")
    print("Shine on until tomorrow, let it be")

def vers_6():
    print("I wake up to the sound of music")
    print("Mother Mary comes to me")
    print("Speaking words of wisdom, let it be")
```
-->