---
id: da354a-ht22
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


### Ytterliggare en övning
Gör ett program som beräknar arean och omkretsen för en cirkel, när användaren anger radien.
1. Fråga användaren efter cirkels radie
2. Skriv ut cirkelns diameter
3. Skriv ut cirkelns area
4. Skriv ut cirkens omkrets
För att göra steg 3 & 4 behöver ni använda er utav pi. Detta har Python en funktion för, läs mer hur man använder modulen `math` i Python [här](https://docs.python.org/3/library/math.html#math.pi).
#### Bonus
5. Kontrollera att användare gör anger siffror, annars kommer ju programmet att krascha!