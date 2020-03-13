---
id: me152a
title: "API Mashup"
---

# Uppgift 2: API Mashup

Syfte med uppgiften:

* att öva på att arbeta med AJAX.
* att öva på att arbeta med API:er.
* att öva på att använda externa bibliotek.
* att öva på att ta fram en idé för en tjänst och sedan implementera den tekniskt och grafiskt.

Inlämning sker i form av en zippad mapp innehållande

* en HTML-fil.
* en CSS-fil.
* en JavaScript-fil.

Uppgiften **ska** genomföras individuellt.
{: .warn}

---

## Uppgiftsbeskrivning

I denna uppgift ska ni skapa en så kallad *API Mashup*, det vill säga kombinera två eller flera API:er till **en** tjänst. Utöver att lösa uppgiften rent tekniskt ska ni även inkludera ett textavsnitt på er tjänst som beskriver er idé, vilka API:er ni valt och vilka lärdomar ni tar med er efter att arbetat med dessa. 

Vad är en *API Mashup*? Kort är det kombinationen av flera API:er till en tjänst, vilket kan vara näst in till vad som helst. För att ge er några exempel (som ni inte ska basera er mashup på):

* En tjänst som ger användaren tips på spellistor från spotify baserat på dagens väderlek.
* En tjänst som är ett quiz (spel) där användaren får utdrag från wikipedia om en huvudstad och ska sedan placera en nål på en världskarta där staden finns.
* En tjänst där låttexter spelas upp med en text-to-speech och användaren ska gissa vilken låt det gäller.
* En tjänst där användaren kan söka på ett ord och betydelsen presenteras från en ordbok i kombination med giffar (.gif) baserat på ordet.

Det är egentligen bara er egen fantasi och tillgängliga API:er som sätter er begränsning. För att hitta intressanta API:er att arbeta med kan ni ta en titt på följande sidor:

* [https://github.com/public-apis/public-apis](https://github.com/public-apis/public-apis)
* [https://any-api.com](https://any-api.com)

Tänk på att först tänka er en idé och kolla sedan om det finns API:er för att genomföra idén. Var noga med att läsa igenom dokumentationen för det API ni valt så ni vet om datan finns som ni behöver eller inte.

Er tjänst måste också innehålla CSS som gör den någorlunda användbar, det ska alltså kännas som en tjänst och inte en *exempelsida* eller dylikt. Slutligen måste ni använda er av minst ett externt bibliotek, till exempel jQuery, Axios, Anime.js, Chart.js - en sökning på Google kommer ge er en uppsjö av alternativ (baserat på vad ni behöver)

---

## Kravspecifikation

* Alla era variabler **ska** ha tydliga och relevanta namn. Det vill säga inte något i form av `let abc = ...`.
* Alla funktioner **ska** dokumenteras med en kommentar som beskriver **vad syftet är**, **vilka argument den tar emot** och **vad den returnerar**.
* Ni ska använda **minst** två stycken API:er.
* Ni ska använda **minst** ett externt bibliotek (t.ex. jQuery, Axios, Anime.js, popper.js, chart.js, m.m.).
* Er tjänst ska innehålla ett avslutande textavsnitt som beskriver er idé, vilka API:er ni valt och vilka lärdomar ni tar med er efter att arbetat med dessa.
* Tjänsten ska vara funktionell och användbar vad gäller både det tekniska och det grafiska.

All kod ska godkännas av [JSHint](https://jshint.com/) **och** genomgå [Beautifier](https://beautifier.io/) (eller något likvärdigt).
{: .info}
