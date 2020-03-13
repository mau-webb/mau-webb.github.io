---
id: da344a
title: "Bootcamp: HTML/CSS"
---

# Bootcamp: HTML/CSS

I detta *Bootcamp* ska ni öva på att skriva grundläggande HTML och CSS, för att strukturera innehåll och därefter presentera (utseendet) det på ett användarvänligt vis. Upplägget är indelat i fyra delar, läs igenom respektive del noggrant så ni inte missar något krav.

Om ni inte har ett textredigeringsprogram så rekommenderar vi att ni använder [Visual Studio Code](https://code.visualstudio.com/).
{: .info}

**Lycka till!**

---

## Del 1: En personlig webbplats

I denna första del ska ni skapa en grundläggande webbplats där fokus ligger på att öva på att använda olika HTML-element. Innehållet på sidan ska reflektera något intresse ni har, t.ex. filmer/serier, en sport, matlagning, med mera. Eftersom ni endast ska skriva HTML i denna del, inte CSS, så kommer utseendet vara enkelt - detta är OK.

Ni kommer bli hänvisade till relevanta platser på [Mozillas webbdokumentation](https://developer.mozilla.org/en-US/) genom samtliga delar för detta *Bootcamp*. Detta är en bra samlingsplats för dokumentation kring webben för HTML, CSS och JavaScript. Som både hålls uppdaterad och har bra exempel.

För att komma igång med just HTML kan vi rekommendera läsningen på "[Getting started with HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started)". 

**Kraven** för denna första del är att skapa en webbplats innehållande följande HTML-element:

* Paragrafer: `<p>`
* Länkar: `<a>`
* Rubriker: `<h1>, <h2>, <h3>, <h4>, <h5>, <h6>`
* Listor: `<ul>, <ol>`
* Bilder: `<img>`
* Betoning: `<em>, <strong>`
* Kommentarer: `<!-- en kommentar -->`

Relevant dokumentation: [HTML text fundamentals](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/HTML_text_fundamentals) och [Creating hyperlinks](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Creating_hyperlinks).

Sidans innehåll ska kännas relevant för det intresse ni valt att presentera. Det vill säga att ni kan inte endast bara lägga till alla element och fylla på med lite text, det ska kännas som en "riktig" webbplats.

Dessa element styr hur ni strukturerar ert innehåll, men en webbplats innehåller mer än så. För att ge er en grund att utgå från kan ni ta en titt på följande exempel:

HTML
{: .code-header}

``` html
<!doctype html>
<html>
    <head>
        <title>Min webbplats</title>
        <meta charset="utf-8">
    </head>
    <body>
        <!-- Ert innehåll -->
    </body>
</html>
```

I ovanstående exempel kan vi se att vi behöver ange dokumenttypen (`<!doctype html>`), vilket kort kan beskrivas som att vårt dokument ska tolkas som HTML5 och framåt. Sedan har vårt dokument en indelning av `<head>` och `<body>` vilket är **information om dokumentet** och **dokumentets innehåll** respektive. För stunden räcker det med `<title>` och `<meta charset="utf-8">` i vårt `<head>`, [men det finns givetvis mer möjligheter](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/The_head_metadata_in_HTML). 

När ni lyckats presentera ert intresse genom elementen i kravlistan är ni färdiga. Ni måste inte inkludera exakt alla element, det viktiga är att innehållet kommer fram.

Be någon av handledarna ta en titt på er HTML för att utesluta att ni missförstått något eller bara för tips om förbättringar.
{: .info}

### Validera er HTML

Det är inte ovanligt att misstag görs när vi skriver HTML, eller kod generellt. För HTML finns [The W3C Markup Validation Service](http://validator.w3.org/) som kontrollerar att ert dokument är korrekt skrivet, annars kommer ni få relevanta felmeddelande för att kunna korrigera era misstag.

---

## Del 2: Tabeller och formulär

I denna del kommer ni att arbeta med tabeller och formulär. Båda dessa användas för att hantera och presentera data på olika vis. Mer specifikt brukar vi använda tabeller för att presentera data på ett strukturerat vis och formulär för att skicka eller hämta data.

**Skapa en ny HTML-fil för denna del.**

### Uppgiften

Du har fått i uppdrag av en hyresvärd att producera ett formulär för ansökan om lägenheter. Hyresvärden har redan, genom en extern utvecklare, ett skript för att ta emot och spara ansökningar, men behöver din hjälp för att producera ett formulär. Hyresvärden behöver även en tabell som presenterar dessa tillgängliga lägenheter. Både formuläret och tabellen behöver inte vara grafiskt tilltalande men måste vara användarvänliga och tillgänliga för så många personer som möjligt.

#### Lägenhetstabellen

För att hyresvärden ska kunna presentera sina tillgängliga lägenheter på ett strukturerat vis så bör detta göras genom en tabell. För att ha en utgånspunkt kommer ni bli presenterade med ett designförslag som ni sedan ska efterlikna (se nedan).

![lägenhetstabell](../images/table.png) _1. Lägenhetstabell_

Tabellen ska byggas med element som beskriver innehållet så bra som möjligt. Förutom de vanligare tabell-elementen `<table>` (tabell), `<tr>` (tabellrad) och `<td>` (tabellcell) så ska ni använda er av:

* `<thead>` och `<tbody>` för att skilja på tabellhuvud och innehåll.
* `<th>` för att markera rubrikceller.
* `<caption>` för att inkludera en beskrivning av tabellen.

Relevant dokumentation: [HTML table basics](https://developer.mozilla.org/en-US/docs/Learn/HTML/Tables/Basics).

#### Lägenhetsformulär: steg 1

Efter ni konstruerat er lägenhetstabell ska ni skapa ett ansökningsformulär. Grunden för ett formulär kan vara väldigt enkelt. Ta en titt på följande exempel:

Formulär
{: .code-header}

``` html
<form action="http://webshare.mah.se/ctfroh/da158a/formtest.php">
    <fieldset>
        <legend>Ansök om bostad</legend>
        <button type="button">Ansök</button>
    </fieldset>
</form>
```

Från detta kan vi avläsa följande:

* All data i formuläret ska skickas till (via attributet `action`) adressen `http://webshare.mah.se/ctfroh/da158a/formtest.php`.
* Det enda innehåll vi har just nu är en knapp med texten "Ansök".
* Vi använder `<fieldset>` för att ange en sektion i formuläret, just nu har vi bara en.

Inkludera detta formulär på er sida så ni har någonting att börja experimentera med. *Vad händer när ni klickar på ansök?*

För att formuläret verkligen ska skickas när ni klickar på knappen så måste attributet `type` ha ett speciellt värde (alltså inte `"button"`). **Undersök** hur ni kan ändra attributet `type` så att ni kan skicka formuläret. **Ni ska även** redigera formuläret (`<form>`) så att det skickas med HTTP-metoden `POST` (detta görs genom attributet `method`).

Relevant dokumentation: [Your first form](https://developer.mozilla.org/en-US/docs/Learn/Forms/Your_first_form).

#### Lägenhetsformulär: steg 2

Användaren ska kunna mata in mer data i ert formulär. Börja med att lägga till fält med möjlighet att skriva in för- och efternamn. Placera dessa textrutor ovanför ansökningsknappen. För att skapa textrutor använder ni elementet `<input>` och anger att attributet `type` ska vara `"text"`.

När vi skickar data är det viktigt att namnge all denna data, det vill säga så vi skickar data i form av `namn:värde` par. Detta görs genom att alla formulärselement kan ha attributet `name`, värdet för detta attribut kommer bli namnet på datan som skickas. Till exempel:

``` html
<input type="text" name="message">
```

Om en användare fyllt i detta fält med `"Mitt meddelande"` hade vi skickat vidare `namn:värde` paret `message:"Mitt meddelande"`.

Det rekommenderas att ni namnger **alla** era fält i formuläret, välj också namn som representerar värdet och undvik specialtecken och mellanslag i namnen.

När ni lagt till fält för för- och efternamn bör ni ha något likt detta:

![lägenhetsformulär](../images/form.png) _2. Lägenhetsformulär_

När ni skickar vidare detta formulär (dvs. klickar på "Ansök") bör ni få ett svar innehållande:

![lägenhetsformulär svar](../images/form_response.png) _3. Svar från lägenhetsformuläret_

Om rutan är röd har ni fel `method` och ser ni inte namnen på era värden har ni glömt fylla i attributen `name` korrekt. 
{: .info}

#### Lägenhetsformulär: steg 3

Nästa steg är att förbättra hur benämningarna på era textrutor är skrivna (i bilden nummer 2 är benämningarna "Förnamn" och "Efternamn"). Detta görs med elementet `<label>` som är tillför att lägga till etiketter (benämningar) till era formulärsfält. Utöver att texten förtydliga innebörden av textrutan så blir även texten klickbar vilket ytterligare ökar användbarheten. Se nedan för ett exempel och notera samtliga attribut.

``` html
<label for="price">Pris</label>
<input type="text" name="price" id="price">
```

För att koppla samman en `<label>` med (till exempel) `<input>` behöver etiketten (label) ha attributet `for` med samma värde som för fältets (input) `id`.

Om ni inte redan lagt till dessa så lägg till elementet `<label>` i ditt formulär.

#### Lägenhetsformulär: steg 4

Nu har ni experimenterat med de mest grundläggande delarna kring formulärsskapande. Det finns några andra viktiga formulärselement som är bra att känna till. För att pröva dessa kan ni utöka ert lägenhetsformulär med följande:

* Textfält (`<input>`) för telefonnummer och nuvarande adress.
* En textruta (`<textarea>`) för att kunna ange eventuella extrabehov (allergier, krav på hiss, m.m.).
* En dropdown (`<select>`) där användaren kan välja vilken lägenhet som ansökan gäller (utgå från objektsnummren i tabellen).
* Radioknappar (`<input type="radio">`) där användaren kan ange om dom ska bo ensam, med sambo eller flera stycken.
* Checkboxar (`<input type="checkbox">`) där användaren kan ange att dom är över 18 år och godkänner att deras uppgifter hanteras enligt personuppgiftslagen.

---

## Del 3: CSS

Cascading Style Sheets (CSS) utgör grunden för i princip alla visuella aspekter av en modern webbplats. CSS är inte begränsat till webbsidor i HTML, utan är ett generellt språk för stilmallar med många användningsområden. Webben är dock dess största anvädningsområde och det är detta som ska utforskas i denna del.

### Uppgiften

I denna del ni utgå ifrån ett färdigt HTML-dokument för att gradvis bygga på detta med CSS. På vägen kommer ni att stöta på många av de grundläggande koncept som krävs för att utforma webbsidor.

Ni ska utgå från ett färdigt [HTML-dokument](../assets/forskning.html) (högerklicka och "Spara som ..."). Öppna upp dokumentet och ta en titt på hur det är strukturerat. Det är viktigt att hålla koll på strukturen för att sedan utforma hur CSS:en (utseendet) ska appliceras. I slutet av denna del (3) hittar ni en exempelbild på hur ni ska ändra utseendet på det färdiga HTML-dokumentet ni blivit tilldelat.

När ni öppnar dokumentet i en webbläsare så kommer ni se att det är inte speciellt visuellt tilltalande. Detta kan vi såklart lösa med hjälp av CSS. Genom stilmallar (CSS) kan vi överskrida webbläsarens standardvärden för utseende, så som färg på texten, typsnitten, bakgrundsfärger, med mera. För att kunna ange sin CSS i sitt HTML-dokument kan vi (till exempel) ange detta med elementet `<style>`, som vi kommer placera i vårt dokumenthuvud (`<head>`). 

``` html
<head>
    <!-- Tidigare kod ... -->
    <style type="text/css">
        /* Här kommer ni placera er CSS. */
    </style>
</head>
```

Notera att kommentarer i CSS skrivs med `/* ... */`.
{: .info}

#### Applicera CSS

Att skriva CSS görs genom att ange vad (**selektor**), det vill säga vilket element, som ska få någon färg och form (**attribut: värde;**). En **selektor** kan skrivas på många vis men dom tre mest grundläggande är följande: `element`, `class`, `id`.

``` css
/* Alla paragrafer (<p>) */
p {}

/* Alla länkar (<a>) */
a {}

/* Alla element med `class="my-class"` */
.my-class {}

/* Elementet med `id="my-id"` */
#my-id {}
```

Efter vi bestämt vilket eller vilka element vi vill ändra utseende på måste vi ange vilken färg och form som ska ändras. Det finns en uppsjö av olika attribut vi kan påverka, till exempel:

``` css
/* Alla paragrafer (<p>) */
p {
    color: red;
}

/* Alla länkar (<a>) */
a {
    font-size: 28px;
}

/* Alla element med `class="my-class"` */
.my-class {
    background-color: blue;
}

/* Elementet med `id="my-id"` */
#my-id {
    font-weight: bold;
    font-style: italic;
}
```

Relevant dokumentation: [CSS selectors](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors).

Var noggranna med att ange attribut som `attribute: value;` och att hela grupperingen är inom `{ ... }`.
{: .info}

När ni anger CSS på ett element som innehåller andra element kommer dessa också att ärva utseendet (därav Cascading). Skulle vi därför ange att `body { color: green; }` så hade all vår text på sidan blivit grön. Färger kan också anges som [hexkod](https://www.color-hex.com), till exempel `body { color: #0088cc; }`.

Relevant dokumentation: [Cascade and inheritance](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Cascade_and_inheritance).

#### Typsnitt

Typsnitt anger vi genom `font-family: ...;`. Om ett typsnitt finns eller inte beror delvis på besökaren (om det är installerat på deras dator) och delvis på avsändaren (om det är installerat på servern). Däremot kan ni förhålla er till [denna listan](https://www.cssfontstack.com) till att börja med.

För att ytterligare förstärka att användaren presenteras med ett typsnitt ni vill ha kan ni ange flera typsnitt i följd. Då kommer webbläsaren (från vänster till höger) pröva respektive typsnitt och använda sig av det första som finns tillgänligt. Till exempel `font-family: Helvetica, Arial, sans-serif;`. Avsluta alltid med en typsnittsfamilj, det vill säga om det är med eller utan [seriffer](https://sv.wikipedia.org/wiki/Seriff). 

Om ett typsnitt har flera ord anges dessa inom citationstecken, till exempel `font-family: "Times New Roman";`.

#### Extern CSS

Att skriva all sin CSS internt genom `<style>` är inte optimalt. Om både ditt HTML-dokument och din CSS blir stor kommer din fil bli svår att underhålla. Ytterligare en fördel med att ha extern CSS är att denna fil kan inkluderas till flera dokument. Då får vi också en tydlig seperation mellan struktur (innehåll) och presentation (utseende).

För att skapa en extern CSS-fil skapar ni en ny fil med filändelsen `.css`, till exempel `styles.css`, i samma mapp som er HTML-fil. Sedan ersätter ni ert `<style>`-element med följande:

``` html
<head>
    <!-- Tidigare kod -->
    <link rel="stylesheet" href="style.css">
</head>
```

Om ni gjort rätt bör ert dokument se ut på samma vis som innan men nu har ni istället en extern CSS-fil.

#### Avslut

För att avsluta del 3 ska ni försöka återskapa följande utseende med hjälp av en **extern** CSS-fil. Det behöver inte vara exakt samma färger utan det viktiga är att påverka samma element.

![css exempel](../images/forskning.png) _1. CSS-förslag_

Tänk nu på att kontrollera HTML-dokumentet, vilka element finns? Vilka klasser finns? Vilka ID:n finns?

Relevant dokumentation: [Getting started with CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/Getting_started), [Using your knowledge](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps/Using_your_new_knowledge), [Styling tables](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Styling_tables).

---

## Del 4: Layout med CSS

I den sista delen ska ni öva på att skapa en layout (positionering) med CSS. I dag finns det olika alternativ för att åstadkomma en layout. För att få en överblick kan ni snabbt skumma igenom artikeln [Introduction to CSS layout](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Introduction). Vilket alternativ som man väljer kan bero på flera faktorer, vilka webbläsare måste stödja layouten? Är det en enkel eller avancerad layout? med mera.

Vi har för denna del valt att utgå från alternativet "Flexbox" och för att ge er en god referens rekommenderar vi att ni tar en titt på (och har tillhands) [A Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/). 

### Uppgiften

Målet för uppgiften är att producera en layout, som likt många webbplatser idag, som består av ett sidhuvud, menykolumn, en innehållssektion och en sidfot. Följande bild illustrerar målet:

![css layout goal](../images/css-layout.png) _1. Layout_

För tydlighetens skull är de olika områdena färglagda, det bör framgå vad som är vad. Notera att denna layout även ska ha en begränsad bredd samt vara centrerad.

#### Skelettet

En bra utgånspunkt är att börja lista ut vilken struktur ni vill ha på ert HTML-dokument för att stödja denna layout. Om vi tar en titt på exempelbilden ovan så skulle vi lämpligen kunna dela in våra områden i fyra olika områden. I detta fallet, som tidigare nämnt, sidhuvud, meny, innehåll och en sidfot. Börjar vi fundera vidare över vilka HTML-element som skulle vara passande hade vi, till exempel, kunna tänka oss: `<header>`, `<nav>`, `<main>` och `<footer>` för respektive område.

Börja med att skapa ett tomt HTML-dokument och börja sedan fylla på det med dessa element, fyll respektive element med någon kort text om dess innebörd så vi kan se detta på vår sida sedan. Skapa även en extern CSS-mall och inkludera den (via `<link>`) i `<head>`. Ge respektive område en egen bakgrundsfärg så vi tydligare kan se dessa.

I detta skede bör ni ha något likt:

![css layout goal 2](../images/css-layout2.png) _2. Skelett_

Det nämdes tidigare att vi skulle ha en begränsad bredd och att sidan skulle vara centrerad. Detta kan göras på många vis men ett av de enklare är att placera hela sidans innehåll, hitills våra fyra områden, inom en `<div>` (ge denna ett ID så ni kan komma åt den i er CSS). Sedan kan ni i er CSS ange en högsta tillåtna bredd (`max-width`), säg 900 pixlar eller så.

Undersök därefter hur ni kan använda attributet `margin` för att centrera sidan.

Därefter återstår (rent layoutmässigt) det att positionera er navigation och innehåll horisontellt brevid varandra.

![css layout goal 3](../images/css-layout3.png) _3. Positionering_

Återigen finns det flera lösningar men en av de enklare kan vara att placera både `<nav>` och `<main>` inom en `<div>` (med ett lämpligt ID) och därefter ange att denna ska ha `display: flex;`.

Undersök därefter hur ni kan använda attributet `flex` så att navigationen (till exempel) tar upp 1/3 av bredden och innehållet 2/3.

#### Innehåll

Nu när layouten börjar komma mer på plats är det dags att fylla på med innehåll, så vi har något att applicera färg och form på. För att få en referens kan ni ta en titt på bilden nedan. Dock föreslår vi att ni hittar en egen artikel från en tidning eller dylikt och fyller på med på er sida.

![css layout goal 4](../images/css-layout4.png) _4. Innehåll_

Tänk över hur det ser ut och vilka element som kan representera respektive del, så som `<h1>` för huvudrubrik och `<ul>` för listan, med mera.

Slutligen ska ni fortsätta med CSS för att påverka innehållet enligt följande exempel (färger behöver inte stämma exakt utan det generella utseendet):

![css layout goal 5](../images/css-layout5.png) _5. Utseende_

#### Avslut

Avslutningsvis ska ni skapa en kopia av ert HTML-dokument, ersätta innehållet i `<main>` med en ny artikel. Sedan ska ni göra så att dessa sidor har, i sina menyer, länkar till varandra så att vi kan navigera mellan dessa utan att behöva öppna respektive i en webbläsare. Båda kan inkludera samma CSS-mall (att ni har en extern mall innebär att den är återanvändbar).

Stäm nu av ert resultat med någon av handledarna så att allting blivit rätt och se om ni eventuellt kan få några bra tips på vägen.
