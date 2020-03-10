---
id: da344a
title: "Uppgift 1"
---

# Uppgift 1

I den första uppgiften ska ni göra en enklare webbapplikation som är anpassad till olika enheter (stationära och bärbara datorer, surfplattor och mobiltelefoner). Besökaren ska även kunna skräddarsy upplevelse genom att kunna välja mellan olika stilar (utseenden) på sidan. Den kompletta [uppgiftsbeskrivningen finner ni nedan](#uppgiftsbeskrivning).

Syfte med uppgiften:

* Kunna skapa ett HTML-dokument med god semantisk struktur.
* Kunna anpassa en webbplats för olika enheter med hjälp av CSS.
* Kunna implementera interaktivitet genom grundläggande JavaScript.
* Kunna använda sig av `localStorage` för att spara data lokalt hos besökaren.

---

## Kravspecifikation

**Kod (HTML/CSS/JavaScript)**

* Er kod ska vara tydlig och ha god formatering (indentering).
* Er kod ska dokumenteras med kommentarer vid behov.
* Er kod ska kunna köras utan några felmeddelanden.

**Utseende**

* Innehållet på era sidor ska följa [uppgiftsbeskrivningen](#uppgiftsbeskrivning).
* Er design ska vara väl strukturerad med ett fokus på användbarhet.
* Er design ska vara responsiv och anpassa sig till olika skärmstorlekar.
* Er design ska vara användbar oavsett skärmstorlek. 

**Interaktivitet**

* På mobilversionen av er sida ska menyn kunna visas och döljas, den ska vara dold till att börja med.
* Användaren ska kunna ändra stil (utseende) på sidan (utan att behöva ladda om).
* Valet av stil ska sparas genom `localStorage`.
* Vid sidladdning ska den förvalda stilen visas samt vara förvald i er dropdown-meny.
* Ett implementerat och korrekt fungerande bildspel.

**Utöver kraven kommer en generell helhetsbedömning över kvalitén att göras.** 

Alla krav **ska** vara uppfyllda för att bli godkänd. Uppgifter som **inte** uppfyller dessa krav kommer inte att rättas utan skickas direkt tillbaka för komplettering.
{: .warn}

---

## Inlämning

Inlämning sker i form av en zippad mapp innehållande

* era HTML-filer.
* era CSS-filer.
* er JavaScript-fil.

**Namnge er zippade mapp enligt följande format:** `uppgift-1_efternamn_fornamn.zip`

Det är **inte** tillåtet att använda något externt ramverk eller bibliotek så som till exempel Bootstrap, Foundation, jQuery, React, m.m.
{: .warn}

---

## Uppgiftsbeskrivning

Uppgiften går ut på att ni ska efterlikna en färdig webbplats. Däremot ska ni **inte** efterlikna den grafiska formgivningen (dvs. färg, typsnitt, osv.). Ni **ska** ha samma struktur. Innehåll (text och bilder) samt den grafiska formgivningen ska ni själva bestämma. Nedan kommer respektive undersida, med innehåll och skärmdumpar, att presenteras. Därefter kommer en sektion som presenterar den funktionalitet ni ska implementera.

När ni strukturerar ert HTML-dokument ska ni föredra HTML5-element (så som `<header>`, `<footer>`, `<section>`) framför att till exempel bara använda er av elementet `<div>`.

### Sida 1: Startsidan

På startsidan ska ni ha tre stycken artiklar som representerar följande:

* En kort presentation om dig med en bild (bilden behöver inte vara på er själva).
* Varför du gör denna webbplats (vilka lärandemål uppfyller du?).
* En lista med tre punkter på saker som var/är utmanande med denna uppgift.

Ni ska följa strukturen för hur rutorna (innehållssektionerna) ligger på bilderna nedan. Notera de olika skärmdumparna för olika enheter och hur webbplatsen anpassar sig.

![desktop1](../images/uppgift-1_desktop1.png) _Startida: stationär/bärbar._
![tablet1](../images/uppgift-1_tablet1.png) _Startida: surfplatta._
![mobile1](../images/uppgift-1_mobile1.png) _Startida: mobil._

### Sida 2: Filmer (alt. Galleri)

På denna sida ska ni presentera minst 6 stycken figurer (bild samt text). Dessa ska anpassa sig beroende på vilken enhet som besökaren använder sig av. I exemplena nedan är det bilder på filmer men ni får som sagt välja vad ni själva vill.

![desktop2](../images/uppgift-1_desktop2.png) _Filmer: stationär/bärbar._
![tablet2](../images/uppgift-1_tablet2.png) _Filmer: surfplatta._
![mobile2](../images/uppgift-1_mobile2.png) _Filmer: mobil A._
![mobile2b](../images/uppgift-1_mobile2b.png) _Filmer: mobil B._

### Sida 3: Bildspel

På denna undersida ska ni implementera ett bildspel, kraven för implementation hittar ni nedan.

![desktop3](../images/uppgift-1_desktop3.png) _Bildspel: stationär/bärbar._
![tablet3](../images/uppgift-1_tablet3.png) _Bildspel: surfplatta._
![mobile3](../images/uppgift-1_mobile3.png) _Bildspel: mobil._

---

## Funktionalitet

Det är **inte** tillåtet att använda sig av någon färdigskriven kod eller ett bibliotek.
{: .warn}

### Bildspel

Bildspelet ska byggas med hjälp av JavaScript med följande funktionalitet:

* Bildspelet ska byta bild var tredje sekund efter att sidan laddats, när listan på bilder är slut börjar bildspelet om.
* Bilderna ska i någon mån animeras, till exempel genom CSS-egenskapen `transition`.
* Besökaren ska kunna se vilken den nuvarande bilden är, till exempel `2 av 5`.
* Lösningen ska vara utformat på så sätt att vi ska kunna lägga till en ny bild i er HTML-kod så att den inkluderas i bildspelet automatiskt, utan att vi behöver skriva någon mer JavaScript-kod.

### Interaktiv mobilmeny

På mobilversionen av er webbplats ska ni ha en meny som är utfällbar genom att användaren klickar på "meny" i sidhuvudet. När sidan laddas på en mobil ska menyn först vara dold (den ska visas på övriga enheter). Denna funktionalitet ska implementeras genom JavaScript och knappen för att visa och dölja menyn ska endast vara synlig på mobiler.

### Kunna byta utseende

Besökaren ska kunna välja stilen (utseendet) på er sida. Det ska finnas tre olika varianter på er design (dvs. tre stycken CSS-filer) som användaren ska kunna välja mellan genom en dropdown-meny. Valet av detta ska sedan sparas i `localStorage`. Om användern gjort ett val ska detta vara förvalt när sidan laddas om och även vara förvalt i dropdown-menyn.

