---
id: da344a
title: "Uppgift 2"
---

# Uppgift 2

**Observera** att denna uppgift behöver du endast göra om du väljer att inte delta på och redovisa kursens laborationer.
{: .warn}

I den andra uppgiften ska ni fokusera på funktionalitet som ofta används i webbapplikationer. Vi kommer främst att titta på hantering av externa API samt hur vi kan lagra information hos klienten för att ge en dynamisk upplevelse.

Syfte med uppgiften:

* Fortsätta skapa ett HTML-dokument med god semantiskt struktur.
* Fortsätta kunna anpassa en webbplats för olika enheter med hjälp av CSS.
* Kunna använda externa API för att hämta information.
* Kunna använda sig av ett CSS-ramverk.
* Kunna använda sig av ett JavaScript-bibliotek.

---

## Kravspecifikation

**Kod (HTML/CSS/JavaScript)**

* Er kod ska vara tydlig och ha god formatering (indentering).
* Er kod ska dokumenteras med kommentarer vid behov.
* Er kod ska kunna köras utan några felmeddelanden.

**Utseende**

* Er design ska använda sig av ett CSS-ramverk för layout och formgivning.
* Er design ska vara väl strukturerad med ett fokus på användbarhet.
* Er design ska vara responsiv och anpassa sig till olika skärmstorlekar.
* Er design ska vara användbar oavsett skärmstorlek.

**Interaktivitet**

* Sidan använder sig av ett JavaScript-bibliotek.
* Sidan ska korrekt visa vädret för en besökare.
* Sidan hanterar felsvar från API:erna på ett godtagbart vis.
* Användaren ska kunna söka på filmer och spara dessa till sitt bibliotek.
* Användaren ska kunna betygsätta sina sparade filmer.
* Användaren ska kunna radera filmer från sitt bibliotek.
* När användaren lägger till, raderar eller betygsätter en film ska denna få lämplig feedback.

**Utöver kraven kommer en generell helhetsbedömning över kvalitén att göras.** 

Alla krav **ska** vara uppfyllda för att bli godkänd. Uppgifter som **inte** uppfyller dessa krav kommer inte att rättas utan skickas direkt tillbaka för komplettering.
{: .warn}

---

## Inlämning

Inlämning sker i form av en zippad mapp innehållande

* era HTML-filer.
* er CSS-fil.
* era JavaScript-filer.

**Namnge er zippade mapp enligt följande format:** `uppgift-2_efternamn_fornamn.zip`

---

## Uppgiftsbeskrivning

Kärnan för denna uppgiften är att utgå från en beskrivning över både struktur och funktionalitet. Ni kommer inte få någon färdig design att följa utan ert val av CSS-ramverk kommer till största del att styra utseendet på er webbapplikation. I sektionerna under denna kommer ni att se hur er webbapplikation ska struktureras i form av undersidor och dess innehåll, samt vilken funktionalitet respektive undersida ska ha.

Tänk på att sidan ska vara responsiv och fungera på olika skärmstorlekar. Nedan hittar ni ett litet urval av några populära CSS-ramverk (en sökning på Google kommer ge er fler resultat):

* [Bootstrap](https://getbootstrap.com/)
* [Foundation](https://get.foundation/)
* [Semantic UI](https://semantic-ui.com/)
* [Materialize](https://materializecss.com/)

För att åstadkomma den funktionalitet som presenteras nedan behöver ni nyttja två stycken API:er, vi rekommenderar dessa två men det är tillåtet att använda andra:

* [OpenWeather API](https://openweathermap.org/API) för att hämta information om vädret.
* [OMDb API](http://www.omdbapi.com/) för att hämta information om filmer.

Börja redan nu med att registrera en API-nyckel för respektive sida då det kan ta ett tag innan dom blir aktiverade.
{: .info}

---

## Struktur

Nedan presenteras en lista över de undersidor som ska finnas.

* Startsida: här presenteras information om vädret.
* Sök film:
    * Här ska användaren kunna söka efter en film (titel eller årtal).
    * I resultatlistan ska användaren kunna välja att spara en film till sitt bibliotek.
* Mitt filmbibliotek:
    * Här ska användaren kunna ta bort en film från sitt bibliotek.
    * Här ska användaren kunna betyggsätta sina filmer (t.ex. 1 till 5).

---

## Funktionalitet

Om ett anrop mot ett av era API:er inte fungerar ska ni presentera användaren med information om detta, så dom antingen kan ladda om sidan eller att ni, till exempel, gör ett par försök till.

### Startsidan

På startsidan ska ni implementera funktionalitet för att visa vad det är för väder för besökaren, baserat på vart de befinner sig. Detta görs genom att först ta reda på deras plats (geolocation) och sedan använda platsen genom ett väder-API för att ta reda på:

* aktuell temperatur (Celsius).
* en bild (ikon) på det aktuella väderläget.
* beskrivning av det aktuella väderläget.

Det är tillåtet att använda något annat API för väder än [OpenWeather API](https://openweathermap.org/API). Tänk på att registrera er då det kan ta tid innan er nyckel aktiveras.

För att få en bild via OpenWeather använder ni följande URL `http://openweathermap.org/img/wn/` följt av `<ICON_NAME>@2x.png` där ni ersätter `<ICON_NAME>` med det namn på ikonen ni fick från API:et.
{: .info}

### Sök film

Undersidan "Sök film" ska presentera användaren med en sökruta för att hitta en eller flera filmer, baserat på titel eller årtal. Själva sökningen ska ske genom ett AJAX-anrop till ert API (vi rekommenderar OMDb). Resultatet av sökningen ska presenteras i form av en lista för användaren med:

* Titel.
* Årtal.
* En knapp för att spara filmen till användarens bibliotek.

### Mitt filmbibliotek

Undersidan "Mitt filmbibliotek" ska presentera användaren med en lista över alla sparade filmer. I listan ska respektive film innehålla egenskaperna:

* Bild (poster för filmen).
* Titel.
* Årtal.
* Speltid.
* Länk till IMDB.

Utöver egenskaperna ska det finnas **en knapp som raderar** filmen från användarens bibliotek och möjlighet att **kunna betygsätta filmen**. Hur betygsättningen ska se ut får ni bestämma själva, till exempel kan det vara 5 stycken stjärnor som användaren kan klicka i eller en dropdown-ruta där användaren kan välja 1 - 5.

**Sortera listan** över filmer antingen i **bokstavsordning** eller på **betyget**.


