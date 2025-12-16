---
id: da354b-ht25
title: "Modul 5 - Fil- och felhantering i Python"
---

# Modul 5 - Fil- och felhantering i Python

## Inlämningsuppgift

### 1. Introduktion

Denna inlämningsuppgift är **frivillig** och har som syfte att examinera modul 5 som har fokus på fil- och felhantering. 

**Läs uppgiften noga innan du börjar med den.**

Denna inlämningsuppgift är **frivillig**. Om man gör uppgiften (lämnar in den på Canvas), samt genomför godkänd muntlig redovisning av uppgiften för en lärarassistent fredagen den 19:e december kl. 13 - 16 (bokning av redovisning kommer inom kort) - så får man tillgodoräkna sig **2 poäng** till den ordinarie tentamen.
{: .info}

Inlämningsuppgiften är individuell. Det betyder att studenten enskilt ska utforma och skriva sin inlämning samt kunna redogöra för alla delar av den. Det är så klart inte förbjudet att diskutera uppgiften. Men viktigt är alltså att det man lämnar in representerar ens egna arbete.
{: .warn}

Det är förbjudet att använda hjälpmedel för att skapa/generera kod och/eller lösningar (eller delar av lösning) för uppgiften genom verktyg som t.ex. *ChatGPT*, *Github Copilot*, eller liknande/motsvarande verktyg, på exeminerande uppgifter (som denna) i denna kurs. Skulle detta ske betraktas det som *misstanke om fusk*, vilket kommer leda till en anmälan till disciplinnämnden och ev. avstängning från studier.
{: .warn}

### 2. Uppgiftsbeskrivning

Vi ska i denna uppgift bygga en resultathanterare för en minigolftävling. Minigolftävlingen går ut på att varje person spelar tre varv (rundor) och det totala antalet slag avgör vem som vinner. Programmet ska kunna spara registrerade resultat till en textfil, och läsa in tidigare resultat från filer som följer samma format.

För att spara resultaten ska ni följa denna struktur:

```python
namn;varv1;varv2;varv3
namn;varv1;varv2;varv3
namn;varv1;varv2;varv3
```

För alternativ ett finns en exempelfil att utgå från (med några förinlagda resultat) [här](../files/result.txt).

Programmet i sig ska ha tre funktioner:

1. Visa resultat för spelarna
	- Här ska spelarens namn, resultat för varje varv (total 3st resultat), totalt antal slag, och genomsnittsslag per varv presenteras
2. Registrera resultat för en ny spelare
	- Här ska man ange namn och resultat för varv 1,2,3
3. Radera en spelare (och dennes resultat)
	- Här anger man namnet på den spelare som man vill ta bort från resultatlistan

Ni får själva avgöra om ni vill läsa/skriva till filen varje gång ni kör någon av funktionerna ovan, eller om ni vill göra en "spara" och en "hämta" funktion som läser/skriver till filen.

#### Exempelkörning

![Idle](../images/assignment-4.png)

### Bedömning

Uppgiften kan ge betyget godkänt.

#### Krav för G

För att uppnå godkänt behöver programmet uppfylla uppgiftsbeskrivningen, vara välstrukturerat och väldokumenterat. **Extra viktiga** punkter är:

- Koden ska vara strukturerad med ett antal funktioner, där varje funktion har begränsat syfte och omfattning.
- Koden ska vara tydlig och lättläst med avseende på namngivning, strukturering och kommentarer. Funktioner ska ha en beskrivning i form av _docstrings_ (`"""Kommentar för funktionen"""`-kommentarer). För att få lite svar på vanliga frågor om docstrings, se [PEP 257](../../pep257).
- Ni ska använda er av `try` och `except` för filhantering, t.ex. om filen inte skulle finnas, eller innehåller fel struktur ska lämpligt felmeddelande visas (och programmet ska inte krascha). Ni får gärna använda felhantering vid andra ställen som ni anser lämpliga.
- Filens innehåll ska:
  - följa angiven struktur (som beskrivs i uppgiftsbeskrivningen)
  - sparas i formatet `CSV` (alternativt vara kompatibel med `pickle` eller `json`)
 - Även kvalitén på er kod kommer att bedömas.
 - **Godkänd muntlig presentation och diskussion av uppgiften**

<!--

#### Krav för VG

Utöver att uppfylla kraven för godkänt kan man även implementera så att när man visar resultat ska man kunna sortera resultaten efter kolumnerna (stigande, d.v.s. lägsta värdet först):

- Namn
- Runda 1
- Runda 2
- Runda 3
- Totalt
- Samt orginalordningen

[Exempellösning på VG-utskrift](../files/ex_vg.txt)

-->

#### Detta testas vid rättning

Det här är en kort lista över delar som ska att testas under er demo för den muntliga presentationen. 

1. Körning av programmet (alla funktioner)
2. Körning utan existerande fil
3. Borttagning av existerande fil
4. Inmatning med ogiltig indata
5. Granskning av statistiken
6. Radering av icke-existerande poster

<!--
För VG:

7. Olika sorteringar av statstiken

-->

### Redovisning

Redovisas genom att ladda upp programmets källkod på Canvas, samt muntlig redovisning den *2025-12-19* (bokning sker via Canvas).

Inlämningsuppgifter rättas varje vecka, med onsdag som rullande deadline. Kursens tempo på en modul per vecka. Deadline för modul 5: senast onsdag: *2025-12-17*.