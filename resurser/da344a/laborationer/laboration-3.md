---
id: da344a
title: "Laboration 3"
---

# Laboration 3: Responsive Web Design (RWD)

I denna laboration ska ni bygga en responsiv webbplats. Ni kommer få strukturen presenterad för er samt ett förslag till utseende och innehåll (detta får ni mer än gärna ändra på).

Ni ska anpassa strukturen för tre enheter: *desktop*, *tablet* och *mobile*.

Detta ska ske genom sk. *breakpoints* med hjälp av *media queries*. Följande bredder kan ni utgå ifrån:

* Desktop: `1200px`
* Tablet: `900px`
* Mobile: `600px`

Respektive breakpoints kommer skrivas på följande vis:

Media Queries
{: .code-header}

``` css
/* Mobile */
@media screen and (max-width: 600px) {
    /* Anpassningar ... */
}
```

Tänk på att ni testar era breakpoints med hjälp av webbläsarens utvecklarverktyg.


---

## Kravspecifikation

* Ni ska ha (minst) 3 stycken breakpoints: `1200px`, `900px` och `600px`.
* Den övergripande strukturen ska stämma överens med de struktursförslag som presenteras.
* Ni ska använda er av `display: grid;` för den övergripande strukturen och `display: flex;` för innehållet.
* Ni ska ha elementet `<meta>` för att ställa in er `viewport`.

Ha gärna dessa länkar tillhands då dom är bra referenser för respektive layoutsystem:

* [A Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
* [A Complete Guide to Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)

### Krav på innehåll

* **Sidhuvud**: en titel på webbplatsen och (**valfritt**) en logotyp.
* **Meny**: minst fyra stycken alternativ (dessa måste inte leda någonstans).
* **Innehåll**: en beskrivande text om webbplatsen och några bilder med bildtexter som representerar webbplatsens innehåll.
* **Sidfot**: kontaktinformation (t.ex. namn/företag, mail, telefonnummer), denna kan såklart vara fiktiv.

---

## Struktur

De färger, texter och små ytor mellan olika sektioner i dessa bilder är bara för att **förtydliga**, inget ni alltså ska inkludera. Det är helheten som ni ska efterlikna.

Börja med att skissa upp hur er HTML-kod kan reflektera denna strukturen. I och med ni ska använda er av `display: grid;` så glöm inte att ni då skapar ett rutnät - alltså, *hur många kolumner och rader behöver ni för att åstadkomma denna struktur?*

### Desktop

![Desktop](../images/wireframe_3.png)

### Tablet

![Tablet](../images/wireframe_2.png)

### Mobile

![Mobile](../images/wireframe_1.png)

---

## Innehåll

Här presenteras ni av ett förslag till innehåll (i detta fallet Star Wars). Glöm inte längs hela er utvecklingsprocess att testa er sida på olika bredder (genom utvecklarverktyget i webbläsaren) så ni upptäcker eventuella fel som kan uppstå över tid.

Ersätt gärna innehållet med något eget intresse ni har.

### Desktop

![Desktop content](../images/wireframe_content_3.png)

### Tablet

![Tablet content](../images/wireframe_content_2.png)

### Mobile

![Mobile content](../images/wireframe_content_1.png)

---

## Tips

Här har vi samlat en liten lista av tips som eventuellt kan vara till hjälp:

* Om ni har länkar direkt i en `<nav>` och dessa hamnar på samma rad kan ni exempelvis ange `display: flex;` på denna och sedan använda er av `flex-direction: column;` för att få dom som en kolumn. Ett ytterligare alternativ kan vara att ange `display: block;` på respektive `<a>`.
* För att göra en bild responsiv brukar vi ange både `max-width: 100%;` och `height: auto;`.
* Använd `width: 100%;` om ni vill att ett blockelement ska fylla hela bredden av sitt förälderelement.
* Glöm inte bort att `box-sizing: border-box;` gör att både *padding* och *border* räknas med i bredden av ett blockelement.
* Ta en titt på `flex-wrap` för att få era bilder att inte alla bli på en och samma rad.
