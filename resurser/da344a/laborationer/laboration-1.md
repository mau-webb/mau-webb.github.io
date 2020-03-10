---
id: da344a
title: "Laboration 1"
---

# Laboration 1: Introduktion till JavaScript

Syfte med laborationen:

* att skapa ett första JavaScript-projekt.
* att göra sig bekant med en webbkonsol från valfri webbläsare.
* att göra sig bekant med [JSHint](https://jshint.com/).
* att exekvera (köra) grundläggande JavaScript-kod.

---

## Kom igång

Att skapa ett JavaScript-projekt behöver inte bestå av mer än två filer, en HTML-fil och en JavaScript-fil. Namnen på dessa filer är upp till er själva men för att ge ett exempel hade vi kunnat döpa dessa till `index.html` och `main.js`. Undvik bokstäver som `åäö` i namnen. Skulle filnamnen bestå av flera ord rekommenderas det att separera dessa med ett understreck som så här: `main_navigation.html` eller `instagram_feed.js`.

Skapa nu en HTML- och en JavaScript-fil och placera dom i samma mapp. Att koppla samman dessa kan göras på följande vis:

index.html
{: .code-header}

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

main.js
{: .code-header}

``` js
// Här skapar vi två variabler, den första innehåller text och den andra en siffra.
// Ändra gärna dessa värden till erat egna namn och ålder.
let name = "Jane Doe";
let age = 33;
```

Öppna nu er HTML-fil i en valfri webbläsare och därefter webbkonsolen, i [Firefox](https://www.mozilla.org/sv-SE/firefox/new/) och [Chrome](https://www.google.com/intl/sv/chrome/) görs detta genom `alt + cmd + j` eller `ctrl + alt + j`. Genom webbkonsolen har ni bland annat tillgång till de variabler ni skapat i er JavaScript-fil. För att testa detta skriver ni in namnet på en variabel, till exempel `name` och trycker sedan `Enter`, om allting fungerat som det ska bör ni få en utskrift av erat namn. Skärmdumpen nedan utgår från webbläsaren Chrome.

![Webbkonsollen](../images/webconsole_1.png) _Figur 1. Exempel på utskrift av variabler i webbkonsolen._

Nu har ni ert första fungerande JavaScript-projekt! Nu kan ni gå vidare till nästa del och sedan till uppgifterna, glöm inte att svara på frågorna också.

Alla kommande laborationer kommer utgå från att ni har en existerande HTML-fil som inkluderar en JavaScript-fil.
{: .info}

---

## Utskrifter

Ibland behöver vi få ut väldigt många utskrifter i webbkonsolen och då är det omständigt att manuellt behöva skriva in respektive variabel och sedan trycka `Enter`. Istället kan vi använda oss av funktionen `console.log`. Med denna funktion kan vi i vår JavaScript-fil ange vad vi vill ska skrivas ut. Fyll på er nuvarande JavaScript-fil med följande:

``` js
// Skapa en variabel som vi vill skriva ut
let hobby = "Programming";

// Använd funktionen `console.log` för att skriva ut den
console.log(hobby);
```

Pröva nu att öppna er HTML-fil igen (eller ladda om webbläsaren). Om ni gjort rätt bör ni få en utskrift liknande bilden nedan.

![Webbkonsollen](../images/webconsole_2.png) _Figur 2. Automatisk utskrift med hjälp av `console.log`._

Låt oss pröva att göra lite utskrifter av olika typer:

``` js
// Testa utskrifter av olika typer av data:

console.log(5); // Siffra
console.log("Hello World!"); // Text (sträng)
console.log(true); // Det booleska värdet "sant"

// En lista av strängar
console.log(["Sweden", "Denmark", "Finland"]);
```

En viktig del i att programmera är att dokumentera sin kod och detta görs genom så kallade "kommentarer". Dessa fungerar på samma vis som i HTML. Det vill säga en bit text som bara finns med i filen och aldrig visas. I JavaScript kan vi skriva kommentarer på två vis:

JavaScript-kommentarer
{: .code-header}

``` js
// Så här skrivs kommentarer för en rad

/*
    Så här
    skrivs kommentarer
    på flera
    rader.
*/
```

Alla frågor ska besvaras genom JavaScript-kommentarer.
{: .info}

__Fråga 1.__ Vad händer, och varför, om vi skriver följande?

``` js
// Observera att det är inga citationstecken
console.log(hello);
```

Utöver att endast skriva ut värden kan vi även skriva ut resultatet av en uträkning eller en jämförelse.

``` js
// Exempel på uträkningar
console.log(5 + 12);
console.log(12 - 20);
console.log(80 / 4);
console.log(10 * 100);

// Exempel på jämförelser
console.log(10 > 8);
console.log(15 == 10);
console.log(34 >= 12);
console.log(12 < 5);
console.log(12 <= 12);

// Vi kan även kombinera dessa, dvs. om en uträkning ger ett visst resultat
console.log(5 + 5 > 2);
console.log(10 / 2 == 5);
console.log(8 * 2 != 200);

// För att göra dessa exempel mer läsbara kan vi
// skriva det på följande vis (notera radbrytet)
console.log(
    (5 + 5) > 2
);

// Jämförelser går även att göra med strängar (dvs. text/bokstäver)
console.log("Watson" == "Watson");
console.log("Sherlock" != "Watson");

// Om vi prövar att addera (+) två strängar så gör vi något som
// kallas för att konkatenera strängar (att slå ihop)
console.log("Wat" + "son");
console.log("Sherlock" + " Holmes");
```

Funktionen `console.log` tar inte bara emot variabler för utskrift, utan alla typer av värden, uträkningar och jämförelser.
{: .info}

---

## Uppgift 1

Färdigställ exemplet nedan genom att ersätta alla frågetecken. Samtliga utskrifter måste ge värdet `true` och ni får endast använda följande operatorer __en__ gång: `<`, `>`, `<=`, `==` och `!=`.

Uppgift 1
{: .code-header}

``` js
// Vi skriver ut vilken uppgift detta gäller först
console.log("Uppgift 1.");

// Ersätt frågetecknet med en av de operatorer som listats ovan
console.log(5 * 2 ? 12);
console.log(55 ? 22);
console.log(16 / 4 ? 4);
console.log(8 + 2 ? 128);
console.log(32 * 8 ? 255);
```

---

## Strängar

Att arbeta med strängar (text) är väldigt vanligt inom programmering. Det kan vara allt i från att slå ihop strängar (konkatenera) till att bara vilja skriva ut en del av en sträng (t.ex. första bokstaven). Om vi hade velat skriva ut `"Hello"` från strängen `"Hello World!"` så hade vi använt oss av funktionen `substring`. Med denna funktion kan vi ange ett start och slut, det vill säga "från vilken bokstav till vilken bokstav", dessa start- och slutpunkter brukar kallas för **index**. Nedan finner ni några exempel av detta. Värt att notera är att olikt från `console.log` så skriver vi `.substring` i slutet av en sträng, eller en variabel bestående av en sträng.

.substring()
{: .code-header}

``` js
// Tänk att siffran 0 är positionen innan första bokstaven,
// så vill vi få ut "H" hade vi skrivit följande
console.log("Hello World!".substring(0, 1));

console.log("Hello World!".substring(0, 5));
console.log("Foo bar".substring(4, 7));
console.log("What is your name?".substring(8, 12));

// För att öka läsbarheten kan vi istället definiera variabler,
// att välja ett bra namn på en variabel är inte alltid helt lätt...
let helloWorld = "Hello World!";
let fooBar = "Foo bar";
let whatIsYourName = "What is your name?";

console.log(helloWorld.substring(0, 5));
console.log(fooBar.substring(4, 7));
console.log(whatIsYourName.substring(8, 12));
```

En sträng så som `"Hello"` är egentligen en lista av bokstäverna `["H", "e", "l", "l", "o"]`. I JavaScript börjar vi räkna från 0 i en lista. Det betyder att bokstaven `"H"` har **index** 0, det vill säga första positionen. Varje bokstav eller siffra i en lista brukar benämnas som ett **element**.
{: .info}

__Fråga 2.__ Vad händer, och varför, om vi skriver följande? [Här finner ni dokumentationen för substring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring).


``` js
let name = "Jane Doe";

// Observera att vi har utelämnat den andra siffran
console.log(name.substring(5));
```

---

## Uppgift 2

Använd funktionen `substring` för att skriva ut följande delar av dessa strängar:

* Skriv ut `"Tis"` av `"Tisdag"`.
* Skriv ut `"burgare"` av `"Hamburgare"`.
* Skriv ut `"be back"` av `"I'll be back!"`.

Uppgift 2
{: .code-header}

``` js
console.log("Uppgift 2.");

// Er lösning
```

Börja alltid lösningar på era uppgifter med en `console.log("Uppgift x.")`.
{: .info}

---

## Uppgift 3

Använd funktionerna `substring`, `toUpperCase` och `toLowerCase` för att skriva ut följande delar av dessa strängar:

* Skriv ut `"LEARNING"` av `"It's Learning"`.
* Skriv ut `"good parts"` av `"JavaScript: The Good Parts"`.
* Skriv ut `"GOOD"` av `"JavaScript: The Good Parts"`.
* Skriv ut `"ent Java"` av `"Eloquent JavaScript"`.

Information om respektive funktion [finner ni här](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String).

Exempel: toUpperCase
{: .code-header}

``` js
let title = "Eloquent JavaScript";

// Spara första delen av boktiteln i en ny variabel
let firstPart = title.substring(0, 8);

// Skriv ut värdet i versaler
console.log(firstPart.toUpperCase());
```

---

## Listor

Tidigare har vi fått se att strängar egentligen är listor av bokstäver, och för att hämta ut en del av en sträng har vi använt oss av `substring`. Eftersom en lista kan innehålla vilka värden som helst så måste vi kunna hämta ut ett värde oberoende om det är en bokstav eller en siffra. Detta görs genom att ange ett **index** (position) för ett **element** (värde) vi vill hämta ut. Nedan hittar ni ett exempel med en lista av åldrar (siffror) sparade i variabeln `ages`, genom att skriva `ages[index]` så kan vi hämta ut en ålder från listan. Experimentera med exemplet nedan.

``` js
// En lista av åldrar
let ages = [20, 21, 22, 23, 24];

// Utskrift av ett element (det tredje i detta fallet)
console.log(ages[2]);

// Jämför första och sista elementet
console.log(ages[0] < ages[4]);

// Summera, exempelvis de tre första elementen
console.log(ages[0] + ages[1] + ages[2]);

// Genom att lägga till ".length" i slutet av en lista
// kan vi få ut längden (antal värden) på listan.
console.log(ages.length);
```

---

## Uppgift 4

Från listan `numbers` nedan ska ni

* skapa en variabel vars värde är summan av alla element.
* skapa en variabel vars värde är medelvärdet av alla element.
* skriva ut dessa två variabler i webbkonsolen.

``` js
let numbers = [128, 256, 512, 1024, 2048];
```

---

## Uppgift 5

Från listan `countries` nedan ska ni

* skapa en variabel vars värde är de tre första bokstäverna av det andra elementet.
* skapa en variabel vars värde är medelvärdet av antal bokstäver för alla dessa länder.
* skriva ut dessa två variabler i webbkonsolen.

``` js
let countries = ["Sweden", "Denmark", "Finland", "Norway"];
```
