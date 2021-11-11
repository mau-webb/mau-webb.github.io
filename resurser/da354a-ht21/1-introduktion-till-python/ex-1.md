---
id: da354a-ht21
title: "Modul 1 - Introduktion till Python"
---

# Modul 1 - Introduktion till Python

## 1.a. Bekanta dig med Python & IDLE

#### Rekommenderad läsning

- [Think Python - Chapter 1 The way of the program](http://greenteapress.com/thinkpython2/html/thinkpython2002.html)

### Bakgrund

Python är ett plattformsoberoende, dynamiskt, objektorienterat skriptspråk — lämpligt för såväl prototyputveckling som "tyngre" applikationer (Google, Nasa, Sun Microsystems och Spotify är några av användarna). Det finns tillgängligt för fri nedladdning på [https://python.org/](https://python.org/) och är förinstallerat på Mac OS X, liksom de flesta distributioner av Linux.

Vi kommer i denna kurs att använda oss utav Python 3.x, istället för Python 2.x. Python 2.x används fortfarande utbrett, men eftersom utvecklingen går framåt rör sig allt fler utvecklare mot Python 3.x, varav vi kommer att använda det i denna kurs. Python 2 &amp; 3 liknar varandra väldigt mycket i många aspekter, men Python 3 bröt bakåtkompabilitet vilket gör att en "spricka" har bildats mellan Python 2 &amp; 3.

Den officiella utvecklingsmiljön för Python heter IDLE och följer med installationspaketet. För att köra Python och IDLE behöver vi först installera det.

### Installera Python (egen dator)

Om du sitter vid en egen dator så behöver du installera Python och IDLE. Ni laddar ner Python [här](https://www.python.org), notera att det är <b>versionen 3.10.0</b> som ni ska ladda ner och installera.

### Installera Python (datorsal)

Python är installerat i datorsalarna, det bara att starta IDLE.

### IDLE - utvecklingsmiljön

När python och IDLE är installerade så ska ni bekanta er med IDLE då det är här som ni kommer att skriva och köra er Python-kod. Börja med att öppna IDLE - då kommer ni att mötas av ett fönster som ser ut såhär:

![Idle](../images/idle.png)
I IDLE kan man antingen direkt skriva in Python-kod, eller köra Python-kod (eller program) som man sparat i separata filer. För att se så att IDLE fungerar som det ska kan ni börja med att skriva in följande python-kod (föjt av ett enterslag efter varje rad):

```python
print("My first line of Python code!")
print(7 + 12)
print(5 > 4)
print("The sum of 5 & 2 is: ", 5 + 2)
```

Har ni skrivit av koden <i>exakt</i> som det står ovan, så borde det se ut på följande sätt:

![Idle](../images/idle2.png)

Skulle ni få upp ett felmeddelande (en röd text, se bild nedan) så har ni antagligen missat en bokstav/tecken någonstans (t.ex. ett citat-tecken). Dubbelkolla då vad ni skrivit in och försök igen (vi kommera att titta mer på felmeddelanden senare).

![Idle](../images/idle3.png)

---

### 1.b. Att skriva Python-kod i egna filer

Väljer du *New Window* i *File*-menyn får du ett nytt fönster som är Pythons egen editor. Här kan du skriva Python-kod och exekvera den. Trycker du på F5-tangenten eller väljer *Run Module* i fönstrets *Run*-meny kommer programmet att exekveras (efter att först ha frågat ifall du vill spara det). Resultatet ser du i IDLEs exekveringsfönster (eftersom Python-filer är ren text så är du självklart fri att använda vilket annat textredigeringsprogram som du vill, t.ex. [VS Code](https://code.visualstudio.com/)).

Vill du komma åt Pythons dokumentation kan du trycka på F1-tangenten. Då får du upp Python-dokumentationen antingen i ett eget dokumentfönster eller via nätet i en webbläsare (beroende på vilken datormiljö du använder). Under Tutorial hittar du kortare exempel och förklaringar på hur du skriver Python-kod. Under Python Library Reference finner du mer detaljerad information om nyckelord, inbyggda datatyper och standardbibliotek.

### Övningsuppgift

* Börja med att skapa en ny Python-fil (välj du *New Window* i *File*-menyn) och spara den som *program.py*
* I din fil skriv följande:
```python
print("Hej och välkommen till mitt program!")
print("-" * 25)
print("Summan av 5 & 2 är: ", 5 + 2)
```
* Spara filen & kör den sedan (F5)

När du trycker på F5 (och kör din kod i IDLE) så ser du att alla kod i din fil *program.py* körs, i den ordning som koden är skriven i. Det borde se ut såhär:

![idle](../images/idle4.png)

Tänk på att det är viktigt att filen slutar på **py**, t.ex. *program.py*
{: .info}


### Funktionen "print"

Funktionen **print** skriver ut valda *saker* i IDLE (det som visas blått i fönsterna ovan). *Sakerna* som skrivs ut kan vara av olika datatyper, t.ex. text (strängar), siffror (tal) eller true/false (booleans). Vi väljer alltså vad som ska visas för användaren i IDLE när filen körs genom funktionen **print**.

Testa att skriv i din fil:

```python
2 + 5
print(2 + 5)
```

**Vad är skillnaderna i exmeplen ovan - och vad händer på respektive kodrad?**

Testa gärna att skriva ut lite fler strängar och beräkningar i IDLE. När ni tycker att detta fungerar bra så gå vidare till nästa del av laborationen.
