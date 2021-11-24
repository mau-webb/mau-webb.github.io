---
id: da354a-ht21
title: "Modul 4 - Listor & Lexikon"
---

# Modul 4 - Listor & Lexikon

## Inlämningsuppgift

**Viktigt** Inlämningsuppgiften görs i grupp. Grupperna kommer att skapas slumpmässigt av de studenter som anmält sig till att göra inlämningsuppgiften via Canvas - se mer information där.

### 1. Introduktion

Denna inlämningsuppgift har som syfte att examinera modul 4 som har fokus på listor.

Inlämningsuppgiften är individuell genom grupper. Det betyder att varje student enskilt ska kunna redogöra för alla delar av inlämningsuppgiften.
{: .info}

### 2. Uppgiftsbeskrivning

Uppgiften går ut på att vi ska bygga ett spel, likt Keno, fast i en lite mindre variant. Spelet ska ha följande struktur:

- En meny där man kan välja att spela bingo, visa statistik, eller att avsluta programmet
- Bingo
    - Användaren blir ombedd att ange fem siffror mellan 1 och 25. Ni kontrollerar så att användaren:
        - angett exakt fem siffror
        - att alla siffrorna är korrekta (mellan 1 och 25),
        - att det inte anges några dubeletter av siffror
        - *annars ber ni användaren att ange fem nya siffror*
    - Dragning: Ni slumpar fram 10st tal mellan 1 och 25 som ni sedan presenterar för användaren i en utskrift, i form av en spelplan. (Se exempelkörning nedan - dock behöver din presentation inte se *exakt* likadan ut.)
    - Resultat: Resultatet av dragningen (antal rätt) presenteras för användaren
- Statistik
    - Användaren kan se sina resultat från tidigare spel

#### Exempelkörning

![Idle](../images/a-idle.png)

![Idle](../images/a-idle2.png)

### Tips

Det kan vara en god idé veta hur man göra en sträng till en lista genom funktioner `split()`. Se t.ex.
```python
# Gör om en sträng till en lista genom att splitta strängen genom " " (ett mellanslag)
my_string = "Jag heter Anton"
my_list = my_string.split(" ")

print(my_list) # Skriver ut ["Jag", "heter", "Anton"]
```

Det kan även vara bra att veta hur man göra om en lista med strängar till en lista med nummer. Det kan man göra genom följande kod:
```python
numbers_as_string = ["1", "2", "3"]
numbers_as_int = [int(i) for i in numbers_as_string]
# numbers_as_int är: [1, 2, 3]
```

### Bedömning

Uppgiften kan ge betyget godkänt.

#### För G

För att nå betyget godkänt behöver programmet uppfylla uppgiftsbeskrivningen, vara välstrukturerat och väldokumenterat. Extra viktiga punkter är:

- Koden ska vara strukturerad med ett antal funktioner, där varje funktion har begränsat syfte och omfattning
- Koden ska vara tydlig och lättläst med avseende på namngivning, strukturering och kommentarer.
- Alla funktion som inte är självförklarande ska ha en beskrivning i form av _docstrings_ (`''' Kommentar för funktionen '''`-kommentarer) där funktionens syfte, ev. parametrar & ev. returvärden finns beskrivet. Se t.ex. exemplet [Sten, sax, påse](http://localhost:4000/resurser/da354a/3-iteration-och-selektion/lecture-2/#sten-sax-p%C3%A5se-eller-gr%C3%A4vskopa) för att se **hur** man skriver denna typ av dokumentation.

#### Specifika krav för uppgiften

- Ni ska spara användarens val av siffror i en lista (tips, använd funktionen `split()` för att skapa en lista av användarens val)
- Er spelplan (som används vid presentation av dragningen) ska representeras av en nästlad lista (storlek: 5 * 5).
- De nummer som dras i varje dragning ska sparas i en lista
- Statistiken (antal poäng) för tidigare spel ska sparas i en lista
- Även kvalitén på er kod kommer att bedömas.

#### Detta testas vid rättning

Det här är en kort lista över delar som kommer att testas under rättningen. Får ni rätt på det här *brukar* uppgiften kunna godkännas utan kompletteringar.

1. Körning av programmet
2. Inmatning av tal som är större än 25 och mindre än 1
3. Inmatning av annat än heltal
4. Inmatning av både färre och fler siffror än fem
5. Inmatning av två eller fler lika nummer
6. Flera körningar för att testa slumpmässigheten
7. Alla val i menyn
8. Ej giltiga menyval

### Redovisning

Redovisa genom att ladda upp programmets källkod på Canvas.

Inlämningsuppgifter rättas varje vecka, med söndag som rullande deadline. Deadline för uppgiften är _söndag , 2020-12-13_.