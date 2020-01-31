---
id: da280a
title: "HTML: Länkar"
---

# HTML: länkar

## Inledning

Vad vore webben utan länkar? Inte speciellt utforskande i alla fall, tänk om man hade behövt veta alla webbadresser man ville besöka helt utantill (eller nerskrivna någonstans)? En av grundidéerna med World Wide Web var att man enkelt skulle kunna dela information med varandra - mellan olika servrar - genom navigation med länkar. Så ni ska vi se hur man skapar länkar i HTML.

Vad vore webben utan länkar? Det hade med utan tvekan varit väldigt svårt att utforska de olika webbplatser som finns idag. Tänk bara om vi manuellt behövt fylla i varje webbadress för varje sida vi vill besöka. En av grundidéerna med *World Wide Web* var att vi enkelt ska kunna dela information mellan varandra men även länka samman material tillsammans - så vi kan navigera runt ett nätverk av information. Så nu ska vi ta en titt på hur vi skapar länkar i HTML!

## Länk-elementets uppbyggnad

Elementet för att skapa en länk på en webbsida är <a>. Men bara genom att skriva <a> kommer man inte så långt. Man behöver veta två saker till:

För att skapa en länk i HTML använder vi elementet `<a>`. Men bara genom att skriva `<a>` kommer vi inte så långt. Vi kan tänka oss att en länk har ett par beståndsdelar:

* Vart ska besökaren skickas när de klickar på länken? (dvs. sökvägen)
* Vilken text/bild ska synas för att besökaren ska kunna klicka på länken? (dvs. innehållet)

En komplett länk med både innehåll och sökväg kan se ut på följande vis (i exemplet gör vi en länk till Google):

``` html
<a href="http://google.se">Klicka här för att komma till Google</a>
```

Observera att attributet `href` används för **vart** besökaren ska skickas när den klickar på länken. Det som placeras mellan start- och sluttaggarna är **vad** besökaren kan klicka på för att skickas någonstans.

Exemplet på riktigt: [Klicka här för att komma till Google](https://google.com).

### Sökvägar

Precis som med bilder så anger vi sökvägar i länkar för att skicka en besökare till en ny plats/adress. Det är samma princip som gäller här, dvs. vi har relativa och absoluta sökvägar.

**Relativa sökvägar**

En reltiv sökväg innebär att man utgår från den plats som HTML-filen som bilden ska visas på finns. Detta innebär att man inte behöver oroa sig över vilken URL (webbadress) som bilden har - bara man vet var den ligger i förhållandet till HTML-filen där bilden ska visas. Relativa sökvägar används när bilden man vill visa ligger inom webbplatsen.

För att ta ett exempel kan vi utgå från följande filstruktur (dvs. en mapp med filer):

```
| Min Webbplats
| -- index.html
| -- about.html
```

I ovanstående exempel har vi mappen "Min Webbplats" och i denna har vi två stycken filer, `index.html` och `about.html`. Skulle vi nu vilja göra en länk från "index" till "about" hade vi skrivit på följande vis:

``` html
<a href="about.html">Länk till vår andra sida</a>
```

Anledningen till detta är att eftersom dessa filer (index.html och about.html) ligger i samma mapp behöver jag endast skriva "about.html". Skulle däremot strukturen på våra filer vara annorlunda, t.ex att vi väljer att placera alla sidor i mappen "sidor" istället:

```
| Min Webbplats
| -- index.html
| -- sidor
     | -- about.html
```

Alltså att HTML-sidan "about.html" nu ligger i mappen "Sidor" skulle jag behöva skriva följande HTML-kod för att länka korrekt:

Detta innebär att filen "about" inte befinner sig i samma mapp som "index.html" - därmed **måste** jag ändra min **relativa sökväg** för att det ska blir korrekt så att länken kan fungera. Följande ändring hade jag därmed behövt göra i "index.html":

``` html
<a href="sidor/about.html">Länk till vår andra sida</a>
```

Detta kan tolkas som att sökvägen "sidor/about.html" går "ner" i mappen "sidor" (dvs. `sidor/`) och länkar till sidan `about.html` så att vi kan navigera från en sida till en annan.

**Absoluta sökvägar**

Absoluta sökvägar innebär att vi anger en exakt plats till en sida vi vill att besökaren ska skickas till - dvs. vi utgår inte från vår egen filstruktur. Detta görs oftast när vi vill skicka besökaren till en annan webbplats som befinner sig någon annanstans - t.ex kanske användaren ska skickas till vår facebook profil? osv.

Låt säga att jag då vill skapa en länk till Malmö Högskolas webbplats, som har adressen "http://mah.se", då skriver jag:

Låt oss säga att vi vill skapa en länk till Malmö högskolas startsida, som har adressen `http://mah.se`, då hade vi skrivit följande:

``` html
<a href="http://mah.se">Malmö Högskolas startsida</a>
```

Med andra ord anger vi en exakt sökväg till en annan webbplats (eller en bild för den delen) - notera att oftast ser vi `http://` framför en adress.

## Hur ska länken öppnas?

Man kan genom attributet target ange hur man vill att länken ska öppnas när en besökare klickar på den. Det finns framförallt två värden här som är intressanta:

Vi kan genom HTML-attributet `target` ange hur vi vill att en länk ska fungera när en besökare klickar på den. Det finns huvudsaklige två värden som är av intresse:

* `target="_self"` - standardvärde om vi inte anger något
* `target="_blank"` - innebär att besökaren som klickar på din länk kommer få den nya sidan öppnad i en ny flik

Till exempel:

``` html
<!-- Öppnar länken i samma fönster/flik -->
<a href="http://mah.se" target="_self">Malmö Högskola</a>
<!-- Öppnar länken i nytt fönster/ny flik -->
<a href="http://mah.se" target="_blank">Malmö Högskola</a>
```

Pröva gärna ovanstående kod och experimentera - kan ni göra en länk som är klickbar?
