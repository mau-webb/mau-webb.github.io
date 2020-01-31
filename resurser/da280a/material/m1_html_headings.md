---
id: da280a
title: "HTML: Rubriker"
---

# HTML: rubriker

## Inledning

Rubriker är något vanligt förekommande när vi författar text-dokument. Därför blir det genast viktigt att veta hur vi hanterar rubriker i ett HTML-dokument. Den grundläggande regeln är att ju större rubriken är desto viktigare är den. Utöver detta är det också viktigt att kunna strukturera upp sina rubriker i huvudrubriker och underrubriker för att göra ett dokument mer överskådligt. I HTML-standarden finns det sex nivåer (storlekar) av rubriker - från 1 (störst) till 6 (minst).

## Olika nivåer av rubriker

För att skriva en rubrik i HTML använder vi dessa element:

``` html
<!-- Den största rubriken -->
<h1>Rubrik 1</h1>
<!-- Den näst största rubriken -->
<h2>Rubrik 2</h2>
<!-- Den tredje största rubriken -->
<h3>Rubrik 3</h3>
<!-- Den fjärde största rubriken -->
<h4>Rubrik 4</h4>
<!-- Den femte största rubriken -->
<h5>Rubrik 5</h5>
<!-- Den sjätte största rubriken -->
<h6>Rubrik 6</h6>
```

Där bokstaven "h" är en förkortning för "heading", dvs. rubrik.

Pröva gärna exemplet för att se hur dessa ser ut i en webbläsare - notera de automatiska storlekarna beroende på vilken nivå av rubrik som används.

Det är sedan upp till er själva att välja rätt rubriknivå till ert innehåll - en tumregel är att alltid använda `<h1>` för huvudbriken på er webbplats, därefter går ni ner i nivåerna. Detta bla. för att sökmotorer (Google, osv.) tar hänsyn till vilka rubriknivåer ni använder.
