---
id: da354b-ht24
title: "Modul 1 - Introduktion till Python"
---

# Modul 1 - Introduktion till Python

## 3.a. Debugging

#### Rekommenderad läsning

- [Think Python - Chapter 2.8 Debugging](http://greenteapress.com/thinkpython2/html/thinkpython2003.html#sec23)

### Inledning

När man programmerar och skriver kod, blir det ibland fel. Det är lätt hänt att ett citat-tecken missas, koden indenteras lite fel eller att man har en paratens för mycket/lite. När man sedan försöker köra sin (felaktiga) kod så fungerar den inte och ett felmeddelande visas. Det är då viktigt att man lär sig tyda det felmeddelande som IDLE visar på ett så bra sätt som möjligt, så att man snabbt kan identifiera och åtgärda felet. Felsökning kan vara en riktig tidstjuv, så här kommer tre övningar med vanliga fel som det är bra att känna till.

Visste du att ordet *bug* faktiskt kommer från att en insekt (närare bestämt en nattfjäril) hittats död bland reläerna i en av de tidigare datorerna. Läs gärna mer på wikipedia om detta: [https://en.wikipedia.org/wiki/Software_bug](https://en.wikipedia.org/wiki/Software_bug)
{: .info}

Övningarna går till på så sätt att ni laddar ner en Python-fil, kör denna (den innehåller fel), rättar till felen och när programmet fungerar som förväntat (utan fel) så är övningen klar.

### Övning 1

I denna övning finns det *ett* fel som ni behöver identifiera och fixa till. Tänk på att titta igenom det felmeddelande som IDLE ger er, där ni del får en beskrivning av felet och del vilken rad felet framkallas på.

[Länk till filen](../files/py1.py)

### Övning 2

I denna övning finns det *två* fel som ni behöver identifiera och fixa till. Tänk på att titta igenom det felmeddelande som IDLE ger er, där ni del får en beskrivning av felet och del vilken rad felet framkallas på.

[Länk till filen](../files/py2.py)

### Övning 3

I denna övning finns det *två* fel som ni behöver identifiera och fixa till. Tänk på att titta igenom det felmeddelande som IDLE ger er, där ni del får en beskrivning av felet och del vilken rad felet framkallas på.

[Länk till filen](../files/py3.py)

---

## 3.a. Kommentarer

När man programmerar så är det viktigt att man förstår sin egen kod, ännu viktigare är det att andra förstår din kod. Detta eftersom man i större projekt nästan aldrig är ensam programmerare - utan ett team av programmerare som delar en gemensam kodbas. För att koden ska bli lättförståelig så är det viktigt att man kommenterar sin kod.

I Python kan man kommentera sin kod på två olika sätt:

1. Genom `#` om man vill göra en kommentar som endast är på en rad
2. Genom `"""` om man vill göra en kommentar som sträcker sig över flera rader

Såhär kan det t.ex. se ut, tillsammans med lite kod:

```python
"""Detta är ett program som frågar användaren efter tre tal. När
användaren har angivit dessa tre tal, så multipliceras de med
varandra och resultatet skrivs ut till användaren.
"""

# Välkomnar användaren till vårt program genom en trevlig utskrift
print("----------------------------")
print("| Multipliceringsverktyget |")
print("----------------------------")
print("Ange tre tal, så beräknar vi")
print("produkten av talen!")

# Frågar användaren efter det första talet, och sparar värdet i variabeln nr_1
nr_1 = input("Ange tal nr 1: ")
# Frågar användaren efter det andra talet, och sparar värdet i variabeln nr_2
nr_2 = input("Ange tal nr 2: ")
# Frågar användaren efter det tredje talet, och sparar värdet i variabeln nr_3
nr_3 = input("Ange tal nr 3: ")

# Beräknar produkten av talen (obs. vi gör om talen till nummer för beräkningen)
total_sum = int(nr_1) * int(nr_2) * int(nr_3)

# Skriver ut produkten av talen till användaren
print("Produkten av talen blir: " + str(total_sum))
```

Kommentarerna i exemplet ovan är *enbart* till för oss som läser koden - för att vi ska förstå den bättre. Datorn kommer, när den exekverar Python-koden, att ignorera de rader som är kommentarer.

Tänk på att det för din egen skulle är bra att kommentera din egen kod. Dels för att du ska komma ihåg **vad** koden gör, men även **varför** du valt att skriva koden på ditt valda sätt.
{: .info}

### Övning 1

Din uppgift är att läsa koden nedan - och sedan kommentera vad koden gör. Kommentera högst upp i dokumentet en beskrivning av själva programmet genom en `"""`-kommentar och kommentera sedan vad de olika raderna kod gör genom `#`-kommentarer.

```python
print("------------------")
print("Antons testprogram")
print("------------------")
a = int(input(": "))
b = int(input(": "))
c = int(input(": "))
d = a ** b / c
print(d)
```

**Fundera på:** Var koden ovan tydligt skriven? Om inte - hur skulle du skrivit den för att den skulle bli så enkel att förstå som möjligt?
{: .info}

### Övning 2

Implementera programmet nedan genom att läsa kommentarerna (kopiera kommentarerna till ett eget python-dokument och skriv koden där):

```python
# 1. Välkomna användaren

# 2. Fråga efter användarens ålder

# 3. Beräkna vilket år som som användaren är född, utifrån användaren ålder

# 4. Skriv ut resultatet för användaren
```