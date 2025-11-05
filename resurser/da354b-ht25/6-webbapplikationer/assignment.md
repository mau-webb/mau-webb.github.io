---
id: da354b-ht25
title: "Modul 6 - Webbapplikationer"
---

# Modul 6 - Webbapplikationer

## Inlämningsuppgift

### Introduktion

Denna uppgift går ut på att skapa en enkel webbapplikation, i form av en wiki. Just wiki passar bra, eftersom även en enkel sådan fångar in många viktiga koncept genom att skapa, spara och redigera innehåll.

Denna uppgift ska redovisas genom källkod (lösningen) till uppgiften, **samt en videoinspelning där ni går igenom och förklarar er kod**. Har ni inte gjort videoinspelningar tidigare rekommenderar jag att ni använder Zoom, där ni delar er skärm, och spelar in mötet. Ni har alla som studenter en Zoom-licens för detta. Har ni frågor kring detta så hojta till på en laboration så visar vi hur man gör detta.

Inlämningsuppgiften är individuell. Det betyder att studenten enskilt ska utforma och skriva sin inlämning samt kunna redogöra för alla delar av den. Det är så klart inte förbjudet att diskutera uppgiften. Men viktigt är alltså att det man lämnar in representerar ens egna arbete.
{: .warn}

Det är förbjudet att använda hjälpmedel för att skapa/generera kod och/eller lösningar (eller delar av lösning) för uppgiften genom verktyg som t.ex. *ChatGPT*, *Github Copilot*, eller liknande/motsvarande verktyg, på exeminerande uppgifter (som denna) i denna kurs. Skulle detta ske betraktas det som *misstanke om fusk*, vilket kommer leda till en anmälan till disciplinnämnden och ev. avstängning från studier.
{: .warn}

### Din wiki

I den minimala wikin kan man skapa, ändra och läsa artiklar. Detta är också problemet som du ska lösa.

#### Innehåll

Wikins innehåll är enkelt: artiklar som har en titel och brödtext. Kärnproblemet som måste lösas är hur artiklarna ska sparas.

Att använda en enkel databas hade passat bra - men det lämnar vi till databaskursen (eller, det är tillåtet om du absolut vill). Använd istället enkla textfiler - då kan artikelns titel vara filnamnet, och brödtexten blir filens innehåll. Innehållet kan till och med vara HTML, som ett enkelt sätt att möjliggöra rikare innehåll.

Förslagsvis skapar du en undermapp som endast innehåller artikelfiler.

Ett annat sätt att spara artiklarna skulle kunna vara genom `JSON`, det är upp till er hur ni vill lösa lagringen av information.
{: .info}

#### Gränssnitt och funktionalitet

Det första gränssnittet till en webbapplikation är vilka adresser (URI:er) som används för att komma åt innehållet. Den HTML/CSS som utgör innehållet definierar sedan det grafiska gränssnittet.

Dessa URI:er är en rekommenderad grund för wikin:

* `/` (startsidan): Listar alla artiklar som finns i wikin, som klickbara länkar. Plus annan passande startsideinformation (ditt namn?).
* `/wiki/<sidans namn>/`: Varje individuell artikel - titel och brödtext presenteras. Exakt adress beror på artikelns titel, precis som på Wikipedia (t. ex. `en.wikipedia.org/wiki/Sweden`).
* `/new/`: Visar ett formulär som låter användaren mata in titel och brödtext för en ny artikel.
* `/edit/<sidans namn>/`: Visar ett formulär som låter användaren uppdatera en befintlig artikel.
* `/update/`: Hit skickas formuläret, och här sker uppdateringen/skapandet av artiklar. Formulärdata ska skickas hit med HTTP-metoden POST.

Notera att om du valt `JSON` som sätt att lagra dina artiklar så bör du ha två resurser / vägar in till applikationen, t.ex. `/update/` (uppdaterar en artikel) och `/save/` (sparar en artikel). Använder ni `JSON` så kan det också vara lämpligt att använda ett **id** för att identifiera era artiklar.
{: .info}

Du kan absolut lägga till fler URI:er än så. Du bör använda _templates_ för att dela upp logik och presentation.

#### Exempelvideo

Exempelvideo och förtydligande av funktionalitet för betyget **G**:

<div class="video-frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.25%;"><iframe src="https://www.youtube.com/embed/cPR-wAgrXbk?rel=0" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture;"></iframe></div>
</div>

#### Webbramverk - Bottle

[Bottle](http://bottlepy.org/) är det rekommenderade ramverket på grund av enkelheten i att installera och komma igång. Enklast: ladda hem [`bottle.py`](http://bottlepy.org/bottle.py) till din projektmapp.

#### Dokumentation

Koden ska vara tydlig och lättläst med avseende på namngivning, strukturering och kommentarer. Funktioner ska ha en beskrivning i form av _docstrings_ (`"""Kommentar för funktionen"""`-kommentarer). För att få lite svar på vanliga frågor om docstrings, se [PEP 257](../../pep257).

### Bedömning

Följande krävs för godkänt på uppgiften:

- Den grundläggande kravspecifikationen finns ovan (text + video) ska implementeras.
- **En tydlig och välgrundad genomgång av er kod, genom en videoinspelning**.

#### VG

Uppgiften kan ge VG - men det finns många olika förbättringar som alla kan göra wikin bättre. För VG implementera följande:

* Lägg till möjligheten att ta bort artiklar.
* God felhantering: se till att både titel och brödtext krävs för att ändra/skapa en artikel (validering ska minimum ske på serversidan, d.v.s. i python). Se till att en beskrivande felsida (fel 404) visas om man försöker surfa in på en artikel som inte existerar.
* Använd dina kunskaper i HTML/CSS för att göra ett tilltalande gränssnitt. (Exempelvideon har ingen CSS alls.)

Exempelvideo och förtydligande av funktionalitet för betyget **VG**:

<div class="video-frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.25%;"><iframe src="https://www.youtube.com/embed/ywaO7I6mz3s?rel=0" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture;"></iframe></div>
</div>

### Tips

- I ett template skriver man normalt ut en variabel såhär: <code>&#123;&#123; name &#125;&#125;</code>. För att skriva ut en variabel som innehåller HTML-kod, gör istället: <code>&#123;&#123;!name&#125;&#125;</code>.
- Det är enkelt att utgå ifrån en mapp och få en lista med alla filnamn däri:

```python
from os import listdir

files = listdir("wiki")
print files # a list of all filenames in directory wiki
```

### Redovisning

Redovisa genom att på Cavnas laddar upp programmets källkod, **samt** en videoinspelning där ni går igenom och förklarar er kod. Deadline för modul 6 är söndag **2024-01-19**.