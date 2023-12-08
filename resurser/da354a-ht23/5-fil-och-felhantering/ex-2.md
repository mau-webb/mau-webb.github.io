---
id: da354a-ht23
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

#### Övning 3 - Nolldivision

Skriv en funktion `divide_numbers` som tar två tal som parametrar och returnerar resultatet av att dela det första talet med det andra talet. Lägg till felhantering för att undvika division med noll. Om användaren försöker dela med noll, be dem att skriva in nämnaren igen tills ett giltigt värde ges. Använd en loop för att upprepa inmatningen tills en giltig nämnare ges.

Exempelkörning kan se ut såhär:
```python
Ange täljaren: 3
Ange nämnaren: 5
Resultatet av divisionen är: 0.6

Ange täljaren: 10
Ange nämnaren: 0
Du kan inte dela med noll. Försök igen.
Skriv in en ny nämnare: 5
Resultatet av divisionen är: 2.0
```

#### Övning 4 - Trasig kalkylator

Vår kalkylator är känd för att vara lite slarvig och råkar ibland blanda ihop knapparna. Ditt uppdrag är att skapa en funktion `add_numbers(num_1, num_2)` som tar två tal som parametrar och försöker addera dem. Men var försiktig, för vår kalkylator kan ibland lägga ihop bokstäver istället för siffror och blir helt snurrig!

Din uppgift är att implementera funktionen `add_numbers` och inkludera felhantering för att hantera fall där inmatningen inte är giltig. Om något går snett, låt kalkylatorn säga "Oops! Något gick fel. Prova med riktiga siffror."

Fortsätt att mata in tal tills du skriver "Stop" (utan citationstecken). Programmet kommer att fortsätta att fråga efter tal tills du ger giltig inmatning eller skriver "Stop".

Exempelkörning kan se ut såhär:
```python
Välkommen till Slarviga Kalkylatorn!
Mata in det första talet (eller 'Stop' för att avsluta): 1
Mata in det andra talet (eller 'Stop' för att avsluta): 3
Resultatet av additionen är: 4

Mata in det första talet (eller 'Stop' för att avsluta): 12
Mata in det andra talet (eller 'Stop' för att avsluta): d
Oops! Något gick fel. Prova med riktiga siffror.

Mata in det första talet (eller 'Stop' för att avsluta): 4
Mata in det andra talet (eller 'Stop' för att avsluta): stop
Tack för att du använde Slarviga Kalkylatorn!
```

Lycka till med att hantera vår slarviga kalkylator och fortsätt tills du är nöjd med inmatningen!

#### Övning 5 - Fångad i tid

En tidsmaskin har blandat ihop tidpunkterna och vi måste räkna ut rätt tid igen. Skapa en funktion `calculate_time(hours, minutes)` som tar antalet timmar och minuter och försöker räkna ut rätt tid. Men om tidsmaskinen strular, se till att det visas ett felmeddelande om att tiden är försvunnen i tiden.

Exempelkörning:
```python
Välkommen till Fångad i tid!

Ange antal timmar: 1
Ange antal minuter: 20
Rätt tid är: 1 timmar och 20 minuter

Ange antal timmar: 1
Ange antal minuter: 150
Rätt tid är: 3 timmar och 30 minuter

Ange antal timmar: 3
Ange antal minuter: 2000
Rätt tid är: 36 timmar och 20 minuter

Ange antal timmar: i
Ange antal minuter: 3
Tiden är försvunnen i tiden!

Ange antal timmar: 30
Ange antal minuter: k
Tiden är försvunnen i tiden!

Ange antal timmar: d
Ange antal minuter: d
Tiden är försvunnen i tiden!

Ange antal timmar: stop

Tack för att du använt Fångad i tid!
```

Lycka till med att räkna ut rätt tid och hantera tidsmaskinens konstigheter! Om du har några frågor eller behöver ytterligare hjälp, är jag här för att assistera.

### Exempellösningar

- [Övning 1 - Förbättra er bokhanterare](../ex-solutions/Ö2.1.py)
- [Övning 2 - Kontrollera användarinput](../ex-solutions/Ö2.2.py)
- [Övning 3 - Nolldivision](../ex-solutions/Ö2.3.py)
- [Övning 4 - Trasig kalkylator](../ex-solutions/Ö2.4.py)
- [Övning 4 - Fångad i tiden](../ex-solutions/Ö2.5.py)