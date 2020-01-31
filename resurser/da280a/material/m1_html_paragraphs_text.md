---
id: da280a
title: "HTML: Stycken och text"
---

# HTML: stycken och text

## Inledning

När vi skriver någon form av text, dokument eller rapport är det alltid viktigt att tänka på att dela in innehållet i stycken. Detta för att läsaren ska på ett enklare vis kunna ta till sig innehållet och få en bättre översikt. Men även för att logiskt dela in innehållet, ofta är det så att ett stycke står för sig själv. När vi läser en text är det enkelt för oss att lista ut vilken text som hör ihop (för att kunna delas in i stycken) - detta är väldigt svårt för en dator att lista ut på egen hand. Därför är det viktigt att vi är tydliga och gör detta manuellt i HTML för att innehållet ska presenteras på ett korrekt vis.

## Korrekt styckesindelning i HTML

För att skapa ett stycke (eng. paragraph) i HTML så använder vi oss av elementet `<p>`, t.ex:

``` html
<!-- Det första stycket -->
<p>Detta är mitt första, just nu väldigt korta, stycke</p>
<!-- Det andra stycket -->
<p>Detta är mitt andra, just nu väldigt korta, stycke</p>
<!-- Det tredje stycket -->
<p>Detta är mitt tredje, just nu väldigt korta, stycke</p>
```

Pröva ovanstående exempel och notera hur webbläsaren automatiskt lägger luft/yta runt våra stycken, ungefär som att vi skulle skriva ett dokument i ett program som Word eller dylikt.

### Felaktig styckesindelning i HTML

Något som ofta görs felaktigt med HTML är att skapa ett `<p>` element, fylla detta med innehåll, och sedan separera innehållet med `<br>` (radbryt) - vilket utseendemässigt ger oss olika "stycken". Det problematiska med detta är att `<br>` används för att skapa radbryt inom **ett** stycke, inte mellan flera stycken - dvs. att flera stycken **ska** separeras genom flera olika `<p>` element. Ett felaktigt exempel kan se ut på följande vis:

``` html
<!-- Det är tre stycken -->
<p>
    Detta är mitt första, just nu väldigt korta, stycke
    <br>
    <br>
    Detta är mitt andra, just nu väldigt korta, stycke
    <br>
    <br>
    Detta är mitt tredje, just nu väldigt korta, stycke
</p>
```

Om ni pröver exemplet ovan så ser det korrekt ut - dock tolkar datorn detta som **ett** stycke, med radbryt inom sig. Så det gäller att vara nogrann med hur ni väljer att dela in ert innhåll med `<p>` elementen.

## Fetstil och kursiv text

Det händer ofta att man vill göra delar av sin text, eller ord, fetstilta eller kursiva. Det finns olika element för dessa, men i kursen kommer vi att använda följande element för att göra fetstil/kursiv text:

För att markera ut text som fet eller kursiv används två element:

* `<strong>` - fetstil
* `<em>` - kursiv

Exempel på hur detta kan se ut i ett HTML-dokument:

``` html
<!-- Ett stycke med fetstil text -->
<p>
    <strong>
        Här är ett stycket med text i fetstil
    </strong>
</p>

<!-- Ett stycke med ett ord i fetstil -->
<p>
    Här är ett stycket med text i <strong>fetstil</strong>
</p>

<!-- Ett stycke med kursiv text -->
<p>
    <em>
        Här är ett stycket med kursiv text
    </em>
</p>

<!-- Ett stycke med ett kursivt ord -->
<p>
    Här är ett stycket med <em>kursiv</em> text
</p>
```

Pröva gärna exemplet ovan och experimentera!

### Att välja rätt element

*Men jag har läst att det går att använda både `<strong>` och `<b>` för fetstil - hur vet jag vilket jag ska välja?*

Det stämmer att både elementen `<strong>` och `<b>` gör en text fet i en webbläsare. Skillnaden mellan dessa element går djupare än så, kort sagt kan vi beskriva det såhär:

* `<strong>` - används för hur en text/ett ord ska **bli förstått**, alltså ger semantik till texten/ordet. Detta visar sig t.ex. när en text läses upp av en webbläsare (för bla. blinda människor) då `<strong>` indikerar att det ska läggas *tyngd* på meningen/ordet
* `<b>` - används för att formge ett ord, dvs. göra det fetstilt - utseendemässigt (ingen tyngd i sin betydelse). Numera används stilmallar (CSS) för att påverka utseende på HTML - något som kommer presenteras längre fram i kursen

*Men jag har läst att det går att använda både `<em>` och `<i>` för att göra en text kursiv - hur vet jag vad jag ska välja?*

Det stämmer att både elementen `<em>` och `<i>` gör en text kursiv i en webbläsare. Skillanden mellan dessa element går djupare än så, kort sagt kan vi beskriva det såhär:

* `<em>` - används för hur en text/ett ord ska **bli förstått**, alltså ger semantik till texten/ordet. Detta visar sig t.ex. när en text läser upp av en webbläsare (för bla. blinda människor) då `<em>` indikerar att det ska läggas *betoning* på meningen/ordet
* `<i>` - används för att formge ett ord, dvs. göra det kursivt - utseendemässigt (ingen betoning i sin betydelse). Numera används stilmallar (CSS) för att påverka utseende på HTML - något som kommer presenteras längre fram i kursen

