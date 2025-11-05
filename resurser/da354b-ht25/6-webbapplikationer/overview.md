---
id: da354b-ht25
title: "Modul 6 - Webbapplikationer"
---

# Modul 6 - Webbapplikationer

## Översikt av modul 6

Webbprogrammering är en av de mest populära tillämpningarna för Python. Det passar bra som fördjupning efter att ha gått igenom den grundläggande programmeringen i modul 1-5.

| Innehåll | Kommentar |
| --- | --- |
| [Föreläsning - Star Wars](../lecture) | Introduktion till webbapplikationer med Star Wars-tema |
| [Föreläsning - Genomgång: Bottle](../lecture-2) | Videoinspelningar - Introduktion till Bottle |
| [Föreläsning - Önskelista](../lecture-2) | Vi bygger en önskelista som webbapplikation med Bottle |
| [Övning: Webbapplikation med Bottle](../ex-bottle) | Att skapa en första webbapplikation med Bottle |
| [Övning: Webbapplikation med Flask](../ex-flask) | Att skapa en första webbapplikation med Flask |
| [Övning: Webbapplikation med FastAPI](../ex-fastapi) | Att skapa en första webbapplikation med FastAPI |
| [Inlämningsuppgift](../assignment) | Bygg din egen Wiki! |

**OBS** - När det kommer till övningarna ovan så räcker det med att ni väljer **ett** av ramverken (`Bottle`, `Flask`, eller `FastAPI`). Vet ni inte vilket ni vill välja, så rekommenderar vi `Bottle`.

### Webbramverk

Det finns många konkurrerande ramverk och bibliotek webbprogrammering med Python. Alla delar det grundläggande målet i att förenkla vanliga uppgifter samt att ge en struktur att bygga sitt program efter.

#### Rekommenderat: Bottle

[Bottle](http://bottlepy.org/) är det rekommenderade ramverket på grund av enkelheten i att installera och komma igång. Det snabbaste alternativet är att ladda hem bottle genom deras [webbplats](http://bottlepy.org/docs/stable/) till din projektmapp. Därefter kan du använda Bottle fullt ut.

Bottle, likt de flesta andra pythonprojekt, kan även installeras globalt på systemet med hjälp av så kallade pakethanterare (`pip` eller `easy_install`).

Ni kan ladda ner bottle-filen för hand här: [https://bottlepy.org/bottle.py](https://bottlepy.org/bottle.py)

#### Andra ramverk

- [Flask](http://flask.pocoo.org) är i princip lika enkelt att använda som Bottle - båda kan kallas "mikroramverk". Flask är värt att nämna här på grund as dess popularitet, är vanligt att använda även för webbapplikationer i produktion. Flask bör installeras via `pip` eller `easy_install`.
- [Django](https://www.djangoproject.com) är kanske det mest kända webbramverket för Python, och används av några av nätets största webbplatser. Bra att känna till - och värt att titta vidare på för mer avancerade, databasdrivna webbplatser.
- [FastAPI](https://fastapi.tiangolo.com/) är ett nytt och snabbt ramverk för att bygga webbappar. Det är enkelt att använda och har bra dokumentation. Installera med `pip install fastapi` och `pip install uvicorn`. **Obs**: Det kan vara lite knepigt att starta första gången, på grund av uvicorn, men om ni vill ta er an en extra utmaning så kommer detta ramverket ge er en del fördelar längre fram i andra kurser som [Webbtjänster (DA109A)](https://utbildningsinfo.mau.se/kurs/da109a). Se [denna guide](https://fastapi.tiangolo.com/tutorial/first-steps/) för att komma igång.

### Komma igång med Bottle

Istället för egna påhittade övningar rekommenderas den [tutorial som finns på bottle.org](http://bottlepy.org/docs/dev/tutorial.html#quickstart-hello-world). Den visar viktiga koncept med korta exempel för varje. För [uppgiften](/resurser/da354a/6-webbapplikationer/assignment/) kommer du bara behöva vissa av delarna, men det skadar inte att titta igenom all dokumentation.

#### Exempelprojekt

Viktiga delar av funktionaliteten i Bottle visas även i [detta exempelprojekt](https://github.com/Tibbelit/Example-bottle-app). Du kan även ladda hem koden via den länken (som t.ex. en ZIP-fil).

### Uppgift

[Uppgift: bygg din egen wiki](/resurser/da354a/6-webbapplikationer/assignment/)!