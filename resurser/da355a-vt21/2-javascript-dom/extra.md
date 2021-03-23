---
id: da355a-vt21
title: "2. JavaScript & DOM"
---

# Extra övningar

Vad kul att du hittat hit! Här kommer lite övningar som är bra att träna på när det kommer till JavaScript och DOM. Fråga gärna på laborationstiden om du har något funderingar kring lösningarna!

## Övning 1

I denna uppgiften ska ni skapa en timer med knappar för att starta, stanna och återställa timern. Det räcker med att timern räknar sekunder (inga hundradelar). Denna uppgift använder sig huvudsakligen av funktionen [setInterval](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setInterval) och det rekommenderas att ni läser igenom dokumentationen kort innan ni påbörjar uppgiften.

För att demonstrera funktionen `setInterval` kan ni ta en titt på exemplet nedan. Kort kan vi beskriva `setInterval` som en funktion som tar emot två argument: (1) en funktion som ska upprepas och (2) fördröjningen mellan dessa upprepningar (som anges i millisekunder). Funktionen `setInterval` returnerar ett ID och med detta kan vi avbryta upprepningarna genom funktionen `clearInterval(ID)`.

setInterval
{: .code-header}

``` js
function start() {
    // Tom till att börja med, kommer sedan innehålla vårt ID.
    let intervalID;
    // Kontrollvariabel för antal upprepningar
    let times = 0;
    // Fördröjningen mellan upprepningarna (1sek = 1000ms)
    let delay = 1000;

    function print() {
        times = times + 1;

        if (times > 10) {
            clearInterval(intervalID);
        }

        console.log("It has been run ", times, " times");
    }

    intervalID = setInterval(print, delay);
}
```

Till uppgiften kan ni utgå från följande HTML-mall.

HTML
{: .code-header}

``` html
<div id="timer">
    <p id="seconds">0s</p>
    <button type="button" id="start-timer">Start</button>
    <button type="button" id="stop-timer">Stop</button>
    <button type="button" id="reset-timer">Reset</button>
</div>
```

För att underlätta kommer vi att presentera en lista med ett utgångsförslag. Tänk på att det går att lösa uppgiften på en mängd olika vis.

* Använd er av två variabler: `time` som representerar hur länge vår timer har pågått och `intervalID` som kommer innehålla ID:et för vår intervall-funktion.
* Skapa tre funktioner: `start` som skapar vårt intervall, ökar vår `time` variabel med `1` och ändrar textinnehållet i vår paragraf. `stop` denna raderar endast vårt intervall genom `clearInterval`. `reset` avbryter (med hjälp av `stop`) vårt intervall, återställer vår variabel `time` och återställer texteinnhållet i vår paragraf.
* Applicera dessa tre funktioner till eventet `click` på respektive knapp.

---

## Övning 2

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

### Övning 2: Del A

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

### Övning 2: Del B

I del **B** ska ni nyttja `if`-satser som kontrollerar att respektive fält i förmuläret är korrekt ifyllt (kravlistan finner ni nedan). Skulle alla fälten vara korrekt ifyllda anropar ni `this.submit();` annars skriver ni ut ett kortare felmeddelande i webbkonsolen.

* Förnamn: får endast innehålla `0` till `50` bokstäver
* Efternamn: får endast innehålla `0` till `50` bokstäver
* Ålder: måste vara en `Number` och vara mer än `0`
* Epost: får endast innehålla `0` till `50` bokstäver
* Husdjur: ett husdjur måste vara valt
* Dagar: en dag måste vara vald

---

### Övning 2: Del C

I del **C** ska ni påverkat utseende av fälten i formuläret om någonting inte är korrekt ifyllt. Detta görs enklast genom att lägga till en CSS-klass när någonting är inkorrekt ifyllt. Denna CSS-klass kan till exempel ändra bakgrundsfärgen till röd eller någonting annat som fångar användarens uppmärksamhet.

Baserat på den kravlista ni fann i del **B** så ska ni nu även ändra utseendet när ett fällt är inkorrekt ifyllt.

Tänk på att radioknapparna och checkboxarna ligger i varsin `<div>`, det är därför förmodligen enklast att påverka utseendet på den.
{: .info}
