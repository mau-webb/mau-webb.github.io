---
id: me152a
title: "Laboration 8"
---

# Laboration 8

Syfte med laborationen:

* att öva på att använda Document Object Model (DOM)
* att kombinera tidigare kunskaper för att utnyttja funktionalitet via DOM

Inlämning sker i form av en zippad mapp innehållande:

* en HTML-fil
* en JavaScript-fil
* lösningar på alla **Uppgifter** placeras i JavaScript-filen
* all kod ska godkännas av [JSHint](http://jshint.com/)

Rekommenderad läsning i samband med uppgifterna:

* Funktionerna [alert](https://developer.mozilla.org/en-US/docs/Web/API/Window/alert), [prompt](https://developer.mozilla.org/en-US/docs/Web/API/window/prompt) och [confirm](https://developer.mozilla.org/en-US/docs/Web/API/window/confirm)
* Metoden [addEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener) för att köra en funktion vid ett sk. *event*, t.ex. när någon klickar på en knapp
* Metoderna [document.getElementById](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById) och [document.querySelector](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector) för att antingen hämta ett element baserat på deras ID eller baserat på en CSS-selector
* Metoderna [document.createElement](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement) och [document.createTextNode](https://developer.mozilla.org/en-US/docs/Web/API/Document/createTextNode) för att skapa ett element och för att skapa en textnod (dvs. den text som användaren ser på skärmen)
* Metoderna [.appendChild](https://developer.mozilla.org/en-US/docs/Web/API/Node/appendChild) och [.removeChild](https://developer.mozilla.org/en-US/docs/Web/API/Node/removeChild) för att lägga till ett element i ett annat (eller en textnod) samt för att radera ett element
* Attributen (på HTML-elementen, via DOM) [.children](https://developer.mozilla.org/en-US/docs/Web/API/ParentNode/children), [.firstElementChild](https://developer.mozilla.org/en-US/docs/Web/API/ParentNode/firstElementChild) och [.lastElementChild](https://developer.mozilla.org/en-US/docs/Web/API/ParentNode/lastElementChild)

**Observera** att längst ner i denna laboration finner ni några kodexempel ni kan bejaka.

---

## Uppgift 1

I denna uppgift kommer ni bli tilldelad färdig HTML och CSS som ni fyller er HTML-fil med, detta innebär också att ni behöver endast tänka på JavaScript-koden i denna uppgift.

Uppgiften går ut på att en användare kan klicka på en av tre stycken knappar. Vid ett klick på en knapp så kommer en CSS-klass att läggas till på elementet `<div id="message-box">`. Vilken CSS-klass som läggs till beror på vilken knapp som användaren klickade på. Om ni tar en titt på HTML-koden så ser ni att varje knapp har ett eget ID - värdet av detta ID, t.ex. `success`, kommer vara den CSS-klass som läggs till.

För att förtydliga: om användaren klickar på knappen `<button id="success">Success</button>` så kommer klassen `success` att läggas till på vårt element, dvs. att vårt element kommer därefter att se ut så här: `<div id="message-box" class="success"></div>`.

För att lösa detta kommer ni behöva att hämta varje knapp och sedan lägga till en funktion som körs när en användare klickar på respektive knapp.

HTML
{: .code-header}

``` html
<div id="message-box">
    <p>This is a very important message box!</p>
</div>

<button type="button" id="success">Success</button>
<button type="button" id="error">Error</button>
<button type="button" id="info">Info</button>
```

CSS
{: .code-header}

``` css
#message-box {
    border: 1px solid black;
    padding: 15px;
    font-size: 20px;
}

.success {
    background-color: #dff0d8;
    border-color: #98B98B;
}

.error {
    background-color: #f2dede;
    border-color: #BE9090;
}

.info {
    background-color: #d9edf7;
    border-color: #7294A5;
}
```

---

## Uppgift 2

#### A

I denna uppgift ska göra så att när en användare klickar på knappen så ska en popup-ruta dyka upp, med hjälp av funktionen `prompt`, där besökaren kan fylla i en valfri text. Denna text ska sedan sparas som ett nytt list-element i listan. Grunden för HTML-koden finner ni nedan.

``` html
<ul id="items">
    <li>The first item is free!</li>
</ul>

<button type="button" id="add-item">Add item</button>
```

#### B

Komplettera del **A** med ytterligare en knapp, ni väljer själva ID och knapptext, som raderar det sista elementet i listan varje gång användaren klickar på knappen.

---

## Uppgift 3

I denna uppgift ska ni utgå från HTML-koden nedan. Er uppgift är att göra så att när användaren klickar på knappen "X" i ett av dessa list-element så ska det list-elementet raderas. Dvs. klickar jag på knappen "X" i list-elementet med texten "This is the first item" så ska hela det list-elementet raderas. **Innan** detta raderas måste dock användaren få chans att godkänna detta, det innebär att ni ska använda er av funktionen `confirm` för att säkerhetsställa att användaren faktiskt gör ett aktivt val att radera ett list-element.

Använd er av variabeln `this` inuti den funktion som hanterar klick-eventet för respektive knapp. Ta även en titt på attributet [.parentElement](https://developer.mozilla.org/en-US/docs/Web/API/Node/parentElement).
{: .info}

``` html
<ul>
    <li>
        This is the first item
        <button type="button" class="remove-list-item">X</button>
    </li>
    <li>
        This is the second item
        <button type="button" class="remove-list-item">X</button>
    </li>
    <li>
        This is the third item
        <button type="button" class="remove-list-item">X</button>
    </li>
    <li>
        This is the fourth item
        <button type="button" class="remove-list-item">X</button>
    </li>
</ul>
```

---

## Extrauppgift 1

I den första extrauppgiften kommer ni att arbeta med formulär, detta är en lite större uppgift och är därför indelad i tre delar:

* **A:** Hämta det ifyllda innehållet från formuläret
* **B:** Kontrollera att innehållet är korrekt ifyllt (validering)
* **C:** Ge användaren feedback (genom CSS) om formuläret inte är komplett eller korrekt ifyllt

Ni kommer tilldelas färdig HTML för denna uppgiften. Det finns dock ingen CSS-kod och därmed är det inte speciellt användarvänligt - lägg därför gärna på lite grundläggande CSS så ni ökar användbarheten.

Varje del (A, B, C) är påbyggnader av varandra och bör därför göras i den ordningen.

``` html
<form method="get" action="" id="apply-for-pet">
    <h2>Ansökan om att skaffa husdjur</h2>
    <input type="text" name="firstname"> Förnamn<br>
    <input type="text" name="lastname"> Efternamn<br>
    <input type="text" name="age"> Ålder<br>
    <input type="text" name="email"> Epost<br>
    
    <div id="pets">
        <p>Typ av husdjur?</p>
        <input type="radio" name="pet" value="dog"> Hund<br>
        <input type="radio" name="pet" value="cat"> Katt<br>
        <input type="radio" name="pet" value="fish"> Fisk<br>
        <input type="radio" name="pet" value="bird"> Fågel<br>
    </div>

    <div id="days">
        <p>Vilka dagar arbetar/studerar ni?</p>
        <input type="checkbox" name="day" value="monday"> Måndag<br>
        <input type="checkbox" name="day" value="tuesday"> Tisdag<br>
        <input type="checkbox" name="day" value="wednesday"> Onsdag<br>
        <input type="checkbox" name="day" value="thursday"> Torsdag<br>
        <input type="checkbox" name="day" value="friday"> Fredag<br>
        <input type="checkbox" name="day" value="saturday"> Lördag<br>
        <input type="checkbox" name="day" value="sunday"> Söndag<br><br>
    </div>
    
    <button type="submit">Skicka ansökan</button>
</form>
```

#### A

I del A ska ni hämta det ifyllda formuläret och logga ut all input i konsollen. Innan vi hämtar allt innehåll behöver vi dock utföra två saker:

1. Hämta hela formuläret, dvs. `<form id="apply-for-pet">`
2. Lyssna på när användaren skickar formuläret, så att vi kan logga ut all input innan innehållet skickas vidare, detta görs med eventet `submit`

För att avbryta att formuläret inte skickas, t.ex. till en ny sida, så kan ni bejaka följande kod:

``` js
let form = /* hämta formuläret */;

// Den funktion som ska köras när användaren skickar formuläret
function onSubmit(event) {
    // Denna metod gör att formuläret inte skickar användaren
    // vidare till en ny sida och vi kan därmed styra allt själva
    event.preventDefault();

    // Om vi manuellt sett vill skicka användaren vidare,
    // t.ex. efter vi kontrollerat att allt stämmer, 
    // så skriver vi följande
    this.submit();
}

// Lägg till en event-lyssnar på "submit"
form.addEventListener("submit", onSubmit);
```

Syftet med del **A** är att logga ut allt innehåll i fälten - detta kommer göras i vår ovanstående funktion `onSubmit`. Nyckelordet `this` inuti denna funktion kan ses som att den innehåller hela formuläret (och därmed alla fälten). Dessa är sparade under attributet `this.elements`. Där respektive fält hämtas genom deras HTML-attribut `name=""`. Det vill säga att vill vi skriva ut texten för fältet `<input type="text" name="firstname" />` så kan vi skriva `console.log( this.elements.firstname.value );`. Testa att köra en `console.log` på `this.elements` för att se vad den innehåller.

Detta funkar för samtliga av våra element förutom våra checkboxar, eftersom där kan en användare välja flera val samtidigt. Det innebär att `this.elements.day` är en lista som innehåller varje checkbox. Eftersom det är en lista kan vi ju därför enkelt gå igenom denna med en for-loop. För att kontrollera att en checkbox är vald används attributet `.checked`, dvs. om vi skulle vilja kontrollera om måndag är valt hade vi skrivit `this.elements.day[0].checked`. Detta innebär att ni får nyttja en for-loop för att slutligen skriva ut vilka dagar användaren har klickat i.

#### B

I del **B** kommer ni att nyttja if-satser som kontrollerar respektive fält i förmuläret, kravlistan finner ni nedan. Skulle alla fälten vara korrekt ifyllda anropar ni `this.submit();` annars skriver ni ut ett kortare felmeddelande i konsollen.

* Förnamn - får endast innehålla `0` till `50` bokstäver
* Efternamn - får endast innehålla `0` till `50` bokstäver
* Ålder - måste vara en `Number` och vara mer än `0`
* Epost - får endast innehålla `0` till `50` bokstäver
* Husdjur - ett husdjur måste vara valt
* Dagar - en dag måste vara vald

#### C

I del **C** ska ni påverka utseendet av formuläret baserat på om något av fälten är korrekt ifyllda eller inte. Detta görs enklast på ett av två vis. Antingen gör ni så att när en användare fyller i ett fält på ett inkorrekt vis så lägger ni till en CSS-klass på det fältet, t.ex. som gör att bakgrundsfärgen blir röd. Det andra alternativet är att ni gör detta med hjälp av JavaScript.

För att påverka utseendet (CSS) med JavaScript använder vi oss av attributet `.style`. Det innebär att om vi skulle vilja göra bakgrundsfärgen röd på fältet med förnamnet hade vi kunnat skriva `this.elements.firstname.style.background = "red";`. Det vill säga att attributen efter `.style` är detsamma som i CSS: `.style.background = "red";` är det samma som `{ background: red; }` i CSS.

Baserat på kravlistan i del **B** så ska ni nu göra så att om ett fält inte är korrekt ifyllt så ska utseendet reflektera detta.

Tänk på att radioknapparna och checkboxarna ligger i varsin `<div>`, det är förmodligen enklast att påverka utseendet på den.
{: .info}

---

## Kodexempel

Att skapa ett element
{: .code-header}

``` js
// Skapa ett stycke
let p = document.createElement("p");
// Skapa en textnod
let textNode = document.createTextNode("Leo finally got an oscar!");
// Lägg till textnoden på vårt stycke
p.appendChild(textNode);

// Alternativ till att ändra text på ett element
// p.textContent = "Leo finally got an oscar!";

// Hämta vår <body>
let body = document.querySelector("body");
// Lägg till vårt stycke sist
body.appendChild(p);
```

Att radera ett element
{: .code-header}

``` js
// Vi utgår från följande HTML
// <p id="info">
//     Lite exempel innehåll <a href="google.com" id="link">här.</a>
// </p>

// Hämta de element vi arbetar med
let p = document.getElementById("info");
let a = document.getElementById("link");

// Vi måste utgå från förälder-elementet när vi ska radera
p.removeChild(a);
```

Att lägga till ett event på ett element
{: .code-header}

``` js
// Hämta knappen vi vill ska ha ett klick-event på sig
let button = document.getElementById("my-button");

// Alternativ till att hämta ett element:
// let button = document.querySelector("#my-button");

// Den funktion vi vill ska köras när användaren klickar på knappen
function onMyButtonClick(event) {
    // Den kod du vill ska utföras vid ett klick
    // ...

    // "this" representerar knappen som blev klickad
    console.log(this);

    // "event" innehåller information om eventet (klicket)
    console.log(event);
}

// Ange att vår funktion "onMyButtonClick" ska köras när användaren
// klickar på knappen som vi sparat i variabeln `button`
button.addEventListener("click", onMyButtonClick);
```

Metoden `.addEventListener` tar emot två argument: **1** vilket event (t.ex. *click*) och **2** vilken funktion som ska köras när ett event sker. Denna funktion, som ni själva skapar, blir anropad med ett argument. Detta argument brukar ges benämningen `event` och är ett objekt innehållande, bland annat, information om vilket element som användaren klickade på.
{: .info}
