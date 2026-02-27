---
id: me152a
title: "Laboration 3"
---

# Laboration 3

Syfte med laborationen:

* att göra sig bekant med kontrollstrukturen `for`.
* att fortsätta öva på att använda variabler och listor.
* att genom en kortare uppgiftsbeskrivning kunna formulera en lösning.

Inlämning sker i form av en mapp (zippad) innehållande

* en HTML-fil.
* en JavaScript-fil.
* lösningar på alla **Uppgifter**  i JavaScript-filen.

All kod ska godkännas av [JSHint](https://jshint.com/).
{: .info}

Samtliga uppgifter utgår från att en eller flera for-loop(ar) används.
{: .warn}

---

## Uppgift 1

#### A - Fallande

Återskapa följande utskrift (observera att det är på *en* rad).

``` js
10 9 8 7 6 5 4 3 2 1
```

#### B - Stegvis

Återskapa följande utskrift (notera radbryten).

``` js
3
6
9
12
15
18
21
24
27
30
```

#### C - Multiplar av 2

Återskapa följande utskrift.

``` js
"1, 2, 4, 8, 16, 32, 64, 128"
```

---

## Uppgift 2

#### A - Jämn och ojämn

Återskapa följande utskrift (1 - 20).

``` js
"1 is odd"
"2 is even"
"3 is odd"
"4 is even"
"5 is odd"
"..."
"20 is even"
```

#### B - Multiplikationstabellen

Återskapa följande utskrift (vilken tabell som skrivs ut ska styras genom en variabel som enkelt kan ändras).

``` js
"1 x 9 = 9"
"2 x 9 = 18"
"3 x 9 = 27"
"4 x 9 = 36"
"5 x 9 = 45"
"6 x 9 = 54"
"7 x 9 = 63"
"8 x 9 = 72"
"9 x 9 = 81"
"10 x 9 = 90"
```

#### C - Betygsgrupper

Räkna ut antal procentandelar av respektive betygsgrupp (U, G, VG). Utgå från listan `grades` nedan.

``` js
let grades = ["VG", "VG", "U", "VG", "VG", "G", "U", "G", "G", "VG", "G", "G", "G", "U", "G", "G", "G", "G"];
```

Återskapa följande utskrift baserat på listan `grades`.

``` js
"U: 16.67%, G: 55.56%, VG: 27.78%"
```

För att begränsa antalet decimaler kan ni använda er av funktionen [toFixed](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toFixed).

toFixed
{: .code-header}

``` js
// Exempel av toFixed
let num = 2.3421;
console.log(num.toFixed(2));
// => 2.34
```

---

## Uppgift 3

#### A - 2D

Med utgångspunkt i den två-dimensionella listan `nestedArray` nedan.

``` js
let nestedArray = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
];
```

Återskapa följande utskrift:

``` js
"Array 1 contains:"
1
2
3
4
5
"Array 2 contains:"
6
7
8
9
10
"Array 3 contains:"
11
12
13
14
15
```

En flerdimensionell-lista (en, två, tre, osv.) innebär att en lista innehåller en eller flera listor, som i sin tur också kan innehålla listor.
{: .info}

#### B - Betygsresultat

Med utgångspunkt i listan `gradesFromExam` nedan.

``` js
let gradesFromExam = [
    ["Jane", 68],
    ["Joe", 43],
    ["Watson", 55],
    ["Elize", 71],
    ["Sherlock", 61],
    ["Lisa", 75]
];
```


Och med följande betygsgränser:

* U: mindre än 50
* G: mellan 50 och 70
* VG: mer än 70

Återskapa följande utskrift:

``` js
"Jane: G"
"Joe: U"
"Watson: G"
"Elize: VG"
"Sherlock: G"
"Lisa: VG"
```

#### C - Shackbrädet

Utskriften nedan kan ses som ett rutnät av 6 stycken tecken i X-led (horisontellt) och 6 stycken tecken i Y-led (vertikalt). Ni ska återskapa denna och även skapa två stycken variabler, `x` och `y`, som enkelt ska kunna ändras för att styra denna utskrift. Här kan **två** stycken for-loopar vara en lösning på detta problem.

```
XOXOXO
OXOXOX
XOXOXO
OXOXOX
XOXOXO
OXOXOX
```

---

## Extrauppgift

Återskapa utskriften nedan. Det ska även finnas en variabel, `size`, som styr storleken (eller höjden) på pyramiden.

```
     #
    ###
   #####
  #######
 #########
###########
```
