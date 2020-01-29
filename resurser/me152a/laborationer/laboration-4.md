---
id: me152a
title: "Laboration 4"
---

# Laboration 4

Syfte med laborationen:

* att göra sig bekant med funktioner.
* att fortsätta öva på att använda tidigare koncept som kontrollstrukturer och loopar.
* att genom en kortare uppgiftsbeskrivning kunna formulera en lösning i form av en funktion.

Inlämning sker i form av en mapp (zippad) innehållande

* en HTML-fil.
* en JavaScript-fil.
* lösningar på alla **Uppgifter** i JavaScript-filen.

All kod ska godkännas av [JSHint](https://jshint.com/).
{: .info}

**Observera:**

* Det är tillåtet att återanvända de funktioner ni skapar i alla uppgifter.
* Vissa uppgifter har **restriktioner** över vad som **inte** får användas.

---

## Uppgift 1

Det är **inte** tillåtet att använda er av `Math.max` och `Math.min`.
{: .warn}

#### A - Max

Skapa funktionen `max` som tar emot två stycken argument (siffror) och returnerar det högsta.

max
{: .code-header}

``` js
let highestNumber = max(15, 35);
console.log(highestNumber);
// => 35
```

#### B - Min

Skapa funktionen `min` som tar emot två stycken argument (siffror) och returnerar det lägsta.

min
{: .code-header}

``` js
let lowestNumber = min(31, 20);
console.log(lowestNumber);
// => 20
```

---

## Uppgift 2

#### A - Range

Skapa funktionen `range` som tar emot ett argument (siffra) och returnerar en lista innehållande siffrorna `1` till `n`, där `n` har värdet av det argument som skickades med. Tänk på att listan ska **börja på** siffran `1`.

range
{: .code-header}

``` js
let firstTen = range(10);
console.log(firstTen);
// => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

#### B - RangeStep

Skapa funktionen `rangeStep` som tar emot två argument (siffror) och returnerar en lista innehållande siffrorna `0` till `n`. Det **första** argumentet styr antal element i listan, det vill säga `n`. Det **andra** styr stegen (eller hoppen) mellan dessa. Tänk på att listan ska **börja på** siffran `0`.

rangeStep
{: .code-header}

``` js
let threeStep = rangeStep(5, 3);
console.log(threeStep);
// => [0, 3, 6, 9, 12];
```

---

## Uppgift 3

Det är **inte** tillåtet att använda sig av Array- eller Sträng-metoden `.reverse()`.
{: .warn}

#### A - ReverseString

Skapa funktionen `reverseString` som tar emot ett argument (sträng) och returnerar denna sträng baklänges.

reverseString
{: .code-header}

``` js
let name = reverseString("Sherlock");
console.log(name);
// => kcolrehS
```

#### B - ReverseArray

Skapa funktionen `reverseArray` som tar emot ett argument (lista) och returnerar denna lista baklänges.

reverseArray
{: .code-header}

``` js
let ages = [21, 33, 20, 18, 35];
let reversedAges = reverseArray(ages);
console.log(reversedAges);
// => [35, 18, 20, 33, 21];
```

#### C - Reverse

Skapa funktionen `reverse` som tar emot ett argument (sträng **eller** lista) och returnerar detta baklänges.

reverse
{: .code-header}

``` js
let name = "Sherlock";
let ages = [21, 33, 20, 18, 35];

let reversedName = reverse(name);
let reversedAges = reverse(ages);

console.log(reversedName);
// => kcolrehS
console.log(reversedAges);
// => [35, 18, 20, 33, 21]
```

Detta innebär att ni kommer behöva kontrollera typen av argumentet som funktionen tar emot:

* **Om** det är en *sträng* kan ni använda er av `reverseString`.
* **Om** det är en *lista* kan ni använda er av `reverseArray`.

För att kontrollera vilken typen av någonting, en variabel eller ett argument, kan ni använda er av operatorn `typeof`.

``` js
console.log(typeof "Sherlock");
// => "string"
console.log(typeof [1, 2, 3]);
// => "object"
```

---

## Uppgift 4

#### A - Sum

Skapa funktionen `sum` som tar emot ett argument (lista) och returnerar summan av listans alla element (siffror).

sum
{: .code-header}

``` js
let numbers = [5, 10, 15];
let result = sum(numbers);
console.log(result);
// => 30
```

#### B - CompareSum

Skapa funktionen `compareSum` som tar emot två argument (listor) och returnerar `true` om **summan** av den **första** listan **är mer än summan** av den **andra**, annars `false`.

compareSum
{: .code-header}

``` js
let first = [1, 2, 3];
let second = [10, 20, 30];

let isFirstLarger = compareSum(first, second);
let isSecondLarger = compareSum(second, first);

console.log(isFirstLarger);
// => false
console.log(isSecondLarger);
// => true
```

---

## Uppgift 5

#### A - countChar

Skapa funktionen `countChar` som tar emot två argument (strängar) och returnerar **summan av antalet upprepningar** av ett tecken i en sträng. Det **första** argumentet är själva strängen och det **andra** argumentet är det tecken vi ska räkna.

countChar
{: .code-header}

``` js
let name = "Mississippi";

// Räkna antal upprepningar av tecknet "s" i variabeln `name`
let count = countChar(name, "s");

console.log(count);
// => 4
```

#### B - palindrome

Skapa funktionen `palindrome` som tar emot ett argument (sträng) och returnerar `true` om det är ett palindrom annars `false`. Ett **palindrom** är en sträng som är likadan även om den läses baklänges.

palindrome
{: .code-header}

``` js
let test1 = "sirap i paris";
console.log(palindrome(test1)); // => true

let test2 = "sherlock";
console.log(palindrome(test2)); // => false

let test3 = "maoam";
console.log(palindrome(test3)); // => true
```

Tänk på funktionen `reverse` som ni redan skapat.
{: .info}

---

## Extrauppgift

Skapa funktionen `splitString` som tar emot två argument (strängar). Det **första** argumentet är strängen vi vill dela på och det **andra** argumentet är från vilket tecken (bokstav) vi ska dela strängen på.

splitString
{: .code-header}

``` js
let lorem = "Lorem Ipsum";
let parts = splitString(lorem, "e");

console.log(parts);
// => ["Lor", "em Ipsum"]
```
