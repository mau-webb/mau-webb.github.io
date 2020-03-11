---
id: me152a
title: "Laboration 7"
---

# Laboration 7

Syfte med laborationen:

* att fortsätta öva på att använda sig av objekt i olika situationer.
* att öva på att använda sig av attributet `prototype` i samband med objekt.
* att fortsätta öva på att använda kontrollstrukturerna loopar och funktioner.

Inlämning sker i form av en mapp (zippad) innehållande

* en HTML-fil.
* en JavaScript-fil.
* lösningar på alla **Uppgifter** i JavaScript-filen.

All kod ska godkännas av [JSHint](https://jshint.com/).
{: .info}

Alla funktioner **ska** innehålla en kommentar som kort beskriver vad funktionens **syfte** är (vad den gör), vad den **tar emot** (argument) och vad den **returnerar**.
{: .info}

---

## Uppgiften

Denna laboration består av **en** större uppgift. Konceptet för denna uppgift är att ni ska skapa en kalender som innehåller evenemang, där vi har möjlighet att hantera dessa på olika vis (lägga till, ta bort, filtrera, osv.). Detta innebär att ni kommer skapa objekten `Calendar` och `Event` för att representera detta koncept. Dessa kommer ha diverse attribut och metoder som beskrivs längre ner. När ni skapar metoderna för dessa objekt kommer detta göras genom attributet `prototype`.

Här finner ni mer dokumenation om attributet [prototype](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes).
{: .info}

Innan ni börjar med själva uppgiften så kan ni läsa igenom exemplet nedan för att ha en grund att utgå ifrån.

---

## Exempel: Person

För att praktiskt experimentera med attributet `prototype` kan ni utgå från exemplet nedan. Detta kan ni sedan nyttja som en mall till själva uppgiften.

Person
{: .code-header}

``` js
// Vårt objekt (dvs. vår konstruktor-funktion)
function Person(firstname, lastname, age) {
    this.firstname = firstname;
    this.lastname = lastname;
    this.age = age;
}

// Vår metod (funktion) `getFullName` returnerar för- och efternamn
// tillsammans separerat med ett mellanslag.
Person.prototype.getFullName = function() {
    return this.firstname + " " + this.lastname;
};

// Metoden `sayHello` returnerar en kortare hälsning innehållande både
// för- och efternamn samt åldern.
Person.prototype.sayHello = function() {
    return "Hello my name is " + this.getFullName() + " and I'm " + this.age + " years old";
};

// Metoden `toString` är en unik funktion, när denna finns så kan vi styra
// utskriften av vårt objekt
Person.prototype.toString = function() {
    return this.getFullName() + " (" + this.age + ")";
};

// Skapa en ny instans (ett nytt objekt)
let sherlock = new Person("Sherlock", "Holmes", 38);
console.log(sherlock);
// I webbkonsolen kan ni klicka runt i objektet för att se alla attribut

let name = sherlock.getFullName();
console.log(name);
// => "Sherlock Holmes"

let greeting = sherlock.sayHello();
console.log(greeting);
// => "Hello my name is Sherlock Holmes and I'm 38 years old"

// Om vi konvertera vårt objekt till en sträng så anropas metoden `toString`
console.log(String(sherlock));
// Vad får vi för utskrift?
```

---

## Event

Objektet `Event` kommer att innehålla tre stycken attribut: dag, tid och plats. Dessa tre attribut kommer att kunna hämtas från detta objekt genom tre metoder (funktioner). Nedan listas implementationsbeskrivningen.

* Konstruktornamn: `Event`
* Argument till konstruktorn **och** de attribut som objektet ska ha:
    * `day`, sträng, t.ex. `"Monday"`, `"Tuesday"`.
    * `time`, sträng, t.ex. `"12:00"`, `"14:45"`.
    * `place`, sträng, t.ex. `"Stockholm"`, `"Malmö Arena"`.
* Metoder:
    * `getDay`, inga argument, returnerar `day`.
    * `getTime`, inga argument, returnerar `time`.
    * `getPlace`, inga argument, returnerar `place`.
    * `toString`, inga argument, returnerar en sträng i formatet `"Stockholm @ Monday (12:00)"`.

### Exempel på utskrift

![Exempelutskrift: Event](../images/example_event_complete.png) _Figur 1. Skärmdump av objektet Event._

---
    
## Calendar

Objektet `Calendar` kommer att innehålla ett attribut: evenemang. Utöver detta kommer den innehålla en mängd olika metoder som hanterar dessa evenemang på olika vis. Nedan listas implementationsbeskrivningen.

* Konstruktornamn: `Calendar`
* Argument till konstruktorn **och** de attribut som objektet ska ha:
    * `events`, en lista.
* Metoder:
    * `getEvents`, inga argument, returnerar `events`.
    * `addEvent`, tar emot ett argument i form av ett `event` och lägger till det i listan `events`.
    * `clearEvents`, inga argument, tömmer listan `events` (så listan blir tom).
    * `getEventsByDay`, tar emot ett argument i form av en sträng (`day`) och returnerar en lista över de events som sker på denna dag.
    * `getEventsByTime`, tar emot ett argument i form av en sträng (`time`) och returnerar en lista över de events som sker på denna tid.
    * `getEventsByPlace`, tar emot ett argument i form av en sträng (`place`) och returnerar en lista över de events som sker på denna plats.

### Exempel på utskrift

![Exempelutskrift: Calendar](../images/example_calendar_complete.png) _Figur 2. Skärmdump av objektet Calendar._
