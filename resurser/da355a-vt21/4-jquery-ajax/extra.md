---
id: da355a-vt21
title: "4. jQuery & Ajax"
---

# Extra övningar

{: .info}
Detta är en fortsättning från uppgift 3.a. - del 3

## Sortera filmerna

Nu ska ni sortera filmerna! Eftersom sorteringsfunktioner inte är något vi gått igenom (och i vissa fall något vi använder plugins för) så kommer ni bli tilldelade koden för sorteringen.

Sortera på betyg
{: .code-header}

``` js
function sortByGrade(movieA, movieB) {
    let gradeA = $(movieA).attr("data-grade");
    let gradeB = $(movieB).attr("data-grade");

    return gradeB - gradeA;
}

$("#movie-list").find("li").sort(sortByGrade).appendTo($("#movie-list"));
```

Sortera på alfabetisk ordning
{: .code-header}

``` js
function sortByTitle(movieA, movieB) {
    let titleA = $(movieA).attr("data-title");
    let titleB = $(movieB).attr("data-title");

    if (a < b) {
        return -1;
    } else if (a > b) {
        return 1;
    } else {
        return 0;
    }
}

$("#movie-list").find("li").sort(sortByTitle).appendTo($("#movie-list"));
```

Det som händer är att vi letar upp alla `<li>` inom elementet med `id="movie-list"` och sorterar dessa därefter. Antingen baserat på attributet `data-grade` eller `data-title`. Ni kan se att i båda fallen returnerar vi någon form av siffra. Siffran (positiv, negativ eller 0) styra om vi ska ändra ordningen eller inte.

## Bonus: antal filmer

Visa på ett lämpligt ställe på sidan hur många filmer listan innehåller.

## Bonus: färglägg filmerna

Baserat på filmens betyg ska ni ändra bakgrundsfärgen.

* Betyg 4-5: Grön bakgrundsfärg.
* Betyg 2-3: Gul bakgrundsfärg.
* Betyg 1: Röd bakgrundsfärg.