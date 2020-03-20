---
id: da355a
title: "Laboration 10"
---

# Laboration 10: React

Syftet med denna laborationen är att pröva ett populärt JavaScript-bibliotek/ramverk. I detta fallet har vi valt att utgå från [React](https://reactjs.org/), men **det är tillåtet att välja något annat** (Vue, Angular, m.m.). Ni ska genom det valda ramverket återskapa det ni gjorde i [laboration 7](../laboration-7/), det vill säga applikationen "Min filmlista".

Det rekommenderas att ni tar en stund och läser igenom ert valda ramverks dokumentation, det brukar finnas en "Getting Started" eller introducerande guider och tutorials.

För att snabbt kunna komma igång med just React så finns hjälpmedlet [Create React App](https://github.com/facebook/create-react-app). Med detta kan ni enkelt starta upp ett nytt projekt för att sedan köra igång en utvecklinsmiljö, utan att behöva göra mycket på egen hand.

De flesta bibliotek/ramverk kräver att ni först [installerar Node.js](https://nodejs.org/en/).
{: .info}

---

## Uppgiften

Eftersom ni ska återskapa det ni gjort i laboration 7, men genom ett ramverk/bibliotek där (med största sannolikhet) ni ska strukturera er kod i form av "komponenter"

Ni ska återskapa det ni gjorde i laboration 7 ("Min filmlista") genom ert valda ramverk/bibliotek, eftersom dessa ofta strukturerar applikationer genom så kallade komponenter så kommer ni få ett förslag på struktur. Försök att skapa er en bra överblick, eller idé, över hur ni vill strukturera ert program innan ni börjar (t.ex. skiss på papper).

Förslag: struktur
{: .code-header}

``` html
<MovieApplication>
    <AddMovieForm />

    <Movies>
        <Movies />
        <Movies />
        <Movies />
        <!-- ... -->
    </Movies>

    <SaveMoviesButton />
    <OrderByAlphaButton />
    <OrderByGradeButton />
</MovieApplication>
```

Tänk på att inte skapa allt för stora komponenter, det är oftast enklare att ha flera mindre och kombinera dom.


