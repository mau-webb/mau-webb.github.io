---
id: da395a-vt23
title: "Uppgift - VG"
---

# VG-uppgift

**Observera** att denna uppgift **endast** är obligatorisk för de som siktar på betyget Väl Godkänt (VG). Siktar ni på Godkänt (G) behöver ni **inte** göra denna. Denna uppgift är **individuell**.
{: .warn}

I tidigare uppgifter har vi haft ett fokus på att skapa mindre webbapplikationer på egen hand. I arbetslivet görs detta ofta i samarbete med andra utvecklare, vilket ställer en del krav utöver programmeringen. Denna uppgift kommer att ha ett fokus på att bygga en enklare webbapplikation där vi inkluderar delar inom utvecklingsmetodik så som:

* versionshantering via [GitHub](https://github.com).
* pakethantering via [Yarn](https://classic.yarnpkg.com/en/) eller [NPM](https://www.npmjs.com/).
* dokumentation (en sk. [README](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)).

Syfte med uppgiften:

* Kunna använda sig av Git i kombination med GitHub för versionshantering.
* Kunna använda sig av en pakethanterare för ramverk och bibliotek.
* Kunna dokumentera sitt projekt.

---

## Uppgiftsbeskrivning

Denna uppgift är indelad i fyra delar där den första delen är snarlik tidigare uppgifter: att skapa en webbapplikation. De andra tre delarna handlar om att utföra hela utvecklingsprocessen på ett bra vis som hade fungerat i ett samarbete med andra utvecklare. Närmare bestämt att versionshantera sin kod, så att flera kan arbeta parallellt men även för att kunna få en överblick över vad som gjorts. Att använda sig av en pakethanterare, i ett samarbete med andra utvecklare är det inte rimligt att bara ladda ner en massa JavaScript-filer och att försöka hålla ordning på detta själva. Slutligen att dokumentera både sin kod men även hela projektet, ibland ska ett projekt överlämnas eller bara användas av andra - då är detta den centrala punkten för att informera dessa personer om projektet och hur dom kan komma igång med allting.

**Inlämning sker genom att ni publicerar en länk till er GitHub-sida på Canvas.**
{: .warn}

---

### Del 1: Webbapplikationen

Er uppgift är att skapa en mindre webbapplikation med någon form av funktionalitet via ett (eller flera) API:er. Vad ni väljer för API:er är fritt fram, men följande **krav måste uppfyllas**:

* Ni måste använda **minst** ett API.
* Ni måste använda **minst** två externa bibliotek.

Det är tillåtet att använda sig av bibliotek/ramverk så som React, Vue och Angular men dessa räknas **inte** in bland dessa två externa som är kravet.
{: .info}

För att ge er några **exempel** (inte vad ni ska bygga) så kan ni ta en titt på listan nedan som inspiration:

**Webbapplikation 1**

Visualiserar valutakursen för Bitcoin i ett diagram:

* API: [https://www.coindesk.com/coindesk-api](https://www.coindesk.com/coindesk-api).
* [Axios](https://github.com/axios/axios) som ett bibliotek för AJAX-anrop.
* [Chart.js](https://www.chartjs.org/) som ett bibliotek för att skapa diagram.

**Webbapplikation 2**

Kunna söka på och läsa om Star Wars-karaktärer:

* API: [https://swapi.co/](https://swapi.co/).
* [Axios](https://github.com/axios/axios) som ett bibliotek för AJAX-anrop.
* [Popper](https://popper.js.org/) som bibliotek för att visa små rutor för "överflödig" information.

**Webbapplikation 3**

Visa slumpvis intressant fakta om katter:

* API: [https://alexwohlbruck.github.io/cat-facts/docs/](https://alexwohlbruck.github.io/cat-facts/docs/).
* [Axios](https://github.com/axios/axios) som ett bibliotek för AJAX-anrop.
* [Anime.js](https://github.com/juliangarnier/anime/) som bibliotek för att presentera faktan genom animationer.

---

### Del 2: Versionshantering

Ni ska versionshantera ert projekt genom Git på GitHub. Här ska ni använda god versionshanteringsmetodik (ni kan följa, eller bara få inspiration, från [Gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)).

Så länge ni skapar vettiga branches, har vettiga meddelande i era commits och **inte** publicerar all kod i slutet av uppgiften (när allt är klart) så har ni med största sannolikhet god versionshanteringsmetodik. Ni lämnar sedan bara en länk till er GitHub-sida på Canvas vid inlämning.

---

### Del 3: Pakethantering

Ni ska använda er av pakethanteraren [Yarn](https://classic.yarnpkg.com/en/) eller [NPM](https://www.npmjs.com/) för att hämta era externa bibliotek. Tänk på att i er `.gitignore` exkludera kataloger så som `node_modules` så alla externa bibliotek ni är beroende av **inte** hamnar på GitHub.

När ni skapar ert repository på GitHub kan ni välja att inkludera en `.gitignore` baserat på ett programmeringsspråk, välj då `node` så får ni en bra utgångspunkt.
{: .info}

---

### Del 4: Dokumentation

Ni ska avslutningsvis fylla på er `README.md` (eller skapa en ny) som har tydliga instruktioner för ert projekt. Så som vad projektet är för något, hur vi kan komma igång med det, vilken licens det är publicerat under m.m. För inspiration kan ni enkelt ta en titt på populära projekt på GitHub och använda dom som [mallar](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2). 

## Inlämning på Canvas

Den här gången lämnar du in din inlämning direkt på Canvas. Du skickar helt enkelt in länken till ditt GitHub-repo.