---
id: da354b-ht24
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

#### Övning 3 - Bonusövning till 1 och 2!

Vore det egentligen inte smidigare att spara fotbollsspelarna ovan i lexikon - där varje fotbollsspelare representeras av ett lexikon? Typ såhär:

```python
{
    "name": "Jesper Karlsson",
    "age": 25,
    "club": "Bologna FC"
}
```

Utmaninen är nu att bygga samma program som ovan, men använda lexikon *istället* för listor för att representera fotbollsspelarna.

#### Övning 4 - Konvertera strängar till olika format
I denna övning ska du skapa en funktion som konverterar en sträng till olika format, som till exempel [camel case](https://en.wikipedia.org/wiki/Camel_case), [snake case](https://en.wikipedia.org/wiki/Snake_case), och [kebab case](https://developer.mozilla.org/en-US/docs/Glossary/Kebab_case). Funktionen ska ta en sträng som input och returnera den i de olika formaten.

**Uppgift**:

Skapa en funktion `convert_case(text)` som utför följande konverteringar:

- **Camel Case**: Börjar med liten bokstav och varje nytt ord börjar med stor bokstav. Mellanslag och andra icke-bokstäver tas bort. Exempel: "hello world" blir "helloWorld".
- **Snake Case**: Alla bokstäver är små och ord separeras med understreck (_). Exempel: "hello world" blir "hello_world".
- **Kebab Case**: Alla bokstäver är små och ord separeras med bindestreck (-). Exempel: "hello world" blir "hello-world".
- **Titel Case**: Varje ord börjar med stor bokstav, och alla andra bokstäver är små. Exempel: "hello world" blir "Hello World".

Funktionen ska returnera en lista med de olika konverterade strängarna i ordning: `[camel_case, snake_case, kebab_case, title_case]`.

Exempelkörning:
```python
print(convert_case("hello world"))
# Borde ge ['helloWorld', 'hello_world', 'hello-world', 'Hello World']

print(convert_case("Convert THIS to different Cases"))
# Borde ge ['convertThisToDifferentCases', 'convert_this_to_different_cases', 'convert-this-to-different-cases', 'Convert This To Different Cases']
```

#### Övning 5 - Ord och deras längd
I denna övning ska du skapa en funktion som tar en lista av ord och returnerar en lista av listor, där varje lista innehåller ett ord och dess längd. Listan ska vara sorterad i fallande ordning baserat på ordets längd.

**Uppgift**:

Skapa en funktion word_length_counter(words) som utför följande steg:

1. Iterera över listan av ord och skapa en lista för varje ord innehållande ordet och dess längd.
2. Sortera listan av listor i fallande ordning baserat på ordets längd.
3. Returnera den sorterade listan.

Exempelkörning:

```python
print(word_length_counter(["hello", "world", "Python", "is", "great"]))
# Borde ge [['Python', 6], ['hello', 5], ['world', 5], ['great', 5], ['is', 2]]

print(word_length_counter(["a", "list", "of", "words"]))
# Borde ge [['words', 5], ['list', 4], ['of', 2], ['a', 1]]
```

#### Övning 6 - Ord och deras längd med lexikon
I denna övning ska du skapa en funktion som tar en lista av ord och returnerar en **lista av lexikon**, där varje lexikon innehåller ett ord och dess längd. Listan ska vara sorterad i fallande ordning baserat på ordets längd.

**Uppgift**:

Skapa en funktion `word_length_counter(words)` som utför följande steg:

1. Iterera över listan av ord och skapa ett lexikon för varje ord, där nyckeln är `"word"` och värdet är själva ordet, och en annan nyckel `"length"` där värdet är ordets längd.
2. Sortera listan av lexikon i fallande ordning baserat på värdet av `"length"`.
3. Returnera den sorterade listan.

Exempelkörning:
```python
print(word_length_counter(["hello", "world", "Python", "is", "great"]))
# Borde ge [{"word": "Python", "length": 6}, {"word": "hello", "length": 5}, {"word": "world", "length": 5}, {"word": "great", "length": 5}, {"word": "is", "length": 2}]

print(word_length_counter(["a", "list", "of", "words"]))
# Borde ge [{"word": "words", "length": 5}, {"word": "list", "length": 4}, {"word": "of", "length": 2}, {"word": "a", "length": 1}]
```
