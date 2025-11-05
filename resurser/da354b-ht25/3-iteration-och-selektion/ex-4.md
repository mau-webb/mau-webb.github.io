---
id: da354b-ht25
title: "Modul 3 - Iteration & Selektion"
---

# Modul 3 - Iteration & Selektion

## Nästlade iterationer

### Inledning

Ibland räcker det inte med att man vill upprepa en bit kod med en iteration. Det finns tillfällen då man vill:

1. Upprepa en bit kod
2. För varje gång koden från punkt 1 upprepas, vill vi upprepa en annan kod.

Ett konkret exempel skulle kunna vara: Vi vill skriva ut alla veckor på ett år, och för varje vecka vill vi skriva ut alla dagarna. Den första iterationen (som ansvarar för veckorna) repeteras 52 gånger, medan den inre som skriver ut veckodagarna repeteras 7 gånger _varje gång som den uttry iterationen (veckorna) repeteras_. I kod skulle det se ut såhär:

```python
weeks = range(1, 53)
days = range(1,8)
for week in weeks:
    print(f"Vecka: {week}")
    for day in days:
        print(f"Dag nr: {day}")
```

Och när man kör koden börjar de såhär (och kör alla 52 veckorna):

![Idle](../images/days-with-num.png)

(Vi antar här (för enkelhetens skull) att årets första dag är "dag 1", d.v.s. en måndag, och att året har exakt 52 veckor)

Studera koden ovan noggrant, testkör den, testa att modifiera den. Så att du får en förståelse för hur den fungerar
{: .info}

### Övningar

#### Övning 1

Er första uppgift är att komplettera koden ovan med funktionen `day_name`, som har parametern `day_nr`. Utgå från koden:

```python
weeks = range(1, 53)
days = range(1,8)
for week in weeks:
    print(f"Vecka: {week}")
    for day in days:
        print(f"Dag nr: {day_name(day)}")
```

`day` är alltså i exemplet ovan ett tal mellan 1 och 7 som representerar en veckodag (1 = Måndag, 2 = Tisdag osv.). Använd er av if-satser i funktionen `day_name` för att returnera korrekt namn på dagen. När funktionen är klar ska utskriften se ut såhär:

![Idle](../images/days-with-name.png)

#### Övning 2 - Klockan

I denna övning ska vi skriva ut ett dygn i timmar, minuter och sekunder. Detta genom tre nästlade iterationer.

- Den yttersta iterationen ska representera antalet timmar
- Den mellersta iterationen ska representera antalet minuter
- Den innersta iterationen ska representera antalet sekunder

Resultatet ska se ut enligt följande:

![Idle](../images/the-clock.png)

osv.

#### Övning 3 - Pyramid

Nu ska bi bygga en pyramid av stjärnor genom nästlade iterationer. Den yttre iterationen ska representera varje rad (total 10st) och den inre ska representera varje rads stjärnor. Resultatet ska se ut på följande vis:

![Idle](../images/pyramid.png)