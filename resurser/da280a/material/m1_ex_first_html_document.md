---
id: da280a
title: "Övning 1 - Ett första HTML-dokument"
---

# Övning 1 - Ett första HTML-dokument

## HTML-dokument

Ett HTML-dokument kan huvudsakligen delas in i två delar:

1. Sidhuvud med information om HTML-dokumentet, s.k. meta-data
2. Kropp med den information som ska visas för besökaren

Skapa ett tomt HTML-dokument, du kan utgå från följande mall:

``` html
<html>
    <head>
        <title>Här är titeln på sidan</title>
    </head>
    <body>
        <p>Här har vi sidans innehåll</p>
    </body>
</html>
```

När du skapat ditt HTML-dokument med ovanstående HTML-kod. Testa att öppna HTML-dokumentet i en webbläsare. Såg det ut som du förväntade dig?

När du skapat ditt HTML-dokument utifrån ovanstående mall - testa att öppna dokumentet i en valfri webbläsare. Såg det ut som du förväntade dig?

* Var någonstans på sidan visas `<title>` elementet?
* Var någonstans på sidan visas innehållet i `<body>` elementet?

Testa nu att ändra texten både i titeln för dokumentet och i kroppen för dokumentet, fungerar det som du förväntat dig?

## Innehåll genom HTML

Det är genom ett "element" som vi kan märka upp text så det innehållet får den strukturen vi vill ha (alt. presenteras på det vis vi vill). Vi ska i del 2 av denna övningen lägga till lite mer innehåll på vår sida - inte bara meningen "här har vi sidans innehåll".

Om ni tar [en titt på denna bilden](../assets/da280a_ex1_bild1.png) så kan ni se hur ett element är uppbyggt.

* Start- och sluttagg: ett element har en början (starttagg) och ett slut (sluttagg) för att kunna välja vart det innehåll vi vill markera upp börjar och slutar (t.ex vart en rubrik börjar och slutar). I exemplet ovan har vi en `<h1>` (huvudrubrik). Det innebär att den text inom start- och sluttaggen kommer visas som en huvudrubrik i vårt dokument. Hade vi exempelvis använt oss utav `<p>` istället hade innehållet presenterats som ett stycke
* Formatkod: Detta är namnet på det element vi vill skapa - dvs. hur det innehåll vi har märkt upp kommer att visas i en webbläsare, t.ex `<p>`, `<h1>`, `<b>`, m.m.
* Innehåll: är den del mellan start- och sluttaggarna som vi vill visa för en besökare 

Din uppgift är nu att lägga till mer innehåll i ditt HTML-dokument, nedan visas en lista av vilka element som ska användas (vad du väljer för innehåll är valfritt):

* En huvudrubrik, `<h1>` - [läs mer här](/resurser/da280a/material/m1_html_headings/)
* Två stycken, `<p>` - [läs mer här](/resurser/da280a/material/m1_html_paragraphs_text/)
* En underrubrik, `<h2>` - [läs mer här](/resurser/da280a/material/m1_html_headings/)
* En bild, `<img>` - [läs mer här](/resurser/da280a/material/m1_html_images/)
* En länk, `<a>` - [läs mer här](/resurser/da280a/material/m1_html_links/)

För att se hur du skapar dessa olika element kan du titta på deras förläsningar som är länkade till.

För att se [ett exempel kan ni klicka här](../assets/da280a_ex1_bild2.png).

## Validering av HTML-kod

Nu är det dags att validera ert HTML-dokument, dvs. kontrollera att allt är korrekt. Detta är väldigt viktigt för att upptäcka fel och för att se så att ni förhåller er till de regler kring HTML som finns. Det finns flera anledningar till detta:

* Det skapar kvalité på er kod
* Webbplatsen kommer att visas korrekt i en webbläsare
* Om ni är ett team som arbetar på samma webbplats är det viktigt att alla förhåller sig till samma regler

Ni [validerar er kod på denna sidan](http://validator.w3.org). Här kan ni välja att validera er kod på tre olika sätt:

1. Genom att ange en länk till er webbplats. Observera att detta går bara om ni tillgängliggjort er webbplats på webben (t.ex genom dvwebb)
2. Genom att ladda upp ert HTML-dokument
3. Genom att kopiera och klistra in er HTML-kod i en text-ruta - detta brukar vara det enklaste alternativet.

Vilken metod ni väljer spelar ingen större roll, dock rekommenderas alternativ tre då det är enklast.

Efter ni validerat er kod kommer ni få ett svar om koden är korrekt eller inte. Om koden inte är helt korrekt kommer ni dessutom få olika meddelanden som försöker berätta vad som är fel - här är det viktigt att försöka lösa ett problem i taget. Detta då ett problem kan ge uppkomst till flera andra (tänk er ett vattenfall av fel) - så börja med det första felet och arbeta av dessa allt eftersom.

Lycka till!
