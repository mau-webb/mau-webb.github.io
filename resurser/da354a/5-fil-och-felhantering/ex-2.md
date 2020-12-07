---
id: da354a
title: "Modul 5 - Fil- och felhantering i Python"
---

# Modul 5 - Fil- och felhantering i Python

## 1. Introduktion till felhantering

### Inledning

Ibland när man programmerar så blir det inte alltid som man har tänkt sig. Ibland så smyger sig buggar in i programmen man skriver och programmet kraschar (och i IDLE visas en härligt röd text). Detta kan dels bero på programmet behöver förbättras, men kan även bero på externa faktorer.

Har ni till i övning 1 (Introduktion till filhantering) försökt att öppna en fil som inte finns? Vad händer då?
{: .info}

Att en fil (som kanske borde finnas?) inte finns kan vara en extern faktor varför ett program kraschar, en annan kan vara felaktig inmatning av användaren. Man kan då bygga förebyggande funktionalitet för att hantera fel som dessa. Detta genom metoden `try` och `except`, där man helt enkelt försöker köra något - men skulle det bli fel (t.ex. filen man vill öppna inte finns) så kan man hantera detta fel - utan att programmet kraschar. Smidigt!

### Att hantera fel

Syntaxen i Python för att detta är:

```python
try:
    # Koden man vill försöka att köra
except:
    # Koden som körs, om det misslyckas
```

Ett exempel på detta skulle kunna se ut såhär:

```python
try:
    print("Tal " + 2)
except:
    print("Något blev fel!")
```

Vi försöker i exemplet ovan att skriva ut `"Tal " + 2`, vilket ju kommer att generera ett fel - då vi inte kan skriva ut strängar tillsammans med tal. Istället för att programmet kraschar så körs istället `print("Något blev fel")`.

Man kan i Python fånga olika sorters fel, mer om detta kan ni läsa [här](https://docs.python.org/3/tutorial/errors.html). Det kan ju ibland vara bra att ta reda på vad det är för fel som skapas. En mycket enkel felhantering (för att identifiera felet) skulle kunna se ut såhär:

```python
import sys

try:
    print("Tal " + 2)
except:
    print("Fel:")
    print(sys.exc_info())
```

Detta ser i konsolen, när koden ovan körs, ut såhär:

![Idle](../images/idle6.png)

Ovan ser vi att felet var av typen `TypeError` och beskrivningen av *TypeError* var `cannot concatenate 'str' and 'int' objects`.

### Övningar

#### Övning 1 - Förbättra er bokhanterare

```python
text_file = open("movies.txt", "r")
print(text_file.read())
```

Utgå ifrån koden ovan, och skriv en felhanterare `try`/`except` för att öppna filen. Om filen `movies.txt` inte finns ska ett lämpligt felmeddelande visas, annars ska innehållet i filen skrivas ut:

Om filen *inte finns* ska det se ut såhär:

![Idle](../images/idle7.png)

Om filen *finns* ska det se ut såhär:

![Idle](../images/idle8.png)

Ni kan utgå från [denna fil](../files/movies.txt) (om ni inte vill skapa en egen).

#### Övning 2 - Kontrollera användarinput

Vi ska nu med hjälp av `try`/`except` säkerställa att användaren den input som vi eftersöker. Vi ska helt enkelt fråga användaren efter grader i fahrenheit som vi ska konvertera till celcius. Utgå ifrån koden nedan:

```python
fahrenheit = input('Enter Fahrenheit Temperature:')
fahrenheit = float(fahrenheit)
celcius = (fahrenheit - 32.0) * 5.0 / 9.0
print(celcius)
```

Kör man koden ovan och vi *inte* skriver in ett tal (med eller utan decimaler) så kommer programmet att krascha (testa att skriv in `hej` för att bekräfta detta). Er uppgift är att skriva en felhantering (m.h.a.`try`/`except`) för att kontrollera så att användaren matar in siffror/decimaltal. Ni ska dessutom göra en iteration som körs till det att användaren har matat in korrekt information. En exempelkörning kan se ut såhär:

![Idle](../images/idle9.png)