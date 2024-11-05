---
id: da354a-ht23
title: "Modul 3 - Iteration & Selektion"
---

# Modul 3 - Iteration & Selektion

## Inlämningsuppgift

### Inledning

Denna inlämningsuppgift har som syfte att examinera modul 3 som har fokus på iteration och selektion.

Inlämningsuppgiften är individuell. Det betyder att studenten enskilt ska utforma och skriva sin inlämning samt kunna redogöra för alla delar av den. Det är så klart inte förbjudet att diskutera uppgiften. Men viktigt är alltså att det man lämnar in representerar ens egna arbete.
{: .warn}

Det är förbjudet att använda hjälpmedel för att skapa/generera kod och/eller lösningar (eller delar av lösning) för uppgiften genom verktyg som t.ex. *ChatGPT*, *Github Copilot*, eller liknande/motsvarande verktyg, på exeminerande uppgifter (som denna) i denna kurs. Skulle detta ske betraktas det som *misstanke om fusk*, vilket kommer leda till en anmälan till disciplinnämnden och ev. avstängning från studier.
{: .warn}

### 2. Uppgiftsbeskrivning

Uppgiften går ut på att ni ska bygga ett frågespel, där användaren får svara på frågor som ni (som programmerare av programmet) har skapat. Det ska även finnas en liten statistikdel där man man se hur många frågor man svarat på och hur många gånger man svarat fel.

Programmet ska bestå utav följande komponenter

1. En meny där man:
	- Kan välja att spela vårt frågespel
	- Kan välja att se statistik om frågespelet
	- Kan avsluta programmet
2. Ett frågespel där användaren får en fråga och ska svara rätt på denna
3. En statistikdel där användaren kan se antal besvarade frågor och antal felsvar

#### Menyn

Menyn ska ha tre alternativ:

1. Frågespel
2. Statistik
3. Avsluta

Beroende på vilket val man väljer (1, 2 eller 3) ska korrekt funktion att köras. Skulle man skriva in något annat än 1, 2 eller 3 så ska programmet tala om att menyvalet var felaktigt och man får ett nytt försök att välja ett alternativ (programmet ska inte krascha). Programmet avslutas endast då användaren anger detta (alternativ 3) i menyn (och då **inte** genom funktionen *exit()*).

#### Frågespel

Frågespelet består lämpligen av (bland annat) två funktioner, t.ex. `question_game` och `question`.

1. `question_game` välkomnar användaren till spelet och ställer en fråga åt gången genom att anropa funktionen `question`.
2. Funktionen `question` ska ta två parametrar 1) Frågan som ska ställas, 2) Det korrekta svaret. Så ett exempelanrop på funktionen `question` **ska se ut såhär**:

```python
question("Vilken är Skånes största stad?", "Malmö")
```

Funktionen ska då:

1. Ställa frågan till användaren
2. Ta emot användarens svar
	- Om svaret är korrekt så gratuleras användaren (och ni noterar att en fråga är besvarad)
	- Om svaret är felaktigt så berättas detta för användaren, och användaren får en ny möjlighet att svara på frågan (tills frågan är korrekt besvarad). Här noterar ni också varje gång användaren svarar fel på en fråga.
3. När frågan är korrekt besvarad är funktionen `question` klar

#### Statistik

Statistikdelen ska berätta för användaren hur många frågor man besvarat och hur många gånger man svarat fel (totalt). Denna information ska ni ha samlat in i funktionen `question`. Ett sätt att hålla koll på statistiken är genom [globala variabler](http://stackoverflow.com/questions/423379/using-global-variables-in-a-function-other-than-the-one-that-created-them).

#### Exempelkörning

![Idle](../images/idle15.png)

### Bedömning

Uppgiften kan ge betyget godkänt. För att nå detta betyg behöver programmet uppfylla uppgiftsbeskrivningen, vara välstrukturerat och väldokumenterat. Extra viktiga punkter är:

1. Koden ska vara strukturerad med ett antal funktioner, där varje funktion har begränsat syfte och omfattning
2. Koden ska vara tydlig och lättläst med avseende på namngivning, strukturering och kommentarer.
3. Funktioner ska ha en beskrivning i form av _docstrings_ (`"""Kommentar för funktionen"""`-kommentarer).

#### Specifika krav för uppgiften

- All er kod (förutom globala variabler) ska finnas i funktioner.
- Ni ska ha en funktion `question` som har två parametrar (fråga, svar) som hanterar frågeställningen till användaren.
- Era funktioner ska använda sig utav parametrar där detta är lämpligt, och returnera värden där detta är lämpligt.
- Även kvalitén på er kod kommer att bedömas.

#### Detta testas vid rättning

Det här är en kort lista över delar som kommer att testas under rättningen. Får ni rätt på det här brukar uppgiften kunna godkännas utan kompletteringar.

1. Körning av programmet
2. Val av samtliga menyalterntiv, samt några icke-existerande, inkluderat både större och mindre nummer
3. Val av menyalternativen flera gånger
4. Frågorna besvaras med både korrekta och felaktiga svar. Vid felaktiga svar förväntas en ny chans att besvara frågan att ges.

**Viktigt**: Kontrollera att **alla** punkter under rubriken *Bedömning* är uppfyllda innan du skickar in
{: .info}

### Redovisning

Redovisa genom att ladda upp programmets källkod på Canvas.

Inlämningsuppgifter rättas varje vecka, med onsdag som rullande deadline. Kursens tempo på en modul per vecka. Deadline för modul 2: senast _onsdag: 2023-11-29_.