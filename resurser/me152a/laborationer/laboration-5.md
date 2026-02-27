---
id: me152a
title: "Laboration 5"
---

# Laboration 5: Repetition

Syfte med laborationen:

* att färdigställa tidigare laborationer.
* att fortsätta öva på att använda sig av variabler, kontrollstrukturer och funktioner.
* att fortsätta öva på att skriva välformaterad kod och dokumentation.

---

## Extrauppgifter

Nedan presenteras några extrauppgifter som fortsätter att behandla funktioner. Beskrivningarna innehåller antal argument, typerna för dessa samt vilken typ funktionen returnerar.

Alla funktioner **ska** innehålla en kommentar som kort beskriver vad funktionens **syfte** är (vad den gör), vad den **tar emot** (argument) och vad den **returnerar**.
{: .info}

---

### Uppgift A - reverseNumber

Skapa en funktion som tar emot ett argument, en siffra (t.ex. `2941`, `32512`), och returnerar denna baklänges (siffra).

reverseNumber
{: .code-header}

``` js
let n = 33157;
let reversed = reverseNumber(n);

console.log(reversed);
// => 75133
```

---

### Uppgift B - toTitleCase

Skapa en funktion som tar emot ett argument, en sträng (t.ex. `"flock of seagulls"`), och returnerar denna sträng där varje ord nu börjar med en stor bokstav.

toTitleCase
{: .code-header}

``` js
let s = "flock of seagulls";
let converted = toTitleCase(s);

console.log(converted);
// => "Flock Of Seagulls"
```

---

### Uppgift C - leftPad

Skapa en funktion som tar emot två argument, båda ska vara siffror, och returnerar en sträng. Där funktionen lägger till nollor framför det **första** argumentet om värdet har mindre tecken än vad det **andra** argumentet anger. Bejaka exemplet nedan:

leftPad
{: .code-header}

``` js
let n = 15;
let padded = leftPad(n, 3);

console.log(padded);
// =>  "015"

let n2 = 8;
let padded2 = leftPad(n2, 4);

console.log(padded2);
// => "0008"
```

---

### Uppgift D - findWord

Skapa en funktion som tar emot ett argument, en sträng, och returnerar det längsta ordet (sträng). Om flera ord är lika långa kan ni returnera det första.

findWord
{: .code-header}

``` js
let s = "The Quickest Brown Fox";
let word = findWord(s);

console.log(s);
// => "Quickest"
```
