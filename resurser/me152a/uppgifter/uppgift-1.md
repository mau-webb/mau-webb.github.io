---
id: me152a
title: "Filmdatabas"
---

# Uppgift 1: Filmdatabas

Syfte med uppgiften:

* att öva på att arbeta med ett färdigt dataset.
* att öva på att bearbeta data från ett format till ett annat.
* att öva på att skapa en implementation av ett givet problem baserat på en beskrivning.
* att öva på att använda Array-metoder istället för traditionella for-loopar.

Inlämning sker i form av en zippad mapp innehållande

* en HTML-fil.
* en JavaScript-fil.
* ett dataset (som ni blir tilldelade nedan).
* lösningar på **Uppgiften** i JavaScript-filen.

Uppgiften **ska** genomföras individuellt.
{: .warn}

---

## Uppgiftsbeskrivning

Ni ska skapa ett objekt som hanterar en databas över filmer och serier. Denna data kommer från [OMDb](https://www.omdbapi.com/), en tjänst som hämtar information från [IMDB](https://www.imdb.com/) och ger oss det i ett format vi kan arbeta med ([JSON](http://json.org/)).

Innan ni börjar med implementationen av ert databas-objekt så rekommenderar vi att ni går igenom och gör er bekanta med det dataset ni ska arbeta med. Vad finns det för data? Hur är den formaterad? Hur ska jag strukturera min kod baserat detta?

[Klicka här](../assets/dataset.js) för att komma åt den JavaScript-fil innehållande det **dataset** som ni ska utgå från. Ni kan antingen inkludera denna som en separat fil eller kopiera innehållet till en egen fil.
{: .info}

---

## Kravspecifikation

* Alla era variabler **ska** ha tydliga och relevanta namn. Det vill säga inte något i form av `let abc = ...`.
* Alla funktioner **ska** dokumenteras med en kommentar som beskriver **vad syftet är**, **vilka argument den tar emot** och **vad den returnerar**.
* Alla funktioner **ska** implementeras genom attributet `prototype`.

All kod ska godkännas av [JSHint](https://jshint.com/) **och** genomgå [Beautifier](https://beautifier.io/) (eller något likvärdigt).
{: .info}

---

## Implementation

Nedan listas en övergripande implementationsbeskrivning för ert objekt. Här hittar ni namn på funktionerna, vilka argument dom tar emot och vad respektive funktion ska returnera.

Vad respektive funktion ska returnera ser ni efter tecknet **->** och kan tolkas på följande vis:

Exempel: `[{ name, age }`, detta tolkas som en **lista** av objekt med attributetn `name` och `age`.

``` js
[{ name: "Sherlock Holmes", age: 34 }, { name: "John Watson", age: 32 }];
```

### Konstruktor

* `Database(dataset)`

### Funktioner

* `getAll()` **->** `[{ title, year, runtime, imdbID, genre, actos }]`
* `getAllMovies()` **->** `[{ title, year, plot, genre, actors }]`
* `getAllShows()` **->** `[{ title, year, plot, seasons, genre, actors }]`
* `filterByRelease(fromYear, toYear)` **->** `[{ title, year, imdbID }]`
* `filterByIMDBRating(rating)` **->** `[{ title, imdbRating, imdbVotes }]`
* `filterByRuntime(time)` **->** `[{ title, runtime, imdbID }]`
* `filterByGenre(genre)` **->** `[{ title, genre, imdbID }]`

De funktioner som filtrerar på betyg och speltid kan utgå från att alla filmer eller serier som har **mindre än** betyget eller speltiden ska filtreras bort.

Ta en titt på laboration 7 för att få lite repetition på hur ni ska strukturera ert objekt.
{: .info}

---

## Kodexempel

For-loop
{: .code-header}

``` js
// Vi vill göra om denna array innehållande objekt
var people = [
    { firstname: "Jane", lastname: "Doe" },
    { firstname: "Peter", lastname: "Andrews" },
    { firstname: "Kirsten", lastname: "Wiig" }
];

// till följande array:
// ["Jane Doe", "Peter Andrews", "Kirsten Wiig"]

// Vår funktion som bearbetar datan på det vis vi vill
function converToNames(data) {
    // Vi skapar en tom array för att sedan fylla denna med namn
    var names = [];
    // Gå igenom alla objekt och lägg till namnen i vår tomma array
    for (var i = 0; i < data.length; i++) {
        names.push(data[i].firstname + " " + data[i].lastname);
    }
    // Skicka tillbaka alla namn
    return names;
}

var people = [
    { firstname: "Jane", lastname: "Doe" },
    { firstname: "Peter", lastname: "Andrews" },
    { firstname: "Kirsten", lastname: "Wiig" }
];

// Nu innehåller variabeln "result":
// ["Jane Doe", "Peter Andrews", "Kirsten Wiig"]
var result = convertToNames(people);
```

Map
{: .code-header}

``` js
// Samma exempel som ovan fast med map istället.
var people = [
    { firstname: "Jane", lastname: "Doe" },
    { firstname: "Peter", lastname: "Andrews" },
    { firstname: "Kirsten", lastname: "Wiig" }
];

// Slå ihop attributen firstname och lastname till en sträng
var names = people.map(function(person) {
    return person.firstname + " " + person.lastname;
});

console.log(names);
// => ["Jane Doe", "Peter Andrews", "Kirsten Wiig"]

// Map med siffror:
var numbers = [1, 2, 3, 4, 5];

// "map" tar emot en funktion, som i sin tur tar emot
// varje element från en array. Det som skickas tillbaka
// från denna funktionen är det som sparas i den nya arrayen
var doubled = numbers.map(function(number) {
    return number * 2;
});

// Detta innebär att vi kan avläsa ovanstående som:
// return 1 * 2; => 2
// return 2 * 2; => 4
// return 3 * 2; => 6
// ...

// doubled => [2, 4, 6, 8, 10]
``` 

Filter
{: .code-header}

``` js
var animals = [
    { type: "Dog", age: 3 },
    { type: "Cat", age: 5 },
    { type: "Dog", age: 8 },
    { type: "Turtle", age: 12 },
    { type: "Dog", age: 2 }
];

// Vi kontrollerar om attributet "type" är lika med "Dog"
// Om så är fallet kommer vår funktion att returnera
// "true" och då sparas vårt resultat
var dogs = animals.filter(function(animal) {
    return animal.type == "Dog";
});

console.log(dogs);
// dogs =>
// [
//     { type: "Dog", age: 3 },
//     { type: "Dog", age: 8 },
//     { type: "Dog", age: 2 }
// ]
``` 

Map och filter
{: .code-header}

``` js
var people = [
    { firstname: "Jane", lastname: "Doe", age: 31 },
    { firstname: "Peter", lastname: "Andrews", age: 29 },
    { firstname: "Kirsten", lastname: "Wiig", age: 38 },
    { firstname: "Michael", lastname: "Higgins", age: 25 },
    { firstname: "Eliza", lastname: "Thomson", age: 41 }
];

var names = people
    .filter(function(person) {
        return person.age > 30;
    })
    .map(function(person) {
        return person.firstname + " " + person.lastname;
    });

console.log(names);
// => ["Jane Doe", "Kirsten Wiig", "Eliza Thomson"]

// Alternativt: skapa funktionerna innan ni använder dom med map och filter
const filterByAge30 = function(person) {
    return person.age > 30;
};

const getFullname = function(person) {
    return person.firstname + " " + person.lastname;
};

var names = people.filter(filterByAge30).map(getFullname);

console.log(names);
// => ["Jane Doe", "Kirsten Wiig", "Eliza Thomson"]
```
