---
id: da354b-ht25
title: "Modul 2 - Funktioner"
---

# Modul 2 - Funktioner

## Föreläsning - Funktioner (2)

<div class="frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.2696%; padding-top: 58px;"><iframe src="https://www.slideshare.net/slideshow/embed_code/key/bqsN1Gwr1JRbI" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no"></iframe></div>
</div>

---

Ni kan även ladda ner PDF-versionen av presentationen [här](../pdf/2024-Funktioner2.pdf).

---

Här kommer dagens exempelkod:

### Moduler i Python

```python
from random import randint

# Skriv ut ett slumptal mellan 0 och 100
print(randint(0,100))
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

```py
'''
This module presents the lyrics to the song: Let it be, by Beatles
'''

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

#### my_functions.py
```py
from datetime import date, datetime

def get_users_name():
    """Hämtar användarens namn
    
    Returns:
        str: Användarens namn
    """
    user_name = input("Vad heter du? ")
    return user_name

def calculate_sum_of_two_numbers(first_number, second_number):
    """Räknar ut summan av två tal
    
    Args:
        first_number: Det första talet vi vill räkna med
        second_number: Det andra talet vi vill räkna med
        
    Returns:
        int: Summan av de två talen
    """
    sum_of_numbers = first_number + second_number
    return sum_of_numbers

def get_int_from_user():
    """Frågar användaren efter ett heltal, och returnerar sedan detta som datatypen heltal
    
    Returns:
        int: Det heltal som användaren angivit
    """
    number = input("Ange ett heltal: ")
    return int(number)

def days_to_christmas():
    """Beräknar tid till julafton
    
    Returns:
        datetime: Tid kvar till julafton
    """
    today = datetime.now()
    christmas_date = datetime(2024, 12, 24)
    days_left = christmas_date - today
    return days_left
```

#### demo.py
```py
from my_functions import get_users_name, calculate_sum_of_two_numbers, get_int_from_user

def main():
    name = get_users_name()
    number_1 = get_int_from_user()
    number_2 = get_int_from_user()

    result = calculate_sum_of_two_numbers(number_1, number_2)

    print(name + " Summan blir: " + str(result))

    print("{}, summan blir {}".format(name, result))
    print(f"{name}, summan blir {result}")

main()
```

#### demo_2.py
```py
from my_functions import days_to_christmas

print(days_to_christmas())
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