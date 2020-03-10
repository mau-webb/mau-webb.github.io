---
id: da344a
title: "Laboration 8"
---

# Laboration 8: Geolocation

I denna laboration ska vi titta på hur vi kan använda enhetens GPS för att få den aktuella positionen. Vi kommer göra detta stegvis:

1. Ta reda på information om vår plats.
2. Ta reda på när vi byter plats.
3. Visa hur fort vi rör oss.

[Här finner ni dokumentationen över Geolocation](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation).

---

## Steg 1: Ta reda på information om vår plats

För att ta reda på vår plats (och information om den) så kommer vi använda oss av funktionen `getCurrentPosition`. Alla funktioner relaterade till Geolocation ligger under objektet `navigator`, likt `window` för funktioner som `window.alert` och `window.prompt`.

Funktionen `getCurrentPosition` tar emot tre stycken argument, en funktion för när vi lyckades hitta vår position, en funktion för när vi inte lyckades och slutligen ett objekt innehållande ett gäng inställningar.

För att ni ska kunna experimentera med detta kan ni utgå från följande mall.

getCurrentPosition
{: .code-header}

``` js
// Vi kommer fylla på denna i steg 2.
let options = {};

function success(position) {
    // Ta en titt i er webbkonsol och se vad den innehåller.
    console.log("This is our position: ", position);
}

function error(err) {
    console.warn("Something went wrong: ", err.message);
}

// Skicka med våra funktioner och inställningar,
// dessa kommer sedan anropas när en position försöker fastställas.
navigator.geolocation.getCurrentPosition(success, error, options);
```

Pröva den ovanstående koden på en grundläggande HTML-sida och kolla i er webbkonsol.

* Vilka egenskaper har objektet `position`?
* Vilka värden kan ni få ut kring er position från objektet `coords`?

Skriv ut en del av denna informationen i er HTML, något i stil med:

![exempel 1](../images/geo1.jpg) _Steg 1._

---

## Steg 2: Ta reda på när vi byter plats

För att uppdatera vår position medan vi rör oss använder vi funktionen `watchPosition`. Denna tar emot samma argument som `getCurrentPosition` men returnerar även oss ett ID som vi kan använda oss av för att avbryta det hela (precis som med `setInterval`).

Nu kommer vi även att inkludera lite inställningar till detta anrop så ta en titt på exemplet nedan.

watchPosition
{: .code-header}

``` js
let options = {
    // Försök tvinga enheten till en så precis position som möjligt
    enableHighAccuracy: true,
    // Maximal tid i millisekunder som enheten har på sig att ge oss en position
    timeout: 5000,
    // Hur länge vår position får tillfälligt lagras (millisekunder)
    maximumAge: 0
};

function success(position) {
    // Ta en titt i er webbkonsol och se vad den innehåller.
    console.log("This is our position: ", position);
}

function error(err) {
    console.warn("Something went wrong: ", err.message);
}

// Skicka med våra funktioner och inställningar,
// dessa kommer sedan anropas kontinuerligt medan vi rör på oss.
let watchID = navigator.geolocation.watchPosition(success, error, options);

// Skulle vi sedan vilja avbryta detta hade vi anropat `clearWatch`
navigator.geolocation.clearWatch(watchID);
```

Pröva nu även denna ovanstående kod och skriv även ut resultatet på er HTML-sida.

![exempel 2](../images/geo2.png) _Steg 2._

Här gör Anton en liten sprint utanför Gäddan och rör sig i cirka 4.8m/s (drygt 17km/h) - tro det eller ej!

Nu är det er tur att se hur ni rör er!

---

## Steg 3: Visa hur fort vi rör oss

Ni ska i den sista delen berätta för användaren hur snabbt dom rör på sig och ge feedback genom olika färger.

* Röd = Långsamt (< 5km/h)
* Gul = Mellan (> 5km/h, < 10km/h)
* Grön = Snabbt (> 10km/h)

Tänk på att ni får tillbaka hastigheten i *meter per sekund*, men vi vill för användaren visa hastigheten som *km per timme*. Använd följande formel för att åstadkomma detta:

```
1 meter per sekund = 3.6 kilometer per timme
```

Nu ska ni visa upp resultatet i stil med:

![exempel 3](../images/geo3.jpg) _Steg 3._

När ni fått det att fungera **så gå ut en sväng och testa!** Att sitta inomhus gör att precisionen blir så låg att den data ni får blir ganska oanvändbar.
