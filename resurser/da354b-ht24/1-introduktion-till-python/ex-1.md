---
id: da354b-ht24
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

Om du sitter vid en egen dator så behöver du installera Python och IDLE. Ni laddar ner Python [här](https://www.python.org), notera att det är <b>versionen 3.13.*</b> (eller den senaste versionen som släppts) som ni ska ladda ner och installera.

När du installerar python, var noga med att **kryssa i rutan** för *Add python to PATH*
{: .info}

### Installera Python (datorsal)

Python är installerat i datorsalarna, det bara att starta IDLE.

### Visual Studio Code - utvecklingsmiljön

När Python är installerat så ska ni bekanta er med Visual Studio Code (VS Code) då det är här som ni kommer att skriva och köra er Python-kod. VS Code är en modern och kraftfull kodeditor som används av många professionella utvecklare. 

1. Ladda ner och installera VS Code från [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Installera Python-tillägget i VS Code:
   - Öppna VS Code
   - Klicka på Extensions-ikonen i sidomenyn (eller tryck Ctrl+Shift+X, alternativt Cmd+Shift+X på Mac)
   - Sök efter "Python"
   - Installera tillägget från Microsoft

![VS Code med Python-tillägget](../images/vscode-python-extension.png)

För att testa att allt fungerar, skapa en ny fil och spara den med ändelsen `.py`. Skriv sedan följande kod:

```python
print("My first line of Python code!")
print(7 + 12)
print(5 > 4)
print("The sum of 5 & 2 is: ", 5 + 2)
```

För att köra koden kan du:
- Klicka på "play"-knappen i övre högra hörnet
- Högerklicka i editorn och välja "Run Python File in Terminal"
- Använda kortkommandot Ctrl+F5

![VS Code med Python-kod och körningsresultat](../images/vscode-running-python.png)

Skulle ni få upp ett felmeddelande så har ni antagligen missat en bokstav/tecken någonstans (t.ex. ett citat-tecken). VS Code hjälper er genom att markera fel direkt i koden med röda understrykningar.

![VS Code felmeddelande](../images/vscode-error-example.png)

### Att skriva Python-kod i VS Code

VS Code erbjuder många användbara funktioner för Python-utveckling:
- Automatisk kodkomplettering
- Felmarkering i realtid
- Inbyggd debugger
- Integrerad terminal

### Organisera ditt arbete

Innan du börjar koda är det bra att skapa en dedikerad mapp för kursen:

1. Skapa en mapp på din dator (t.ex. "python-programmering")
2. Öppna VS Code och välj "File > Open Folder" (eller Ctrl+K Ctrl+O)
3. Välj den mapp du just skapade
4. Nu kan du se mappstrukturen i VS Codes filutforskare (sidopanelen till vänster)

Det rekommenderas att du skapar undermappar för varje modul eller tema, till exempel:
```
python-programmering/
    modul-1/
        program.py
        ovning1.py
    modul-2/
        ...
```

Detta gör det enklare att:
- Hitta dina filer senare
- Hålla ordning på olika övningar
- Arbeta med flera filer samtidigt
- Återkomma till tidigare kod för repetition

För att skapa en ny Python-fil:
1. Högerklicka på önskad mapp i filutforskaren
2. Välj "New File"
3. Ge filen ett namn med ändelsen `.py`


### Mer information om VS Code

Läs mer om VS Code i [denna guiden](../../vs-code).

### Övningsuppgift

* Skapa en ny Python-fil i VS Code och spara den som `program.py`
* I din fil skriv följande:
```python
print("Hej och välkommen till mitt program!")
print("-" * 25)
print("Summan av 5 & 2 är: ", 5 + 2)
```
* Spara filen (Ctrl+S) och kör den genom att klicka på play-knappen eller använda Ctrl+F5

När du kör din kod ska resultatet visas i den integrerade terminalen, ungefär såhär:

![VS Code körning av övningsuppgift](../images/vscode-exercise-example.png)

Tänk på att det är viktigt att filen slutar på **py**, t.ex. *program.py*
{: .info}


### Funktionen "print"

Funktionen **print** skriver ut valda *saker* i terminalfönstret. *Sakerna* som skrivs ut kan vara av olika datatyper, t.ex. text (strängar), siffror (tal) eller true/false (booleans). Vi väljer alltså vad som ska visas för användaren i terminalen när filen körs genom funktionen **print**.

Testa att skriva i din fil:

```python
2 + 5
print(2 + 5)
```

**Vad är skillnaden i exemplen ovan - och vad händer på respektive kodrad?**
- På första raden utförs beräkningen men inget visas i terminalen
- På andra raden utförs beräkningen och resultatet skrivs ut i terminalen med hjälp av print-funktionen
