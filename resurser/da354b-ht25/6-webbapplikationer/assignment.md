---
id: da354b-ht25
title: "Modul 6 - Webbapplikationer"
---

# Modul 6 - Webbapplikationer

## Inlämningsuppgift

### Introduktion

Publiceras i samband med workshopen den 16/12.

<!--

Denna uppgift går ut på att skapa en enkel webbapplikation, i form av en wiki **med hjälp av generativ AI - exempelvis ChatGPT**. Att bygga just en wiki passar bra, eftersom även en enkel sådan fångar in många viktiga koncept genom att skapa, spara och redigera innehåll på en webbsida.

Denna inlämningsuppgift **ska lösas** genom generativ AI. Detta innebär att uppgiften redovisas genom följande: **Källkod till din lösning**, **loggbok över dina prompts** och **reflektionsrapport över ditt arbete**.
{: .info}

Det är väldigt viktigt att ni deltar i workshopen om **Mjukvarutveckling med AI** tisdagen den 16:e december - där vi kommer att gå igenom förväntningar, instruktioner, samt påbörjar arbetet med inlämningsuppgiften.
{: .info}

Inlämningsuppgiften är individuell. Det betyder för denna uppgift att studenten enskilt ska utforma och skriva sin **loggbok över prompts** och **reflektionsrapport över sitt arbete**. Källkoden ska dock vara genererad av generativ AI.
{: .warn}

### Din wiki - Vad du ska bygga

I denna wiki kan man skapa, ändra, läsa och radera artiklar. Utgå från videon nedan för att se hur detta kan fungera - det är upp till dig, med hjälp av ChatGPT hur ni ska lösa denna uppgift.

#### Innehåll

Wikins innehåll är enkelt: artiklar som har en titel och brödtext. Kärnproblemet som måste lösas är hur artiklarna ska sparas.

Att använda en enkel databas hade passat bra - men det lämnar vi till databaskursen (eller, det är tillåtet om du absolut vill). Använd istället formatet *JSON* eller enkla textfiler - då kan artikelns titel vara filnamnet, och brödtexten blir filens innehåll. Innehållet kan till och med vara HTML, som ett enkelt sätt att möjliggöra rikare innehåll.

#### Gränssnitt och funktionalitet

Följande vyer (som minimun) ska finnas på er webbplats:

- Startida: Lista upp alla artiklar i wikin
- Artikelsida: Visar upp en specifik artikel för besökaren
- Skapa artikel-sida: Här ska man kunna skapa en artikel med text och innehåll
- Uppdatera artikel-sida: Här ska man kunna redigera en specifik artikel (rubrik och brödtext)

Övriga krav som ska implementeras är:
- Kunna radera en artikel
- Felhantering: Man ska inte kunna surfa till en artikel som inte finns
- Felhantering: Man ska inte kunna skapa/uppdatera en artiekl utan att ange titel eller brödtext
- Snygga till er Wiki med CSS

#### Exempelvideo

Exempelvideo - Funktionalitet

<div class="video-frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.25%;"><iframe src="https://www.youtube.com/embed/AlSIGOtIwvk?rel=0" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="accelerometer *; clipboard-write *; encrypted-media *; gyroscope *; picture-in-picture *; web-share *;" referrerpolicy="strict-origin"></iframe></div>
</div>


#### Webbramverk - Bottle / Flask / FastAPI

[Bottle](http://bottlepy.org/) är det rekommenderade ramverket på grund av enkelheten i att installera och komma igång. Enklast: ladda hem [`bottle.py`](http://bottlepy.org/bottle.py) till din projektmapp. Ni är dock välkomna att välja vilket webbramverk som ni använda.

#### Dokumentation

Koden ska vara tydlig och lättläst med avseende på namngivning, strukturering och kommentarer. Funktioner ska ha en beskrivning i form av _docstrings_ (`"""Kommentar för funktionen"""`-kommentarer). För att få lite svar på vanliga frågor om docstrings, se [PEP 257](../../pep257).

### Bedömning

Följande delar bedöms vid er inlämning:

1. Källkoden för er lösning
2. Prompt-loggbok
3. Reflektionsrapport

### Redovisning

Redovisa genom att på Canvas laddar upp programmets källkod, ert prompt-dagbok, samt er reflektionsrapport. Deadline för modul 6 är söndag **2025-01-18**.

-->