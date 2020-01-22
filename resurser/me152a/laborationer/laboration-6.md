---
id: me152a
title: "Laboration 6"
---

# Laboration 6

Syfte med laborationen:

* att öva på att använda sig av objekt i olika situationer.
* att fortsätta öva på att använda kontrollstrukturer, loopar och funktioner.

Inlämning sker i form av en mapp (zippad) innehållande:

* en HTML-fil
* en JavaScript-fil
* lösningar på alla **Uppgifter** placeras i JavaScript-filen
* all kod ska godkännas av [JSHint](http://jshint.com/)

**Observera** att alla funktioner ni skapar ska ha en kommentar där ni beskriver följande:

* vad funktionen tar emot för argument
* vad funktionen returnerar

---

## Uppgift 1

#### A

``` js
let box = { width: 12, height: 16 };
```

Skapa en if-sats som kontrollerar om objektet ovan har attributet `area`, om detta finns ska ni skriva ut `A large box` om arean är mer än 200 annars skriver ni ut `A small box`. Om attributet **inte** finns ska ni räkna ut arean och sedan lägga till detta attribut med det uträknade värdet samt skriva ut `This box has an area of ...`.

#### B

Skapa ett objekt innehållande attributen för- och efternamn, ålder, och en lista av filmtitlar - alla dessa kan vara fiktiva. Med detta objekt ska ni skapa följande utskrift:

```
Sherlock Holmes (38) likes the following titles:
    - Willy Wonka and the Chocolate Factory
    - Airplane!
    - The Holiday
```

**Observera** att ni ersätter denna exempeldata med er egen fiktiva data.

---

## Uppgift 2

#### A

Ni ska använda er av en for-loop för att skriva ut samtliga av dessa attribut. För att använda sig av en for-loop i kombination med ett objekt [kan ni läsa mer här](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in).

``` js
let person = {
    firstname: "Jane",
    lastname: "Doe",
    age: 31,
    siblings: ["Peter", "Eliza"],
    anonymous: true,
    city: "Miami",
    state: "California"
};
```

#### B

Ni ska skapa funktionen `getAttributes` som tar emot ett argument, ett objekt, och returnerar alla attribut från detta objekt i en lista. Nedan visas ett exempel.

``` js
let box = { width: 12, height: 16 };
let boxAttrs = getAttributes(box);
console.log(boxAttrs); // => ["width", "height"]
```

---

## Uppgift 3

#### A

Ni ska skapa en så kallad konstruktor-funktion. Denna ska ha namnet `Rectangle` och tar emot två stycken argument, båda siffror, höjd och bredd. Denna funktion ska bilda ett objekt som har följande attribut:

* `height` (det första argumentet)
* `width` (det andra argumentet)
* En metod (funktion) vid namn `area` som vid anrop räknar ut rektangelns area och returnerar denna

``` js
// Skapa en rektangel där vi anger höjd och bredd
let rec = Rectangle(15, 12);

// Kontrollera att våra attribut stämmer
console.log(rec.height); // => 15
console.log(rec.width); // => 12
console.log(rec.area()); // => 180
```

#### B

Ni ska skapa en funktion som filtrerar en lista av rektanglar baserat på deras area. Funktionen ska heta `filterByArea` och tar emot två stycken argument. Det **första** argumentet representerar den minsta area en rektangel måste ha för att passera filtreringen och det **andra** argumentet är själva lista över rektanglar.

``` js
let rec1 = Rectangle(5, 3);
let rec2 = Rectangle(7, 9);
let rec3 = Rectangle(12, 14);

let rectangles = [rec1, rec2, rec3];
let filteredRectangles = filterByArea(150, rectangles);

// Denna utskrift bör ge er en lista innehållande en rektangel,
// eftersom vi valde att filtrera på en area av 150.
console.log(filteredRectangles);
```
