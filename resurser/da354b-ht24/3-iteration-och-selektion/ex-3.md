---
id: da354b-ht24
title: "Modul 3 - Iteration & Selektion"
---

# Modul 3 - Iteration & Selektion

## Introduktion till iterationer

### Inledning

Iterationer (eller **loopar** som det också brukar kallas) används flitigt inom programmering för att repetera kod. Om man repetera en sak, eller viss kod t.ex. 10 gånger, så vill vi ju inte behöva upprepa (skriva) samma kod 10 gånger. Vi kan då istället göra en iteration som upprepar vår kod 10 gånger, mycket smidigare!

En iteration hjälper oss alltså att upprepa vald kod en eller flera gånger.

#### Olika typer av iterationer

Vi kommer i denna modul titta på två olika typer av iterationer, `for` och `while`. Både iterationer har samma syfte, d.v.s. att repetera en viss kod. Men de skiljer sig lite åt som ni kommer se i exemplen nedan. En tumregel på vilken av iterationerna man ska använda är: om man vet hur många gånger iterationen ska repeteras så väljer man `for`, om man inte vet så väljer man `while`.

### Iteration: for

En [for-iteration](https://docs.python.org/3.10/tutorial/controlflow.html#for-statements) används oftast när man vet hur många gånger en vald bit kod ska upprepas. I Python används ofta for-iterationer i samband med _listor_ (t.ex. skriva ut alla saker i en lista), som vi kommer att titta närmare på i nästa modul. Syntaxen för en for-iteration är följande:

```python
for i in x:
    # Do something
```

`x` i exmplet ovan är en mängd av något slag, t.ex. en lista, en sträng. `i` representerar vaje "sak" i listan/sekvensen, eller varje tecken i strängen.

Bra att ha koll på (smygstart på listor/sekvenser) är funktionen [`range()`](https://docs.python.org/2/library/functions.html#range). Denna funktion skapar en sekvens med tal och är bra om man vill repetera en iteration x antal gånger. Exempel på användning av funktionen `range`:

```python
range(1) # Ger sekvensen: (0)
range(10) # Ger sekvensen: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
range(2, 5) # Ger sekvensen: (2, 3, 4)
range(5, 15) # Ger sekvensen: (5, 6, 7, 8, 9, 10, 11, 12, 13, 14)
```

Vi kommer i denna modul att nöja oss med att använda funktionen med ett argument, t.ex. `range(10)`, där 10 kommer representera hur många gånger vår iteration kommer att upprepas. Exempel på iterationer:

```python
# Iteration som körs 10 gånger
for i in range(10):
    # Skriver ut "Kod i for-iterationen!" varje gång iterationen körs (totalt 10 gånger)
    print("Kod i for-iterationen!")

# Iteration som körs 5 gånger
for i in range(5):
    # Skriver ut aktuellt nummer från sekvensen som genereras av funktionen "range"
    print(f"{i} rundan som iterationen går!")
```

_Tänk på att_ functionen `range` börjar räkna från 0, om inget annat anges.

__Övning__: Kopiera och testkör koden i exemplet ovan. Testa att ange olika värden för hur många gånger de olika iterationerna ska repeteras - fungerar det som förväntat?
{: .info}

### Iteration: while

`While`är en annan typ av iteration. Till skillnade från for-iterationer som repeterar en bit kod ett bestämt antal gånger, så repeterar while-iterationer en bit kod _så länge ett vilkor är uppfyllt_. Vi behöver alltså inte på förhand bestämma hur många gånger iterationen ska repeteras, utan det kan variera varje gång iterationen körs. Syntaxen för en while-iteration är följande:

```python
while test:
    # Do something
```

`test` i kodexemplet är ett _vilkor_ som antingen resulterar i sant eller falskt. Så länge vilkoret är sant så upprepas iterationen ytterliggare en gång. Om vilkoret istället är falskt så avbryts iterationen. Låt säga att vi vill göra en while-iteration som repeterar vår kod 10 gånger, då skulle det se ut såhär:

```python
i = 0
while i < 10:
    print(f"Kod i while-iterationen! 'i' är: {i}")
    i = i + 1
```

Iterationen ovan har vilkoret `i < 10`, alltså om variabeln `i` är mindre än 10 så repeteras koden i iterationen en gång till (och testar sedan vilkoret igen), om `i` är 10 eller större så kommer iterationen av avbrytas. Vi säger innan iterationen att `i = 0` och varje gång som iterationen repeteras blir `i` ett större. Detta ända till `i` får värdet `10` och vilkoret `i < 10` inte längre är sant - och iterationen avslutas.

Vi nämnde innan att man ofta använder while-iterationer när man inte vet hur många gånger en iteration ska repeteras (till skillnad från exemplet ovan). Ett exempel på det kan vara att man t.ex. frågar användaren om iterationen ska repeteras en gång till. Se exempel:

```python
print("Test av while-iteration")
while input("Vill du köra en gång till? ") == "Ja":
    print("Ett varv i while-iterationen!")
print("Slut på det roliga")
```

I exemplet ovan kommer vi att skriva ut `Ett varv i while-iterationen!` så länge användaren svara `Ja` på frågan "Vill du köra en gång till?" (då vårt vilkor blir sant). När vi inte svarar `Ja` blir vilkoret falskt och iterationen avslutas. Se exempelkörning av koden ovan:

![Example of while-loop](../images/test-while-loop.png)

__Övning:__ Testkör de två kodexemplen ovan - se så att de fungerar. För kodexempel ett, ändra så att iterationen körs 15 gånger istället för 10. För kodexempel två, byt ut frågan och svaret i while-vilkoret till valfri ny fråga/svar.

### Övningar

#### Övning 1 - Upprepning

Använd en for-iteration för att skriva ut strängen `Iterationen 'for' sparar massor med arbete!` 15 gånger. Gör sedan samma sak fast med en while-iteration och strängen `Iterationen 'while' sparar massor med arbete!`. Utskriften ska se ut såhär:

![Example of for- and while-loops](../images/for-and-while-loops.png)

#### Övning 2 - Upprepning (igen)

Emma har varit elak i klassen och har därför fått som hemuppgift att skriva meningen "Jag ska inte kasta suddgummin på Kalle!" 500 gånger. Hjälp Emma med hemuppgiften genom att skriva en funktion som skriver ut meningen 500 gånger. Kalla funktionen `def emma():`. Resultatet ser ut på följande sätt:

![Idle](../images/elaka-emma.png)

osv.

#### Övning 3 - Funktioner och iterationer

Er uppgift är att skriva funktionen `print_num_times` som ska ha två parametrar. Den första parametern `content` ska innehålla det som ska skrivas ut och den andra parameters `times` ska innehålla hur många gånger det ska skrivas ut. Ni kan utgå från exempelkoden:

```python
content = input("Vad vill du skriva ut? ")
times = int(input("Hur många gånger vill du skriva ut det? "))
print_num_times(content, times)
```

Exempelkörning kan se ut såhär:

![Idle](../images/hej-hopp.png)

#### Övning 4 - Räkna Bokstäver

Bli en bokstavsdetektiv med funktionen `count_letters(word)`! Den här hemliga agenten tar emot ett mystiskt ord som sitt uppdrag och avslöjar hur många bokstavsledtrådar det innehåller. Låt oss knäcka koden och räkna bokstäverna!


Exempelkörning kan se ut såhär:

```python
Antal hemliga bokstavsledtrådar i 'chokladkaka42' är: 11
Antal hemliga bokstavsledtrådar i 'axels32_katter_åt' är: 13
Antal hemliga bokstavsledtrådar i 'piano2' är: 5
```