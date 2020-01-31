---
id: da280a
title: "Övning 2 - Text (stycken, rubriker, listor, m.m.)"
---

# Övning 2 - Text (stycken, rubriker, listor, m.m.)

## Restaurang Vegano

I de kommande övningarna har vi fått i uppdrag att skissa upp en webbplats åt en påtagligt påhittad restaurang vid namnet Vegano. Som du säkert förstått vi det här laget används HTML för att strukturera upp en webbplats innehåll, t.ex. vilken ordning rubrikerna kommer i och när listor ska dyka upp osv. Detta är inte mycket olikt hur vi strukturerar upp ett Word-dokument. Estetiken och utseendet på webbplatsen kommer senare så det behöver vi inte oroa oss för nu.

Restaurangen har önskat att följande text ska finnas på webbplatsen:

* Titel för webbplatsen som syns i webbläsarfliken
* En huvudrubrik med restaurangens namn, samt en underrubrik för deras slogan
* En kortare presentation av restaurangen
* En menylista över deras lunchalternativ

## Titel i webbläsarfliken

För att komma igång behöver vi sätta upp en grundläggande struktur i vårt HTML-dokument. Kommer du ihåg vilka delar ett HTML-dokument brukar delas in i? Vi ska börja med det första, nämligen sidhuvudet (eng. head) och detta bör ligga längst upp i vårt dokument. Eftersom sidhuvudet innehåller information om dokumentet (s.k. meta-data) så är det även här vi sätter in titeln som webbläsaren kan läsa av och placera i fliken högst upp.

``` html
<!doctype html>
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <!-- ... -->
```

Med ovanstående struktur ska du nu kunna skriva in titeln på dokumentet. Vad sägs om - "Restaurang Vegano"? eller, "Godast mat i södern"? Ordet är fritt - du bestämmer. Om du skrivit rätt i din HTML-kod kommer titeln dyka upp i webbläsarfliken.

## Rubriker

Nu när vi fått ordning på informationen om dokumentet i fråga ska vi börja med det inledande innehållet. Vi har nu gått ner från sidhuvudet och ska börja arbeta med kroppen (eng. body). Det är här vi kommer placera vårt innehåll.

``` html
<!doctype html>
<html>
    <head>
        <title></title>
    </head>
    <body>
    </body>
</html>
```

Försök nu placera in en passande rubrik samt en underrubrik (slogan) i kroppen (body) - tänk på att storleken på rubrikerna bestäms i ordningen 1 (störst) till 6 (minst).

``` html
<h1><h2><h3><h4><h5><h6>
```

## Presentation och stycken

iFörhoppningsvis sitter rubriken på plats! Nu är det dags att skriva en presentation och placera den i rätt ordning. Restaurangen har önskat en egen presentation, men du får gärna strunta i vad de tycker och skriva en bättre om du önskar. Använd paragraf-taggar för presentationen!

Förhoppnignsvis sitter nu rubriken på plats! Nu är det dags att skriva en presentation av restaurangen och placera den i rätt ordning. Restaurangen har önskat en egen presentation, men du får gärna strunta i vad de tycker och skriva något bättre om du så önskar. Använd elementet för stycken till presentationen!

``` html
<p></p>
```

*"Vegano erbjuder helekologisk och vegetarisk lunchbuffé för endast 69 kronor. Under kvällstid har du som gäst möjlighet att boka ett Vin & Vego-bord med säsongsbetonad meny med passande viner till. Vi är belägna på Vildmåsvägen 111 i Lund, välkomna! Vår lunchmeny finner ni nedan."*

## Menylista

Slutligen vill restaurangen att en del av deras lunchmeny ska finnas tillgänglig. Uppdelningen bör vara i rubriker med kalla och varma rätter med varsin punktad lista.

De kalla rätterna ska vara pasta romano, broccolipaj och vegetarisk pastrami. De varma rätterna ska vara svamprisotto, ärtlasagne och pasta arrabiata.

``` html
<ul>
    <li></li>
    <li></li>
    <li></li>
</ul>
```

Har du klarat detta är du på god väg att ha skapat din första hemsida à 1998 style! Oroa dig inte, det kommer bli bättre med tiden. Resultatet än så länge [bör se ut ungefär såhär](../assets/da280a_ex2_bild1.png).
