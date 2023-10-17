---
id: da354a-ht23
title: "Modul 3 - Iteration & Selektion"
---

# Modul 3 - Iteration & Selektion

## Iteration och selektion

### Inledning

I denna del finns det bra övningar som täcker in både funktioner, iterationer, seletioner.

## Övningar

### Övning 1

Inled med att skriv funktionen `udda1()`, som ska skriva ut samtliga udda tal i intervallet 1-100.
`1 3 5 7 9 11 13 15 ... 97 99`

Förbättra sedan utskriften så att det finns kommatecken mellan talen. Det sista kom-matecknet ska inte skrivas ut!
`1, 3, 5, 7, 9, 11, 13, 15 ... 97, 99`

Utskriften kan göras genom att en från början tom textsträng `svar = ""` fylls på med hjälp av konkatenering (+ operator mellan strängar) i en while-iteration. Därefter skrivs textsträngen ut. Skriv även funktionen `udda2(limit)` så att samtliga udda tal från 1 till och med limit. T.ex. udda(9) skriver ut:
`1, 3, 5, 7, 9`

Du kan behöva en for-iteration. En funktion `range` kan användas för att generera heltal. `range(start, stopp, steg)` de två sista parametrarna kan uteslutas. Funktionen kan användas i en for-iteration på följande vis:

```python
for i in range(4,7,2):
    print(i)
```

Och det ger utskriften:

```bash
4
6
```

### Övning 2

Skriv en funktion, `positive_negative()`, som
- Frågar efter ett heltal
- Skriver ut om talet är positivt, negativt eller noll
Detta görs ett valfritt antal gånger. Användaren får själv avgöra om han/hon vill sluta efter varje utskrift.

### Övning 3

Skriv funktionen `interval_sum(a, b)` (du kan anta att både a och b är heltal) som ska utföra följande:

- Kontrollera att a är mindre än, eller lika med b
- Om ovanstående villkor är uppfyllt så ska funktionen
    1. Skriva ut intervallet
    2. Skriva ut en lista av alla heltal i intervallet (inklusive intervallgränserna)
    3. Returnera summan av alla heltal i intervallet (inklusive intervallgränserna)
- Om villkoret inte är uppfyllt ska None returneras

Till exempel skall följande körningar ge resultatet:
```python
>>> print(f'Summan av heltalen mellan 4 och 7: {interval_sum(4, 7)}')
Intervallet: 4-7
[4, 5, 6, 7]
Summan av heltalen mellan 4 och 7 är 22
```

**Tips**: För att skriva ut `[1, 2, 3, 4, 5, 6, 7, 8, 9]` kan man skriva ```print(list(range(1,10))) ```
{: .info}

### Övning 4 - Betygsgenerator

Skriv ett program som frågar användaren efter fem tentamenspoäng. Programmet skall visa ett bokstavbetyg för varje poäng samt även visa medel-betyget bland alla poäng. Skriv följande funktioner i programmet.

`calc_average`

Den här funktionen skall fråga efter fem (5) tentamenspoäng som argument och returnera medelpoängen.

`determine_grade`

Denna funktion skall ta en tentamenspoäng som argument och sedan returnera dess motsvarighet i bokstavsbetyg. Se tabell 1 för hur konvertering mellan poäng och betyg skall ske.

<table>
	<tr>
		<th>Poäng</th>
		<th>Betyg</th>
	</tr>
	<tr>
		<td>90-100</td>
		<td>A</td>
	</tr>
	<tr>
		<td>80-89</td>
		<td>B</td>
	</tr>
	<tr>
		<td>70-79</td>
		<td>C</td>
	</tr>
	<tr>
		<td>60-69</td>
		<td>D</td>
	</tr>
	<tr>
		<td>Under 60</td>
		<td>E</td>
	</tr>
</table>


### Övning 5
Skriv ett program som genererar 100 slumpmässiga nummer och sedan räknar ut hur många av dessa nummer som är jämna respektive udda. Använd biblioteket `random` för att lösa denna uppgift.