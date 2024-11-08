---
id: da354a-ht23
title: "Modul 2 - Funktioner"
---

# Modul 2 - Funktioner

## Struktur av program

#### Rekommenderad läsning

- [Think Python - Chapter 3  Functions](http://greenteapress.com/thinkpython2/html/thinkpython2004.html)

### Inledning

När man programmerar är det viktigt att ha en bra och tydlig struktur på sitt program. Ett sätt att åstakomma detta är att noga dela upp sin kod i mindre funktioner, där _en funktion gör en sak_. På så sätt delar man upp sin kod i mindre bitar och koden blir mycket mer lättöverskådlig. I denna övning ska vi träna på att strukturera upp vår kod på ett bra sätt.

Se följande exempel. Vi har ett program som låter användaren multiplicera tre tal med varandra och programmet skriver sedan produkten av talen:

```python
name = input("Vad heter du? ")
print("*"*30)
print("Välkommen " + name + "!")
print("I detta program kan du mulitplicera tre tal med varandra - så beräknar vi produkten åt dig.")
print("Du kommer nu att får mata in de tre tal som du vill multiplicera med")
num_1 = int(input("Vilket är tal nr.1: "))
num_2 = int(input("Vilket är tal nr.2: "))
num_3 = int(input("Vilket är tal nr.3: "))
result = num_1 * num_2 * num_3
print("Produkten av dina valda tal är: " + str(result))
print("*"*30)
```

Detta program skulle vi kunna dela upp i mindre bitar - för att få en bättre och tydligare struktur. T.ex. såhär:

```python
def multiply_program():
    """Huvudfunktionen för multiplikationsprogrammet"""
    name = get_name()
    welcome(name)
    num_1 = get_number(1)
    num_2 = get_number(2)
    num_3 = get_number(3)
    result = multiply_three_numbers(num_1, num_2, num_3)
    print_result(result)

def get_name():
    """Frågar besökaren efter namn"""
    return input("Vad heter du? ")

def welcome(name):
    """Välkomnar besökaren och berättar programmets funktion"""
    print("Välkommen " + name + "!")
    print("I detta program kan du mulitplicera tre tal med varandra - så beräknar vi produkten åt dig.")
    print("Du kommer nu att får mata in de tre tal som du vill multiplicera med")

def get_number(number):
    """Frågar användaren efter ett tal"""
    return input("Vilket är tal nr." + str(number) + ": ")

def multiply_three_numbers(number_1, number_2, number_3):
    """Beräknar produkten av tre tal"""
    return int(number_1) * int(number_2) * int(number_3)

def print_result(result):
    """Skriver ut resultatet och tackar användaren"""
    print("Produkten av dina valda tal är: " + str(result))
    print("*"*30)

multiply_program()
```

Själva programmet ovan styrs av funktionen `multiply_program` (som sedan använder sig utav de övriga funktionerna) som vi kör längst ner i vårt kodexempel ovan. Skulle man vilka "optimera" funktionen `multiply_program` så skulle man kunna skriva funktionen på detta sätt:

```python
def multiply_program():
    """
    Huvudfunktionen för multiplikationsprogrammet
    """
    welcome(get_name())
    print_result(multiply_three_numbers(get_number(1), get_number(2), get_number(3)))
```

Till en början kan det tyckas att man skriver "mycket" kod när man delar upp sitt program i funktioner. Men ju mer kod man skriver ju nödvändligare blir det. Detta inte bara för att få en bättre översikt över sitt program, utan också för att saker som felsökning blir mycket enklare om man delat upp sitt program i funktioner. Dessutom händer det ofta att man återanvänder funktioner, som t.ex. funktionen `get_number` ovan - och man vill ju inte skriva samma kod mer än en gång!

### Övning 1

I denna del ska vi återanvända funktionen `yards_to_meters` som ni skrev i den förra övningen. Ni ska uppdatera ert program så att de olika delarna nu hamnar i en egen funktion (en funktion gör en sak), och ni ska ha följande funktioner:

* En huvudfunktion som styr hela programmet (likt `multiply_program` ovan)
* En funktion som välkomnar användaren
* En funktion som frågar efter antalet meter
* En funktion som beräknar resultatet
* En funktion som presenterar resultatet

Inspireras gärna av exemplet i introduktionen till denna övningsdel

## Övning 2

I denna övningen ska vi göra strukturera upp ett valutakonverteringsprogram, en förbättrad variant från det som ni byggde i modul 1. Programmet ska vara uppdelat i lämpliga funktioner, med en huvudfunktion som styr programmet. Det är upp till er hur ni väljer att dela upp de olika funktionerna. Diskutera sedan gärna med labbhandledaren kring er lösning - varför har ni strukturerat upp programmet som ni gjort? Vad hade ni kunnat göra annorlunda?

Resultatet av ert program ska vara följande:

![](../images/idle11.png)