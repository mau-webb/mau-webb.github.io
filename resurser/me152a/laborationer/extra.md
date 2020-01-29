---
id: me152a
title: "Extra"
---

# Extra: SVG och visualisering med D3.js

Syftet med denna laborationen är att vi ska arbeta med att visualisera data med hjälp av det väldigt populära biblioteket [D3.js](https://d3js.org/). Detta bibliotek används för att skapa allt ifrån enkla cirkeldiagram till interaktiva och animerade nätverksdiagram och så vidare (ta gärna en titt på hemsidan för att direkt se olika exempel). Vad D3.js möjliggör är ett enkelt sätt att arbeta med [SVG (skalbar vektorgrafik](https://developer.mozilla.org/en-US/docs/Web/SVG) som finns tillgängligt genom HTML. Det vill säga att SVG är en samling HTML-element som vi kan använda för att skapa allt ifrån fyrkanter, cirklar och linjer - dvs. det som krävs för att skapa ett diagram eller någon annan typ av grafik.

Detta innebär även att vi kommer dela upp laborationen i två huvudsakliga delar. Den första, och kortare, är alltså SVG (Scalable Vector Graphics) och den andra är D3.js och hur detta bibliotek används i samband med SVG och HTML.

Det finns givetvis en massa information kring båda dessa på webben. Denna laborationen utgår huvudsakligen från två källor:

* [Dashing D3.js](https://www.dashingd3js.com/)
* [D3 Tutorials](http://alignedleft.com/tutorials/d3) - som även blivit boken "Interactive Data Visualization for the Web" från O'Reilly.
* [Index över tutorials](https://github.com/mbostock/d3/wiki/Tutorials)

---

## Del 1: SVG

För att använda sig av SVG och därmed kunna skapa grafik så behöver vi placera allt innehåll inom elementet `<svg>`. Här anger vi även en bredd (width) och höjd (height) för den yta vi vill ha tillgänglig. Det innebär att vi kan ha flera olika SVG-element innehållande olika typer av grafik.

SVG har ett gäng grundläggande grafiska element. De vanligaste av dessa är: rektangel, cirkel, rak linje och polygon.

För att börja med att skapa en rektangel kan vi utgå från nedanstående mall:

Pröva alla de exempel som finns för att praktiskt bekanta er med SVG
{: .info}

``` html
<!doctype html>
<html>
    <head>
        <title>SVG</title>
        <meta charset="utf-8">
    </head>
    <body>
        <svg height="200" width="200">
            <rect x="0" y="0" height="50" width="50" fill="red" />
        </svg>
    </body>
</html>
```

Som ni säkerligen noterar så använder sig SVG av HTML-attribut för att ange saker som höjd, bredd, position (x och y), färger, m.m. En annan **viktig** punkt är att x och y positionerna 0 innebär högst uppe i vänstra hörnet.

Ett par av de andra elementen vi har är:

* `<circle>`
* `<line>`
* `<polygon>`

För att kort experimentera med dessa kan ni pröva följande exempel (nu förutsätter vi att ni har grunden för ett HTML-dokument färdigt (dvs. `<html>`, `<head>` och `<body>`).

Cirkel
{: .code-header}

``` html
<svg height="100" width="100">
    <circle cx="50" cy="50" r="25" fill="yellow" />
</svg>
```

Linje
{: .code-header}

``` html
<svg height="100" width="100">
    <line x1="5" y1="5" x2="50" y2="50" stroke="black" stroke-width="4" />
</svg>
```

Polygon
{: .code-header}

``` html
<svg height="100" width="100">
    <polygon
        fill="yellow"
        stroke="black"
        stroke-width="2"
        points="05,30 15,10 25,30" />
</svg>
```

Alla dessa olika attribut är något som kan ses som svårt i början men blir förhoppningsvis lite enklare med tiden, i denna laborationen kommer vi huvudsakligen att arbeta med rektanglar och raka linjer. Så ni kan ju fokusera på dessa först och främst. Kompletta listor över vilka attribut respektive element har finner ni i listan nedan (som kan vara bra att ha till hands om ni vill kolla upp detta senare):

* [Rektangel](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/rect)
* [Cirkel](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/circle)
* [Linje](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/line)
* [Polygon](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/polygon)

Vad gäller utseende för grafiken (cirklar, rektanglar, osv.) så kan detta likt HTML också styras genom CSS, istället för att ange en massa attribut som `fill` och `stroke-width`
{: .info}

En alternativ läsning till det som kort presenterats ovan finner ni här:

* [Basic Building Blocks](https://www.dashingd3js.com/basic-building-blocks)
* [An SVG Primer](http://alignedleft.com/tutorials/d3/an-svg-primer)

Tänk på att ni kan fortfarande använda er webbläsares utvecklarvertyg för att inspektera och redigera er SVG-kod.
{: .info}

---

## Del 2: D3.js

Efter att ni kort bekantat er med SVG och hur dessa element ser ut så är givetvis nästa steg att använda oss av [D3.js](https://d3js.org/). Detta inkluderas i ert HTML-dokument likt vilken annan JavaScript fil som helst (tänk på hur ni gjorde med jQuery-biblioteket). Så kan antingen gå in på deras sida och ladda ner rätt JavaScript-fil eller så kan ni utgå från följande grund:

``` html
<!doctype html>
<html>
    <head>
        <title>Laboration 10 - SVG och D3.js</title>
        <meta charset="utf-8">
    </head>
    <body>
        <!-- Hämta hela D3-biblioteket via nätet -->
        <script src="https://d3js.org/d3.v3.min.js" charset="utf-8"></script>
        <!-- Detta är er egen externa JavaScript-fil -->
        <script src="main.js"></script>
    </body>
</html>
```

Tänk på att vi utgår från att ni har en tom JavaScript-fil som vi sedan kan fylla på och experimentera med!

Vad kan vi göra med D3.js då? Vi kan göra mycket mer än att bara arbeta med SVG, D3 tillhandahåller grundläggande funktioner som ni säkerligen stött på i bibliotek som jQuery. Dessa funktioner kan vara att lägga till nya HTML-element på vår sida, det kan vara att ändra texten i ett element eller lägga till event för när en besökare klickar på en knapp eller dylikt. Eftersom det är ett annat bibliotek skrivs detta givetvis på ett annorlunda vis (enligt vad D3 anser vara bra).

Först och främst finner vi hela D3 och dess funktioner under objektet `d3`. Några av de vanligare funktionerna (alt. metoderna) är följande:

* `select()` - hämta ett eller flera element
* `append()` - lägg till ett nytt element
* `text()` - lägg till eller ändra texten för ett element
* `attr()` - lägg till eller ändra ett attribut för ett element
* `style()` - lägg till eller ändra ett CSS-attribut för ett element
* `on()` - lägg till ett event

Om ni nu har skapat er en tom JavaScript-fil kan ni nu gå vidare och pröva dessa funktionerna.

``` js
// Här väljer vi <body> -> lägger till ett <p> -> och anger en text
d3.select("body").append("p").text("Added a new paragraph!");
```

I ovanstående exempel ser ni väldigt grundläggande användning av D3, en sak som är värt att notera är att vi väldigt ofta använder oss av en slags kedje-syntax (eng. "chaining"). Det vill säga att vi anropar flera metoder efter varandra. Detta kan enkelt också skrivas på ett mer läsbart vis (vilket givetvis är valfritt). Till exempel:

``` js
// JavaScript bryr sig inte om radbryt efter funktionsanrop på ett objekt
d3.select("body")
    .append("p")
    .text("Added a new paragraph!");
```

För att gå vidare och pröva lite utförligare exempel kan ni ta en titt på nedanstående kod.

``` js
d3.select("body")
    .append("button")
    .text("Click me!")
    .attr("id", "myButton")
    .style("background", "yellow")
    .style("border", "1px solid black");

d3.select("#myButton")
    .on("click", function() {
        alert("You clicked the button!");
    });
```

Baserat på ovanstående exempel - kan ni tolka vad som händer innan ni provar koden? Försök att göra er bekväma med dessa funktionerna och pröva gärna något själv.

Nästa steg är att istället för att arbeta med vanliga HTML-element så vill vi börja arbeta med SVG. Vi kan enkelt börja med att skapa en cirkel. Börja med att skapa ett `<svg>` element där ni anger både höjd och bredd till `100` samt att ni ger denna ett `id` med värdet `"svg-test"`. Pröva därefter nedanstående kod exempel.

``` js
d3.select("#svg-test")      // Vårt SVG-element
    .append("circle")       // Det grafiska elementet
    .attr("cx", 50)         // Startposition i x-led
    .attr("cy", 50)         // Startposition i y-led
    .attr("r", 50)          // Radie (tänk storlek)
    .style("fill", "blue"); // Fyllnadsfärg
```

Ett alternativ att ha ett `<svg>` element redan skapat i sin kod är att även skapa detta genom D3. Det innebär endast ett par extra rader (utifrån föregående exempel).

``` js
d3.select("body")
    .append("svg")          // Vårt SVG element
    .attr("height", 100)    // Höjden
    .attr("width", 100)     // Bredden
    .append("circle")
    .attr("cx", 50)
    .attr("cy", 50)
    .attr("r", 50)
    .style("fill", "blue");
```

---

## Att utgå från befintlig data

Att skapa enskilda element på detta viset är inget en ofta gör utan det brukar vara att vi utgår från någon slags data. Till exempel kanske vi hämtar data från ett API eller skapar den själva, men att utgå från en större mängd data är vad som oftast görs. Detta innebär att ytterligare ett par funktioner kommer att användas. I de kommande exempel är detta:

* `selectAll()` - som `select()` fast den hämtar flera element
* `enter()` - används i kombination med `select()` och `selectAll()` för att skapa "placeholders" som ska fyllas med innehåll och sedan läggas till i HTML-dokumentet
* `data()` - används för att fylla ett element med data/innehåll

För att kort demonstrera detta kan ni pröva följande exempel:

``` js
var names = ["Jane Doe", "John Doe", "Sherlock Holmes"];

d3.select("body")
    .selectAll("p")
    .data(names)
    .enter()
    .append("p")
    .text("placeholder");
```

I ovanstående exempel skapas det tre stycken `<p>` element där varje har texten "placeholder". Detta kan avläsas som att `selectAll` skapar tillfälliga `<p>` genom att avläsa den data vi skickar till `data()` (dvs. antalet) och `enter()` skapar dessa på riktigt i samband med `append()` metoden.

Vad vi vill göra är dock att alla våra namn i vår array ska hamna i respektive `<p>`. Detta innebär att istället för att vi skriver texten "placeholder" i `text()` metoden så kan vi skicka med en anonym funktion istället. Vad detta innebär är att när vi skickar med funktioner till metoder som `text()` (och många andra) så kommer denna funktionen få elementen från vår array ("names" i detta fallet) som argument. Ta en titt på exemplet nedan och pröva det också:

``` js
var names = ["Jane Doe", "John Doe", "Sherlock Holmes"];

d3.select("body")
    .selectAll("p")
    .data(names)
    .enter()
    .append("p")
    .text(function(name) {
        return name; 
    });
```

Detta innebär att den funktion vi skickar med till `text()` styr vad varje `<p>` kommer innehålla. Eftersom denna blir tilldelad varje element från vår array av namn kan vi enklast bara returnera namnet direkt.

Vanlig praxis inom kod som skrivs med D3 är att skriva om vårat exempel med text-metoden på ett kortare vis: `.text(function(d) { return d; })`, detta då det är något som är så vanligt
{: .info}

En alternativ förklaring kring detta [finner ni här](https://www.dashingd3js.com/binding-data-to-dom-elements).

---

## Exempel: rektanglar från befintlig data

För att göra ett lite mer utförlig exempel med lite mer praktisk och användbarkod så kan vi tänka oss att vi vill åstadkomma vad bilden nedan visar (tre stycken färgade rektanglar efter varandra).

![Exempel - rektanglar](../images/image_1.png) _Exempel 1. Färgade rektanglar efter varandra._

Den data vi kommer utgå ifrån kommer innehålla X och Y positionerna för respektive rektangel (tänk på att X och Y positionen 0 är högst uppe till vänster). Vi kommer även att istället för att skriva en väldigt lång kedja av metodanrop så ska vi logiskt dela in det hela. Nedan finner ni koden för grunden av detta:

``` js
// Positionerna för våra rektanglar, detta kan även
// avläsas som att varje rektangel har x=20 y=20, x=60 y=60, osv.
var positions = [20, 60, 100];

// Här skapar vi vårt <svg> element som ska innehålla all grafik
var svgContainer = d3.select("body")
                    .append("svg")
                    .attr("width", 200)
                    .attr("height", 200);

// Här utgår vi från vårt <svg> element och skapar varje rektangel
// dvs. tre stycken, fortfarande utan några attribut dock
var rectangles = svgContainer.selectAll("rect")
                    .data(positions)
                    .enter()
                    .append("rect");

// Här lägger vi till alla attribut för varje rektangel. Här kan
// ni notera att höjd och bredd anger vi manuellt till 30 pixlar.
var rectAttrs = rectangles
                .attr("x", function(d) { return d; })
                .attr("y", function(d) { return d; })
                .attr("height", 30)
                .attr("width", 30);
```

Om ni prövar ovanstående exempel bör ni få tre stycken svarta rektanglar i följd. Ta en stund att gå igenom exemplet och försök att förstå hur allting hänger ihop och varför vi valde att dela upp koden också. Värt att nämna är att D3 själv (genom metoderna *selectAll*, *data* och *enter*) loopar genom den data vi tillandahåller och vi behöver därmed inte tänka på det.

Nästa steg är att lägga på färg på respektive rektangel, detta görs genom metoden `style()`. Vad vi kommer behöva göra i detta fallet (vilket inte är väldigt praktiskt) är att baserat på vår data (de positionerna vi har) bestämma färg för varje rektangel. Ta en titt på exemplet nedan.

``` js
var rectAttrs = rectangles
                .attr("x", function(d) { return d; })
                .attr("y", function(d) { return d; })
                .attr("height", 30)
                .attr("width", 30)
                .style("fill", function(d) {
                    if (d <= 20) {
                        return "red";
                    } else if (d <= 60) {
                        return "green";
                    } else if (d <= 100) {
                        return "blue";
                    } else {
                        return "black";
                    }
                });
```

Ett bättre alternativ till att ha all data samlad som en enkel array är att representera varje rektangel som ett objekt med tillhörande attribut för höjd, bredd, osv. Detta kan se ut på följande vis:

``` js
var rectangleData = [
    { x: 20, y: 20, height: 30, width: 30, color: "red" },
    { x: 60, y: 60, height: 30, width: 30, color: "green" },
    { x: 100, y: 100, height: 30, width: 30, color: "blue" }
];

var svgContainer = d3.select("body")
                    .append("svg")
                    .attr("width", 200)
                    .attr("height", 200);

var rectangles = svgContainer.selectAll("rect")
                    .data(rectangleData)
                    .enter()
                    .append("rect");

// Observera hur alla metoder använder sig av funktioner
// som i sin tur nyttjar attributen från ett objekt (rektangel)
var rectAttrs = rectangles
                .attr("x", function(d) { return d.x; })
                .attr("y", function(d) { return d.y; })
                .attr("height", function(d) { return d.height; })
                .attr("width", function(d) { return d.width; })
                .style("fill", function(d) { return d.color; });
```

Genom att ha tydliga objekt som representerar varje rektangel kan vi förenkla våra metoder som styr utseendet för våra rektanglar. Ytterligare ett steg vi kan ta är att introducera grundläggande interaktion genom ett **klick-event**.

``` js
var rectAttrs = rectangles
                .attr("x", function(d) { return d.x; })
                .attr("y", function(d) { return d.y; })
                .attr("height", function(d) { return d.height; })
                .attr("width", function(d) { return d.width; })
                .style("fill", function(d) { return d.color; })
                .on("click", function(d) {
                    alert("The color is " + d.color + "!");
                });
```

Ytterligare en vanlig form av interaktion kan vara att radera ett element, t.ex. när vi klickar på det. Hur hade vi löst detta med D3? Den enklaste metoden är att ge varje rektangel ett unikt `id` och därefter göra så att när vi klickar på ett element så raderar vi det element baserat på dess `id`.

``` js
var rectAttrs = rectangles
                .attr("x", function(d) { return d.x; })
                .attr("y", function(d) { return d.y; })
                .attr("height", function(d) { return d.height; })
                .attr("width", function(d) { return d.width; })
                // Notera att alla dessa funktioner tar emot datan som första 
                // argumentet och index (positionen) som det andra
                .attr("id", function(d, index) { return "rect" + index; })
                .style("fill", function(d) { return d.color; })
                .on("click", function(d, index) {
                    // Hämta rektangeln, t.ex., med id="rect0" och radera den
                    d3.select("#rect" + index).remove();
                });
```

---

## Exempel: grundläggande stapeldiagram

För att ta ett steg vidare med rektanglar kan vi tänka oss att vi vill skapa ett stapeldiagram likt bilden nedan.

![Exempel 2 - stapeldiagram](../images/image_2.png) _Exempel 2. Stapeldiagram_

I bilden ovan utgår vi från en kanvas (den yta vi placerar våra grafiska element på) med 100 pixlar höjd och 200 pixlar bredd. Den har även åtta stycken staplar varpå varje stapel har värdet 0 till 100.

---

### Steg 1: data

I detta exempel kommer vi utgå från två dataset, så vi längre fram kan skifta mellan dessa.

``` js
// Data kommer representeras som tiotal mellan 0 till 100
// Dessa styr höjden av varje stapel
var dataset1 = [20, 40, 30, 60, 80, 90, 60, 10];
var dataset2 = [50, 50, 60, 40, 30, 80, 90, 100];
```

---

### Steg 2: kanvas

Nästa steg är att lägga grunden för vår kanvas, i detta fallet bryter vi även ut höjd och bredd i variabler för att ha möjlighet att enkelt kunna ändra dimensionerna på vårt diagram.

``` js
var svgHeight = 100;
var svgWidth = 200;

var svgContainer = d3.select("body")
                    .append("svg")
                    .attr("height", svgHeight)
                    .attr("width", svgWidth);
```

---

### Steg 3: staplar

Det tredje steget innebär endast att skapa ett element (`<rect>`) för varje stapel så vi i det sista steget kan ändra utseendet för dessa. **Observera** att vi börjar att använda `dataset1`

``` js
var rectangles = svgContainer.selectAll("rect")
                    .data(dataset1)
                    .enter()
                    .append("rect");
```

---

### Steg 4: utseende

I det fjärde steget ska vi ange hur vi vill att våra staplar ska presenteras, dvs. bredden, färgen, ytan mellan varje stapel osv. Här arbetar vi med fyra stycken attribut: `x` (horisontell position), `y` (vertikal position), `height` och `width`.

``` js
var rectAttrs = rectangles
                .attr("x", 0)
                .attr("y", 0)
                .attr("height", function(d) { return d; })
                .attr("width", 20);
```

I ovanstående exempel har vi anget att höjden ska komma från vårt `dataset1` (dvs. värden mellan 0 till 100). Vi har även anget en fast bredd på 20 pixlar. Problemet i detta fallet är att vi - om ni testar att inspektera i webbläsaren för att se hur den genererade HTML-koden blivit - får alla staplar ovanpå varandra. Detta innebär att vi måste ändra `x` värdet för respektive stapel.

Tänk nu på att om vi har en bredd på 20 pixlar för varje stapel och vill ha, t.ex., 1 pixel mellan varje stapel så kommer vi såfall behöva ha följande `x` värde:

```
Stapel 1: 0 (börjar längst till vänster)
Stapel 2: 21 (börjar där föregående slutar + 1 pixel som mellanrum)
Stapel 3: 42 
Stapel 4: 63
...osv
```

Hur kan vi åstadkomma detta? Det gemensamma för alla dessa staplar är ju bredden (20) och mellanrummet (1) - `21`. Vi kan även se progressionen -> 21, 42, 63, osv. Ta en titt på lösningen nedan och försök att tolka och förstå hur det hänger ihop.

``` js
var rectAttrs = rectangles
                .attr("x", function(d, index) {
                    // Index börjar på 0, och blir därefter 1, 2, 3, osv.
                    // Vilket innebär:
                    //  0 * 21 = 0
                    //  1 * 21 = 21
                    //  2 * 21 = 42
                    return index * 21; 
                })
                .attr("y", 0)
                .attr("height", function(d) { return d; })
                .attr("width", 20);
```

Sådär! Enda nackdelen nu är att det är upp och ner 😡.

Hur räknar vi då ut vart varje stapel ska börja? Eftersom y = 0 innebär högst uppe så vill vi, beroende på höjden av varje stapel, räkna ut vart den ska börja så staplarna står på rätt håll. För att inte tråka ut er så är formeln ganska enkel `höjden av vår kanvas minus höjden på en stapel`.

``` js
var rectAttrs = rectangles
                .attr("x", function(d, index) {
                    return index * 21; 
                })
                .attr("y", function(d) {
                    return svgHeight  - d; 
                })
                .attr("height", function(d) { return d; })
                .attr("width", 20);
```

Nu bör det se bra ut! Ett par punkter som är värda att tänka på här är att vi hade kunnat skapa ytterligare variabler för bredden av en stapel samt ytan mellan varje - för att ytterligare underlätta att ändra på dessa saker.

För att läsa mer ingående om exempel kring stapeldiagram [kan ni klicka är](http://alignedleft.com/tutorials/d3/making-a-bar-chart).
{: .info}

---

### Steg 5: interaktion

I det femte steget ska vi lägga till en knapp i vårt HTML-dokument som ska skifta mellan vår data, dvs. `dataset1` och `dataset2`. Därefter ska vi även lägga till så att det blir en animation när vi skiftar också 😎.

Börja med att lägga till knappen `<button id="toggle">Toggle</button>` i ert HTML-dokument. Den del vi **inte** behöver ändra på sedan tidigare är:

``` js
var dataset1 = [20, 40, 30, 60, 80, 90, 60, 10];
var dataset2 = [50, 50, 60, 40, 30, 80, 90, 100];

var svgHeight = 100;
var svgWidth = 200;

var svgContainer = d3.select("body")
                    .append("svg")
                    .attr("height", svgHeight)
                    .attr("width", svgWidth);
```

**Observera** att den kod ni hade efter detta kommer vi ändra ganska mycket på.

Nästa steg är att lägga till ett *klickevent* för vår knapp, en variabel som håller koll på vilken data som visas samt funktionen som hanterar skiftet mellan våra dataset.

``` js
// Enkel boolean för att hålla koll på våra dataset
var toggle = true;

// Lägg till ett klickevent och skifta mellan våra dataset
// Observera att här använder vi funktionen "update" som
// vi också ska skapa
d3.select("#toggle").on("click", function() {
    if (toggle) {
        update(dataset2);
        toggle = false;
    } else {
        update(dataset1);
        toggle = true;
    }
});
```

Nästa steg är att lägga till den funktion som ska hantera skiftet mellan våra dataset. Kort kan denna beskrivas som att den "gör om" alla våra staplar baserat på det dataset vi skickar till funktionen.

``` js
// Tar emot det dataset vi vill och skapar staplar därefter
function update(dataset) {
    var rects = svgContainer.selectAll("rect").data(dataset);
    
    rects.enter().append("rect");

    rects
        .attr("x", function(d, index) {
            return index * 21; 
        })
        .attr("y", function(d) {
            return svgHeight  - d; 
        })
        .attr("height", function(d) { return d; })
        .attr("width", 20);
}

// Kör första gången så vi har ett diagram från början
update(dataset1);
```

Vad vi egentligen gjorde var att all den kod som hanterade våra staplar och deras utseende placerade vi i en egen funktion som tog emot ett dataset som argument så vi dynamiskt kan ändra detta på ett enkelt vis.

Att ändra så att det blir en mindre animation är inte speciellt svårt, vi behöver endast lägga till två rader.

``` js
function update(dataset) {
    var rects = svgContainer.selectAll("rect").data(dataset);
    
    rects.enter().append("rect");

    rects
        // Detta innebär kort att alla attribut kommer
        // att animeras in med en varaktighet på 500ms
        .transition()
        .duration(500)
        .attr("x", function(d, index) {
            return index * 21; 
        })
        .attr("y", function(d) {
            return svgHeight - d; 
        })
        .attr("height", function(d) { return d; })
        .attr("width", 20);
}
```

---

## Övningar

Samtliga övningar utgår från det svarta stapeldiagram ni gjort sen tidigare - så se dessa som påbyggnader.

#### Övning 1

Gör så att ni slumpar fram en array av siffror mellan 0 - 100 istället för att ha två hårdkodade dataset. Ni ska även öka antalet staplar till 16 stycken. Här får ni givetvis öka bredden på diagrammet.

#### Övning 2

[Baserat på denna guiden](http://alignedleft.com/tutorials/d3/making-a-bar-chart) så ska ni även lägga till text på era staplar så en besökare kan se vilka värden dessa har.

#### Övning 3

Ni ska nu göra så att era staplar är färgade och att varje färg har någon koppling till värdet för stapeln, det är tillåtet att utgå från guiden som användes i övning 2.

#### Övning 4

Gör så att när en besökare klickar på en knapp (t.ex. "toggle" knappen i tidigare övningar) så ska data hämtas från ett API via AJAX (det är tillåtet att använda jQuery) och sedan ska ert stapeldiagram fyllas med denna data (via `update()` funktionen). Detta innebär givetvis att ni behöver hitta ett API som kan ge er någon data i form av siffror.
