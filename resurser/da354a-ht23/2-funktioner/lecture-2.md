---
id: da354a-ht23
title: "Modul 2 - Funktioner"
---

# Modul 2 - Funktioner

## Föreläsning - Funktioner (2)

Publiceras efter att föreläsningen ägt rum.

<!--
<div class="frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.2696%; padding-top: 58px;"><iframe src="https://www.slideshare.net/slideshow/embed_code/key/LRxlOex9DYwwyL" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="encrypted-media;"></iframe></div>
</div>

Här kommer dagens exempelkod:

### Enkla funktioner

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
    """
    Funktion som säger god morgon
    """
    print("Godmorgon!")


def get_teacher_name():
    """
    Funktion som returnerar kursens lärare
    """
    return "Anton", "Johan"

def get_nrs():
    """
    Frågar användaren efter två nummer och returnerar dessa
    """
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
'''
This module presents the lyrics to the song: Let it be, by Beatles
'''

def song():
    '''
        Prints the full song
    '''
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