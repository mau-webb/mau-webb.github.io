---
id: da280a
title: "HTML: Bilder"
---

# HTML: bilder

## Inledning

Ett talesätt är att en bild säger mer än tusen ord - och visst vill vi ha möjlighet att inkludera bilder på våra webbplatser. Det kan inte bara bli mer informativt med bilder men ofta ger det även mer liv till en webbplats - bilder är bra helt enkelt!

## Bild-elementets uppbyggnad

### Sökvägar

Det element som används för att skapa en bild på en webbplats är `<img>`. Men bara genom att skriva detta element så kommer vi inte så långt. Vi anger visserligen att en bild ska visas - men inte vilken bild. Vi behöver alltså specificera vilken bild och var denna befinner sig - så den kan visas. Detta görs genom HTML-attributet "src" (eng. source) - här fyller vi i sökvägen till bilden (sökvägen är alltså en beskrivning av vart vår bild befinner sig på en dator, t.ex i en mapp). Detta kan göras på ett av två sätt:

* Relativt
* Absolut

**Relativa sökgvägar**

En relativ sökväg innebär att vi utgår från samma plats (mapp) som vår HTML-fil befinner sig (dvs. den fil där vi vill att en bild ska visas). Detta innebär att vi behöver inte oroa oss över vilken URL (webbadress) bilden har - så länge vi vet vart vår bild befinner sig i relation till vår HTML-fil. Relativa sökvägar används när bilden vi vill visa ligger inom webbplatsen (dvs. den kommer inte t.ex. från en utomstående webbplats).

För att ta ett exempel kan vi utgå från följande filstruktur (dvs. en mapp med filer):

```
| Min Webbplats
| -- index.html
| -- sommar.jpg
```

I ovanstående exempel har vi mappen "Min Webbplats" och i denna har vi två stycken filer, `index.html` (vår HTML-fil) och `sommar.jpg` (vår bild). Skulle jag nu vilja visa bilden `sommar.jpg` på webbplatsen `index.html` så hade jag skrivit följande:

``` html
<img src="sommar.jpg">
```

Anledningen till detta är att eftersom dessa filer (index.html och sommar.jpg) ligger i samma mapp behöver jag endast skriva "sommar.jpg". Skulle däremot strukturen på våra filer vara annorlunda, t.ex att vi väljer att placera alla bilder i mappen "bilder" istället:

```
| Min Webbplats
| -- index.html
| -- bilder
     | -- sommar.jpg
```

Detta innebär att bilden befinner sig inte i samma mapp som min HTML-fil - därmed **måste** jag ändra min **relativa sökväg** för att det ska blir korrekt så att bilden kan visas. Följande ändring hade jag därmed behövt göra i min HTML-fil:

``` html
<img src="bilder/sommar.jpg">
```

Detta kan tolkas som att sökvägen "bilder/sommar.jpg" går "ner" i mappen bilder (dvs. `bilder/`) och hämtar bilden `sommar.jpg` så denna sedan kan visas på vår webbplats.

**Absoluta sökvägar**

Absoluta sökvägar innebär att vi anger en exakt plats till vart den bild vi vill ska visas befinner sig - vi utgår inte från vart vår HTML-fil är för att komma åt vår bild. Detta görs oftast när vi vill inkludera bilder på vår webbplats som befinner sig någon annanstans - kanske refererar vi till ett fotografi som en annan fotograf tagit? Eller om vi t.ex. hittat en bild via Google eller dylikt.

Låt oss säga att jag vill visa en bild på Star Wars-logotypen och genom en sökmotor hittar en bild som ligger på adressen `https://c2.staticflickr.com/4/3801/13389420833_99e5b4bc70_b.jpg`. För att visa upp denna bild på en webbplats hade jag då behövt skriva:

``` html
<img src="https://c2.staticflickr.com/4/3801/13389420833_99e5b4bc70_b.jpg">
```

Med andra ord behöver jag skriva ut den exakta sökvägen direkt till bilder som befinner sig "utanför" vår webbplats.

### Om en bild inte kan visas?

Det hände ibland att bilder inte kan visas av olika anledningar. Det kan vara så att sökvägen till en bild helt enkelt är fel eller att en bild bytt plats (detta riskerar man framförallt när man länkar till bilder utanför sin webbplats, då man inte kan styra över om dessa t.ex. tas bort). Då skulle man ändå vilja berätta om att det var tänkt att visa en bild, och en text som beskriver vad bilden visar. Detta gör man genom attributet alt. Exempel på användning av alt-attributet:

Det händer ibland att bilder inte kan visas av olika anledningar, vi kanske stavar fel på vår sökväg, vi kanske råkade radera vår bild eller helt enkelt bara flyttat bilden från en mapp till en annan och glömt ändra sökvägen. Då finns det möjlighet för oss att ange att en alternativ text kan visas om bilden inte kan hittas för någon anledning. Till exempel:

``` html
<img src="star_wars.jpg" alt="Star Wars-logotyp">
```

Om ni testar ovanstående exempel, utan att ha en bild som heter `star_wars_.jpg` bör ni istället få fram texten "Star Wars-logotyp". Ytterligare en fördel med detta är att för personer som t.ex. är blinda - dvs. som får webbplatsens innehåll uppläst - så kommer dessa personer förstå att i denna delen av texten skulle en logotyp av Star Wars finnas - användbart!
