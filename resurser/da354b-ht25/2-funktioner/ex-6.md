---
id: da354b-ht25
title: "Modul 2 - Funktioner"
---

# Modul 2 - Funktioner

## Utskriftsfunktioner

### Inledning

Hittillls när vi gjort utskrifter i våra program så har vi skapar utskrifterna genom att slå ihop strängar, t.ex. på följande sätt:

```python
name = "Anton"
age = 35
city = "Lund"

print(name + " är " + str(age) + "år och bor i " + city)
#=> Anton är 35år och bor i Lund
```

Detta fungerar visserligen fint, men har två brister:

1. Det är svårt att få en bra översikt av strängen (många `+` och strängar som slås ihop)
2. Vi behöver konvertera icke-strängar (t.ex. nummer (ålder) i exemplet ovan) till strängar

Python har andra utskriftsfunktioner som är bra att lära sig nu, mer om detta nedan! :)

### Utskrift genom funktionen `format()`

Istället för att slå ihop strängar vid utskrifter, så kan vi *stoppa in* värden i strängar genom funktionen `format()`. Skulle vi ta exemplet i inledningen och istället använda funktionen `format()` vid utskriften så skulle det så ut såhär (med samma resultat):

```python
name = "Anton"
age = 35
city = "Lund"

print("{} är {}år och bor i {}".format(name, age, city))
#=> Anton är 35år och bor i Lund
```

Personligen tycker jag att det blir mycket enklare att se helheten för utskriften, samt att vi slipper att omvandla datatyper till strängar vid utskrifter. Tittar vi närmre på funktionen så ser vi att `{}` ersätts av ett värde. Det första argumentet till funktionen `format` hamnar ersätter den första `{}`, osv.

![Exempel på format-funktionen](../images/format-function.png)

Vill man kan man även namnge platserna på följande sätt:

```python
name = "Anton"
age = 35
city = "Lund"

print("{n} är {a}år och bor i {c}".format(n=name, a=age, c=city))
#=> Anton är 35år och bor i Lund
```

#### Övningar

Gör om följande utskrifter så att de använder `format()`-funktionen:

```python
course_name = "Introduktion till programmering"
course_code = "DA354A"
course_credits = 7.5

print(course_name + "(" + course_code + ")" + ": " + str(course_credits) + "hp")
```

För koden nedan, gör en utskrift som använder sig utav `format()`-funktionen.

```python
title = "Star Wars"
year = 1977
director = "George Lucas"

#=> Star Wars släpptes 1977 och regisserades av George Lucas"
```

### Utskrift med `f` (Formatted string literals)

Sedan Python version 3.6 så kan man även använda s.k. *Formatted string literals* för att skriva ut variabler i en sträng. Detta gör det möjligt att direkt ange variabler (värden) i en sträng, vilket kan snabba upp hur vi gör utskrifter. Detta "*aktiveras*" genom att man skriver `f` framför den sträng man vill använda variabler i, t.ex.

```python
name = "Anton"
age = 35
city = "Lund"

print(f"{name} är {age}år och bor i {city}")
#=> Anton är 35år och bor i Lund
```

#### Övningar

Gör om följande utskrifter så att de använder `f`-metoden:

```python
course_name = "Introduktion till programmering"
course_code = "DA354A"
course_credits = 7.5

print(course_name + "(" + course_code + ")" + ": " + str(course_credits) + "hp")
```

För koden nedan, gör en utskrift som använder sig utav `f`-metoden.

```python
title = "Star Wars"
year = 1977
director = "George Lucas"

#=> Star Wars släpptes 1977 och regisserades av George Lucas"
```

Vilket sätt tycker du fungerar smidigast när man vill göra utskrifter? Tänk på att det är viktigt att ha koll på detta under resterande delar av kursen.
{: .info}