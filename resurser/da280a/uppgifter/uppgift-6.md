---
id: da280a
title: "Inlämningsuppgift 6"
---

# Inlämningsuppgift 6

Betyg: U/G

## Inledning

I den sista inlämningsuppgiften ska vi fortsätta att arbeta med layouter för webbplatser. Vi ska nu, utöver att titta på den övrgripande layouten även fokusera på att prsentera text tillsammans med bilder. Dessutom ska vi även ta en titt på hur vi kan mobilanpassa våra webbplatser (grundläggande).

## Syfte

Syftet med den sista uppgiften är att vidare utöka våra kunskaper kring layoutskapande för webbplatser, men med ett större fokus på innehåll och anpassning mot olika enheter.

## Uppgift

Denna uppgift går ut på att ni ska skapa en sida som [följer denna mallen](../material/assets/da280a_inl6_bild1.jpg) (temat är dock valfritt, inget krav att ni använder just Star Wars-temat som i detta fallet).

Denna bilden visar strukturen (layouten) för er webbplats, dvs. inte exakt hur den ska se ut (dock med ett förvalt tema för att förtydliga). Det innebär att ni själva får välja vilka färger, typsnitt, m.m. som ni vill använda er av för att göra webbplatsen tilltalande - tänk på att välja ett tema så utseendet är konsekvent. **Dock** måste alla delar (komponenter) som återfinns i bilden finnas med på er webbplats.

[Här finner ni en lite mer detaljerad beskrivning av de olika delarna.](../material/assets/da280a_inl6_bild2.jpg)

Länkarna i menyn behöver inte leda någonstans, men de måste utformas med elementet: `<a>`.

För att göra sidan mer responsiv (dvs. mobilanpassa, eller enhetsanpassa) så ska den [se ut på följande vis](../material/assets/da280a_inl6_bild3.jpg) när vi besöker den via en mobiltelefon (tips: ni kan dra ihop webbläsar fönstret för att snabbt testa också). Som ni kan se så finns alla element förutom logotypen med i mobilversionen av vår webbplats.

Nedan finner ni en lista över innehållet på webbplatsen:

**Om vi besöker webbplatsen genom en dator:**

* En vänsterkolumn
    * Logotyp
    * Meny
* En huvudkolumn
    * Huvudrubrik
    * Tre bilder med tillhörande bildtext
    * Två stycken avgränsningslinjer
    * Ett avsnitt med text tillsammans med en bild till höger
    * En sidfot

**Om vi besöker webbplatsen med en mobil:**

* En vänsterkolumn (som nu ligger *ovanför* innehållet)
    * Meny
* En huvudkolumn (som nu ligger *under* menyn)
    * Huvudrubrik
    * Tre bilder med tillhörande bildtext
    * Två stycken avgränsningslinjer
    * Ett avsnitt med text tillsammans med en bild till höger
    * En sidfot

Detta löser ni genom något som kallas för "media queries", dessa gör att vi kan ange att för en viss skärmupplösning (tänk storlek/bredd) så kommer vissa CSS-regler att gälla (alt. aktiveras). Mer [information om detta finner ni här](http://www.w3schools.com/cssref/css3_pr_mediaquery.asp).

## Kravspecifikation

**Följande krav ställs på er kod:**

* Valideras genom [W3C's valideringsverktyg](http://validator.w3.org) - koden **måste** därför vara felfri
* Korrekt struktur i form av indentering (indrag)
* Dokumentation i form av kommentarer
* Korrekt användning av HTML-element för de olika typerna av information som ni har på er sida (tänk på de semantiska elementen från HTML5)

**Följande krav ställs på uppgiften:**

* Webbplatsen måste följa den beskrivning som återfinns i uppgiftsbeskrivningen vad gäller innehåll och visuell utformning
* Webbplatsen måste använda sig av **en** CSS-fil, denna måste även vara extern dvs. **inte** "inline"
* Webbplatsens innehåll ska styra höjden, dvs. ni får inte ha en fast höjd på innehållet genom CSS

Kvalitén på er kod kommer även att bedömas.

## Inlämning

*Glöm inte att kontrollera alla kraven innan du lämnar in din uppgift.*

När du är färdig med din uppgift ska du ladda upp **en** `.zip` fil innehållande alla dina filer på Canvas. Du ska även publicera din lösning på webshare och bifoga en länk till er sida i kommentarsfältet på Canvas vid inlämning.

Lycka till!
