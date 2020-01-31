---
id: da280a
title: "Indentering av kod"
---

# Indentering av kod

## Introduktion

Med indentering menar vi att vi strukturerar upp vår källkod (HTML) på ett sätt som underlättar för oss människor att läsa koden. Detta kan tyckas vara lite tidskrävande och kanske till och med onödigt just nu i början, speciellt vid mindre HTML-dokument (t.ex mindre än 100 rader) samt att det är endast en själv som läser koden. Försök att tänka er ett större scenario, där ni är ett team på ett antal utvecklare som arbetar med samma HTML-dokument, som dessutom innehåller över 1000 rader kod - då blir det en utmaning för varje person att snabbt kunna läsa och förstå vad koden innebär.

Med "att förstå kod" menar vi här främst - strukturen - på vårt HTML-dokument. Det vill säga vilka HTML-element som befinner sig i andra osv.

### Att tolka HTML

När en dator läser in och tolkar vårt HTML-dokument (koden), för att sedan visa den som en webbplats, så bryr den sig *inte* om indentering (indrag). Den bryr sig endast om i vilken ordning de olika HTML-elementen kommer i och att de är korrekt skrivna (t.ex enligt HTML5-standarden). Med andra ord hade vi kunnat skriva ett HTML-dokument på följande vis:

``` html
<!doctype HTML><html><head><meta charset="utf-8"><title>Testsida</title></head><body><h1>Välkommen till min testsida!</h1><p>... och här är en länk till <a href="http://mah.se">Malmö Högskolas</a> webbplats.</p></body></html>
```

Med detta som utgångspunkt kan vi snabbt se hur svårt det är att läsa igenom denna koden, därmed kan vi dela upp samma HTML-dokument på följande vis:

``` html
<!doctype HTML>
<html>
<head>
<meta charset="utf-8">
<title>Testsida</title>
</head>
<body>
<h1>Välkommen till min testsida!</h1>
<p>... och här är en länk till <a href="http://mah.se">Malmö Högskolas</a> webbplats.</p>
</body>
</html>
```

I ovanstående exempel har vi våra HTML-element på egna rader, vilket gör det mycket enklare att läsa - dock kan vi ta det ytterligare ett steg, genom att **indentera** vår kod på följande vis:

``` html
<!doctype HTML>
<html>
    <head>
        <meta charset="utf-8">
        <title>Testsida</title>
    </head>
    <body>
        <h1>Välkommen till min testsida!</h1>
        <p>... och här är en länk till <a href="http://mah.se">Malmö Högskolas</a> webbplats.</p>
    </body>
</html>
```

Notera att en dator tolkar samtliga av dessa HTML-dokument på samma vis, så utseendemässigt är dessa identiska - dock hoppas jag att ni själv noterar hur mycket enklare det sista exemplet är att tolka jämfört med det första.

I figur 3 kan vi tydligt se genom indenteringen (indragen för de olika elementen) stukturen på dokumentet. Vi kan se att <html>-elementet är det första elementet (så kallat rot-element) och genom indragen kan vi se att <html>-elementet har två barn (element i sig), nämligen elementen <head> och <body>. Detta då dessa två element ligger en nivå (ett indrag) under <html>-elementet (som är dess föräldrar).

För att indentera vår kod kan vi tänka oss att vårt HTML-dokument har någon form av hierarki - som ett träd - där `<html>` är vårt yttersta element. Inuti i detta finner vi två stycken: `<head>` och `<body>` - därför är dessa indenterade ett steg. Vidare har dessa två element egna element också som därmed är indenterade ytterligare ett steg, därefter fortsätter denna processen på samma vis. Med andra ord brukar vi benämna detta som att `<html>` elementet har två "barn" och dessa barn har en "förälder", dessa "barn" (som är på samma nivå) brukar även benämnas som "syskon".

## Hjälpmedel

Det är naturligtvis bäst att själv sköta sin indentering, och därmed även finna den som passar er bäst (vad tycker du är läsbart?). Dock finns det givetvis hjälpmedel online och i vissa textredigare (eng. editors). Ett exempel på ett onlineverktyg är [dirtymarkup](http://dirtymarkup.com) - tänk dock på att oavsett verktyg så **måste** koden validera (vara korrekt skriven) för att ni ska kunna använda dessa hjälpmedel utan problem

Så testa er fram för att se vad ni själva tycker är bäst!
