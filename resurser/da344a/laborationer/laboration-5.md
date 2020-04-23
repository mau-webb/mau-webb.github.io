---
id: da344a
title: "Laboration 5"
---

# Laboration 5: jQuery

jQuery är ett av världens mest populära JavaScript-bibliotek. Det är bland annat designat för att göra det enklare att arbeta med Document Object Model. Det vill säga modifiera element, hantera händelser (t.ex. musklick), animera CSS, m.m. jQuery har även stöd för plugins och dessa är oftast gratis att ladda ner, vilket innebär att det går snabbt att både hitta lösningar på vanliga problem och att komma igång med sitt projekt.

På [jQuerys webbplats](https://jquery.com/) hittar ni bland annat hur ni ska komma igång och deras dokumentation. Det är en viktig kunskap att kunna läsa och förstå dokumentation när man använder sig av ett bibliotek eller ramverk, därför kommer det också vara en del av denna laborationen.

Vi börjar laborationen med ett par övningar och längre ner finner ni några konkreta uppgifter att utföra.

---

## Kom igång

För att använda oss av jQuery måste vi inkludera det på vår webbplats. Detta kan göras på två vis:

1. Ladda ner jQuerys JavaScript-fil och inkludera den i ert HTML-dokument.
2. Länka till jQuerys JavaScript-fil som finns online.

Alternativ 2 innebär att ni måste ha en internetuppkoppling eftersom ni länkar till en resurs online.

För att demonstrera detta, och för att ni ska komma igång, så kan vi ta en titt på följande kod:

Inkludera jQuery
{: .code-header}

``` html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Laboration 11</title>
    </head>
    <body>
        <!-- Metod 1: Inkludera jQuery lokalt-->
        <script src="sökväg/till/jquery-3.4.1.min.js"></script>

        <!-- Metod 2: Inkludera jQuery online-->
        <script src="https://code.jquery.com/jquery-3.4.1.min.js" integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" crossorigin="anonymous"></script>

        <!-- Din egen kod -->
        <script src="sökväg/till/din/kod"></script>
    </body>
</html>

```

Notera de två olika metoderna, väljer ni metod 1 kan ni [gå in här](https://jquery.com/download/) och välja att ladda ner "Download the compressed, production jQuery 3.4.1". Glöm inte heller att skapa er egen JavaScript-fil och inkludera den utöver jQuery.

För att pröva detta så att allting fungerar korrekt kan vi lägga till följande kod i vår JavaScript-fil:

jQuery
{: .code-header}

``` js
// Variabeln `$` är oftast synonym med variabeln `jQuery`, dvs. den variabel
// som innehåller hela biblioteket.

// Här kör vi vår funktion när hela vår dokument (HTML-dokumentet)
// har laddat klart. Det är ofta en bra idé att göra så här så att du
// vet att din HTML har laddat klart innan du börjar göra någonting med den.
$(document).ready(function() {
    window.alert("The page has finished loading!");
});
```

Om ni fick en popup-ruta så ska allting fungerat som det ska, nu är ni igång!

---

## Lär känna jQuery

För att bekanta oss med jQuerys funktioner är det rekommenderat att experimentera, som med så mycket annat. En viktig sak att känna till som tidigare nämnt är att jQuery sparar hela sitt bibliotek i variabeln `$` och när ni söker om jQuery online kommer ni med största sannolikhet även stöta på det då. Ni kommer också märka att jQuerys kärnfunktionalitet (att hämta ett element, för att sedan göra någonting med det) är väldigt likt de funktioner vi tidigare stött på: `document.querySelector` och `document.querySelectorAll`.

Ta en titt på exemplen nedan.

Exempel: jQuery
{: .code-header}

``` js
// All funktionalitet för biblioteket tillgängliggörs
// genom variabeln jQuery, med alternativet "$"

jQuery; // Hela biblioteket
$; // Det vanligare alternativet

// Observera att "$" är det faktiska variabelnamnet,
// tänk på att "document" är en global variabel som
// tillkommer i alla webbläsare
$(document).ready(function() {
    // Gör någonting när ert dokument har laddat klart
});

// Om vi vill hämta ett eller flera element från vårt dokument:

// 1. Hämta alla element av en typ (t.ex alla paragrafer)
let p = $("p");

// 2. Hämta ett element baserat på ett id
let nav = $("#navigation");

// 3. Hämta alla element baserat på en klass
let items = $(".items");

// När vi hämtar ett element med jQuery får vi extra
// funktionalitet i form av metoder

// Vi kan enkelt redigera befintliga HTML-attribut
// t.ex om vi utgår från elementet:
// <a href="http://google.se" id="google">Google</a>

// Ändra från google till imdb
let a = $("#google");
a.attr("href", "http://imdb.com");

// I detta fallet används metoden "attr" för att
// redigera befintliga HTML-attribut

// Vi kan enkelt söka efter ett eller flera element
// inuti ett annat

// Inom elementet med id "wrapper" vill vi hitta
// taggen <a> med klassen "facebook"
let fb = $("#wrapper").find("a.facebook");

// Vi kan enkelt ändra HTML eller text innehåll för
// ett element, t.ex om vi utgår från paragrafen:
// <p id="message">This is important!</p>

let p = $("#message");

// Metoden "text" används för att ändra rå-text
p.text("Message has changed");

// Metoden "html" används om vi även vill inkludera HTML
p.html("Message has <strong>changed</strong>");

// Vi kan enkelt lägga till nya element till befintliga
// Tänk att vi har en lista <ul id="items"></ul>

// Hämta listan
let ul = $("#items");
// Metoden "append" används för att lägga till ett element
ul.append("<li>I'm the last element!</li>");

// Vi kan enkelt radera element från DOM genom metoden "remove"

// Radera alla paragrafer med klassen "message", tänk på att dessa
// försvinner (dvs. de blir inte endast dolda)
$("p.message").remove();

// Vi kan enkelt lägga till "click" events på element

// Lägg till "click" eventet på elementet med klassen "send"
$(".send").click(function() {
    // För att få tillgång till jQuery's metoder kan vi göra på följande vis
    let button = $(this);
    // Gör någonting... t.ex ändra texten på knappen
    button.text("You have now clicked the button!");
});

// Alternativt: $(".send").on("click", function() { ... });

// En fördel med detta är att vi kan lägga till ett "click" event
// på flera element samtidigt, t.ex alla listelement
$("li").click(function() {
    let li = $(this);
    // Om vi anropar "text" utan någon parameter så hämtar vi texten istället
    alert( li.text() );
});

// Vi kan enkelt gå igenom (och göra vad vi vill) flera element
// utan att behöva skapa någon loop och så vidare, detta
// görs genom metoden "each"
$("li.item").each(function() {
    let li = $(this);
    // Skriv ut textinnehållet för alla listelement
    // med klassen "item"
    console.log( li.text() );
    // eller t.ex, radera alla
    li.remove();
    // eller t.ex, ändra innehållet
    li.text("Text has changed!");
    // osv.
});

// Vi kan även hämta JSON från en URL (t.ex ett API)

// Den URL vi vill hämta ifrån
let url = "https://api.dryg.net/dagar/v2.1/2020/02/02";

$.getJSON(url, function(response) {
    // Gör något med `response`
});

// jQuery har även metoder för simpla animationer, detta förutsätter att:
// antingen är HTML-elementet redan dolt (dvs. display: none) för att visas 
// eller att det är synligt för att sedan döljas.

// Fade in / out
$("#message").fadeOut();
$("#message").fadeIn();

// Slide up / down
$("#message").slideUp();
$("#message").slideDown();
``` 

Utöver att hämta element och lägga till händelser (t.ex. musklick) så är det vanligt att vi ändrar eller animerar CSS-egenskaper. För att ändra en CSS-egenskap med jQuery använder vi oss av funktionen `.css("egenskap", "värde");`. Till exempel:

``` js
// Ge alla paragrafer på sidan blå text-färg
$("p").css("color", "blue");

// Gör alla element med klassen `important` fetstilda
$(".important").css("font-weight", "bold");

// Ge elementet med id="contact" grön bakgrund
$("#contact").css("background-color", "green");
```

#### Övning 1: ändra CSS-egenskaper

[Ladda ner denna HTML-fil](../assets/jquery_css_ex.html) och länka sedan in jQuery (ni bestämmer med vilken metod) och skapa sedan en egen JavaScript-fil som ni kan arbeta med. Ni ska utföra följande punkter med jQuery:

* Ge er webbplats grå bakgrundsfärg.
* Ge alla `<section>` grön bakgrundsfärg.
* Ge huvudrubriken på webbplatsen blå textfärg.
* Ge länkarna på webbplatsen gul textfärg och gör så att de inte längre är understrukna. 

#### Övning 2: hämta CSS-egenskaper

Eftersom vi kan ändra CSS-egenskaper kan vi även kontrollera vilka CSS-egenskaper ett element har. Till exempel för att kontrollera om ett element är dolt eller inte för om vi ska visa eller dölja det. För att hämta en CSS-egenskap använder vi oss återigen av `.css()` men vi anger inget värde:

``` js
// Hämta bakgrundsfärgen för elementet med id="start"
let bg = $("#start").css("background-color");
console.log("Background color: ", bg);
```

[Ladda ner denna HTML-fil](../assets/jquery_css_ex2.html) och länka sedan in jQuery (ni bestämmer med vilken metod) och skapa sedan en egen JavaScript-fil som ni kan arbeta med. Ni ska utföra följande punkter med jQuery:

* Ta reda på vilken bakgrundsfärg webbplatsen har.
* Ta reda på vilken textstorlek som huvudrubriken har.
* Ta reda på vilken textstorlek som paragraferna har.
* Ta reda på höjden för elementet med `id="primary"`.

Spara respektive värde i en variabel och slutligen skriv ut alla dessa i webbkonsolen.

#### Övning 3: händelser

En vanligt förekommande sak på webbplatser och något som jQuery förenklar är att hantera händelser, dvs.

* när användaren klickar på en knapp så ska vi...
* när webbplatsen är färdigladda så ska vi...
* när användaren för muspekaren över menyn så ska vi...
* med mera.

Utan jQuery så hade vi använt oss av funktionen `.addEventListener`. Med den funktionen så skickar vi med en funktion som ska anropas när en händelse sker (t.ex. att användaren klickar på en knapp). jQuerys alternativ är inte mycket annorlunda men heter istället `.on()` och sedan finns det även `.off()` om vi skulle vilja ta bort en händelse-funktion.

``` js
// När användaren klickar på elementet med id="start", så kommer
// funktionen `welcome` att anropas.
$("#start").on("click", welcome);

// När användaren klickar på en paragraf skriver vi ut ett meddelande
// i webbkonsolen. Notera att vi kan både skicka med en funktion vi definerat
// eller som i detta fallet, skapa en funktion samtidigt som vi skickar med.
$("p").on("click", function() {
    console.log("Clicked a paragraph!");
});

// När användaren klickar på elementet med klassen "make-green" så
// ändrar vi textfärgen till grön.
$(".make-green").on("click", function() {
    // Variabeln `this` representerar det element som händelsen är kopplad till.
    // Genom att använda oss av jQuery's funktion för att hämta ett element,
    // kan vi enkelt ta elementet som var klickat på och sedan göra något med det.
    $(this).css("color", "green");
});
```

[Ladda ner denna HTML-fil](../assets/jquery_css_ex2.html) och länka sedan in jQuery (ni bestämmer med vilken metod) och skapa sedan en egen JavaScript-fil som ni kan arbeta med. Ni ska utföra följande punkter med jQuery:

* När användaren klickar på en paragraf ska paragrafen dom klickade på få röd textfärg.
* När användaren för muspekaren över någon av rubrikerna så ska rubriken bli understruken (och när de för bort muspekaren återställs den).
* När användaren dubbelklickar på en paragraf ska textstorleken öka (den ska öka för varje gång dom dubbelklickar).

---

## Uppgift 1

Ni ska skapa en mindre miniräknare för räknesättet multiplikation. Gränssnittet ska ha rutor för följande:

* En textruta för tal 1.
* En textruta för tal 2.
* En textruta för resultatet som **inte** ska kunna redigeras.

Resultatet ska beräknas så fort som det finns två tal i båda rutorna. Så här hade ett exempel kunnat se ut:

![calculator](../images/calc.png) _Miniräknare_

---

## Uppgift 2

Ni ska nu validera ett formulärs data innan det skickas iväg. De fält som ni ska ha är följande:

* Namn
* Ålder
* Epost

När användare vill skicka iväg formuläret ska ni validera så att användaren matat in korrekt data, använd händelsen `submit` kopplat till elementet `<form>`. Om användaren matat in inkorrekt data ska ni göra bakgrundsfärgen för fältet rött. Dessutom så ska ni, så fort ett fält har korrekt data i sig, göra bakgrundsfärgen vit igen. Så här hade ett exempel kunnat se ut:

![validate](../images/validation.png) _Validering_

För att ge er en startpunkt i HTML och JavaScript kan ni utgå från följande:

HTML
{: .code-header}

``` html
<form action="#" method="get" id="newsletter">
    <!-- Lägg till era fält här ... -->
    <button type="submit">
        Skicka
    </button>
</form>
```

JavaScript
{: .code-header}

``` js
// När formuläret skickas (dvs. när användaren klickar på submit-knappen).
$("#newsletter").on("submit", function(event) {
    // Hindra formuläret från att skicka iväg användaren.
    event.preventDefault();

    // Här placerar ni er validerings kod.

    // Om allting var korrekt - skicka vidare användaren.
    $("#newsletter")[0].submit();
});
```

Parametern `event` som vi angett att vår funktion ska ta emot är en parameter som alltid skickas med till funktioner som hanterar händelser. Denna innehåller bland annat information om vilket element det gäller, när det skedde, m.m. Vi kan även (som i detta fallet) avbryta *standardbeteendet*, att avbryta att användaren skickas vidare innan vi gjort vår logik.

---

## Uppgift 3

Ni ska nu skapa ett litet formulär där vi kan mata in filmer som vi sett samt ge dessa ett betyg. Så här kan detta tänkas se ut (vi använder oss av [Bootstrap](https://getbootstrap.com/) för utseendet här):

![movies](../images/movies.png) _Filmlista_

#### Kunna lägga till en film

Det första ni ska göra är att ge användaren möjlighet att lägga till en film. Användaren ska mata in följande saker:

* Titel på filmen.
* Betyget för filmen.

Det ska sedan finnas en knapp ("Spara film") och när användaren klickar på denna ska filmen sparas i listan. Vi vill visuellt visa filmens betyg genom stjärnor, och ge möjlighet att radera en film genom ett kryss ("X"). Ikoner kan ni hitta på [Iconfinder](https://www.iconfinder.com/). Glöm inte att dubbelkolla licensen för ikonerna.

Ett exempel på den HTML som kan användas för respektive film kan se ut så här:

En film
{: .code-header}

``` html
<li data-grade="5" data-title="Star Wars">
    Star Wars
    <img src="star.png" alt="Star">
    <img src="star.png" alt="Star">
    <img src="star.png" alt="Star">
    <img src="star.png" alt="Star">
    <img src="star.png" alt="Star">
    <img src="delete.png" alt="Delete movie">
</li>
```

Denna HTML-bit går att lösa på flera vis, t.ex. med en nästlad `<div>` m.m.

Här använder vi oss av attributet `data-` där vi kan spara information om filmen i vår HTML. Detta innebär att vi kan sedan nyttja det för att till exempel sortera våra filmer. [Läs mer om data-attributen här](https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes).

Använd jQuery-funktionen `.val()` för att hämta indata från användaren (textrutan och dropdown-menyn). Använd sedan jQuery-funktionen `.append()` för att lägga till en film sist i listan.

#### Bättre hantering av indata

Nu ska ni se till att användaren verkligen ger er rätt information när dom skapar en film. Kontrollera att:

* användaren skriver in en titel.
* användaren väljer ett betyg (inte "Välj betyg").
* formuläret återställs efter en film är tillagd (t.ex. kan ni nyttja jQuery-funktionen `.trigger("reset")`).

Skulle användaren inte mata in korrekt indata ska ni visa detta på ett lämpligt sätt för användaren och be dom försöka igen.

#### Kunna ta bort en film

Ni ska nu göra så att användaren kan radera en film från listan, genom att klicka på det röda krysset. Använd jQuery-funktionen `.remove()` för att göra detta. Tänk på att ni ska radera hela `<li>` elementet, dvs. klickar dom på krysset kan ni använda `.parent()` för att gå upp ett steg i element-hierarkin och komma åt list-elementet.

**Det ska gå att radera filmer som nyligen blivit tillagda**. Inte bara de som fanns från början (om ni har en filmlista fylld från början).

#### Sortera filmerna

Nu ska ni sortera filmerna! Eftersom sorteringsfunktioner inte är något vi gått igenom (och i vissa fall något vi använder plugins för) så kommer ni bli tilldelade koden för sorteringen.

Sortera på betyg
{: .code-header}

``` js
function sortByGrade(movieA, movieB) {
    let gradeA = $(movieA).attr("data-grade");
    let gradeB = $(movieB).attr("data-grade");

    return gradeB - gradeA;
}

$("#movie-list").find("li").sort(sortByGrade).appendTo($("#movie-list"));
```

Sortera på alfabetisk ordning
{: .code-header}

``` js
function sortByTitle(movieA, movieB) {
    let titleA = $(movieA).attr("data-title");
    let titleB = $(movieB).attr("data-title");

    if (a < b) {
        return -1;
    } else if (a > b) {
        return 1;
    } else {
        return 0;
    }
}

$("#movie-list").find("li").sort(sortByTitle).appendTo($("#movie-list"));
```

Det som händer är att vi letar upp alla `<li>` inom elementet med `id="movie-list"` och sorterar dessa därefter. Antingen baserat på attributet `data-grade` eller `data-title`. Ni kan se att i båda fallen returnerar vi någon form av siffra. Siffran (positiv, negativ eller 0) styra om vi ska ändra ordningen eller inte.

#### Bonus: antal filmer

Visa på ett lämpligt ställe på sidan hur många filmer listan innehåller.

#### Bonus: färglägg filmerna

Baserat på filmens betyg ska ni ändra bakgrundsfärgen.

* Betyg 4-5: Grön bakgrundsfärg.
* Betyg 2-3: Gul bakgrundsfärg.
* Betyg 1: Röd bakgrundsfärg.
