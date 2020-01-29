---
id: me152a
title: "Laboration 2"
---

# Laboration 2

Syfte med laborationen:

* att göra sig bekant med kontrollstrukturerna `if` och `while`.
* att göra sig bekant med funktionalitet från webbläsaren ([window](https://developer.mozilla.org/en-US/docs/Web/API/Window)).
* att fortsätta öva på att använda variabler.
* att fortsätta öva på att använda listor ([Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)).
* att öva på att söka och tolka dokumentation från [MDN web docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript).

Inlämning sker i form av en mapp (zippad) innehållande

* en HTML-fil.
* en JavaScript-fil.
* lösningar på alla **Uppgifter** i JavaScript-filen.

All kod ska godkännas av [JSHint](https://jshint.com/).
{: .info}

---

## Uppgift 1

Denna uppgift består av fem stycken deluppgifter (A - E). Dessa behandlar listor på olika vis och kräver att ni söker genom [dokumentationen](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) för att kunna färdigställa dem. Det rekommenderas att ni läser om följande funktioner: reverse, concat, push, join och indexOf.

I kommentarerna nedan kan ni notera `// => ...`, denna kommentar visar på vilken utskrift ni bör få ut i webbkonsolen om ni gjort rätt.
{: .info}

#### A - Omvänd lista

Färdigställ exemplet nedan.

``` js
let list = [3, 5, "Jane", true, 144, false];
let reversedList = /* Färdigställ denna del */;

// Skriv ut den omvända listan
console.log(reversedList);
// => [false, 144, true, "Jane", 5, 3]
```

#### B - Ihopslagen lista

Färdigställ exemplet nedan.

``` js
let firstList = [1, 2, 3, 4, 5];
let secondList = [6, 7, 8, 9, 10];
let lists = /* Färdigställ denna del */;

// Skriv ut de ihopslagna listorna
console.log(lists);
// => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

#### C - Påbyggd lista

Färdigställ exemplet nedan.

``` js
let list = [];

/* Färdigställ denna del */

// Skriv ut listan
console.log(list);
// => [4, 7, "Watson", true, 33, false]
```

#### D - Sammanslagen lista till en sträng

Färdigställ exemplet nedan.

``` js
let information = ["Sherlock Holmes", 33, "Detective"];
let output = /* Färdigställ denna del */;

// Skriv ut informationen
console.log(output);
// => "Sherlock Holmes, 33, Detective"
```

#### E - Positionen av ett element

Färdigställ exemplet nedan.

``` js
let names = ["Watson", "Jane", "Sherlock", "Doe"];

let janeExists = /* Färdigställ denna del */;
let johnExists = /* Färdigställ denna del */;

// Skriv ut resultaten
console.log("Jane exists:", janeExists);
// => "Jane exists: true"
console.log("John exists:", johnExists);
// => "John exists: false"
```

---

## Uppgift 2

Denna uppgift handlar om att nyttja den inbyggda funktionalitet som finns i dagens webbläsare. Bland de vanligare funktionerna så har vi möjlighet att få en användares input, antingen som text eller som ett "Ja" eller "Nej", eller bara ge ett meddelande till en användare. Denna funktionalitet är indelad i tre funktioner:

* [alert](https://developer.mozilla.org/en-US/docs/Web/API/Window/alert) - visa ett meddelande till användaren
* [prompt](https://developer.mozilla.org/en-US/docs/Web/API/Window/prompt) - hämta input från en användare
* [confirm](https://developer.mozilla.org/en-US/docs/Web/API/Window/confirm) - be användare godkänna eller avböja

Dessa används på följande vis:

Exempel: alert, confirm, prompt
{: .code-header}

``` js
// Visa ett meddelande
window.alert("Hello!");

// Ge användaren möjlighet att godkänna eller avböja - denna ger tillbaka "true" eller "false"
let areYouSure = window.confirm("Are you sure?");
console.log("Am I Sure?", areYouSure);

// Ge användaren möjlighet att fylla i ett värde - denna ger tillbaka en sträng
let username = window.prompt("What's your username?");
console.log("Username:", username);
```

Genom att nyttja dessa tre funktionerna ska ni skapa ett mindre program som gör följande:

* Skapa en variabel innehållande en **tom** lista, denna kommer sedan att fyllas på med innehåll.
* Fråga användaren efter deras namn och spara detta namnet i listan.
* Fråga användaren om de har ett husdjur eller inte (som `true` eller `false`) och spara detta i listan.
* Fråga användaren om deras ålder (som en siffra) och spara detta i listan.
* Visa denna informationen som ett meddelande (alert) enligt följande format: `"Sherlock Holmes, true, 33"`.
* Skriv även ut denna lista i webbkonsolen enligt följande format: `["Sherlock Holmes", true, 33]`.

För att konvertera en sträng till en siffra kan ni använda er av funktionen [Number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number) på följande vis: `let n = Number("123");`, notera att vi skrev strängen `"123"`.
{: .info}

---

## Uppgift 3

Denna uppgift introducerar kontrollstruktrerna `if` och `while`. Med hjälp av dessa kan vi skapa ett program som körs på obestämd tid, i jämförelse mot ovanstående uppgift där vi själva bestämmer när programmet slutar. Först demonstreras dessa kontrollstrukturer och sedan hittar ni uppgiftsbeskrivningen för denna uppgift (Gissningsspelet).

Exempel 1: if
{: .code-header}

``` js
let number = 45;

// Genom en jämförelse kan vi styra vilken output som användaren får.
if (number > 50) {
    console.log("The number is more than 50!");
} else {
    console.log("The number is less than 50!");
}
```

Exempel 2: if
{: .code-header}

``` js
// Det går också att göra flera jämförelser efter varandra genom `else if`.
let amount = -15;

if (amount > 100) {
    console.log("The amount is too high!");
} else if (amount == 50) {
    console.log("The amount is perfect.");
} else if (amount > 0 && amount < 50) {
    console.log("The amount is to low!");
} else {
    console.log("The amount cant be negative!");
}
```

Läs igenom ovanstående exempel och försök följa med hur variabeln `amount` går igenom kontrollstrukturen `if`. Vilken utskrift blir det? Pröva att ändra värdet på `amount`.

**Observera** att vid den tredje jämförelsen används operatorn `&&`. Detta är en så kallad [logisk operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_Operators) och används för att gruppera flera jämförelser tillsammans.

Om vi tar exemplet: `amount > 0 && amount < 50`, så kan vi tolka detta som att "amount är **mer** än 0 **och** amount är **mindre** än 50".

Exempel 1: while
{: .code-header}

``` js
// Exempel 1 - manuell kontroll
let counter = 0;

while (counter < 10) {
    console.log(counter);
    // Öka `counter` med 1
    counter = counter + 1;
}
```

Exempel 2: while
{: .code-header}

``` js
// Exempel 2 - dynamisk kontroll
let shouldContinue = true;

while (shouldContinue) {
    let message = window.prompt("Give me a message!");
    console.log("Message:", message);
    shouldContinue = window.confirm("Do you want to continue?");
}
```

Genom kontrollstrukturen `while` kan vi få vårat program att fortsätta göra saker utan att vi själva behöver skriva en massa kod. Vi kan (genom kod) beskriva när vårt program ska sluta. I ovanstående exempel 1 kan vi se att våran sk. "while-loop" kommer att fortsätta skriva ut variabeln `counter` så länge denna är mindre än 10. Det vill säga att så länge våran kontroll i `while (...)` ger `true` kommer våran while-loop att fortsätta upprepa kodblocket inom `{ ... }`.

**Observera** att om kodblocket *alltid* ger `true` kommer koden aldrig att sluta och det finns risk att din webbläsare krashar eller att du får starta om den.

I exempel 2 väljer vi istället att ta användarens input genom `confirm` (som ger oss `true/false`) för att genom detta styra när vår while-loop ska sluta.

### Gissningsspelet

Ni ska skapa ett mindre spel där en siffra ska slumpas fram (1 till 10) och användaren ska gissa sig fram till denna. Nedan kommer en beskrivning av programmet i punktform:

* Skapa variabeln `number` innehållande en siffra mellan 1 och 10, denna ska slumpas fram.
* Skapa variabeln `guesses` som börjar på 0 och kommer att ökas med 1 för varje gång användaren gissar fel.
* Skapa variabeln `correct` som håller koll på om användaren gissat rätt eller inte.
* Skapa en while-loop som nyttjar variabeln `correct` för att bestämma när den ska sluta köras.
* I while-loopen:
    * Hämta användarens gissning och spara det i variabeln `input`.
    * Konvertera denna till en siffra och jämför denna mot `number`.
    * Om jämförelsen stämmer så ge användaren meddelandet `Your guess is right!` annars `Incorrect, keep going.`.
    * Om jämförelsen stämde så ska ni uppdatera värdet av variabeln `correct` så att er while-loop slutar.
    * Om jämförelsen inte stämde så ska ni öka variabeln `guesses` med 1.
* Efter while-loopen: ge användaren meddelandet `Number of guesses: x`, där `x` ersätts med värdet från er variabel `guesses`.

#### Att slumpa fram en siffra

För att slumpa fram en siffra mellan 1 och 10 kan ni använda er av funktionerna [random](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random) och [ceil](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/ceil). Funktionen random ger oss en slumpmässig siffra mellan 0 och 1 (med decimaler) och ceil används för att avrunda uppåt.

Pröva detta exempel i webbkonsolen:

``` js
Math.ceil(Math.random() * 10);
```

Detta innebär att vi slumpar fram en siffra mellan 0 till 1 (0.351, 0.745, osv.), multiplicerar denna med 10 (3.51, 7.45, osv.) och sedan avrundar vi denna uppåt (4, 8, osv.).

---

## Extrauppgift

**Denna uppgift är frivillig.**

Skapa ett program som skriver ut alla siffror mellan `1` till `100`, med följande krav:

* Om siffran är delbar med `3` ska ni istället skriva ut `Foo`.
* Om siffran är delbar med `5` ska ni istället skriva ut `Bar`.
* Om en siffra är delbar med `3` **och** `5` ska ni istället skriva ut `FooBar`.
* Övriga siffror skriver ni ut utan modifikation.

Tänk på att ni kommer behöva använda er av `if` för att kontrollera om en siffra är delbar med `3` eller `5`. Detta kan ni exempelvis göra genom modulus operatorn `%`. Denna operator fungerar på följande vis:

Modulus
{: .code-header}

``` js
// Kontrollera om variabeln `number` är delbar med 2
let number = 18;

if (number % 2 == 0) {
    console.log("Number is divisible by 2");
}
```

Nedan finner ni även ett exempel på utskriften av de 15 första talen:

``` js
1
2
"Foo"
4
"Bar"
"Foo"
7
8
"Foo"
"Bar"
11
"Foo"
13
14
"FooBar"
```

Tänk på att ordningen på er `if`-sats spelar stor roll i hur programmet fungerar.
{: .info}
