---
id: da280a
title: "Inlämningsuppgift 3"
---

# Inlämningsuppgift 3

Betyg: U/G

## Inledning

I den tredje inlämningsuppgiften ska vi fokusera på att göra ett formulär i HTML. Vi kommer att använda oss av olika element för ett formulär t.ex. textfält, checkboxar, radioknappar m.m. Vi kommer även att använda oss funktioner (attribut) från HTML5 så som "placeholders" (text som syns innan fältet är ifyllt) för textfält och validering av formulärsdata.

## Syfte

Syftet med den tredje uppgiften är att ni ska behärska formulär i HTML med olika typer av fält (text, knappar, dropdown-menyer, m.m.) för att samla in data från en besökare. I denna uppgift kommer vi endast fokusera på gränsnittet mot besökaren (dvs. formuläret) och inte vad som sker efter att en besökare skickar datan vidare, t.ex. till en server som sparar den eller dylikt.

## Uppgift

Ni har fått ett uppdrag om att göra ett formulär till tidningen Blomstermålabladet. Denna tidningens anställda är nyfikna på vem som besöker deras webbplats och vad dessa tycker om webbplatsen, men även vilka delar som besöks mest. Dessutom vill de ge besökarena som svarar på formuläret möjligheten till att vinna en T-shirt om de fyller i sin epost och vad de tycker om webbplatsen.

Detta innebär att er uppgift är att bygga ett formulär för detta ändamål. Hur formuläret bör se ut när det är färdigt är [något i stil med följande](../material/assets/da280a_inl3_form.png).
**Formuläret ska bestå av följande delar:**

1. Kontaktuppgifter
    * Namn (får innehålla text)
    * Ålder (får endast innehålla siffror)
2. Dina besök på blomstermålabladet
    * Hur ofta besöker du blomstermålabladet?
        * Varje dag (radioknapp)
        * Varannan dag (radioknapp)
        * Varje vecka (radioknapp)
    * Vilka delar av blomstermålabladet brukar du besöka?
        * Nyheter (checkbox)
        * Utrikes (checkbox)
        * Inrikes (checkbox)
        * Sport (checkbox)
        * Skvaller (checkbox)
        * Väder (checkbox)
        * Övrigt (checkbox)
3. Vinn en T-shirt!
    * Bästa med blomstermålabladet (textfält)
    * Sämsta med blomstermålabladet (textfält)
    * Epost (måste vara en korrekt epost)
    * Storlek (dropdown-menyn, med "M" förvalt), med följande alternativ (i denna ordning):
        1. XS
        2. S
        3. M
        4. L
        5. XL
4. Skicka/återställ
    * Skicka (knapp som skickar formuläret)
    * Återställ (knapp som återställer formuläret)

Följande fält **måste** fyllas i innan det får skickas:

* Namn
* Ålder
* Ett av alternativen under "Hur ofta besöker du blomstermålabladet?"

Varje del av formuläret (de delar som har en ram runt sig i bilden) ska vara i form av ett `<fieldset>` med tillhörande `<legend>`.

Formuläret ska sedan skickas (när besökaren klickar på "skicka") till följande adress: `http://webshare.mah.se/tszagh/response.php` med metoden `GET`. Den sidan kommer att tolka den data som ni skickar och sedan skriva ut den. Så att ni kan se att ert formulär skickar korrekt data.

[Ett exempel på hur detta ser ut kan ni ser här.](../material/assets/da280a_inl3_data.png)

**Tips**

* [Här finner ni en lista med olika typer av textfält](http://www.w3schools.com/tags/att_input_type.asp)
* [Information om att ange att ett fält måste vara i fyllt](http://www.w3schools.com/tags/att_input_required.asp)
* [En beskrivning av textfält](http://www.w3schools.com/tags/att_input_placeholder.asp)
* Tänk på att de nya funktionerna från HTML5 (t.ex "placeholder", "email", osv.) bara fungerar i moderna webbläsare - vilket vi är medvetna om i denna uppgiften

## Kravspecifikation

**Följande krav ställs på er kod:**

* Valideras genom [W3C's valideringsverktyg](http://validator.w3.org) - koden **måste** därför vara felfri
* Korrekt struktur i form av indentering (indrag)
* Dokumentation i form av kommentarer
* Korrekt användning av HTML-element för de olika typerna av information som ni har på er sida

**Följande krav ställs på uppgiften:**

* Formuläret måste innehålla alla de delar som beskrivs i uppgiften
* Varje del (sektion) av formuläret måste utformas med hjälp av `<fieldset>` tillsammans med `<legend>`
* Fälten "namn", "ålder" och "Hur ofta besöker du blomstermålabladet?" måste vara ifyllda
* Fältet "ålder" får endast innehålla siffror
* Fältet "epost" får endast innehålla en korrekt epsot
* Fältet "storlek" ska vara förifyllt med alternativet "M", men samtidigt lista de andra alternativen i ordningen: XS, S, M, L, XL
* Formuläret ska skicka besökaren till följande adress `http://webshare.mah.se/tszagh/response.php` med metoden `GET`
* Knappen "återställ" ska återställa (nollställa) formuläret
* HTML-attributet `name` **måste** användas på samtliga formulärsfält (dvs. textfält, radioknapp, osv.)

Kvalitén på er kod kommer även att bedömas.

## Inlämning

*Glöm inte att kontrollera alla kraven innan du lämnar in din uppgift.*

När du är färdig med din uppgift ska du ladda upp **en** `.zip` fil innehållande alla dina filer på Canvas. Du ska även publicera din lösning på webshare och bifoga en länk till er sida i kommentarsfältet på Canvas vid inlämning.

Lycka till!
