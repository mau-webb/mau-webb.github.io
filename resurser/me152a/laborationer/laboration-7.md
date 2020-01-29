---
id: me152a
title: "Laboration 7"
---

# Laboration 7

Syfte med laborationen:

* att fortsätta öva på att använda sig av objekt i olika situationer.
* att öva på att använda sig av attributet `prototype` i samband med objekt.
* att fortsätta öva på att använda kontrollstrukturer, loopar och funktioner.

Inlämning sker i form av en mapp (zippad) innehållande:

* en HTML-fil
* en JavaScript-fil
* lösningar på alla **Uppgifter** placeras i JavaScript-filen
* all kod ska godkännas av [JSHint](http://jshint.com/)

**Observera** att alla funktioner ni skapar ska ha en kommentar där ni beskriver följande:

* vad funktionen tar emot för argument
* vad funktionen returnerar

När ni skapar ett objekt ska ni **alltid** använda er av operatorn `new` framför, dvs. `let p = new Person();`.
{: .info}

---

## Uppgiften

Denna laboration består av **en** uppgift och är således en aning mer omfattande än tidigare uppgifter. Konceptet för denna uppgift är att skapa en *kalender* som hanterar ett obestämt antal *events*. Detta innebär att ni kommer skapa objekt som representerar dessa, dvs. `Calendar` och `Event`. I jämförelse med föregående laboration kommer dessa objekt och deras funktioner att skapas genom att använda er av prototyp-kedjan (ett exempel på hur detta fungerar presenteras längre ned).

Ni kommer få en beskrivning över *vad* ni ska implementera, men *hur* ni väljer att göra det är upp till er själva - då det är möjligt att lösa detta på olika vis.

#### Exempel på prototyp

För att få en kortare praktiskt introduktion till objekt med tillhörande funktioner genom `prototype` kan ni bejaka exemplet nedan:

``` js
// Vårt objekt (dvs. vår konstruktor-funktion)
function Person(firstname, lastname, age) {
    this.firstname = firstname;
    this.lastname = lastname;
    this.age = age;
}

// Funktionen (också kallat metod) `getFullName` returnerar
// för- och efternamn tillsammans separerat med ett mellanslag.
Person.prototype.getFullName = function() {
    return this.firstname + " " + this.lastname;
};

// Funktionen `sayHello` returnerar en kortare hälsning innehållande
// både för- och efternamn samt åldern.
Person.prototype.sayHello = function() {
    return "Hello my name is " + this.getFullName() + " and I'm " + this.age + " years old";
};

// Funktionen `toString` är en speciell funktion då gör det möjligt att
// påverka utskriften när objektet anropas av funktionen `String`
Person.prototype.toString = function() {
    return this.getFullName() + " (" + this.age + ")";
};

// Observera att vi använder oss av operatorn `new`
let sherlock = new Person("Sherlock", "Holmes", 38);
console.log(sherlock);

let name = sherlock.getFullName();
console.log(name);

let greeting = sherlock.sayHello();
console.log(greeting);

// Observera vad som händer när vi konverterar vårt objekt till en sträng
// - om vi definierat en `toString` funktion så anropas den.
console.log( String(sherlock) );
```

Kopiera och pröva ovanstående kodexempel för att känna på hur det fungerar.

---

### Event

Objektet `Event` kommer att innehålla tre stycken attribut: day, tid och plats. Dessa tre attribut kommer att kunna hämtas från detta objekt genom tre funktioner (dvs. **metoder**). Nedan listas implementationsbeskrivningen.

* Konstruktornamn: `Event`
* Argument till konstruktorn (samt de attribut som ska finnas):
    * `day` - sträng i formatet `Monday`, `Tuesday`, osv.
    * `time` - sträng i formatet `12:00`, `14:45`, osv.
    * `place` - sträng i formatet `Stockholm`, `Malmö Arena`, osv.
* Metoder:
    * `getDay` - inga argument, returnerar `day`
    * `getTime` - inga argument, returnerar `time`
    * `getPlace` - inga argument, returnerar `place`
    * `toString` - inga argument, returnerar en sträng i formatet (exempel) `Stockholm @ Monday (12:00)`

---
    
### Calendar

Objektet `Calendar` kommer att innehålla ett attribut: events. Utöver detta kommer den innehålla en mängd olika metoder som hanterar dessa på olika vis. Nedan listas implementationsbeskrivningen.

* Konstruktornamn: `Calendar`
* Argument till konstruktorn (samt de attribut som ska finnas):
    * `events` - en lista, antingen tom eller fylld av ett eller flera `Event`
* Metoder:
    * `getEvents` - inga argument, returnerar listan över alla events
    * `addEvent` - tar emot ett argument i form av ett event och lägger sedan till detta i listan över events, returnerar `undefined`
    * `clearEvents` - inga argument, tömmer listan av events (dvs. det blir en tom lista), returnerar `undefined`
    * `getEventsByDay` - tar emot ett argument i form av en sträng (`day`) och returnerar en lista över de events som sker på denna dag
    * `getEventsByTime` - tar emot ett argument i form av en sträng (`time`) och returnerar en lista över de events som sker på denna tid
    * `getEventsByPlace` - tar emot ett argument i form av en sträng (`place`) och returnerar en lista över de events som sker på denna plats

---

## Exempel på utskrifter

Nedan visas två skärmdumpar på exempelutskrifter från respektive objekt.

![Exempelutskrift: Event](../images/example_event_complete.png) _Figur 1. Event_

![Exempelutskrift: Calendar](../images/example_calendar_complete.png) _Figur 2. Calendar_
