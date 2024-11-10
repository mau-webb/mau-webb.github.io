---
id: da354b-ht24
title: "Modul 3 - Iteration & Selektion"
---

# Modul 3 - Iteration & Selektion

## Nästlade if-satser

### Inledning

#### Flera test i ett vilkor

Ibland när man programmerar så räcker det inte med att man bara testar en sak i en if-sats (t.ex. `i < 10`, om `i` är mindre än 10), utan man vill testa två saker (t.ex. om `i < 10` och `i > 0`, alltså om `i` är mindre än 10 och större än 0). Detta kan man göra genom att kombinera olika test m.h.a. nyckelorden __och__ samt __eller__.

Låt säga att vi vill testa om ett tal är _större än 0 och mindre än 10_, hur skulle detta se ut?

```python
x = 5
if x > 0 and x < 10:
	print(f"{x} är mellan 0 och 10")
else:
	print(f"{x} är inte mellan 0 och 10")
```

För att vilkoret `x > 0 and x < 10` ska bli sant så behöver _både_ `x > 0` och `x < 10` vara sant. Man använder nyckelorder `and` för att kombinera fler olika test.

Men ibland vill man inte kontrollera att flera uttyck är sanna, utan kanske om _ett av flera_ uttryck är sanna. Detta gör man med hjälp av nyckelordet `or`. I exemplet nedan vill vi kontrollera ett tal är större _eller_ mindre än 0.

```python
x = 5
if x > 0 or x < 0:
	print(f"{x} är större eller mindre än 0")
else:
	print(f"{x} är 0")
```

I exemplet ovan blir vilkoret sant om antingen `x > 0` eller  `x < 0` är sant. Beroende på vad man vill testa i en if-sats kan nyckelorden `and` och `or` vara till stor hjälp.

#### Nästlade if-satser

När man skriver program i Python kommer man förr eller senare till en situation där man har många if-satser, och där man har _if-satser i if-satser_, detta kallas för nästlade if-satser. Det skulle kunna se ut såhär:

```python
number = input("Vilket tal vill du testa? ")
# Kontrollerar så att användaren har anget enbart siffror
if number.isdigit():
    # Kontrollerar om talet är positivt, negativt eller 0
    if int(number) > 0:
        print(f"{number} är större än 0")
    elif int(number) < 0:
        print(f"{number} är mindre än 0")
    else:
        print(f"{number} är 0")
else:
    print("Du får endast skriva in siffror")
```

I exemplet ovan ser vi ett exempel nästlade if-satser. Kör man koden så hände följande steg:

1. Vi frågar användaren efter ett tal
2. Vi kontrollerar om användaren endast skrivit in siffror
	- Om det bara är siffror inmatade:
		- Testar om numret är större än 0:
			- Om sant: Skriver ut att numret är större än 0 och avslutar if-satsen
			- Om falskt: Går vidare till `elif`
		- Testar om numret är mindre än 0:
			- Om sant: Skriver ut att numret är mindre än 0 och avslutar if-satsen
			- Om falskt: Går vidare till `else`
		- Skriver ut att talet är 0
	- Om det inte bara är siffror inmatade:
		- Berättar för användaren att bara siffror är tillåtna

Det finns som ni kan se många användningsområden för nästlade if-satser.

### Övningar

#### Övning 1 - Miniräknare

Din uppgift är att skriva ett enkel miniräknare som:

1. Frågar användaren om två tal som ska räknas med
2. Frågar användaren vilket räknesätt som ska användas
	- Om användaren inte väljer ett korrekt räknesätt ska detta meddelas
3. Om användaren väljer division ska ni kontrollera så att användaren inte försöker dividera med 0
	- Om användaren försöker dividera med 0 ska det meddelas att detta ej är tillåtet
4. Om steg 2 och 3 är OK, så ska resultatet av beräkningen presenteras för användaren

Såhär kan slutresultatet se ut:

![Idle](../images/idle6.png)

#### Övning 2 - Jämföra tärningsslag

Vi kan sedan förra inlämningsuppgiften slå tärningar (slumpa fram ett tal mellan 1 och 6). Nu ska vi slumpa fram tre tärningsslag och kontrollera följande:

1. Har alla tärningar samma värde?
2. Har två av tärningarna samma värde?
3. Har alla tärningar olika värde?

Denna uppgift ska ni lösa på två olika sätt:

1. Med nästlade if-satser
2. Genom vilkor med flera tester (if, elif, else)

Slutresultatet ska bli detsamma får båda era lösningar och se ut på följande sätt:

![Idle](../images/idle7.png)