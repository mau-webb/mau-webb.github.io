---
id: da280a
title: "Övning 3 - Bilder och länkar"
---

# Övning 3 - Bilder och länkar

## Fräscha upp webbplatsen

Vegano har besämt sig för att göra webbplatsen mer tilltalande och därför önskar de ha en smakfull bild på restaurangen samt ett par länkar till de vanligaste sociala medierna som de använder: facebook, twitter och instagram. De skulle även vilja ha en länk som går till en del av hemsidan som visar deras öppettider.

Vi ska i denna övning utgå från föregående kod som vi redan knåpat ihop. Resultatet efter våra tillägg bör rimligen [se ut på detta vis](../assets/da280a_ex3_bild2.png).


## Huvudbild - absolut sökväg

Det första vi kan börja med är att leta upp en trevlig bild på en restaurang. Har du ingen bild [kan du ta denna bilden](../assets/da280a_ex3_bild2.jpg). Använd hela länkens adress och stoppa in den som din sökväg (absolut). Vegano önskar ha bilden precis under sina huvudrubriker - något i stil med det här:

``` html
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
    </head>
    <body>
        <h1></h1>
        <!-- placera sökvägen till bilden inom src="" -->
        <img src="">
    </body>
</html>
```

## Ikoner - relativ sökväg

Nästa utmaning vi ska ta oss an är att lägga upp ikoner för de sociala medierna facebook, twitter och instragram på slutet av sidan och dessutom göra dessa klickbara. Vi börjar med ikonerna - till skillnad från föregående bild ska vi nu försöka länka dessa direkt från en mapp på vår dator. Det vill säga som en relativ sökväg. Varje ikon kommer behöva en egen `<img>`. [Ladda ner följande zipfil](../assets/da280a_ex3_images.zip) och packa sedan upp filerna till samma mapp som du placerat ditt HTML-dokument. Sökvägen bör då bli något i stil med:

``` html
<img src="images/namnet-på-din-bild">
```

Försök nu att få in samtliga ikoner på rätt plats med rätt sökväg i ditt HTML-dokument!

## Klickbara ikoner

I [beskrivningen över länkar](/{{ site.resource_path }}/da280a/material/m1_html_links/) bekantade vi oss med elementet `<a>` (eng. anchor) där vi kan ange, som med bilder, relativa eller absoluta sökvägar till en annan plats. Det rolga är att bilderna/ikonerna kan också vara länkar! För att göra en klickbar ikon behöver vi definera dels vad som ska vara klickbart (vår ikon) och vart besökaren ska hamna när de klickar på den (t.ex facebook). Detta görs genom att vi nästlar (eng. nesting) våra element - i detta fallet en `<img>` tillsammans med en `<a>`:

``` html
<a href="länk-till-annan-sida">
    <img src="images/namnet-på-din-bild">
</a>
```

Det vill säga att vi kan inte bara placera text inom länk-taggarna, utan bilder också. Använd gärna adresserna till de olika sociala mediernas startsida för enkelhetens skull. Pröva gärna att byta ut mot andra adresser och se vad som händer - t.ex vad händer om du har samma adress inom `href` som bildens `src`?

## Öppettider

Eftersom du redan vid det här laget lyckats få klickbara ikoner så kommer denna delövning vara väldigt enkel. Det första vi behöver göra är att skapa ett nytt HTML-dokument i samma mapp som ditt nuvarande HTML-dokument. Du kan döpa den till något i stil med `oppettider.html`. Det viktiga är att du använder rätt namn senare till din relativa sökväg. Skapa sedan en enkel rubrik innehållande "Våra öppettider" och därefter en lista (`<ul>`) med alla öppettider - dessa bestämmer du själv.

I ditt huvuddokument ska du nu lägga till en liknande rubrik med "Våra öppettider" precis under huvudbilden. Den ska agera ankare (länk) till vårt nyskapade dokument! Nästla nu elementet `<a>` i din rubrik:

``` html
<h2>
    <a href="ditt-nya-html-dokument.html">
        Våra öppettider
    </a>
</h2>
```

Klar? Bra jobbat! Nu har vi lagt till lite trevligare estetik, mer interaktion och kommit ett steg närmare rätt århundrade.
