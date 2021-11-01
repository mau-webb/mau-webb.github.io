---
id: da354a
title: "Modul 2 - Funktioner"
---

# Modul 2 - Funktioner

## Inlämningsuppgift

### 1. Introduktion

Denna inlämningsuppgift har som syfte att examinera modul 2 som har fokus på funktioner och moduler. Läs igenom hela uppgiften noga innan då påbörjar din lösning.

Inlämningsuppgiften är individuell. Det betyder att studenten enskilt ska utforma och skriva sin inlämning samt kunna redogöra för alla delar av den. Det är så klart inte förbjudet att diskutera uppgiften. Men viktigt är alltså att det man lämnar in representerar ens egna arbete.
{: .warn}

### 2. Uppgiftsbeskrivning

Uppgiften går ut på att bygga ett enkelt tärningsspel där:

1. Användaren får ange sitt namn och blir välkomnad
2. Användaren får gissa vilken summa tre tärningar får ihop
3. Programmet slår tre tärningar och visar varje tärnings resultat
4. Programmet visar användarens gissning, summan av tärningsslagen och presenterar hur nära gissningen var
5. Programmet tackar användaren för visat intresse

Här finns en bild som tydliggör stegen ovan som ska utföras:

![Idle](../images/assignment.png)

#### Tips

- Tips är att använda funtionen [abs()](https://docs.python.org/3/library/functions.html#abs) för att beräkna hur nära användarens gissning var.

### 3. Bedömning

Uppgiften kan ge betyget godkänt. För att nå detta betyg behöver programmet uppfylla uppgiftsbeskrivningen, vara välstrukturerat och väldokumenterat. Extra viktiga punkter är:

- Koden ska vara strukturerad med ett antal funktioner, där varje funktion har begränsat syfte och omfattning
- Koden ska vara tydlig och lättläst med avseende på namngivning, strukturering och kommentarer. Funktioner som inte är självförklarande ska ha en beskrivning i form av _docstrings_ (`''' Kommentar för funktionen '''`-kommentarer).

#### Specifika krav för uppgiften

- Ni ska använda funktionen [`randint`](https://docs.python.org/2/library/random.html#random.randint) från standardmodulen [`random`](https://docs.python.org/2/library/random.html) för att "slå era tärningar" (generera ett tal mellan 1 och 6).
- Ni ska ha en funktion vars enda uppgift är att _slå_ en tärning (genererar ett nummer mellan 1 och 6) och sedan returnerar tärningens värde.
- Era funktioner ska använda sig utav parametrar där detta är lämpligt, och returnera värden där detta är lämpligt.
- Även kvalitén på er kod kommer att bedömas.

### 4. Detta testas vid rättning

Det här är en kort lista över delar som kommer att testas under rättningen. Får ni rätt på det här brukar uppgiften kunna godkännas utan kompletteringar.

1. Körning av programmet
2. Gissning med negativa tal

### 5. Redovisning

Redovisa genom att ladda upp programmets källkod på Canvas i en Zip-fil.

Inlämningsuppgifter rättas varje vecka, med söndag som rullande deadline. Försök att hålla kursens tempo på en modul per vecka. Deadline för modul 2: senast _söndag 2020-11-29_.