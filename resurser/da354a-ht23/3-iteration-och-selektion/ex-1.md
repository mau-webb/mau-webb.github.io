---
id: da354a-ht23
title: "Modul 3 - Iteration & Selektion"
---

# Modul 3 - Iteration & Selektion

## Introduktion till selektion

### Inledning

Ofta när man programmerar så kommer man till tillfällen då man vill göra olika saker beroende på situationen. Ett exempel skulle kunna vara en meny i ett program: om användaren väljer alternativ 1 så körs funktion 1, om användaren väljer alternetiv 2 så körs funktion 2 osv. Alltså när man i vardagligt språk använder ordet _om_. Detta görs i Python genom en __if-sats__. Syntax för detta är:

```python
if vilkor:
    # Gör detta
else:
    # Annars gör detta
```

`vilkor` i exemplet ovan är ett _test_ som antingen resulterar i `true` eller `false` (antingen är testet sant eller falskt). Är vilkoret sant kommer den kod som finns vid kommentaren `# Gör detta` att köras, om det är falskt kommer den kod som finns vid kommentaren `# Annars gör detta` att köras.

Här kommer ett exempel där vi vill kontrollera om ett tal är positivt eller inte, och skriver ut resultatet:

```python
number = 7
if number > 0:
    print(f"Talet: {number} är positivt!")
else:
    print(f"Talet: {number} är negativt!")

number = -2
if number > 0:
    print(f"Talet: {number} är positivt!")
else:
    print(f"Talet: {number} är negativt!")
```

Vårt vilkor i if-satserna ovan är `number > 0`, där vi kontrollerar om talet `number` är större än 0. Om talet är större än 0 körs kodraden `print("Talet: " + str(number) + " är positivt!")`, i alla andra fall körs kodraden `print("Talet: " + str(number) + " är negativt!")`. En testkörning ger således följande resultat:

![Idle](../images/idle5.png)

Det ser ju ut att fungera bra! Men vad händer om vi skriver `number = 0` och sedan kör if-satsen? Då kommer ju vårt program att säga att talet är negativt (eftersom det _inte_ är positivt, vilket vi testar). Detta löser vi genom att lägga till ytterliggare ett alternativ i vår if-sats genom `elif vilkor:` (förkortning för _else if_). Alltså kommer koden att se ut såhär:

```python
number = 0
if number > 0:
    print(f"Talet: {number} är positivt!")
elif number == 0:
    print("Talet är 0!")
else:
    print(f"Talet: {number} är negativt!")
```

Koden i exemplet ovan körs enligt följande steg:

1. Vi kontrollerar om talet är större än 0.
	- Om ja: Vi skriver ut att talet är positivt och avbryter vår if-sats.
	- Om nej: Vi hoppar vidare till nästa steg i if-satsen (`elif number == 0:`)
2. Vi kontrollerar om talet är 0.
	- Om ja: Vi skriver ut att talet är 0 och avbryter vår if-sats.
	- Om nej: Vi hoppar vidare till nästa steg i if-satsen (`else:`)
3. Eftersom talet varken är större än 0 eller exakt 0 så måste det vara mindre än 0. Så vi skriver ut att talet är negativt.

Notera att man endast kommer till steg 3 om _både_ vilkoren i steg 1 och 2 är falska.

Vilka olika vanliga operatorer/vilkorssatser som finns i Python kan ni läsa om [här](http://greenteapress.com/thinkpython2/html/thinkpython2006.html#sec56).

### Övningar

#### Övning 1 - Namnövning

I denna övning ska du skriva en funktion som avgör hur lång en sträng är. Det gör du med funktionen len. Exempel: `len("Kristina")` returnerar 8.

Skriv en funktion i Python som heter `name` som frågar efter en persons förnamn. Om namnet är högst 5 bokstäver långt ska meddelandet _"&lt;name&gt;, your name is short and sweet!"_ skrivas ut, annars ska _"&lt;name&gt;, your name is long and difficult!"_ skrivas ut. Funktionen börjar så här:

```python
def name():
```

Notera att "&lt;name&gt;" bara är ett exempel på input från användaren. Använd funktionen `input` för inmatningen.

#### Övning 2 - Maxvärden

I denna övning ska du skriva två funktioner som var och en returnerar det största av de två parametervärden. Börja med att skriva funktionen:

```python
def max_2(num_1, num_2):
```

Du ska använda if-satser (ev. bör du även använda else) med vettiga villkor för att finna det största av de båda parametrarna. Skriv sedan funktionen:

```python
def max_3(num_1, num_2, num_3):
```

Använd funktionen `max_2` när du skapar den andra funktionen.

#### Övning 3 - Betygsberäknare

I denna övning ska du skapa två funktioner som samverkar för att beräkna betyg utifrån poäng. Du kommer att bygga funktionen `calculate_grade` som tar emot en poängsumma och returnerar ett betyg baserat på följande tabell:

- Poäng över eller lika med **90** ger betyget **A**
- Poäng över eller lika med **80** ger betyget **B**
- Poäng över eller lika med **70** ger betyget **C**
- Poäng över eller lika med **60** ger betyget **D**
- Poäng över eller lika med **50** ger betyget **E**
- Poäng under **50** ger betyget **F**

`grade_report()`: Skriv en funktion som inte tar några parametrar. Funktionen ska be användaren att ange en poängsumma och sedan använda funktionen calculate_grade för att beräkna betyget. Funktionen ska sedan skriva ut betyget.

`calculate_grade(points)`: Skriv en funktion som tar emot en poängsumma som parameter. Funktionen ska använda ovanstående tabell för att bestämma och returnera det motsvarande betyget.


Exempel på körning:

```python
Ange poängsumma: 85
Betyg: B
```

**Tips:** Du kan använda funktionen `int()` för att konvertera en sträng till ett heltal.

### Exempellösningar

- [Övning 3 - Betygsberäknare](../ex-solutions/Ö1.3.py)