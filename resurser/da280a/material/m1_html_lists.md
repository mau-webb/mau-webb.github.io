---
id: da280a
title: "HTML: Listor"
---

# HTML: listor

## Inledning

Att skapa en lista av information är ett smidigt sätt att gruppera och strukturera någon form av innehåll. Ibland vill vi skapa listor utan inbördes ordning (icke-ordnade listor) och ibland med numrering (ordnade listor). Vi ska nedan ta en titt på hur detta görs med HTML.

## List-elementets uppbyggnad

En lista i HTML innebär alltid minst två element. Det första bestämmer typen av listan, dvs. en icke-ordnad lista `<ul>` eller en ordnad lista `<ol>`. Det andra elementet är det element som används för att representera en punkt i en av dessa listor och detta görs med `<li>` (eng. list item), dvs. en punkt i listan. 

En icke-ordnad lista kan se ut på följande vis:

``` html
<!-- En oordnad lista med tre punkter -->
<ul>
    <li>Första punkten</li>
    <li>Andra punkten</li>
    <li>Tredje punkten</li>
</ul>
```

Observera här hur vi använder kombinationen av `<ul>`, som bestämmer typen av listan, och `<li>` som representerar varje individuell punkt i vår lista. Inuti i `<li>` kan vi dessutom fylla på med en massa olika typer av information och HTML-element som bilder, länkar, m.m.

En ordnad lista kan se ut på följande vis:

``` html
<!-- En ordnad lista med tre punkter -->
<ol>
    <li>Första punkten</li>
    <li>Andra punkten</li>
    <li>Tredje punkten</li>
</ol>
```

Notera att innehållsmässigt ser denna listan ut som tidigare lista med en skillnad - det yttre elementet `<ol>`, som återigen besämmer vilken typ av lista det är vi vill göra.

## Nästlade listor

Det går utmärkt att ha "listor i listor", alltså nästlade listor genom HTML. Detta kan i början vara lite småknepigt, då nästlade element lätt blir förvirrade om man inte är van vid en större mängd HTML-kod.

Det går till och med utmärkt att ha "listor i listor", dvs. en underlista - detta kallas även för nästlade listor. Detta kan anses vara en aning krångligt men i praktiken är det inte så svårt. Det gäller bara att placera din "underlista" på rätt plats i din huvudlista - för att förenkla så kan ni ta en titt på exemplet nedan:

``` html
<!-- En ordnad nästlad lista -->
<ol>
    <li>Första punkten
        <!-- En ordnad underlista till "Första punkten" -->
        <ol>
            <li>Första underpunkten</li>
            <li>Andra underpunkten</li>
            <li>Tredje underpunkten</li>
        </ol>
    </li>
    <li>Andra punkten
        <!-- En ordnad underlista till "Andra punkten" -->
        <ol>
            <li>Första underpunkten</li>
            <li>Andra underpunkten</li>
            <li>Tredje underpunkten</li>
        </ol>
    </li>
    <li>Tredje punkten
        <!-- En ordnad underlista till "Tredje punkten" -->
        <ol>
            <li>Första underpunkten</li>
            <li>Andra underpunkten</li>
            <li>Tredje underpunkten</li>
        </ol>
    </li>
</ol>
```

Pröva gärna exemplet och experimentera - försök att förstå hur underlistor fungerar och uppskatta även vikten av att vi indenterar koden korrekt här (det är lätt att det blir *väldigt* svårt att läsa av en lista annars).
