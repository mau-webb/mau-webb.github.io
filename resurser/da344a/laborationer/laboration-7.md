---
id: da344a
title: "Laboration 7"
---

# Laboration 7: Storage

I denna laboration kommer vi utgå från **uppgift 3** i **laboration 5** (filmlista). Där vi kommer bygga vidare så att istället för att de filmer som blivit tillagda försvinner när sidan laddas om så ska dom istället sparas lokalt hos användaren. Detta kommer vi göra genom `localStorage`, som ger oss möjlighet att enkelt kunna spara data i form av strängar.

I uppgiften som vi utgår ifrån tittade vi även på hur vi kunde sortera filmer, vi ska göra så att sorteringen sparas för **sessionen** endast. Det vill säga att när användaren stänger ner sin webbläsare så ska sorteringen nollställas. Detta kommer vi göra genom `sessionStorage`, som även denna ger oss möjlighet att spara data i form av strängar.

---

## Spara data i localStorage

Om vi ska spara våra filmer i `localStorage` (som endast tar emot strängar) behöver vi kunna konvertera vår lista (se nedan) till ett vettigt format. Till att börja med får vi fundera ut hur vi vill strukturera vår data. Till exempel kunde vi valt att strukturera våra filmer på följande vis:

Filmlista
{: .code-header}

``` js
let movies = [
    { title: "Star Wars", grade: 5 },
    { title: "Titanic", grade: 4 },
    { title: "Drive", grade: 1 }
];
```

Här har vi en lista av våra filmer, innehållande titel och betyg. Hade vi velat kunna sortera på något mer än betyg kunde vi lagt till ett `id` eller kanske `date` för när filmen lades till i listan.

Med denna lista så vill vi konvertera den på något vis så det blir en sträng så vi kan spara det i `localStorage`. Som tur är finns det populära dataformatet [JSON](https://www.json.org/json-en.html) vilket är ett format baserat på just JavaScript-objekt. Dessutom har webbläsare inbyggda funktioner för att konvertera fram och tillbaka - `JSON.stringify` och `JSON.parse`.

Så om vi enkelt velat spara våra filmer i `localStorage` (i formatet JSON) hade vi kunnat skriva något i stil med:

localStorage
{: .code-header}

``` js
// När användaren klickar på `spara`
${"#save-moves").on("click", function() {
    // Ta vår lista över filmer och konvertera den till JSON (sträng)
    let jsonMovies = JSON.stringify(movies);
    // Spara vår JSON under nyckeln `movies` i localStorage
    localStorage.setItem("movies", jsonMovies);
});
```

I korthet, vi tar vår lista (array) och omvandlar den till JSON (sträng), sedan sparar vi det i `localStorage` under nyckeln *movies* (för att vi ska kunna hämta datan senare). 

För att kontrollera att allting faktiskt har sparats kan ni öppna webbkonsolen i er webbläsare och välja **Resources** (detta är i Chrome, andra webbläsare kan ha en annan benämning). Där bör ni nu se både er nyckel och vilken data den innehåller.

![console](../images/localstorage-console.png) _1. localStorage_

---

## Skiss

Om vi tar den kod vi skrivit hitills och sätter samman en övergripande skiss på vår kod (som ni kan utgå från) får vi följande:

Skiss
{: .code-header}

``` js
// Vår lista över filmer
let movies = [
    { title: "Star Wars", grade: 5 },
    { title: "Titanic", grade: 4 },
    { title: "Drive", grade: 1 }
];

function printMovies(movies) {
    // TODO: skriver ut alla filmerna från arrayen `movies`
}

function getStars(grade) {
    // TODO:
    // baserat på `grade` så returnerar denna funktionen HTML till 
    // när vi ska visa filmen
}

function loadMovies() {
    // TODO:
    // läser in våra filmer från localStorage, skriver ut dom i listan,
    // och sparar dom i arrayen `movies`
}

$("#save-movie").on("click", function() {
    // TODO:
    // sparar en film i vår array `movies` när vi klickar på "Spara film"
    // och skriver sedan ut den uppdaterade listan av filmer genom
    // funktionen `printMovies`
});

$("#save-movies").on("click", function() {
    // Spara våra filmer i localStorage
    let jsonMovies = JSON.stringify(movies);
    localStorage.setItem("movies", jsonMovies);
});

$("#order-alphabetic").on("click", function() {
    // TODO: sorterar filmera i alfabetisk ordning
});

$("#order-grade").on("click", function() {
    // TODO: sorterar filmera på betyg
});

$(".delete-movie").on("click", function() {
    // TODO: tar bort en film från vår array
});

// Skriver ut filmerna i vår lista när sidan laddats klart
$(document).ready(function() {
    printMovies(movies);
});
```

---

## Uppgift 1

Skriv klart funktionen `printMovies` så att den skriver ut filmerna i vår HTML baserat på argumentet `movies`.

---

## Uppgift 2

Skriv klart funktionen för att spara en ny film. Så att vi kan lägga till fler filmer i vår lista. Det kan även vara en bra idé att automatiskt spara filmerna i `localStorage` när användaren sparar en ny film, så dom inte glömmer att spara senare. Detta är dock upp till er själva. Ha gärna [dokumentationen för localStorage till hands](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage).

För att lägga till ett element sist i en array i JavaScript använder ni array-metoden `.push(element)`.
{: .info}

---

## Uppgift 3

Skriv klart funktionen `loadMovies` för att ladda in filmer från `localStorage`. Istället för att vår lista *movies* ska vara hårdkodad ska ni ladda in filmerna från `localStorage`, skriva ut dom och spara dom i *movies*. Så att användaren sedan kan fortsätta lägga in fler filmer. Ni kan då uppdatera den bit som tidigare skrivit ut filmerna när siddan laddas till att anropa denna funktionen istället.

För att läsa in data från `localStorage` kan ni ta en titt på följande exempel:

JSON.parse
{: .code-header}

``` js
let jsonMovies = localStorage.getItem("movies");
let movies = JSON.parse(jsonMovies);
console.log("Loaded movies: ", movies);
```

---

## Uppgift 4

Gör det möjligt för användaren att radera filmer från vår lista. Tänk på att dessa ska tas bort från vår array *movies*. Det kan även vara en bra idé att automatiskt uppdatera `localStorage` samtidigt, så att dom även raderas där, så att dom inte råkar ladda om sidan och filmen är tillbaka. Men detta är upp till er själva.

För att radera ett element från en array så kan ni nyttja array-metoden `.splice()`. [Här finner ni dokumentationen för splice](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice).
{: .info}

---

## Uppgift 5

Skriv klart funktionerna för att sortera filmerna i alfabetisk ordning eller efter betyg. Tänk på att sidan ska komma ihåg hur ni valt att sortera filmerna under hela sessionen som användaren besöker webbplatsen (dvs. tills dom stänger webbläsaren). Så när nya filmer läggs till ska listan sorteras utan att användaren behöver klicka på att sortera.

För att spara data för *sessionen* använder ni er av `sessionStorage`, den fungerar på samma vis som `localStorage`. [Här finner ni dokumentationen för sessionStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage).
{: .info}

---

## Extrauppgift

Gör så att användaren kan filtrera filmerna (inte bara sortera). Detta kan göras på flera vis, till exempel kan ni lägga till attributen för **genre** och **årtal** (då den släpptes) till respektive film. Sedan hade ni kunnat lägga till fält för att välja genre (dropdown) eller ange ett årtal (text) som sedan filtrerar resultaten.

---

## Exempelkod: HTML

Här har ni tidigare mall för filmlistan (vi använder oss av Bootstrap för utseendet).

HTML
{: .code-header}

``` html
<div class="row container-fluid" style="padding:0 50px;">
<div class="xs-col-12">
    <h1>Min filmlista</h1>

    <form>
        <fieldset>
            <legend>Lägg till en film</legend>
            <div class="form-group">
                <label for="title">Titel:</label>
                <input
                    type="text"
                    class="form-control"
                    id="title"
                    placeholder="Titel här...">
            </div>

            <div class="form-group">
                <label for="Grade">Betyg:</label>
                <select id="grade"  class="form-control">
                    <option value="0">Välj betyg här...</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                </select>
            </div>

            <div class="form-group">
                <button id="save-movie" class="btn btn-success">
                    Spara film
                </button>
            </div>
        </fieldset>
    </form>

    <h2>Inlagda filmer</h2>
    <ul id="movie-list"></ul>

    <button id="save-movies" class="btn btn-default">
        Spara filmer
    </button>
    <button id="order-alphabetic" class="btn btn-primary">
        Alfabetisk ordning
    </button>
    <button id="order-grade" class="btn btn-primary">
        Betygsordning
    </button>
</div>
</div>
```
