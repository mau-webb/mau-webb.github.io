---
id: me152a
title: "Laboration 6"
---

# Laboration 6

Syfte med laborationen:

* att öva på att använda sig av objekt i olika situationer.
* att fortsätta öva på att använda kontrollstrukturer, loopar och funktioner.

Inlämning sker i form av en mapp (zippad) innehållande

* en HTML-fil.
* en JavaScript-fil.
* lösningar på alla **Uppgifter** i JavaScript-filen.

All kod ska godkännas av [JSHint](https://jshint.com/).
{: .info}

---

## Uppgift 1

### A: Box

Skapa en `if`-sats som kontrollerar om objektet `box` har attributet `area`. Om detta attribut finns och är **mer än** 200 så skriver ni ut `"The box is large!"` annars skriver ni ut `"The box is small."`. Om attributet **inte** finns ska ni **räkna ut** arean och sedan **lägga till** detta attribut (med det uträknade värdet) till objektet `box`, sedan skriver ni ut `"This box has an area of x"` (ersätt x med den uträknade arean).

Box
{: .code-header}

``` js
let box = { width: 12, height: 16 };
```

### B: Person

Skapa objektet `person` innehållande attributen: för- och efternamn, ålder och en lista av filmtitlar (allting kan vara fiktivt). Ni ska sedan nyttja detta objekt för att skapa följande utskrift (notera både radbryt och indentering).

Exempelutskrift
{: .code-header}

```
Sherlock Holmes (38) likes the following titles:
    - Willy Wonka and the Chocolate Factory
    - Airplane!
    - The Holiday
```

**Ersätt** ovanstående exempel med er egen fiktiva data.

---

## Uppgift 2

### A: User

Ni ska använda er av en for-loop för att skriva ut samtliga värden av dessa attribut. Det är **inte** tillåtet att använda sig av `console.log(user.firstname);` och så vidare. För att använda sig av en for-loop i kombination med ett objekt kan ni läsa om "[for ... in](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)".

User
{: .code-header}

``` js
let user = {
    id: "85Fd0eRYg2a",
    firstname: "Jane",
    lastname: "Doe",
    age: 31,
    siblings: ["Peter", "Eliza"],
    anonymous: true,
    city: "Miami",
    state: "California"
};
```

### B: getAttributes

Skapa funktionen `getAttributes` som tar emot ett argument (objekt) och sedan returnerar alla attribut från detta objekt i form av en lista av strängar.

getAttributes
{: .code-header}

``` js
let box = { width: 12, height: 16 };
let boxAttributes = getAttributes(box);

console.log(boxAttributes);
// => ["width", "height"]

let cat = { sound: "Meow", legs: 4 };
let catAttributes = getAttributes(cat);

console.log(catAttributes);
// => ["sound", "legs"];
```

---

## Uppgift 3

### A: Rectangle

Skapa en så kallad konstruktor-funktion med namnet `Rectangle`. Denna funktion ska ta emot två stycken argument (siffror), höjd och bredd. Detta objekt ska ha följande attribut:

* `height` (det första argumentet).
* `width` (det andra argumentet).
* Metoden (en funktion) `area` som räknar ut och returnera rektangelns area.

Rectangle
{: .code-header}

``` js
// Skapa en rektangel där vi anger höjd och bredd
let rec = new Rectangle(15, 12);

// Kontrollera att våra attribut stämmer
console.log(rec.height);
// => 15
console.log(rec.width);
// => 12
console.log(rec.area());
// => 180
```

Här hittar ni dokumentation om  operatorn [new](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new).
{: .info}

### B: filterByArea

Skapa funktionen `filterByArea` som ska filtrera en lista av rektanglar baserat på deras area. Funktionen ska ta emot två stycken argument (en lista och en siffra). Det **första** argumentet är en lista av rektanglar som ska filtreras. Det **andra** argumentet är den area som vi ska filtrera på, om en rektangels area är **mindre än** detta argument ska den filtreras bort.

filterByArea
{: .code-header}

``` js
// Respektive rektangel
let r1 = new Rectangle(5, 3);   // Area: 15
let r2 = new Rectangle(7, 9);   // Area: 63
let r3 = new Rectangle(12, 14); // Area: 168

// Alla rektanglar tillsammans
let rectangles = [r1, r2, r3];

// Filtrera bort alla rektanglar vars area är mindre än 150
let filteredRectangles = filterByArea(rectangles, 150);

// Detta bör ge er en utskrift av en lista endast innehållande rektangel nr 3.
console.log(filteredRectangles);
```
