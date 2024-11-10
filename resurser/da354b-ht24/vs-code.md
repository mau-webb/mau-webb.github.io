---
id: da354b-ht24
title: "Visual Studio Code"
---

# Visual Studio Code

[Visual Studio Code](https://code.visualstudio.com/) är en textredigerare från [Microsoft](https://www.microsoft.com/sv-se), som är gratis och öppen källkod. Den är kraftfull och har många funktioner, kanske lite för många i början. Vi har därför satt ihop en liten guide för att komma igång.

## Installation

Gå till Visual Studio Code och ladda ner programmet. Installera det som vilket annat program som helst.

## Grundläggande användning

När du öppnar programmet ser du en ganska tom skärm. I mitten finns en vit yta där du skriver din kod. Till vänster finns en meny med filer och mappar, och till höger finns en meny med verktyg och inställningar.

För att skapa en ny fil, tryck på File och sedan New file. Skriv din kod och spara filen genom att trycka på File och sedan Save, alternativt klicka Ctrl + S (för Windows) eller Cmd + S (för macOS).

## Kortkommandon

Visual Studio Code har många kortkommandon för att snabbt navigera och skriva kod. Här är några exempel:

- Ctrl + C (Cmd + C) - Kopiera
- Ctrl + V (Cmd + V) - Klistra in
- Ctrl + Z (Cmd + Z) - Ångra
- Ctrl + S (Cmd + S) - Spara
- Ctrl + F (Cmd + F) - Sök
- Ctrl + Shift + F (Cmd + Shift + F) - Sök i filer
- Ctrl + P (Cmd + P) - Öppna fil
- Ctrl + Shift + P (Cmd + Shift + P) - Öppna kommandorad
- Ctrl + Shift + I (Cmd + Shift + I) - Formatera kod

## Inställningar

Du kan ändra inställningar för Visual Studio Code genom att trycka på File och sedan Preferences. Här kan du ändra saker som färgschema, teckensnitt och kortkommandon. Vi skulle rekommendera att du kollar igenom inställningarna och ser vad som passar dig bäst, men undvik att ändra kortkommandon för dessa kan vara bra att lära sig.

### Auto Save
En inställning som kan vara bra att ändra är Auto Save. När denna inställning är påslagen sparar Visual Studio Code automatiskt dina ändringar, så att du inte behöver trycka på Spara-knappen hela tiden. Du kan ändra inställningen genom att trycka på File och sedan Auto Save. Alternativt kan du trycka på Ctrl + Shift + P (Cmd + Shift + P) och skriva Auto Save.


### Word Wrap
En tredje inställning som kan vara bra att ändra är Word Wrap. När denna inställning är påslagen bryter Visual Studio Code raden när den blir för lång, så att du inte behöver scrolla horisontellt. Denna inställning är av som standard. Du kan ändra inställningen genom att trycka på File och sedan Preferences och sedan Settings. Sök efter Word Wrap och bocka i rutan. Alternativt kan du trycka på Ctrl + Shift + P (Cmd + Shift + P) och skriva Word Wrap.

### Themes
Visual Studio Code har stöd för olika teman, som ändrar färgschemat på texten. Du kan ändra tema genom att trycka på File och sedan Preferences och sedan Color Theme. Välj ett tema som passar dig bäst.

### Extensions
Visual Studio Code har stöd för extensions, som är tillägg som lägger till extra funktioner. Du kan installera extensions genom att trycka på View och sedan Extensions. Sök efter en extension och tryck på Install för att installera den.

Det kan vara bra att vänta lite med att installera extensions tills du har lärt dig grunderna i Visual Studio Code, eftersom de kan vara lite överväldigande i början, men det finns många bra extensions som kan underlätta ditt arbete. Här är listan på några extensions som vi rekommenderar:

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)
- [Jinja](https://marketplace.visualstudio.com/items?itemName=wholroyd.jinja)

## Extra tips

### Felsökning och Problem
- Den röda understrukningen i koden visar syntax-fel
- Gul understrykning visar varningar
- Klicka på lampikonen som dyker upp bredvid koden för snabba åtgärdsförslag
- Se alla problem genom att klicka på varningssymbolen i statusfältet längst ner

### Split Editor
Du kan dela editorn för att visa flera filer samtidigt:
- Högerklicka på en flik och välj "Split Editor"
- eller dra en flik till höger/vänster sida av editorn