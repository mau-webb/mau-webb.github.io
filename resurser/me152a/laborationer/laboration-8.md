---
id: me152a
title: "Laboration 8"
---

# Laboration 8

Syfte med laborationen:

* att öva på att använda Document Object Model (DOM).
* att kombinera tidigare kunskaper med funktionalitet via DOM.

Inlämning sker i form av en zippad mapp innehållande

* en HTML-fil.
* en JavaScript-fil.
* lösningar på alla **Uppgifter** i JavaScript-filen.

All kod ska godkännas av [JSHint](https://jshint.com/).
{: .info}

**I slutet av denna laboration finner ni både kodexempel och länkar till relevant dokumentation.**

---

## Uppgift 1

I denna uppgift så kommer ni bli tilldelad färdig HTML- och CSS-kod, detta innebär att ni endast behöver fokusera på JavaScript-koden i denna uppgift.

Uppgiften går ut på att en användare ska kunna klicka på en av tre stycken knappar. Vid ett klick på en av dessa så kommer en CSS-klass att läggas till på elementet `<div id="message-box">`. Vilken CSS-klass som läggs till beror på vilken knapp som användaren klickade på. Om ni tar en titt på HTML-koden så ser ni att varje knapp har ett eget `id`, det är värdet av detta `id` som ska läggas till som en ny CSS-klass.

Det vill säga, klickar användaren på knappen med `id="success"` så ska CSS-klassen `"success"` läggas till på vår `<div>`. Vilket hade resulterat i `<div id="message-box" class="success">`.

För att lösa detta kommer ni behöva hämta respektive knapp och sedan lägga till en funktion som körs när en användare klickar på knappen.

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

### Del A

I denna uppgift ska ni göra så att när en användare klickar på en knapp så ska en ruta dyka upp (`window.prompt`) där användaren kan fylla i en bit text. Denna text ska sedan sparas som ett nytt list-element i en lista. Utgå från HTML-koden nedan.

``` html
<ul id="items">
    <li>The first item is free!</li>
</ul>

<button type="button" id="add-item">Add item</button>
```

### Del B

Komplettera del **A** med ytterligare en knapp, ni väljer själva ID och knapptext, som raderar det sista elementet i listan varje gång användaren klickar på knappen.

---

## Uppgift 3

I denna uppgift ska ni utgå från HTML-koden nedan. Ni ska göra så att när en användare klickar på en av knapparna med texten "X" så ska list-elementet (där knappen är placerad) raderas.

Det vill säga, klickar jag på knappen "X" i det första list-elementet med texten "This is the first item" så ska hela detta list-element raderas. **Innan det raderas** ska användaren presenteras med en ruta för att godkänna detta (`window.confirm`) för att säkerhetsställa att det var ett aktivt val.

Använd er av variabeln `this` i den funktion som hanterar klick-eventet. Ta då även en titt på attributet `.parentElement`.
{: .info}

HTML
{: .code-header}

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

## Extrauppgift

I denna uppgift kommer ni att arbeta med ett formulär. Detta är en lite större uppgift och är därför indelad i tre delar:

* **A:** Hämta det ifyllda innehållet från formuläret
* **B:** Kontrollera att innehållet är korrekt ifyllt (validering)
* **C:** Ge användaren feedback (genom CSS) om formuläret inte är komplett eller inkorrekt ifyllt

Ni kommer tilldelas färdig HTML för denna uppgiften. Det finns dock ingen CSS-kod och därmed är det inte speciellt användarvänligt, skriv därför lite CSS som ökar användbarheten.

Varje del (A, B, C) är påbyggnader av varandra och bör göras i den ordningen.

HTML
{: .code-header}

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

---

### Extrauppgift: Del A

I del A ska ni hämta det ifyllda formuläret och skriva ut all input i webbkonsolen. Innan vi hämtar allt innehåll behöver vi dock utföra två saker:

1. Hämta hela formuläret och spara det i en variabel (`form`).
2. Lyssna på när användaren skickar formuläret (eventet `submit`) så att vi kan skriva ut all input innan innehållet skickas vidare.

För att förstå hur vi avbryter att formuläret skickare vidare användaren kan ni bejaka exemplet nedan:

preventDefault
{: .code-header}

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

I denna del ska vi skriva ut allt innehåll från formuläret. Detta kommer vi göra i funktionen `onSubmit`. Nyckelordet `this` i denna funktion representerar formuläret och innehåller därför allt innehåll.

Allt innehåll sparas under `this.elements` och respektive fält finns under deras namn från HTML-koden (`name="..."`). Till exempel fältet `<input type="text" name="firstname" />` kommer sparas under `this.elements.firstname` och för att hämta värdet lägger vi till attributet `value`, det vills säga `this.elements.firstname.value`.

Detta fungerar på alla våra fält i formuläret **förutom** våra checkboxar, eftersom där kan användaren välja flera val samtidigt. Det innebär att `this.elements.day` är en lista av respektive checkbox. Eftersom det är en lista kan vi enkelt gå igenom denna med hjälp av en for-loop.

För att kontrollera att en checkbox är vald kan ni kontrollera att attributet `checked` är `true`. Till exempel om vi ska kontrollera den första checkboxen hade vi skrivit `this.elements.day[0].checked`.

---

### Extrauppgift: Del B

I del **B** ska ni nyttja `if`-satser som kontrollerar att respektive fält i förmuläret är korrekt ifyllt (kravlistan finner ni nedan). Skulle alla fälten vara korrekt ifyllda anropar ni `this.submit();` annars skriver ni ut ett kortare felmeddelande i webbkonsolen.

* Förnamn: får endast innehålla `0` till `50` bokstäver
* Efternamn: får endast innehålla `0` till `50` bokstäver
* Ålder: måste vara en `Number` och vara mer än `0`
* Epost: får endast innehålla `0` till `50` bokstäver
* Husdjur: ett husdjur måste vara valt
* Dagar: en dag måste vara vald

---

### Extrauppgift: Del C

I del **C** ska ni påverkat utseende av fälten i formuläret om någonting inte är korrekt ifyllt. Detta görs enklast genom att lägga till en CSS-klass när någonting är inkorrekt ifyllt. Denna CSS-klass kan till exempel ändra bakgrundsfärgen till röd eller någonting annat som fångar användarens uppmärksamhet.

Baserat på den kravlista ni fann i del **B** så ska ni nu även ändra utseendet när ett fällt är inkorrekt ifyllt.

Tänk på att radioknapparna och checkboxarna ligger i varsin `<div>`, det är därför förmodligen enklast att påverka utseendet på den.
{: .info}

---

## Kodexempel

Skapa ett element
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
// Lägg till vårt stycke sist i <body>
body.appendChild(p);
```

Radera ett element
{: .code-header}

``` js
// Vi utgår från följande HTML
// <p id="info">
//     Lite innehåll <a href="google.com" id="link">här.</a>
// </p>

// Hämta de element vi arbetar med
let p = document.getElementById("info");
let a = document.getElementById("link");

// Vi måste utgå från förälder-elementet när vi ska radera
p.removeChild(a);
```

Lyssna på ett event (t.ex. klick)
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

Metoden `addEventListener` tar emot två argument. Det **första** är vilket event det gäller (t.ex. "click") och det **andra** är vilken funktion som ska köras när detta event sker. När detta event sker anropas denna funktion med ett argument (vilket ofta döps till `event`) som innehåller information om eventet.
{: .info}

---

## Dokumentation

Rekommenderad läsning i samband med uppgifterna:

* Funktionerna [alert](https://developer.mozilla.org/en-US/docs/Web/API/Window/alert), [prompt](https://developer.mozilla.org/en-US/docs/Web/API/window/prompt) och [confirm](https://developer.mozilla.org/en-US/docs/Web/API/window/confirm).
* [.addEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener) för att köra en funktion vid ett **event**.
* [document.getElementById](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById) och [document.querySelector](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector) för att antingen hämta ett element baserat på deras ID eller på en CSS-selector.
* [document.createElement](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement) och [document.createTextNode](https://developer.mozilla.org/en-US/docs/Web/API/Document/createTextNode) för att skapa ett element och för att skapa en textnod.
* [.appendChild](https://developer.mozilla.org/en-US/docs/Web/API/Node/appendChild) och [.removeChild](https://developer.mozilla.org/en-US/docs/Web/API/Node/removeChild) för att lägga till ett element i ett annat (eller en textnod) samt för att radera ett element.
* Attributen [.children](https://developer.mozilla.org/en-US/docs/Web/API/ParentNode/children), [.firstElementChild](https://developer.mozilla.org/en-US/docs/Web/API/ParentNode/firstElementChild) och [.lastElementChild](https://developer.mozilla.org/en-US/docs/Web/API/ParentNode/lastElementChild).
