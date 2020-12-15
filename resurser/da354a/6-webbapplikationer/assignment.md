---
id: da354a
title: "Modul 6 - Webbapplikationer"
---

# Modul 6 - Webbapplikationer

## Inlämningsuppgift

### Introduktion

Denna uppgift går ut på att skapa en enkel webbapplikation, i form av en wiki. Just wiki passar bra, eftersom även en enkel sådan fångar in många viktiga koncept genom att skapa, spara och redigera innehåll.

Inlämningsuppgiften är individuell. Det betyder att studenten enskilt ska utforma och skriva sin inlämning samt kunna redogöra för alla delar av den. Det är så klart inte förbjudet att diskutera uppgiften. Men viktigt är alltså att det man lämnar in representerar ens egna arbete.
{: .warn}

### Din wiki

I den minimala wikin kan man skapa, ändra och läsa artiklar. Detta är också problemet som du ska lösa.

#### Innehåll

Wikins innehåll är enkelt: artiklar som har en titel och brödtext. Kärnproblemet som måste lösas är hur artiklarna ska sparas.

Att använda en enkel databas hade passat bra - men det lämnar vi till databaskursen (eller, det är tillåtet om du absolut vill). Använd istället enkla textfiler - då kan artikelns titel vara filnamnet, och brödtexten blir filens innehåll. Innehållet kan till och med vara HTML, som ett enkelt sätt att möjliggöra rikare innehåll.

Förslagsvis skapar du en undermapp som endast innehåller artikelfiler.

Ett annat sätt att spara artiklarna skulle kunna vara genom `JSON`, om ni är mer bekväma med detta.
{: .info}

#### Gränssnitt och funktionalitet

Det första gränssnittet till en webbapplikation är vilka adresser (URI:er) som används för att komma åt innehållet. Den HTML/CSS som utgör innehållet definierar sedan det grafiska gränssnittet.

Dessa URI:er är en rekommenderad grund för wikin:

* `/` (startsidan): Listar alla artiklar som finns i wikin, som klickbara länkar. Plus annan passande startsideinformation (ditt namn?).
* `/wiki/<sidans namn>/`: Varje individuell artikel - titel och brödtext presenteras. Exakt adress beror på artikelns titel, precis som på Wikipedia (t. ex. `en.wikipedia.org/wiki/Sweden`).
* `/edit/`: Visar ett formulär som låter användaren mata in titel och brödtext för en ny eller befintlig artikel.
* `/update/`: Hit skickas formuläret, och här sker uppdateringen/skapandet av artiklar. Formulärdata ska skickas hit med HTTP-metoden POST.

Du kan absolut lägga till fler URI:er än så. Du bör använda _templates_ för att dela upp logik och presentation.

#### Exempelvideo

Till denna instruktion finns [en kort video](https://www.youtube.com/watch?v=PfvNfbC3qKk). Den visar hur wikin kan se ut "in action" och är ett bra komplement till beskrivningen ovan. (Notera att du gärna får göra din wiki mer tilltalande att använda!)

<div class="video-frame">
    <iframe width="640" height="480" src="//www.youtube-nocookie.com/embed/PfvNfbC3qKk?rel=0" frameborder="0" allowfullscreen></iframe>
</div>


#### Webbramverk - Bottle

[Bottle](http://bottlepy.org/) är det rekommenderade ramverket på grund av enkelheten i att installera och komma igång. Enklast: ladda hem [`bottle.py`](http://bottlepy.org/bottle.py) till din projektmapp.

#### Startkod (valfritt)

För att komma igång kan du använda nedanståden [startkod](https://gist.github.com/fohlin/12085142c756e611c57c). Den utgår ifrån att Bottle används, och baserar sig på rekommenderade adresserna ovan. För att använda koden är det viktigt att gå igenom den och sätta sig in hur den är uppbyggd.

<script src="https://gist.github.com/fohlin/12085142c756e611c57c.js"></script>


### Bedömning

Den grundläggande kravspecifikationen finns ovan (text+video) och uppfylls den nås också betyget G.

#### VG

Uppgiften kan ge VG - men det finns många olika förbättringar som alla kan göra wikin bättre. Implementera minst _tre_ av följande förslag:

* Lägg till möjligheten att ta bort artiklar.
* Modifiera hanteringen av artikeltext, så att användaren inte behöver ange `<p>` eller `<br>` för att radbrytningar ska visas på webbsidan.
* Se till att man automatisk skickas till rätt artikel efter redigering/skapande. (Istället för att behöver klicka sig vidare, som i filmen.)
* God felhantering: se till att både titel och brödtext krävs för att ändra/skapa en artikel (validering ska minimum ske på serversidan, d.v.s. i python). Se till att en beskrivande felsida (fel 404) visas om man försöker surfa in på en artikel som inte existerar.
* Använd dina kunskaper i HTML/CSS för att göra ett tilltalande gränssnitt. (Exempelvideon har ingen CSS alls.)



### Tips

- I ett template skriver man normalt ut en variabel såhär: <code>&#123;&#123; name &#125;&#125;</code>. För att skriva ut en variabel som innehåller HTML-kod, gör istället: <code>&#123;&#123;!name&#125;&#125;</code>.
- Det är enkelt att utgå ifrån en mapp och få en lista med alla filnamn däri:
    ```python
    from os import listdir

    files = listdir("wiki")
    print files # a list of all filenames in directory wiki
    ```

### Redovisning

Redovisa genom att ladda upp programmets källkod på Canvas. Deadline för modul 6 är söndag **2021-01-17**.