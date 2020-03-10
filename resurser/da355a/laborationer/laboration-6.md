---
id: da355a
title: "Laboration 6"
---

# Laboration 6: AJAX

I denna laboration kommer vi börja med att introducera begreppet AJAX som idag nästan är synonymt med att skapa dynamiska webbplatser. Dynamiska i den mening att vi kommer att hämta och skicka information till vår webbplats utan att den laddas om. Denna information, eller data, kommer vi hämta ifrån ett så kallat [API](https://en.wikipedia.org/wiki/Web_API). I vårat fall kommer vi använda oss av [ett API för Chuck Norris skämt](http://www.icndb.com/api/) och [ett för information om filmer](https://www.omdbapi.com/). Ni kommer bli tilldelad en färdig grund (se nedan) som ni kommer bygga ut stegvis.

[Klicka här för att ladda ner den zipfil innehållande grunden.](../assets/chuck_norris.zip)
{: .info}

---

## Uppgift 1: Chuck Norris

Börja med att ladda ner zipfilen och ta en titt på filerna. Notera att vi använder oss av både CSS-ramverket [Bootstrap](https://getbootstrap.com/) och JS-biblioteket jQuery genom externa URL:er. Detta är ofta ett smidigt sätt att komma igång med ett projekt, eller bara för att experimentera som i dagens laboration.

Om ni öppnar upp HTML-filen bör ni presenteras med något i stil med detta:

![chuck 1](../images/cn1.jpg) _1. Chuch Norris_

Och om ni klickar på knappen bör ett skämt hämtas från API:et och visas likt:

![chuck 2](../images/cn2.jpg) _2. Chuck Norris_

---

## Steg 1: kategorier

Alla skämt vi hämtar från vårt API kan delas in i olika kategorier. Vi vill att användaren ska kunna välja en kategori på skämtet som ska hämtas. Detta ska göras genom en dropdown-meny.

Detta innebär att ert AJAX-anrop mot API:et måste innehålla en parameter i sin URL, i detta fallet `limitTo`. För att ta reda på mer om detta så gå in på dokumentationen för API:et och sedan ner till rubriken "Limiting categories".

Gör nu så att användaren kan välja mellan kategorierna:

* all categories
* nerdy
* explicit

Nu bör ni ha en tjänst som ser ut på följande vis:

![chuck 3](../images/cn3.jpg) _3. Chuck Norris_

Gör nu så att om användaren inte valt en av kategorierna så ska inget anrop skickas till API:et, utan användaren ska få någon form av feedback om att dom måste välja en kategori först (t.ex. röd bakgrund eller kanske en text som dyker upp).

När ni fått dessa bitar på plats så går ni vidare!

---

## Steg 2: för- och efternamn

I detta steg ska vi göra så att vi kan ange ett för- och efternamn som visas istället för "Chuck Norris". Utseendemässigt kan ni utgå från följande:

![chuck 4](../images/cn4.jpg) _4. Chuck Norris_

För att hitta om hur ni ändrar ert anrop (likt vad ni gjorde med `limitTo`) kan ni söka upp rubriken "Changing the name of the main character" på dokumentationen för API:et. Här hittar ni att ni kan ange både `firstName` och `lastName`.

Det är nu er uppgift att implementera detta. När ni gjort det bör ni få ett resultat likt detta:

![chuck 5](../images/cn5.jpg) _5. Chuck Norris_

Gör nu så att användaren måste ange både för- och efternamn, rutorna får inte lämnas tomma. Gör även så att rutorna är ifyllda med "Chuck Norris" från början - så att användaren inte måste göra något för att kunna få ett skämt direkt.

---

## Steg 3: antal skämt

I detta steg ska vi utöka antalet skämt som hämtas. Just nu hämtas bara ett åt gången. Vi vill istället att användarna ska kunna ange hur många skämt som ska hämtas. Detta genom en siffra (1 - 10). För att hitta i API:ets dokumentation om att ange antal skämt så sök på rubriken "Fetching multiple random jokes".

Utseendemässigt bör ni få ihop något likt detta:

![chuck 6](../images/cn6.jpg) _6. Chuck Norris_

Gör så att användaren endast kan fylla i siffror mellan 1 till 10, annars ger ni användaren feedback om detta.

När användaren fyllt i allting korrekt bör dom få ett resultat som ser ut så här:

![chuck 7](../images/cn7.jpg) _7. Chuck Norris_

---

## Uppgift 2: Filmsökning

I denna uppgift blir ni inte tilldelad en färdig grund, dock är det ni gjort i uppgift 1 mall nog för att kunna återanvända stora delar. Denna uppgift påminner även om en del som ni kan göra i inlämningsuppgift 2, så färdigställer ni denna har ni en utgångspunkt till den.

### Filmsökning

Ni ska göra det möjligt för användaren att kunna söka på filmer genom att ange en titel. För att detta ska ni använda API:et för filmer (OMDb). **Notera** att ni måste skapa/registrera er för en gratis API-nyckel. Börja med att gå in och gör det (ibland kan registreringen ta ett tag). Därefter rekommenderar vi att ni läsar på lite om dokumentationen - hur ska vår URL se ut om vi ska söka på titel? Hur ser datan ut som vi får tillbaka?

För att fortsätta på tidigare spår tänker vi att ni skapar ett utseende likt detta:

![movie 1](../images/mf1.jpg) _1. Moviefinder_

Gör så att användaren måste skriva in **minst 3 tecken** i sökrutan för att kunna göra en sökning.

När användaren gjort en sökning kan ni presentera sökresultatet i stil med:

![movie 2](../images/mf2.jpg) _2. Moviefinder_

Denna uppgift är tänkt att ni ska kunna lösa till stor del själva. Det är ju givetvis fritt fram att fråga, men ge det ett ordentligt försök först - diskutera med varandra också!
