---
id: me152a
title: "Laboration 11"
---

# Laboration 11

Syfte med laborationen:

* att öva på att använda ett JavaScript-bibliotek (jQuery).
* att fortsätta öva på att använda funktioner för att hämta extern data.
* att fortsätta öva på att använda Document Object Model (DOM).

Inlämning sker i form av en zippad mapp innehållande

* en HTML-fil.
* en JavaScript-fil.
* lösningar på **Uppgifter** i JavaScript-filen.

All kod ska godkännas av [JSHint](https://jshint.com/).
{: .info}

**jQuery:**

* [Dokumentation: jQuery](http://api.jquery.com/)
* [Ladda ner jQuery](https://jquery.com/download/) ("Download the compressed ...")

---

## Inledning

Ett av de vanligaste JavaScript-biblioteken i produktion idag är [jQuery](https://jquery.com/) (även om bibliotek som React, Angular, och Vue.js är mer populära). Det är ett bibliotek vars funktionalitet är väldigt bred och generell, detta innebär att med hjälp av detta kan vi skapa allt ifrån animationer, bildspel, till att hämta information från ett API och så vidare. Således kan detta bibliotek även ses som att det "förenklar" den process ni tidigare genomgått när ni arbetat med funktionerna för Document Object Model.

Som med alla andra JavaScript-filer måste vi inkludera jQuery i vårt HTML-dokument.

HTML
{: .code-header}

``` html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Laboration 11</title>
    </head>
    <body>
        <!-- Inkludera jQuery -->
        <script src="sökväg/till/jQuery"></script>
        <!-- Din egen kod -->
        <script src="sökväg/till/din/kod"></script>
    </body>
</html>
```

För att kort introducera lite funktionalitet kan ni gå igenom den kod som presenteras nedan med tillhörande kommentarer.

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

Det som presenterats ovan är ett mindre urval av all den funktionalitet som finns tillgänglig genom biblioteket jQuery. De har givetvis en dokumentationssida där ni finner mer utförliga exempel, ibland kan det även vara värt att söka på webben för ytterligare exempel.

---

## Uppgiften

Tanken med denna uppgift är att ni ska nyttja kärnfunktionalitet från biblioteket jQuery samt använda er av API:et [http://jservice.io](http://jservice.io). Med hjälp av jQuery och detta API ska ni skapa ett minimalt frågespel där ni (utöver API:et) måste använda er av jQuery-funktionerna som listas nedan. Ni ska även använda er av CSS för att göra ert spel mer tilltalande och användbart.

Om ni har ett eget förslag på ett API så får ni gärna använda er av det istället.
{: .info}

* `.getJSON()`: används för att hämta data (tänk `fetch`).
* `.on()`: används på samma vis som `.addEventListener()`.
* `.text()` eller `.html()`: dessa används för att ändra text respektive HTML för ett element.
* `.fadeIn()`: används för att animera synligheten (från osynlig till synlig) på ett element (ni kan till exempel animera in resultatet från ett API).
* `.append()`: används på samma sätt som för `.appendChild()` men med mer möjligheter.

Hur ni väljer att skapa frågespelet är upp till er själva baserat på vad API:et kan tillhandahålla.

**Tänk på att** jQuerys funktioner går att anropa efter varandra. Till exempel om vi skulle vilja lägga till en paragraf med text, dölja den och sedan animera in den (genom dess opacitet), så hade vi kunnat skriva på följande vis:

``` js
$("#mitt-exempel-id").append("<p>Hello world!</p>").hide().fadeIn();
```
