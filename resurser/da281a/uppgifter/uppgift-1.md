---
id: da281a
title: "Inlämningsuppgift 1"
---

# Inlämningsuppgift 1

Betyg: U/G

## Syfte

Syftet med den första inlämning är att bekanta sig både med programmeringsmiljön (textredigerare, webbläsare, osv.) samt med grundläggande programmering. I detta fallet handlar dessa delar om att kunna spara data av olika typer och med dessa kunna utföra saker så som att jämföra, beräkna, m.m.

Inför denna uppgiften rekommenderas det starkt att läsa kapitel 1 och 2 i boken Eloquent JavaScript.

**Obs** där det står "skriv ut i konsollen" så menas detta att ni använder er av `console.log()`.

## Uppgiften

Denna uppgift är indelad i mindre deluppgifter, det rekommenderas att försöka hålla sig till den ordning som presenteras (då svårighetsgraden ökar med varje). Uppgifterna kan lösas på många olika vis, det finns alltså inte alltid ett korrekt svar utan ibland kan det finnas ett flertal. När ni söker information via webben efter lösningar eller hjälp på vägen så rekommenderas det starkt att oavsett vad ni hittar - försök att förstå hur det fungerar - experimentera och utforska koden med hjälp av webbkonsollen.

Tips 1: testa gärna att klistra in er kod på [JSHint](http://jshint.com/) för att se om den kan ge förslag på förbättringar. Det är en sida som följer vissa standarder för hur en bör skriva kod på ett korrekt vis.

Tips 2: testa gärna att använda er av tjänsten [Dirty Markup](https://www.dirtymarkup.com/) som hjälper er formatera er kod.

**Glöm inte att läsa igenom kravspecifikation innan ni börjar, så ni inte missar någonting eller får komplettera på grund av slarvfel.** 

### Uppgift 1

Utifrån kodexemplet nedan ska ni färdigställa samtliga utskrifter. Alla utskrifter ska ge värdet `true` och ni får endast använda följande operatorer **en** gång: `<`, `>`, `<=`, `==`, `!=`.

``` js
console.log( 5 * 2   12 );
console.log( 55   22 );
console.log( 16 / 4   4 );
console.log( 8 + 2   128 );
console.log( 32 * 8   255 );
```

### Uppgift 2

Använd sträng-metoden `.substring()` för att skriva ut följande delar av dessa strängar:

1. Skriv ut `"Tis"` av `"Tisdag"`
2. Skriv ut `"burgare"` av `"Hamburgare"`
3. Skriv ut `"be back"` av `"I'll be back"` 

Tips: spara gärna varje sträng som en egen variabel och nyttja därefter `.substring()` på dessa så blir det lättare att läsa!

### Uppgift 3

Kombinera sträng-metoderna `.substring()`, `.toLowerCase()` och `.toUpperCase()` för att skriva ut följande delar av dessa strängar:

1. Skriv ut `"LEARNING"` av `"It's Learning"`
2. Skriv ut `"good parts"` av `"JavaScript: The Good Parts"`

### Uppgift 4

I uppgift 4 ska ni utgå från följande array:

``` js
var numbers = [128, 256, 512, 1024, 2048];
```

1. Skapa en variabel med namnet `sumOfNumbers` vars värde är summan av alla siffrorna i arrayen `numbers`, skriv även ut denna i konsollen
2. Skapa en variabel med namnet `avgNumber` vars värde är medelvärdet av alla siffrorna i krrayen `numbers` (detta görs genom `summan / antal`). Tänk på att medelvärdet ska kunna räknas ut även om vi själva lägger till eller tar bort ett par siffror, dvs. är det inte tillåtet att skriva `summan / 5` (för att vi har fem siffror). Skriv även ut medelvärdet i konsollen
3. Lägg till ett element (siffra) i slutet av arrayen vars värde är summan av alla siffror (tips nyttja variabeln ni tidigare skapade), skriv även ut den nya arrayen i konsollen

### Uppgift 5

I uppgift 5 ska ni utgå från följande array:

``` js
var countries = ["Sweden", "Denmark", "Finland", "Norway"];
```

1. Skriv ut de tre första bokstäverna av det andra elementet i konsollen
2. Räkna ut och skriv ut medelvärdet för antal bokstäver för alla element i konsollen

### Uppgift 6

I uppgift 6 ska ni utgå från följande array: 

``` js
var values = [3, 5, "Jane", true, 144, false];
```

Ta reda på hur ni kan få innehållet av arrayen `values` att hamna i motsats ordning (baklänges) och skriv sedan ut detta i konsollen.

### Uppgift 7

I uppgift 7 ska ni slå ihop tre stycken arrayer till **en** egen array, utgå från följande arrayer:

``` js
var names = ["Jane", "Joe", "Eliza"];
var ages = [21, 34, 22];
var hasPet = [true, false, true];
```

Spara den nya arrayen i variabeln `multipleArrays`.

### Uppgift 8

I uppgift 8 ska ni ta reda på hur ni kan slå ihop alla element av en array till en sträng, dvs. array till text (sträng). Ni ska utgå från följande array: 

``` js
var actors = ["Sherlock", "Watson", "Bo"];
```

Med denna array ska ni skriva ut resultatet konsollen i formatet: `"Sherlock - Watson - Bo"`.

### Uppgift 9

I uppgift 9 ska ni använda er av en `if`-sats som styr vilken utskrift det blir i konsollen givet värdet på en variabel. Denna if-sats ska innehålla tre delar och utföra jämförelser mot en variabel med namnet `amount`.

1. Om variabeln `amount` är *mindre än* `50` så ska ni skriva ut `"Less then 50!"` i konsollen
2. Om variabeln `amount` är *mer än eller lika med* `50` och *mindre än* `65` så ska ni skriva ut `"Optimal range for the amount!"` i konsollen
3. I alla andra fall så ska ni skriva ut `"Too much!"`

### Uppgift 10

I uppgift 10 ska ni använda er av en `for`-loop för att slippa att manuellt använda er av `console.log()` för att göra flera utskrifter, som i detta fall annars hade varit väldigt repetitivt. Den utskrift ni ska uppnå med er for-loop är följande:

``` bash
#
##
###
####
#####
######
#######
########
```

*I exemplet ovan är det 8 rader.*

## Kravspecifikation

* På första raden i er fil ska ni använda raden `"use strict";` för att göra webbläsaren mer strikt i sin tolkning av er kod
* Samtliga uppgifter ska markeras med en kommentar innan uppgiften innehållande uppgiftsnummret, dvs. `// Uppgift 1.` för första uppgiften osv.
* Det får inte visas några felmeddelande i webbkonsollen
* All JavaScript-kod ska placeras i en egen fil och länkas in till ert HTML-dokument
* All JavaScript-kod måste ha godtycklig indentering, dvs. allting får inte vara vänsterställt eller allt för svårt att läsa

## Inlämning

**Glöm inte kontrollera att ni skickat med svar på alla uppgifter och att ni följt kravspecifikationen.**

Ni ska skriva all er JavaScript-kod i ett separat dokument (dvs. med filändelsen `.js`) (se exempelfilen main.js här nedan). Ni ska även skriva en enkel HTML-fil som länkar till Javascript-filen med en Script-tagg (se exempelfilen index.html här nedan). Skicka in dessa dokumentet (en HTML-fil och en JavaScript-fil) som en `.zip` på Canvas . Döp denna enligt formatet `inl1_Förnamn_Efternamn.zip`.Ni ska även ladda upp dessa filer på dvwebb (en [guide om detta finner du här](/{{ site.resource_path }}/da281a/material/m1_intro_dvwebb/)) - och därefter ska du även inkludera länken dit.

Glöm inte att skriva ert namn och datorid högst upp i filen!

Här nedan finner ni en exempelmall (HTML + JavaScript) för inlämningen:

**index.html**

{% highlight html linenos %}
<!doctype html>
<html>
    <head>
        <title>Inlämningsuppgift 1</title>
        <meta charset="utf-8">
    </head>
    <body>
        <script src="main.js"></script>
    </body>
</html>
{% endhighlight %}

**main.js**
{% highlight js linenos %}
/* Här kan ni placera ert namn och dator-id. */

/**
 * Uppgift 1
 * =========
 */

/**
 * Uppgift 2
 * =========
 */

/**
 * Uppgift 3
 * =========
 */
{% endhighlight %}



Lycka till!
