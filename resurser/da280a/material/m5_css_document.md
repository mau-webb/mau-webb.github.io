---
id: da280a
title: "CSS i externt dokument"
---

# CSS i externt dokument

## Syfte

CSS (Cascading Style Sheets) utgör grunden för i princip alla de visuella aspekterna av en modern webbplats. CSS är dock inte ett språk begränsat till just HTML utan har fler användningsområden, dock är webben dess största användningsområde - och det är detta som vi ska utforska i denna laboration.

## Lärandemål

Efter genomförd laboration ska du:

* veta hur CSS skrivs
* veta hur CSS appliceras på ett HTML-dokument
* kunna känna till och ändra på grundläggande CSS-egenskaper, t.ex. färger och storlekar

## Uppgift

I denna laboration ska du utgå från ett färdigt HTML-dokument för att sedan gradvis bygga på med mer och mer CSS. På vägen kommer du att stöta på många av de grundläggande koncept inom CSS som krävs för att utforma en visuellt förbättrad webbplats.

Börja med att [ladda ner detta HTML-dokument](../assets/da280a_ex_css_webpage.html) (högerklicka och välj "Spara som" eller motsvarande). Ta sedan en titt på hur dokumentet är uppbyggt - strukturen på HTML-dokumentet och dess element är väldigt viktigt att känna till för att sedan kunna applicera CSS (utseende).

När du öppnar HTML-dokumentet i en webbläsare så kommer du finna att det inte är så visuellt tilltalande (eftersom ingen CSS ännu är applicerad). Detta kan vi ändra - genom att skriva en stilmall med CSS! Genom en CSS-fil (stilmall) kan vi ändra på det utseende som webbläsaren anger som standardvärde och överskrida med vad vi själv finner passar. Vart börjar vi då med att skriva vår CSS? Det finns ett par alternativ, just nu börjar vi med att lägga till elementet `<style>` i sidhuvudet (`<head>`) på följande vis:

``` html
<style type="text/css">
    /* Mellan start- och sluttaggarna kommer vår CSS */
</style>
```

### Grundstil

När du lagt till elementet `<style>` är det dags för att skriva lite CSS! Om du inte gjort det så bör du först läsa de kapitel som hänvisas till från kurslitteraturen som bla. behandlar "[CSS-regler](http://reference.sitepoint.com/css/rulesets)" och "[deklarationsblock](http://reference.sitepoint.com/css/declarationblocks)". Det kan även vara bra att undersöka hur [CSS-kommentarer](http://www.sitepoint.com/web-foundations/css-comments/) fungerar - eftersom en välkommenterad kod alltid är lättare att förstå.

Fortsätt nu med att skriva en CSS-regel som anger bakgrundsfärg (`background-color`) och förgrundsfärg (dvs. textfärg, `color`) för `<body>` (för att enkelt hitta passande färger kan du använda dig av [Adobe onlinetjänst för färgscheman](https://color.adobe.com/explore/newest/?time=all)).

Övergå därefter till att ändra på textens storlek samt typsnitt (fortfarande för elementet `<body>`, eftersom allt innehåll ligger i detta element kommer det därmed påverkas av dessa CSS-regler). Detta gör du med egenskaperna `font-size` samt `font-family`.

**Att tänka på**

* Alla typsnitt finns inte installerade på alla datorer. [Denna tabell](http://media.24ways.org/2007/17/fontmatrix.html) kan vara en enklare indikation till hur vanligt ett typsnitt är.
* Ange gärna mer än ett typsnitt. Genom att ge en lista av flera typsnitt så kan vi styra andra- och tredjeval, osv. Det vill säga om ett typsnitt inte finns tillgängligt används ett annat osv. Till exempel kan vi skriva `font-family: Helvetica, Arial, sans-serif;`
* Ange alltid en typsnittsfamilj som det sista alternativet. Dvs. ett typsnitt med eller utan seriffer (fötter), t.ex. `sans-serif` eller `serif`
* I modernare webbläsare går det även att inkludera egna eller andras typsnitt tack vare egenskapen "[@font-face](http://reference.sitepoint.com/css/at-fontface)" i CSS, en tjänst som underlättare detta är [Google Web Fonts](https://www.google.com/fonts/)

### Extern stilmall

Fram till hit har du skrivit din CSS i en inbäddad mall (`<style>`). Det är nästan alltid bättre att försöka separera sin CSS och HTML, dvs. att placera din stilmall i en egen fil (t.ex `stilmall.css`). På detta vis kan du även använda samma stilmall till flera HTML-dokument samtidigt.

Kopera all din CSS-kod till en ny tom textfil. Spara denna fil i samma mapp som ditt HTML-dokument med filändelsen `.css`. När du kontrollerat att du sparat filen kan du ta bort `<style>` elementet från ditt HTML-dokument och sedan välja att din externa CSS-fil ska gälla istället. Detta görs genom elementet `<link>` på följande vis (denna placeras i `<head>`):

``` html
<link href="minmall.css" type="text/css" rel="stylesheet">
```

Om vi använder dokumenttypen HTML5 (`<!doctype HTML>`) kan vi istället skriva:

``` html
<link href="minmall.css" rel="stylesheet">
```

Observera att du behöver byta ut `minmall.css` till den fil som du själv sparade. Om allt gått bra så bör ditt dokument se ut som innan, men nu har du all din CSS i en egen fil.

### Avvikande stilar och länkar

När vi arbetar med CSS så är det en bra strategi att skriva så generella regler som möjligt. Det sparar arbete och gör koden mer kompakt, genom att minska upprepning. Men ofta vill vi ha några avvikande egenskaper; allt bör ju inte se likadant ut. Skriv en regel som byter typsnittför alla rubrikerna `<h1>` till `<h6>`. Du kan även ändra färg eller andra egenskaper som du tycker passar.

Något som av användbarhetsmässiga skäl ofta har en distinkt stil är länkar. Dessa är också speciella i den bemärkelsen att de har en viss interaktivitet; de ser oftast annorlunda ut när de är besökta eller när muspekaren befinner sig ovan för dem. För att definiera stilar för dessa olika tillstånd används pseudoklasser. I detta skede behöver du inte fördjupa dig i vad begreppet innbär. Studera följande exempel:


``` css
a {
    /* Här definieras grundstilen för alla länkar */
}

a:visited {
    /* Gäller bara besökta länkar */
}

a:hover, a:focus {
    /* Gäller bara när muspekaren är över (hover), eller när
       länken är markerad med hjälp av tangenbordet (focus) */
}
```

Använd denna mall för att bestämma hur dina länkar ska se ut. Se till att skillnaden mellan de tre tillstånden är tillräckligt stor så att användaren märker det.

### Identiteter

Studera sedan följande tre CSS-regler. Läs igenom dom, jämför med strukturen på HTML-dokumentet och försök tänka dig vad resultatet kan bli. Klistra sedan in dessa regler i din stilmall och se vad som händer.

``` css
table {
    background-color: #ffff99;
    border: 1px solid #cccccc;
    width: 300px;
}

thead {
    background-color: #ffff33;
}

td, th {
    padding: 5px;
}
```

Som du bör ha noterat förändrar dessa stilregler utseendet för båda tabellerna i dokumentet. Behåll dessa stilregler men komplettera med en ny som endast påverkar den andra tabellen på ett valfritt vis.

För att åstadkomma detta behöver du kunna identifiera den andra tabellen och sedan påverka den i din CSS. Detta görs naturlogt nog med HTML-attributet `id`. Den andra tabellen har redan en identitet definierad `id="personal"`. Du kan således använda dig av denna (s.k. "selektor") genom att skriva `#personal` i din stilmall. T.ex `#personal { ... }`. Skapa denna regel och ändra utseendet.

### Klasser

En identitet är unik och kan endast förekomma en gång i samma HTML-dokument. Du kan ha flera olika `id` men med olika namn. För att påverka flera olika eller samma element samtidigt används istället "klasser". Det fungerar på samma vis som identiteter men med vissa skillnader, i HTML används attributet `class=""` och i CSS används en punkt istället för en hashtag, dvs. `id="personal"` hade skrivits som `class="personal` och `.personal { ... }`.

Skapa en CSS-regel som påverkar klassen "viktig" och ge den ett utmärkande utseende. De två översta listpunkterna har denna klass och får således detta utseende.

## Validering och feedback

När du är klar kan ditt dokument se ut som bilden nedan. Exakta färga, typsnitt, osv. är valfritt - men du får gärna arbeta med att göra dokumentet mer visuellt tilltalande!

![Exempel av CSS lösning](../assets/da280a_ex_css_bild1.png)
