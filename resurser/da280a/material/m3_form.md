---
id: da280a
title: "Formulär"
---

# Formulär

## Inledning

Som du säkerligen lagt märke till när du surfar runt på webben så finns det formulär nästan överallt. På ett eller annat vis vill vi kunna skicka data till eller mellan de olika webbplatser vi besöker. Det kan vara allt ifrån en sökning på via Google (där vi skriver in något sökord i textfältet), inloggningar till diverse webbplatser (där vi skriver in användarnamn och lösenord i textfält) till att kommentera på en webbplats. Nästan överallt finns formulär i olika former för att utföra olika saker - gemensamt är att de är till för att skicka någon form av data.

Vi ska här ta en titt på hur de mest grundläggande delarna av ett formulär fungerar.

## Grunden för ett formulär i HTML

Det finns vissa saker som alltid ska finnas med i ett formulär - de delar som krävs för att formuläret ska fungera på ett korrekt vis. Följande delar är bra att ha koll på:

* Elementet `<form>` (som bestämer vart vårt formulär börjar och slutar)
    * Attributen `action` (vart formuläret ska skickas) och `method` (hur datanskickas i formuläret)
* Elementet `<input>` (som är ett av de element som representerar formulärsfält så som textfält osv.)
    * Attributen `type` (vilken typ av fält, som text, lösenord, osv.), `name` (namnet på vårt element/den data som skickas) och `value` (vissa element bör ha ett värde, så som radioknappar och checkboxar)

Ett grundläggande formulär kan därför se ut på följande vis:

``` html
<form action="server.php" method="get">
    Förnamn: <input type="text" name="firstname">
    Efternamn: <input type="text" name="lastname">
    <input type="submit" value="Skicka">
</form>
```

Från ovanstående formulär kan vi utläsa följande:

* Formuläret kommer skickas till adressen `server.php`
* Formuläret kommer att skicka data med metoden `get`
* Formuläret har två textfält, varpå det första heter `firstname` och det andra `lastname`
* Ett knapp (`type="submit"`) vars innehåll (`value`) är "Skicka", när denna klickas kommer den att skicka att ifyllt i de andra fälten till `server.php`. Observera att det är `type="submit"` som utgör den knapp som skickar ett formulär

Detta kan se ut på följande vis i en webbläsare:

![Formulär 1](../assets/da280a_form_bild1.png)

Skulle vi fylla i formuläret enligt ovan hade vi fått följande:

![Formulär 2](../assets/da280a_form_bild2.png)

Om vi sedan klickar på knappen "Skicka" så kommer vårt innehåll (data) att skickas till `server.php` med metoden `get`.

![Formulär 3](../assets/da280a_form_bild3.png)

Det viktiga att ta med sig från detta är att vi väljer att namnge våra fält (`firstname` och `lastname`) för att den som tar emot datan (det kan vara en annan webbplats/person) ska veta vilken data den tar emot. Dvs. att om bara två namn skickas kan personen som tar emot detta inte veta vilket som är för- och vilket som är efternamn. Med andra ord så när vi namnger våra fält får de någon slags kontext till sitt eget formulär så att den som tar emot datan kan tolka den på ett korrekt vis.

## Testa att skicka data

Nedan finner ni ett formulär där ni kan testa att fylla i innehåll och sedan skicka datan. Er data kommer skickas till en testsida som berättar för er vilken data som skickades med formuläret. Pröva och se därefter vilka namn som är angivna till datan som skickades.

<div id="test-form" style="padding: 20px 20px 30px 20px">
    <form method="get" action="http://dist1.webbintro.se/form_answer.php">
        <p>Namn: <input type="text" name="name"></p>
        <p>Meddelande: <input type="text" name="message"></p>
        <input type="submit" value="Skicka formulär">
    </form>
</div>

Detta är HTML-koden för formuläret:

``` html
<form method="get" action="http://dist1.webbintro.se/form_answer.php">
    <p>Namn: <input type="text" name="name"></p>
    <p>Meddelande: <input type="text" name="message"></p>
    <input type="submit" value="Skicka formulär">
</form>
```

## Metoderna GET och POST

När vi skickar data genom ett formulär så kan vi välja att skicka den på två vis (två metoder):

* `GET` (standard om inget anges)
* `POST`

Kort sagt kan detta beskrivas som att om metoden `GET` används så skickas all informationen genom en URL (dvs. dessa är helt synliga) i jämförelse med `POST` då allt skickas "bakom kulisserna" (dvs. dessa är inte synliga) - dock är de inte hemliga men personer utan någon speciell kunskap kan inte se innehållet. Inget är egentligen mer säkert än de andra men det är två olika sätt att skicka data med för olika ändamål.

Läs mer om detta på [W3Schools](http://www.w3schools.com/tags/ref_httpmethods.asp).
