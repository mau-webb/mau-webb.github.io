---
id: da354a-ht23
title: "Modul 4 - Listor & Lexikon"
---

# Modul 4 - Listor & Lexikon

## Nästlade listor

### Inledning

Listor har visat sig vara väldigt smidiga när vi vill hantera data. Men ibland kan det vara begränsade att bara använda sig utav _endimensionella_ listor och det istället är bättre att använda sig utav _flerdimensionella_ listor (nästlade listor). Detta framförallt om man vill ha datastruktur som liknar en tabellstruktur med rader och kolumner.

Ett exempel på en nästlad skulle kunna se ut såhär:

```python
nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Den nästlade listan ovan skulle kunna, som tidigare nämnt, kunna liknas vid en tabell med tre rader med tre kolumner på varje rad. Hur skriver man då ut en nästlad lista? Det enklaste är nästlade for-iterationer, t.ex. såhär (för att skriva ut listan ovan):

```python
# Skriv ut alla tal på en ny rad
for i in nested_list:
    for j in i:
        print(j)

# Skriva ut i talen kolumner
for i in nested_list:
    for j in i:
        print(j, end="") # Ingen radbrytning efter utskrift
    print("") # Radbrytning
```

I exemplet ovan representerar `i` de inre listorna och `j` representerar själva siffrorna. Med andra ord kan man säga att `i` representerar raderna och `j` kolumnerna på varje rad.

Testa gärna att kopiera koden, testkör den i IDLE och prova att ändra i koden för att förstå nästlade listor bättre!

### Övningar

#### Övning 1 - Fotbollsspelare i listform

Vi ska nu skapa en nästlad lista där vi sparar information om olika fotbollsspelare. Den yttre listan ska innehålla x antal listor som i sig innehåller spelarens namn, ålder och klubb. Vi vill alltså skapa en struktur som ser ut något i stil med:

<table>
	<tr>
		<td>Viktor Claesson</td>
		<td>31</td>
		<td>FC Köpenhamn</td>
	</tr>
	<tr>
		<td>Niklas Hult</td>
		<td>33</td>
		<td>Elfsborg</td>
	</tr>
	<tr>
		<td>Jesper Karlsson</td>
		<td>25</td>
		<td>Bologna FC</td>
	</tr>
</table>

Som vi kan se så vill vi att varje rad ska innehålla en fotbollsspelare och kolumnerna ska innehålla namn/ålder/klubb. Er uppgift är nu att skapa denna struktur i en nästlad lista. Inspireras gärna av exemplen i introduktionen. När ni fått till de nästlade listorna så ska de också skriva ut och presentera spelarna på ett snyggt sätt. Ni ska minst ha _fem_ spelare i er struktur.

#### Övning 2 - Lägg till/ta bort spelare

Utgå från den lista ni skapade i förra övningen och bygg ny funktionalitet till ert program som gör det möjligt för användaren att lägga till och ta bort en spelare (alltså lägga till eller ta bort en _rad_ i er struktur).

#### Exempelkörning för övning 1 och 2

![Idle](../images/idle7.png)

#### Bonusövning! - Listor med lexikon

Vore det egentligen inte smidigare att spara fotbollsspelarna ovan i lexikon - där varje fotbollsspelare representeras av ett lexikon? Typ såhär:

```python
{
    "name": "Jesper Karlsson",
    "age": 25,
    "club": "Bologna FC"
}
```

Utmaninen är nu att bygga samma program som ovan, men använda lexikon *istället* för listor för att representera fotbollsspelarna.