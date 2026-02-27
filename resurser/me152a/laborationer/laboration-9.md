---
id: me152a
title: "Laboration 9"
---

# Laboration 9

Syfte med laborationen:

* att öva på att använda funktionen `fetch` för att hämta data.
* att fortsätta öva på att använda Document Object Model (DOM).

Inlämning sker i form av en zippad mapp innehållande

* en HTML-fil.
* en JavaScript-fil.
* lösningar på **Uppgifter** i JavaScript-filen.

All kod ska godkännas av [JSHint](https://jshint.com/).
{: .info}

---

## Fetch

Den inbyggda funktionen `fetch` används för att både hämta och skicka data. I denna laboration kommer vi endast utgå från att hämta data, för att sedan visa resultatet i form av HTML. Vi kommer därför använda oss av två stycken API:er för att öva på detta. Ett API (inom ramen för denna laboration) kan kort beskrivas som en tjänst som tillhandahåller data som vi kan hämta genom en eller flera URL:er, även kallade *endpoints*. 

I **uppgift 1** kommer ni att använda er av ett API som heter "Dog API" och ger oss möjlighet att hämta hundbilder i olika varianter och i **uppgift 2** kommer ni använda er av ett API som heter "Random user" som tillhandahåller fiktiva användare (tänk "Lorem ipsum" fast för användardata).

### Hur fungerar fetch?

Funktionen `fetch` är en funktion som returnerar ett objekt till oss, där detta objekt i sin tur har funktioner vilket innebär att vi kommer skapa en sk. kedja av funktionsanrop. Detta låter klurigare än vad det är, dock kräver det att ni är nogranna med att strukturera er kod på grund av detta.

Nedan visas ett exempel där vi nyttjar ett API ([Svenska Dagar](https://api.dryg.net/)) som ger oss data om namnsdagar, om det är en röd dag, m.m.

Exempel: funktionen fetch
{: .code-header}

``` js
// Strukturen för att använda sig av Fetch kan ses som på följande vis:

// 1. Ange URL/Adress/Endpoints
// 2. Ange en funktion som konverterar den data vi hämtar till JSON,
//    dvs. vi får ett JavaScript-objekt att arbeta med 
// 3. Gör sedan någonting med detta objekt, t.ex. logga ut det i konsollen
// 4. (Valfritt) Ange en funktion som körs när någonting går fel

fetch("https://api.dryg.net/dagar/v2.1/2019/03/18") // 1.
    .then(convertToJSON) // 2.
    .then(logResult) // 3.
    .catch(onError) // 4.

// Vi hade kunnat skapa dessa funktioner på följande vis:
// Notera att funktionerna som placeras inom "then()" blir
// alltid anropade med resultatet av förfrågan mot API:et

// Resultatet från "fetch" har en funktion som konverterar 
// datan till JSON
function convertToJSON(result) {
    console.log(result);
    return result.json();
}

// Vi kan enkelt logga ut det i konsollen för att se vad det innehåller
function logResult(result) {
    console.log(result);
}

// När någonting går fel anropas denna funktionen och vi skriver ut
// ett mindre felmeddelande samt loggar ut ett objekt som innehåller
// information om vad som just gick fel
function onError(error) {
    console.log("Oops! something went wrong.", error);
}
```

Baserat på ovanstående exempel hade vi kunnat modifiera funktionen `logResult` så att den istället till exempel skapat en paragraf `<p>` innehållande de som har namnsdag, eller vad vi annars hade tyckt varit lämpligt baserat på den data vi fått.

I uppgifterna nedan rekommenderas det att pröva att besöka respektive API:s endpoint (URL) för att se vilken data ni får tillbaka, det vill säga klistra in URL:en i adressfältet i er webbläsare. Firefox formaterar datan på ett läsvänligt vis.
{: .info}

---

## Uppgift 1

**Endpoint:** `https://dog.ceo/api/breeds/image/random` ([Dog Api](https://dog.ceo/dog-api/documentation/random))

Ni ska i den första uppgiften skapa en knapp och när en användare klickar på denna ska ni hämta en slumpad hundbild och sedan visa denna på er sida.

Använd CSS för att göra gränssnittet någorlunda användarvänligt.

---

## Uppgift 2

**Endpoint:** `https://randomuser.me/api/?results=10` ([Random User](https://randomuser.me/documentation#results))

Ni ska i den andra uppgiften skapa en knapp och när en användare klickar på denna ska ni **hämta 10 stycken** fiktiva användare och visa dessa på er sida. Vilken data om respektive användare ni ska visa är upp till er själva men ni ska nyttja **minst 5 stycken** attribut.

Använd CSS för att göra gränssnittet någorlunda användarvänligt.
