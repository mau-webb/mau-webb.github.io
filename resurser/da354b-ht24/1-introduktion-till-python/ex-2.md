---
id: da354b-ht24
title: "Modul 1 - Introduktion till Python"
---

# Modul 1 - Introduktion till Python

## 2.a. Variabler & datatyper

#### Rekommenderad läsning

- [Think Python - Chapter 2 Variables, expressions and statements](http://greenteapress.com/thinkpython2/html/thinkpython2003.html)

### Inledning

Precis som i andra programmeringsspråk så använder man i Python variabler för att spara olika värden, som kan vara bra att ha koll på. En variabel med värde skrivs såhär i Python:

```python
variabelnamn = värde
```

Exempel på olika variabler:

```python
name = "Anton"
year = 2023
leap_year = False
```

Som ni kanske noterat innehåller de tre olika variablerna ovan (`name`, `year`, `leap_year`) tre olika datatyper. De olika datatyperna finns till för att tydliggöra vilken typ av information som sparas i variabeln. Är det text, siffror eller sant/falskt värden som sparas i variabeln?

1. `Anton` är av typen *sträng* (`str`)
2. `2023` är av typen *heltal* (`int`)
3. `leap_year` är av typen *boolean* (`bool`)

Det finns fler datatyper i Python, men till en börjar så använder vi de tre i listan ovan.

### Övningar - Variabler & datatyper

#### En första övning i att använda variabler:

1. Skapa en ny Python-fil i mappen för modul 1 och skriv in följande kod:
```python
name = "Anton"
print("Hej " + name + "!")
```
2. Kör koden genom att klicka på play-knappen eller använd Ctrl+F5
3. Ändra värdet för variabeln `name` till ditt eget namn
4. Kör koden igen och se hur utskriften i terminalen uppdateras med ditt namn

<p class="info">
    Det som händer ovan är att vi <strong>slår ihop</strong> tre strängar till en genom <code class="highlighter-rouge">+</code>. Vi kan allså läsa ut:
    <code class="highlighter-rouge">print("Hej " + name + "!")</code> som <code class="highlighter-rouge">print("Hej " + "Anton" + "!")</code> i exemplet ovan.
</p>

#### Att tänka på vid utskrifter med textsträngar & tal

Till skillnad från vissa andra programmeringsspråk (t.ex. JavaScript) så kan man i Python inte konkatenera (lägga ihop) en textsträng och ett tal. Följande exempel fungerar alltså inte:

```python
product = "T-shirt"
price = 100
print("Produkten: " + product + " kostar " + price + "SEK")
```

Kör man koden ovan så kommer man att få följande fel:

```python
Traceback (most recent call last):
  File "C:/Users/tsanti/Desktop/main.py", line 3, in <module>
    print("Produkten: " + product + " kostar " + price + "SEK")
TypeError: can only concatenate str (not "int") to str
```

Den sista raden i felmeddelande talar om att vi inte kan konkatenera en sträng (str) med ett tal (int). Detta kan man lösa genom att göra om talet till en sträng, genom funktionen `str()`, se fungerande kod:

```python
product = "T-shirt"
price = 100
print("Produkten: " + product + " kostar " + str(price) + "SEK")
```

### En andra övning i att använda variabler:

Vi ska nu göra ett enkelt program som beräknar summan av två tal. De två talen ska anges i vars en variabel och summan ska sedan skrivas ut genom att använda "print"-funktionen. När du kör programmet ska det se ut såhär i terminalen:

![Exempel på körning av programmet](../images/vscode-exemple-of-using-vars.png)

1. Skapa en ny Python-fil som vi ska jobba i
2. Kopiera in koden nedan till er Python-fil (och spara filen på lämplig plats)
```python
print("Summan av " + str(first_number) + " och " + str(second_number) + " är " + str(first_number + second_number))
```

Ni behöver nu skapa variablerna `first_number` och "second_number" för att ert program ska fungera.

* Tänk på att variablerna `first_number` och `second_number` ska ligga ovanför `print`-funktionen då dokumentet läses uppifrån och ner.

### Tips

Man kan alltid kontrollera datatypen för ett värde direkt i VS Code genom att skriva följande i din fil:

```python
x = 10
print(type(x))
```

```sh
<class 'int'>
```
---

## 2.b. Användarinput

Hittills har vi bestämt värdet på de variabler som vi skapat, t.ex. vad vi heter, vilka tal vi vill räkna med osv. Denna information skulle ju bli mer intressant om vi kan få den från personen som använder vårt program. Vi kan i Python fråga användaren efter input/indata till vårt program genom funktionen `input()`.

Vill vi fråga användaren efter dennes namn (och spara det som användaren skriver in i variabeln `name`) så kan vi skriva:

```python
name = input("Vad heter du? ")
```

Variabeln `name` kommer då att innehålla det namn som användaren angett i terminalen när programmet körs.

Vill vi sedan välkomna användaren, så kan vi helt enkelt skriva ut det namn som användaren skrev in, genom att använda oss utav variabeln `namn`.

```python
name = input("Vad heter du? ")
print("Hej " + name + "!")
```

När du kör programmet kommer det se ut något i stil med:

![Idle](../images/vscode-name-input.png)

### Övningsuppgift 1

Vi ska nu utöka programmet ovan som hälsar personen välkommen. Vi ska, förutom att fråga efter personens namn, även fråga var personen bor och personens ålder. När vi är klara så ska det se ut något i denna stilen:

![Exempel på körning av programmet](../images/2-1.png)

Tillvägagångssätt:

1. Förutom att hämta in namnet från besökaren till ert program, ska vi nu skapa två variabler till där vi ska spara besökarens hemstad och ålder
2. Utgå från koden ovan, men modifiera den enligt:
   1. Skapa en variabel `name` och använd funktionen `input` för att hämta in svaret från användaren
   2. Skapa variabeln `location` och använd funktionen `input` för att hämta in svaret från användaren
   3. Skapa variabeln `age` och använd funktionen `input` för att hämta in svaret från användaren
   4. Uppdatera "print"-raden så att den även skriver ut besökarens hemstad och ålder (så att det ser ut som på bilden ovan)

### Övningsuppgift 2

Vi ska nu bygga ett enkelt multiplikationsprogram. Programmet ska fråga användaren efter två tal, sedan visa produkten av dessa talen (se resultatet på bilden nedan). Programmets kod bör följa en struktur som liknar den ni använde vid [övningsuppgift 1](#%C3%B6vningsuppgift-1).

![Exempel på körning av programmet](../images/2-2.png)

* Tänk på att den input som man får från användaren genom funktionen `input` är av datatypen sträng. Alltså - för att räkna med de tal som användaren skriver in behöver vi göra om numret till ett tal (till exempel genom att använda `int()`), t.ex. såhär:

```python
first_number = int(input("Tal 1: "))
```

I övrigt är det upp till er hur ni konstruerar programmet, så länge resultatet liknar utskriftsbilden ovan.

### Övningsuppgift 3 - extra utmaning

Vi ska nu skapa ett program som multiplicerar ett tal med sig självt (kvadrerar talet). Programmet ska fråga använderen om **ett tal** och sedan skriva ut kvadraten av talet.

Exempel på hur resultatet kan se ut såhär:
```python
Tal: 5
5 * 5 = 25
```
eller såhär:
```python
Tal: 5
5^2 = 25
```

Om du löste uppgiften med att använda `variabel * variablen`, testa att använda [`**`-operatorn](https://www.geeksforgeeks.org/what-does-the-double-star-operator-mean-in-python/) istället (använd `number ** 2` istället för `number * number`). Vad händer? 
