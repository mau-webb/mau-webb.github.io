---
id: da280a
title: "Övning - Layout med CSS"
---

# Layout med CSS

I denna laboration ska vi öva på positionering med CSS och att få flera element på en webbplats att arbeta tillsammans för att bilda en layout. Vi kommer att gå igenom hur vi skapar en layout som vi kan använda på flera sidor samtidigt.

## Övning

Målet är att producera en layout som likt många webbplatser på webben består av ett sidhuvud, en menykolumn, en innehållskolumn och en sidfot. Bilden nedan försöker illustrera detta på ett visuellt vis:

![CSS layout example 1](../assets/da280a_ex_css_layout_bild1.png)

För tydlighetens skull är de olika delarna färgade, det bör framgå vilken del som är vad. Notera även att denna layout ska ha en begränsad bredd samt vara centrerad.

### Skelettet

En bra punkt att börja på är att lista ut vilken struktur HTML-dokumentet måste ha för att kunna stödja denna layout. Det ter sig naturligt att ha fyra separata delar för de olika områdena - denna indelning bör göras med element som semantiskt beskriver vad varje del av webbplatsen representerar (t.ex. sidhuvud, navigation, sidfot, osv.). Genom att ge olika `id` till de olika delarna kan vi sedan ge dessa olika utseenden genom CSS.

Skapa ett nytt HTML-dokument och infoga de element som är lämpliga för denna layout i bilden ovan (`<head>`, `<nav>`, `<section>`, `<footer>`). Lägg till lite tillfällig text för att fylla ut med innehåll så vi kan se att allt är på rätt plats.

Även om det fungerar så är det ännu inte så visuellt tilltalande. Skapa en extern stilmall (CSS) och applicera den på HTML-dokumentet (se elementet `<link>` från föregående övning). Ge sedan olika bakgrundsfärger till de fyra delarna genom att hänvisa till respektive `id` du nyss skapat.

I detta skedet kan det exempelvis se ut på följande vis:

![CSS layout example 2](../assets/da280a_ex_css_layout_bild2.png)

### Positionering

Som det nämndes ovan ska denna layout ha en fast bredd och centreras. Börja med att innesluta de fyra delarna i en ny `<div>` med `id="container"`. Sedan kan du i en ny CSS-regel ange bredden för denna - välj en "lagom" bredd (t.ex 900 pixlar eller så).

Denna `<div>` ska sedan centreras, i detta fallet med hjälp av egenskapen `margin` - undersök hur denna egenskap kan användas i detta syfte.

Därefter återstår det faktum att navigationen och innehållsdelen ska ligga brevid varandra. För att åstadkomma detta krävs tre steg:

1. Ange önskvärd bredd för respektive del. Var noga med att totalbredden inte blir större än bredden för `id="container"`
2. Använd egenskapen `float` för att låta navigationen dra sig åt vänster och innehållsdelen dra sig åt höger (eller tvärt om, om du föredrar det)
3. Sidfoten ska alltid hamna under navigationen och innehållet - undersök hur du kan använda egenskapen `clear` för detta ändamål

I detta skedet bör du ha en centrerad layout som exempelvis kan se ut på följande vis:

![CSS layout example 3](../assets/da280a_ex_css_layout_bild3.png)

### Innehåll

Nu är det dags att bestämma sig för vad som bör finnas i varje del på webbplatsen - dvs. innehållet. Som alltid är det lämpligt att först bestämma vilka HTML-element som bäst kan beskriva informationen - för att först därefter definiera utseendet med CSS. Här följer ett förslag på vilket innehåll som bör finnas - och var, samt vilken HTML som är lämplig.

* `<header>`
    * Logotyp: `<h1>`
    * Tagline: `<p>`
* `<nav>`
    * Meny med länkar: `<ul>`, `<li>` och `<a>`
    * Länkar till W3C-validatorn: Den HTML som ges efter godkänd validering
* `<section>`
    * Rubrik på innehåll: `<h2>`
    * En mängd text: `<p>` och vad annat som ter sig lämpligt
* `<footer>`
    * Upphovsrättsinformation: `<p>`

Skapa denna struktur och om du inte kan komma på något eget ämne för innehållet så kan du låna en artikel från din favorittidning (men kopiera i så fall själva texten, inte källkoden).

Därefter kan det se ut ungefär såhär:

![CSS layout example 4](../assets/da280a_ex_css_layout_bild4.png)

### Bättre form

När det gäller vidare visuell utformning av denna webbsida så finns det förstås lika många möjliga inriktningar som det finns människor. Här följer några förslag:

När det gäller vidare visuell utformning av denna webbplats så finns det förstås lika många möjliga inriktningar som det finns människor. Här följer några förslag:

* Ta bort bakgrundsfärgen för `<nav>`, `<section>` och lägg till bakgrundsfärg för `id="container"`. Ändra bakgrundsfärg för `<header>` och `<footer>`
* Välj ett snyggt typsnitt och ange en textstorlek
* Definiera hur länkar ska se ut (glöm inte `:visited` och `:hover`)
* Lägg till `padding` för att få lite luft mellan text och layoutens ramar (tänk på att `padding` påverkar totalbredden för elementet)
* Ta bort listpunkterna från navigationsmenyn och gör den mer distinkt i sitt utseende
* Ge logotypen ett unikt utseende
* Centrera texten i `<footer>`
* Experimentera!

Webbplatsen kan sedan exempelvis se ut så här:

![CSS layout example 5](../assets/da280a_ex_css_layout_bild5.png)

### Flera sidor

Eftersom all CSS ligger i en extern stilmall kan samma utseende enkelt appliceras på flera undersidor. Kopiera ditt HTML-dokument och klistra in det i en ny fil. Byt ut innehållet i `<section>` till något annat och länka sedan mellan dessa två HTML-dokument i navigationen.

## Validering och feedback

Det är viktigt att under processens gång att [validera HTML](http://validator.w3.org) samt att [validera CSS](https://jigsaw.w3.org/css-validator/).
