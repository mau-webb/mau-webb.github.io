---
id: da354b-ht24
title: "Modul 1 - Introduktion till Python"
---

# Modul 1 - Introduktion till Python

## Case (3) - Valfritt


### Inledning

Nu kan du bygga vidare på koncepten du använt hittils, för konstruera ett program av
egen design. Här är några förslag på lämpliga inriktningar:

- En bensinpump, som låter användaren skriva in mängden tankad bensin och sedan
presenterar slutsumman som ska betalas.
	- *Om du vill öva på kommande koncept*: låt också användaren välja typ av
	bensin och avgör med en if-sats vad literpriset blir.
- En mobilkostnadsberäknare, som låter användaren skriva in antal ringda minuter,
skickade SMS, nedladdade megabyte och/eller andra saker du tycker är relevant.
Resultat kan t. ex. vara total månadskostnad på ett lättläsligt vis.
	- *Om du vill öva på kommande koncept*: låt också användaren välja vilket abonnemang priserna ska beräknas efter
- Eget val! (. . . men se till att användarinmatning, beräkningar och formatterad
utskrift finns med.)


Oavsett inriktning så är det viktigast att källkoden är välstrukturerad, med avseende
på namngivning. Se även till att kommentera, i de fall där koden inte talar för sig själv.

Lycka till! =)

---


### Cirkelövning - Radie till Omkrets och Area
Gör ett program som beräknar arean och omkretsen för en cirkel, när användaren anger radien.
1. Fråga användaren efter cirkels radie
2. Skriv ut cirkelns diameter
3. Skriv ut cirkelns area
4. Skriv ut cirkens omkrets
För att göra steg 3 & 4 behöver ni använda er utav pi. Detta har Python en funktion för, läs mer hur man använder modulen `math` i Python [här](https://docs.python.org/3/library/math.html#math.pi).
#### Bonus
5. Kontrollera att användare gör anger siffror, annars kommer ju programmet att krascha!

### Tidsskillnadsövning - Skillnad mellan två tider
Gör ett program som beräknar skillnaden mellan två tidpunkter på samma dag. Användaren anger först starttiden och sedan sluttiden.

Instruktioner:
1. Fråga användaren efter timmar och minuter för starttiden.
2. Fråga användaren efter timmar och minuter för sluttiden.
3. Beräkna skillnaden mellan dessa två tider i sekunder.
4. Skriv ut den beräknade tidsskillnaden i sekunder.

Exempel på hur resultatet kan se ut:
Om användaren anger starttiden 12:30 och sluttiden 14:45, ska programmet skriva ut skillnaden i sekunder, t.ex.:

```python
Starttid (timmar): 12
Starttid (minuter): 30

Sluttid (timmar): 14
Sluttid (minuter): 45

Skillnad i sekunder: 8100
```
