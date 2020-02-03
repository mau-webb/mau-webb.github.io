---
id: me152a
title: "Laboration 10"
---

# Laboration 10: Repetition

Syfte med laborationen:

* att färdigställa tidigare laborationer.
* att fortsätta öva på att använda sig av variabler, kontrollstrukturer och funktioner.
* att fortsätta öva på att skriva välformaterad kod och dokumentation.
* att öva på att bearbeta data.

---

## Extrauppgifter A till F

Nedan hittar ni uppgifterna A till F som handlar om att bearbeta data på olika vis. Ni kommer få ett färdigt dataset som ni kommer utgå ifrån. Ni **ska** i dessa uppgifter använda er av Array-metoderna `map` och `filter`.

Det är **inte** tillåtet att använda traditionella for-loopar för dessa uppgifter.
{: .warn}

---

## Uppgift A

Transformera alla namnen till versaler.

``` js
let names = [
    "Andrew",
    "Peter",
    "Eliza",
    "Kirsten",
    "Jeanette"
];
``` 

---

## Uppgift B

Transformera listan och lägg till attributet `area`, värdet för detta attribut ska räknas ut genom respektive objekts höjd och bredd.

``` js
let triangles = [
    { width: 12, height: 22 },
    { width: 21, height: 12 },
    { width: 35, height: 49 },
    { width: 12, height: 50 },
    { width: 20, height: 35 }
];
``` 

---

## Uppgift C

Filtrera ut alla filmer som släpptes inom perioden 1990 - 2000.

``` js
let movies = [
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

---

## Uppgift D

Filtrera ut alla filmer som släpptes på 2000-talet och transformera resultatet till en lista innhållande alla titlar. Det vill säga något i stil med följande: `["Batman Begins", "Batman: Under the Red Hood", ...]`.

``` js
let movies = [
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

---

## Uppgift E

Filtrera och transformera resultatet till en lista innehållande alla `id` på de `tasks` som är avklarade **och** hade hög prioritet.

``` js
let todoList = {
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

---

## Uppgift F

Filtrera och transformera resultatet till en lista innehållande objekt med attributet `name` (vars innehåll är `title` + `id`) **och** ni ska endast ha kvar de `tasks` som **inte är avklarade** och **inte har låg prioritet**. Det vill säga något i stil med följande: `[{ name: "Do something (101)" }, ...]`.

``` js
let todoList = {
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
