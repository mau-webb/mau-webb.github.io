---
id: da281a
title: "Kom igång"
---

# Kom igång

Att skapa ett JavaScript-projekt behöver inte vara mer än en HTML-fil (t.ex. `index.html`) och en JavaScript-fil (t.ex. `main.js`). Namn på filer, som med HTML-filer, spelar ingen roll - dock bör de i viss mån vara logiska och enkla så ni kan länka in dessa till ert HTML-dokument. Hur ni placerar era filer spelar roll, dvs. om era JavaScript-filer ligger i en mapp eller inte - samma sak som för sökvägar till CSS-filer och bilder.

Att koppla samman en HTML-fil med en JavaScript-fil görs på följande vis och är också den grund ni kan utgå för när ni gör uppgifter och dylikt.

Vi rekommenderar textredigeraren [Atom](https://atom.io/)
{: .info}

**HTML**

``` html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>JavaScript Test</title>
    </head>
    <body>
        <!--
        Observera att vi placerar alltid <script>
        precis innan vi stänger <body>, dvs. sist.
        -->
        <script src="main.js"></script>
    </body>
</html>
```

**JavaScript**

``` js
"use strict";

var name = "Jane Doe";
var age = 33;
```

**Obs** vi utgår ifrån att vår HTML- och JavaScript-fil är placerade i samma mapp.

Placera `"use strict";` på första raden i era JavaScript-filer för att webbläsaren ska vara mer strikt vad gäller felhantering av er kod
{: .info}

Öppna nu ert HTML-dokument i er webbläsare (t.ex. Google Chrome) och välj därefter att öppna webbkonsollen - detta görs oftast genom att högerklicka (valfri plats) och sedan välja "Inspect/Inspect element" (eller dylikt). Därefter bör ni kunna navigera till någonting vid namn "Console". Väl där bör ni ha möjlighet att kunna skriva in och experimentera med er JavaScript-kod. Ta en titt på bilden nedan för att se hur det kan se ut.

![Webbkonsollen](../assets/webconsole_1.png) _Figur 1. All JavaScript-kod är tillgänglig genom webbkonsollen._

I vår JavaScript-fil skapade vi två variabler: `name` och `age` (en variabel är en plats vi kan spara information för att senare hämta den). Pröva och gör som i figuren ovan, skriv in namnet på en variabel och tryck sedan `Enter`. Om detta fungerade har ni skapat ert första JavaScript-projekt!

Ni kan utgå från att när exempel presenteras bör ni utgå från någonting ni precis gjort, ni kommer med stor sannolikhet modifiera detta utefter vad ni själva tycker fungerar bra men nu har ni en utgångspunkt i alla fall.

En sak som vi nu gjorde var att manuellt skriva in namnet på en variabel och sedan trycka enter för att se vad den innehöll. Detta är ganska omständigt och det finns givetvis en alternativ metod till att skriva ut saker i webbkonsollen - så att vi slipper göra detta. Detta görs genom någonting om kallas för `console.log()` och är någonting ni kommer göra väldigt mycket.

Modifiera er JavaScript-fil till följande:

``` js
"use strict";

// Skapa en variabel som vi vill skriva ut
var hobby = "Programming";
// Utskrift i konsollen
console.log( hobby );
```

Pröva nu att ladda om er sida och ta en titt i webbkonsollen igen, ni bör få något liknande det i figur 2.

![Webbkonsollen 2](../assets/webconsole_2.png) _Figur 2. Automatisk utskrift genom `console.log`._

Något som är väldigt viktigt med programmering är att kunna dokumentera det en gör med kommentarer, en JavaScript-kommentar kan skrivas på ett av två vis: 

* `// Kommentar som sträcker sig över en rad`
* `/* Kommentar som kan sträcka sig över flera rader */`

Vilken ni väljer är upp till er själva.

Vad mer kan vi få för utskrift? Låt oss pröva att göra lite utskrifter av olika typer:

``` js
"use strict";

// Testa utskrift av olika typer av värden, och en vektor
console.log( 5 );
console.log( "Hello World!" );
console.log( true );
console.log( ["Sweden", "Denmark", "Finland"] );
```

Notera nu att ni skriver ut olika *typer*, inom programmering är det viktigt att skilja på olika typer - dessa kan vara text (string), siffror (number), osv.

Vad händer om vi skulle göra fel? Pröva exemplet nedan.

``` js
"use strict";
// Observera att det är inga citationstecken
console.log( hello );
```

Här får vi ett felmeddelande - kan ni tolka det? Vad beror det på? - svaret på detta är att vi skriver ordet: hello, JavaScript förväntar sig en variabel men vi har ännu inte skapat en sådan. Om vi ändrar exemplet till följande bör felmeddelandet försvinna.

``` js
"use strict";
var hello = "Hello world!";
console.log( hello );
```

Denna process kallas även för att "debugga", att söka efter och korrigera felmeddelanden.

Avslutningsvis kan ni leka lite med nedanstående exempelutskrifter.

``` js
// Uträkningar
console.log( 5 + 12 );
console.log( 12 - 20 );
console.log( 80 / 4 );
console.log( 10 * 100 );
// Det går även att konkatenera (addera) strängar
console.log( "Wat" + "son" );
console.log( "Sherlock" + " Holmes" );

// Jämförelser
console.log( 10 > 8 );
console.log( 15 == 10 );
console.log( 34 >= 12 );
console.log( 12 < 5 );
console.log( 12 <= 12 );
// Det går även att jämföra strängar
console.log( "Watson" == "Watson" );
console.log( "Sherlock" != "Watson" );
// Vi kan jämföra längden
console.log( "Bo".length > "Johannes".length );

// Slutligen kan vi även kombinera uträkningar och jämförelser
console.log( 5 + 5 > 2 );
console.log( 10 / 2 == 5 );
console.log( 8 * 2 != 200 );
```
