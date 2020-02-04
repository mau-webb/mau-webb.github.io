---
id: da281a
title: "Övning: Arraymetoder"
---

# Övning: Arraymetoder

Tanken med denna övning är att öva på att använda olika `Array`-metoder för att bearbeta data i olika former. För att ytterligare förtydliga detta kan ni ta en titt på exemplet nedan.

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

För att lösa ovanstående problem hade vi kunnat göra på följande vis utan att använda oss av `Array` metoder.

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

Att utföra bearbetning på detta vis är givetvis tillåtet och görs väldigt ofta idag. För att göra detta på ett alternativt vis, i detta fallet enligt principerna för funktionell programmering så kan vi nyttja `Array` metoden [map](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Array/map). Metoden `map` tar emot en funktion som appliceras på alla element i en array och returnerar en ny array innehållande resultatet (det som skickades tillbaka från funktionen) detta. Ta en titt på exemplet nedan för att få en tydligare inblick i hur metoden fungerar.

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

Med utgångspunkt i ovanstående exempel kan vi nyttja `map` för att bearbeta det som presenterades i det första exemplet med en array innehållande objekt (med attributen för- och efternamn).

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

Genom att använda metoden `map` kan vi fokusera på vad vi vill utföra med vår data istället för detaljerna (dvs. att skapa en for-loop osv.).

Ytterligare en vanlig metod är `filter`. [Denna metod](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Array/filter), som de flesta array metoder, tar emot en funktion som appliceras på alla element. Vad denna metod dock gör är att den endast skickar tillbaka de element där funktionen returnerade `true`. För att förtydliga kan ni ta en titt på exemplet nedan.

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

Utöver att vi kan använda dessa metoder individuellt som i de exempel som presenterats kan vi även kombinera dessa. Tänk på att eftersom att dessa metoder (`map` och `filter`) skickar tillbaka en ny array - så kan vi även använda dessa metoder på denna arrayen. Detta innebär att vi kan skapa en kedja av anrop till dessa metoder för att i slutändan nå det slutresultat vi vill.

För att demonstrera detta kan vi tänka oss en array innehållande olika personer med deras namn samt ålder - vad vi vill göra är att skapa en ny array av deras namn, men bara med personer vars ålder är mer än 30.

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

Tänk på att det första anropen på `filter` ger oss en array innehållande alla personer vars ålder är mer än 30, vilket innebär att när vi anropar `map` så gör vi detta på den nya arrayen (som är filtrerad) och därmed får vi det slutresultat vi är ute efter. Observera hur koden ser ut (med punkter och strukturen), tänk även på att vi kan fortsätta denna kedjan hur länge vi vill för att nå det resultat vi vill. 

I en tidigare laboration introducerades en metod vid namnet `sort` som används för att sortera elementen i en array utefter den funktion vi tillhandahåller, även [denna](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Global_Objects/Array/sort) är en vanlig metod.

För att utföra de övningar som presenteras nedan är kravet att ni ska använda er av `Array` metoder, vilka och hur ni kombinerar dessa är upp till er själva. Varje övning kommer presentera den array som ni ska bearbeta.

#### Övning 1

``` js
var names = [
    "Andrew",
    "Peter",
    "Eliza",
    "Kirsten",
    "Jeanette"
];
``` 

Transformera alla namnen till versaler.

#### Övning 2

``` js
var triangles = [
    { width: 12, height: 22 },
    { width: 21, height: 12 },
    { width: 35, height: 49 },
    { width: 12, height: 50 },
    { width: 20, height: 35 }
];
``` 

Transformera arrayen och lägg till attributet `area` (innehållande den korrekta arean baserat på attributen `height` och `width`) på alla element.

#### Övning 3

``` js
var movies = [
    { title: "Batman Begins", year: 2005 },
    { title: "Batman", year: 1989 },
    { title: "Batman Returns", year: 1992 },
    { title: "Batman Forever", year: 1995 },
    { title: "Batman & Robin", year: 1997 },
    { title: "Batman: Under the Red Hood", year: 2010 },
    { title: "Batman: The Dark Knight Returns, Part 1", year: 2012 },
    { title: "Batman: Mask of the Phantasm", year: 1993 },
    { title: "Batman: The Movie", year: 1966 },
    { title: "Batman: The Dark Knight Returns, Part 2", year: 2013 }
];
```

Filtrera ut alla filmer som släpptes inom perioden 1990 - 2000.

#### Övning 4

``` js
var movies = [
    { title: "Batman Begins", year: 2005 },
    { title: "Batman", year: 1989 },
    { title: "Batman Returns", year: 1992 },
    { title: "Batman Forever", year: 1995 },
    { title: "Batman & Robin", year: 1997 },
    { title: "Batman: Under the Red Hood", year: 2010 },
    { title: "Batman: The Dark Knight Returns, Part 1", year: 2012 },
    { title: "Batman: Mask of the Phantasm", year: 1993 },
    { title: "Batman: The Movie", year: 1966 },
    { title: "Batman: The Dark Knight Returns, Part 2", year: 2013 }
];
```

Filtrera ut alla filmer som släpptes på 2000-talet och transformera resultatet till en array endast innhållande alla titlar. Det vill säga `["Batman Begins", "Batman: Under the Red Hood", ...]`.

#### Övning 5

``` js
var data = {
    title: "ToDo List",
    tasks: [
        { id: 101, complete: false, priority: "High", title: "Do something" },
        { id: 102, complete: false, priority: "Medium", title: "Do something else" },
        { id: 103, complete: true, priority: "Low", title: "Fix the foo" },
        { id: 104, complete: false, priority: "High", title: "Adjust the bar" },
        { id: 105, complete: true, priority: "High", title: "Fetch the baz" },
        { id: 106, complete: false, priority: "Medium", title: "Clean the apartment" },
        { id: 107, complete: false, priority: "Low", title: "Refactor my code" },
        { id: 108, complete: true, priority: "High", title: "Finish the second assignment" }
    ]
};
```

Filtrera och transformera resultatet till en array innehållande endast alla id på de _tasks_ som är avklarade och hade hög prioritet.

#### Övning 6

``` js
var data = {
    title: "ToDo List",
    tasks: [
        { id: 101, complete: false, priority: "High", title: "Do something" },
        { id: 102, complete: false, priority: "Medium", title: "Do something else" },
        { id: 103, complete: true, priority: "Low", title: "Fix the foo" },
        { id: 104, complete: false, priority: "High", title: "Adjust the bar" },
        { id: 105, complete: true, priority: "High", title: "Fetch the baz" },
        { id: 106, complete: false, priority: "Medium", title: "Clean the apartment" },
        { id: 107, complete: false, priority: "Low", title: "Refactor my code" },
        { id: 108, complete: true, priority: "High", title: "Finish the second assignment" }
    ]
};
```

Filtrera och transformera resultatet till en array innehållande objekt med attributet `name` vars innehåll är `title` + `id` (t.ex "Do something (101)") - där ni endast tar de _tasks_ som inte är avklarade och inte har låg prioritet. Det vill säga `[{ name: "Do something (101)" }, ...]`.

