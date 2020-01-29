---
id: me152a
title: IMDB
---

# Uppgift 1: IMDB

**Uppgiften ska utföras individuellt.**

Syfte med uppgiften:

* att öva på att arbeta med ett färdigt dataset
* att öva på att bearbeta data från ett format till ett annat
* att öva på att skapa en implementation av ett givet problem baserat på en beskrivning
* att öva på att använda Array-metoder istället för traditionella for-loopar

Inlämning sker i form av en zippad mapp innehållande:

* en HTML-fil
* en JavaScript-fil
* ett dataset (antingen som en separat fil eller i er egen fil)
* lösningar på **Uppgiften** placeras i JavaScript-filen
* all kod ska godkännas av [JSHint](https://jshint.com/)
* all kod ska genomgå [Beautifier](https://beautifier.io/) (eller något likvärdigt)

Övrigt:

* alla era variabler **ska** ha tydliga och relevanta namn, dvs. inte något i form av `let x = ...`
* alla funktioner **ska** dokumenteras med en kommentar som beskriver syftet, argumentet och vad den returnerar
* alla funktioner **ska** implementeras genom attributet `prototype`
* ni får **inte** använda er av traditionella `for (...) { ... }` loopar utan istället ska ni använda er av följande Array-metoderna: [Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map) och [Filter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter). Det [finns givetvis fler metoder](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) att använda men *map* och *filter* ska ersätta era for-loopar.

[Klicka här](js/dataset.js) för att komma åt den JavaScript-fil innehållande det dataset som ni ska utgå från. Ni kan antingen inkludera denna som en separat fil genom en `<script>` tag eller bara kopiera innehållet till er egen fil.
{: .info}

# Uppgiftsbeskrivning

Ni ska skapa ett objekt som hanterar en databas över filmer och serier. Denna data kommer från [OMDb](https://www.omdbapi.com/) vilket är en tjänst som hämtar information från [IMDB](https://www.imdb.com/) och ger oss det i ett format vi kan arbeta med - mer specifikt JavaScript-objekt. Detta format brukar även gå under det vanligare namnet [JSON](http://json.org/).

Innan ni börjar med implementationen av ert databas-objekt så rekommenderar vi att ni går igenom och gör er bekanta med datasetet - Vad finns det för data? Hur är den formaterad? Vilka nycklar har vi att tillgå?

## Implementation

Metodbeskrivningen innehåller både namn, vilka argument och vad den returnerar. Vad den returnerar skrivs (efter "->") i formatet `[{ title, year }]`. Detta hade översatts till: en lista av objekt med nycklarna "title" och "year".

#### Konstruktor

`function Database(dataset)`

#### Metoder

* `function getAll()` -> `[{ title, year, runtime, imdbID, genre, actos }]`
* `function getAllMovies()` -> `[{ title, year, plot, genre, actors }]`
* `function getAllShows()` -> `[{ title, year, plot, seasons, genre, actors }]`
* `function filterByRelease(fromYear, toYear)` -> `[{ title, year, imdbID }]`
* `function filterByIMDBRating(rating)` -> `[{ title, imdbRating, imdbVotes }]`
* `function filterByRuntime(time)` -> `[{ title, runtime, imdbID }]`
* `function filterByGenre(genre)` -> `[{ title, genre, imdbID }]`

Metoderna som filtrerar på betyg och speltid kan utgå från att alla filmer/serier som har mindre än betyget eller speltiden, filtreras bort.

## Exempelkod: Map & Filter

Nedan finner ni exempel på kod som använder sig av metoderna Map och Filter.

``` js
// Vi vill göra om denna array innehållande objekt
var people = [
    { firstname: "Jane", lastname: "Doe" },
    { firstname: "Peter", lastname: "Andrews" },
    { firstname: "Kirsten", lastname: "Wiig" }
];

// till följande array:
// ["Jane Doe", "Peter Andrews", "Kirsten Wiig"]
```

``` js
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

**Map:**

``` js
// Exempel
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

``` js
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
``` 

**Filter:**

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

**Map & Filter:**

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
```
