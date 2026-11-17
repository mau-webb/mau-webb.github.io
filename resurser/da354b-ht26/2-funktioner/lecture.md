---
id: da354b-ht26
title: "Modul 2 - Funktioner"
---

# Modul 2 - Funktioner

## Föreläsning - Funktioner

<div class="frame">
    <embed src="../pdf/2026-f.pdf" type="application/pdf" width="100%" height="485px">
</div>

### Dagens exempel

#### Lunchexempel

```python
def heading(text):
    """
    Prints a heading

    Args:
        text (str): Heading
    """
    print("-"*40)
    print(text)
    print("-"*40)

def day_lunch(day, lunch):
    """
    Presents a day with a lunch

    Args:
        day (str) : Weekday
        lunch (str) : Lunch dish
    """
    print("Lunch - " + day +": " + lunch)

def weeks_lunches():
    """
    Presents the lunches this week
    """
    day_lunch("Monday", "Lasanga")
    day_lunch("Tuesday", "Hamburger")
    day_lunch("Wednesday", "Tacos")
    day_lunch("Thursday",  "Pizza")
    day_lunch("Friday", "Soup")


heading("Welcome")
weeks_lunches()
heading("Goodbye")
```

#### Parametrar & argument

```python
def area(width, height):
    """Calculates the area of a rectangle"""
    result = int(width)*int(height)
    return result


user_width = input("Ange bredden: ")
user_height = input("Ange höjden: ")
calc_result = area(user_width, user_height)
print("Resultat: " + str(calc_result))
```
