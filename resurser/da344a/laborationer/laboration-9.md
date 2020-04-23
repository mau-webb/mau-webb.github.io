---
id: da344a
title: "Laboration 9"
---

# Laboration 9: Utvecklingsmetodik

Välkommen till labb 9! Idag ska vi leka lite med git, npm, Webpack och testverktyget Jest. Dessutom, som en bonus, ska du få använda dig av ett terminalfönster! Wohoo!

![gif1](../images/giphy.gif)

Undvik att kopiera kommandona nedan. Skriv av dem istället. Det hjälper dig med din inlärning, även om det känns fruktansvärt onödigt.

**Viktigt att veta:** Jag kommer att använda ordet *katalog* nedan. Det är synonymt med ordet *mapp* som används på Windows. Samma sak, olika ord. Bli inte förvirrad. Anledningen till detta är att det är den svenska översättningen av *directory*, som är den vanliga Unix-beteckningen på kataloger, och används friskt senare i laborationen.

Det här blir roligt!

/Johan

---

## Förberedelser

Kör du på egen dator? Gott, då får du vackert börja med att installera tre programvaror.

---

### Installera Git

Git är verktyget vi använder för versionshantering.

#### Windows

Ladda ner [installationsfilen](https://git-scm.com/download/win) och kör den. Installationen är ganska rättfram.

#### macOS

Det bästa sättet att installera Git på är med verktyget **Homebrew**, som är en pakethanterare för macOS. Öppna upp ett terminalfönster och kör följande kommando:

``` bash
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ brew doctor
```

Homebrew kommer nu att installeras tillsammans med några trevliga utvecklingsverktyg. Låt det köra klart, och kör sedan

``` bash
$ brew install git
```

#### Ubuntu

Öppna ett terminalfönster och skriv följande:

``` bash
$ sudo apt install git
```

---

### Installera Node.js

Med Node.js kan vi göra en herrans massa häftiga saker i JavaScript. Det vi är ute efter i den här labben är framförallt npm, som ingår i Node.js. Med npm kan vi göra häftiga saker som att jobba med externa JavaScript-moduler.

#### Windows

Gå till [nedladdningssidan för Node.js](https://nodejs.org/#download) och ladda ner installationsfilen. Dubbelklicka på filen när den är nedladdad för att installera.

#### macOS

Om du installerade Homebrew ovan, kan du nu använda samma metod för att installear Node.js. Öppna terminalen och skriv:

``` bash
$ brew install node
```

#### Ubuntu

Öppna upp terminalen och skriv

``` bash
$ sudo apt install nodejs npm
```

**Att tänka på om du kör Ubuntu:** På grund av en namnkrock, kallas kommandot för Node.js för *nodejs*, istället för *node* på andra plattformar. Om du stöter på kommandot *node*, byt helt enkelt ut det mot *nodejs*.

---

### Installera Atom

Atom är en vanlig kod-editor. Den har dessutom inbyggt stöd för git.

#### Windows

Gå in på [atom.io](https://atom.io) och ladda ner installationsfilen. Dubbelklicka och installera.

#### macOS

Öppna ett terminalfönster och skriv

``` bash
$ brew cask install atom
```

#### Ubuntu

Öppna upp terminalen och skriv

``` bash
$ sudo snap install atom
```

---

## Del 0: Lär känna terminalen

Här ska vi lära oss att använda oss av terminalen, som är ett fantastiskt verktyg.

---

### Starta terminalen

Öppna ett terminalfönster och gör dig redo för lite terminalarbete. Det här är kul!

#### Windows

Tryck på Windows-knappen och sök efter **Git BASH**. Öppna den.

#### macOS

Öppna Spotlight och sök efter **Terminal**. Öppna den

#### Ubuntu

Öppna terminalen genom att trycka ner `ctrl + alt + t`.

---

### En väldigt kort introduktion till terminalen

Vad är det nu du har blivit inlurad i? Ett terminalfönster? Yes. Förr, när det ibland var bättre, använde vi terminalen och kommandoraden mer än vi gör än idag. Den är fortfarande ett kraftfullt verktyg, som du kommer att få se i den här laborationen.

Det du ser framför dig är en terminal som kör kommandotolken *Bash*. Terminalen och Bash ger dig möjlighet att göra en massa saker som är svåra att få överblick över i ett grafiskt gränssnitt. Det går dessutom att skripta kommandon i terminalen på ett sätt som relativt få lyckats bra med i grafiska miljöer (Apples macOS och hobbyoperativsystemet [Haiku](https://www.haiku-os.org/) är två exempel som lyckats med det, dock). Att arbeta med terminalen är fortfarande relativt vanligt, och väldigt effektivt, i Unix-baserade operativsystem som macOS och Linux. På senare år har även Windows börjat använda det mer igen, främst i form av *PowerShell*.

![Johans terminalfönster](../images/terminal.png)

Min terminal (jag kör Linux-varianten Ubuntu) ser ut så här. Din ser troligtvis lite annorlunda ut, men fungerar på precis samma sätt som min.

#### Hur ett Bash-kommando läses och skrivs

I den här anvisningen kommer du att få se saker som det här:

``` bash
$ touch filename
```

Det ser konstigare ut än vad det är. Dollartecknet $ innebär helt enkelt att det här är ett kommando som du skriver in i terminalen. Du skriver inte ut själva dollartecknet, det finns redan i terminalen om du tittar noga. `touch filename` är ett *kommando*, som består av namnet på ett program, följt av en parameter. Du kommer även att stöta på kommandon med fler parametrar än bara en, samt kommandon helt utan parametrar. Just det här kommandot betyder "skapa en tom fil som heter *filename*". Programmet *touch* skapar alltså tomma filer.

När vi kör en del kommandon kommer vi att få en utskrift. Dessa ska du inte skriva in i din terminal, utan det görs av programmen som körs. I kodlistningar markeras dessa genom att inte föregås av ett $. I princip ser det ut så här:

``` bash
$ kommando parameter1 parameter2
det här är en utskrift
```

#### echo - Ett jätteenkelt kommando

Ditt första kommando är `echo`. Det skriver helt enkelt ut de parametrar som du ger till det. Vi testar:

``` bash
$ echo hej hopp
hej hopp
```

Mäktigt.

---

### Navigera filsystemet med Bash

#### pwd - var är jag någonstans?

Det andra kommandot du får lära dig är *pwd*, som står för *Print Working Directory*. Det berättar för dig var du befinner dig. Vi testar:

``` bash
$ pwd
/home/johan
```

Det här ser lite annorlunda ut, beorende på vilket operativsystem du kör, vilket språk du har valt och vilken version av ditt operativsystem du kör. På macOS kommer det till exempel troligtvis att stå `/User/dittnamn`, medan det på Windows troligtvis kommer att stå `c/Users/dittnamn` eller något liknande.

Det du ser är namnet på din hemkatalog. Här finns alla dina dokument, personliga inställningar och liknande.

#### ls - vad finns här?

Gott så. Nu vet vi var vi är. Men vad finns egentligen här? Vi *skulle* kunna öppna Utforskaren/Finder/Filhanteraren för att titta, men nu har vi trots allt en terminal. Genom att använda kommandot *ls*, som står för *LiSt files* kan vi lista de filer och kataloger som finns här. Så här ser det exempelvis ut hos mig:

``` bash
$ ls
admintoollogs           EvothingsStudio              projekt
Android                 examples.desktop             Publikt
AndroidStudioProjects   git                          shared
Arduino                 host                         sketchbook
Bilder                  Hämtningar                   Skrivbord
Diagram1.dia            IdeaProjects                 snap
Dokument                LICENSE.txt                  Steam
dotnet                  Mallar                       stuff
Downloads               mqtt-spy                     test
eclipse-workspace       Musik                        test.php
eddy                    packages-microsoft-prod.deb  ThirdPartyNotices.txt
elis                    programs                     Video
```

Oj, massor av saker! Vad är allt det här? Först och främst: Vi kan titta vidare genom att ge parametern *-l*. Bindestrecket betyder att det här är en *växel*, en lite speciell parameter som förändrar programmets beteende. Just växeln *l* berättar för *ls* att den ska lista filerna:

``` bash
$ ls -l
totalt 304
drwxrwxr-x  2 johan  johan     4096 Okt  9  2018 admintoollogs
drwxr-xr-x  3 johan  johan     4096 Okt 29  2018 Android
drwxr-xr-x  3 johan  johan     4096 Okt 30  2018 AndroidStudioProjects
drwxrwxr-x  7 johan  johan     4096 Dec 25 19:03 Arduino
drwxr-xr-x  3 johan  johan     4096 Maj  8 22:29 Bilder
-rw-rw-r--  1 johan  johan     2519 Okt 19  2018 Diagram1.dia
drwxr-xr-x  6 johan  johan     4096 Mar 20 09:36 Dokument
-rwxr-xr-x  1 johan  johan   105872 Dec  7 18:47 dotnet
drwxrwxr-x  2 johan  johan     4096 Mar  8 10:48 Downloads
```

Här kan vi se att några av filerna är kataloger (de har ett `d` först i den där konstiga listan med en massa `rwx`). Vi kan också se vem som äger filerna, hur stora de är och när de senast ändrades.

Om vi lägger till en växel till, *a*, kommer vi att lista *alla filer* i katalogen, även de som är dolda! Vi skriver:

``` bash
$ ls -la
totalt 684
drwxr-xr-x  86 johan  johan   4096 Maj  8 22:59 .
drwxr-xr-x   3 root   root    4096 Aug 27  2018 ..
drwx------   3 johan  johan   4096 Jan 17 11:58 .adobe
drwxr-xr-x   2 johan  johan   4096 Okt 23  2018 .advLdap
drwxrwxr-x   7 johan  johan   4096 Mar  8 16:26 .android
drwxrwxr-x   2 johan  johan   4096 Okt  9  2018 admintoollogs
drwxr-xr-x   3 johan  johan   4096 Okt 29  2018 Android
drwxr-xr-x   3 johan  johan   4096 Okt 30  2018 AndroidStudioProjects
drwxrwxr-x   7 johan  johan   4096 Dec 25 19:03 Arduino
drwxr-xr-x   3 johan  johan   4096 Maj  8 22:29 Bilder
-rw-rw-r--   1 johan  johan   2519 Okt 19  2018 Diagram1.dia
```

Nämen! Här är ju en massa nytt! Vad är det vi ser? Först ser vi två nya, konstiga kataloger: `.` och `..`. De är två speciella kataloger. Katalogen `.` betyder *den här katalogen*, medan katalogen `..` betyder *katalogen som finns ovanför den här*. Det här kommer vi att ha nytta av senare.

Vi ser även kataloger och filer vars namn föregås av en punkt, som *.android*. Dessa filer är normalt sett dolda för användaren, och används av program för att spara data som oftast är ointressanta för en vanlig användare. Eftersom vi är utvecklare, är vi inte längre vanliga användare, och har ibland nytta av att kunna se dem.

Vi kan även lista innehållet i andra kataloger än den vi är i just nu. Exempelvis kan vi lista innehållet i katalogen ovanför den vi står i nu genom att skriva

``` bash
$ ls ..
johan
```

#### cd - vi går någon annanstans

Nästa kommando du behöver lära dig är *cd*, som står för *Change Directory*. Med det kommandot kan du navigera i din dators filsystem. Vi kan börja med att gå upp en nivå i din filstruktur:

``` bash
$ cd ..
```

De där två punkterna är samma två punkter som vi stötte på när vi lekte med `ls -la`. Om vi nu testar att skriva `pwd` och `ls` kommer vi att få lite annorlunda utskrifter. Så här ser det ut hos mig:

``` bash
$ pwd
/home
$ ls
johan
```

Din utskrift kommer som vanligt att bero på vilket operativsystem du använder, samt vad du har för användarnamn. Gå tillbaka till din hemkatalog genom att skriva `cd användarnamn`- Så här ser det ut hos mig:

``` bash
$ cd johan
$ pwd
/home/johan
```

Om du skulle gå vilse, kan du alltid hitta hem genom att skriva bara `cd`. Du kan också navigera direkt till en katalog genom att skriva namnet på katalogen. Om jag exempelvis står i katalogen */home* och vill komma till */home/johan/projekt*, skriver jag helt enkelt:

``` bash
$ cd johan/projekt
$ pwd
/home/johan/projekt
```

Vi kan också alltid skriva in hela sökvägen till en katalog, oavsett var vi står. Om jag exempelvis skulle stå i katalogen */home/anton/Bilder/my_little_pony* och vilja gå till */home/johan/projekt*, skriver jag:

``` bash
$ cd /home/johan/projekt
$ pwd
/home/johan/projekt
```

OK, den sista: Ibland kanske du stöter på `~`. Det betyder *min hemkatalog*, precis som att `.` och `..` betyder *den här katalogen* och *överliggande katalog*. Med den kan du, som i exemplet ovan, skriva:

``` bash
$ cd ~/projekt
$ pwd
/home/johan/projekt
```

---

### Lite filhantering

Här kommer lite snabbt några kommandon som du kommer att ha nytta av. Go go, Ghostbusters!

#### mkdir - skapa en ny katalog

Vi skapar kataloger med kommandot *mkdir*, som står för *make directory*. Det följs av en parameter, som anger vad katalogen ska heta. Vi testar att skapa en katalog:

``` bash
$ mkdir projekt
```

Om du nu kör `ls` kommer du att se att du har en ny katalog som heter *projekt*. Passa på att navigera till din nya katalog:

``` bash
$ cd projekt
```

#### touch - skapa filer

Det här har vi redan gjort, men vi testar tillsammans ändå. För att skapa en tom fil använder vi kommandot `touch`. Om vi exempelvis vill skapa filen *bananflugor.txt*, skriver vi

``` bash
$ touch bananflugor.txt
$ ls
bananflugor.txt
```

#### cat - skriv ut innehållet i en fil

Med kommandot `cat` kan vi skriva ut innehållet i en fil. Vi testar:

``` bash
$ cat bananflugor.txt
```

Märk väl att du inte fick någon utskrift. Detta beror på att filen är tom. Vi kan lägga lite information i filen genom att använda `echo` från tidigare:

``` bash
$ echo "hallå!" >> bananflugor.txt
```

De båda `>>` betyder *ta utskriften och skicka den till*, vilket här innebär att vi skriver ut "hallå!" sist i filen *bananflugor.txt*. Praktiskt.

Om vi nu testar `cat` igen, kommer vi att få en roligare utskrift:

``` bash
$ echo "hallå!" >> bananflugor.txt
hallå!
```

#### cp - kopiera filer

Först och främst måste vi vara överens om en sak: kataloger är filer. I princip. De hanteras nästan alltid på samma sätt, utom när de skapas. När de kopieras, flyttas och döps om är de dock att betrakta som samma sak.

Vi kopierar filer genom att använda `cp`, som står för *CoPy file*. Du kan kopiera en eller flera filer, och kan även kopiera rekursivt, vilket kan vara bra att göra om du vill flytta en hel katalog. Ska vi börja med att skapa en kopia av *bananfluga.txt*? Ja, det ska vi!

``` bash
$ cp bananflugor.txt brandbil.txt
$ ls
bananflugor.txt  brandbil.txt
```

Vi kan också kopiera mellan olika kataloger:

``` bash
$ cp bananflugor.txt ..
$ ls ..
bananflugor.txt  projekt
```

Och så klart tillbaka igen:

``` bash
$ cp ../bananflugor.txt vogonpoesi.txt
$ ls
bananflugor.txt  brandbil.txt  vogonpoesi.txt
```

#### mv - flytta och döp om filer

Vi flyttar filer genom att använda `mv`, som står för *MoVe file*. Om vi vill flytta filen *brandbil.txt* upp en nivå gör vi så här:

``` bash
$ mv brandbil.txt ..
$ ls
bananflugor.txt  vogonpoesi.txt
$ ls ..
bananflugor.txt  brandbil.txt  projekt
```

[Vogonpoesi](https://en.wikipedia.org/wiki/Vogon#Poetry) är som bekant Universums tredje sämsta poesi, så om vi skulle vilja döpa om vår fil *vogonpoesi.txt* gör vi även det genom att använda `mv`:

``` bash
$ mv vogonpoesi.txt frukost.txt
$ ls
bananflugor.txt  frukost.txt
```

Slutligen kan vi flytta flera filer på en gång. Vi börjar med att skapa en ny katalog:

``` bash
$ mkdir trams
$ ls
bananflugor.txt  frukost.txt  trams
```

Nu kan vi enkelt flytta alla txt-filer till *trams* genom att skriva

``` bash
$ mv *txt trams
$ ls
trams
$ ls trams
bananflugor.txt  frukost.txt
```

Asterisken (__*__) är ett *wildcard* och betyder *matcha alla strängar*. Således kommer _*txt_ att matcha alla filer som slutar på *txt*.

#### rm - ta bort filer

Slutligen tittar vi på hur vi tar bort filer. Det gör vi med `rm`, som står för *ReMove file*. Om vi exempelvis vill ta bort *brandbil.txt* från ovanliggande katalog skriver vi

``` bash
$ rm ../brandbil.txt
$ ls ..
bananflugor.txt  projekt
```

Vi kan också ta bort flera filer på en gång, precis som när vi kopierade filer ovan. Till skillnad från när vi kopierar, kan vi dessutom ange en lista över filer som vi vill ta bort. Om vi exempelvis vill ta bort alla filer i *trams* kan vi skriva:

``` bash
$ rm trams/bananflugor.txt trams/frukost.txt
$ ls trams
```

Vidare kan vi ta bort en hel katalog genom att använda växeln `r`, som står för *recursive*:

``` bash
$ rm -rf trams
$ ls

```

Det här kommandot tar även bort alla filer och kataloger som finns i *trams*, men eftersom vi tog bort dem tidigare, gör det i det här fallet ingen skillnad. Den extra växeln `f` betyder *force* och gör att du inte behöver bekräfta att varenda fil tas bort, vilket annars är förvalt när du tar bort något rekursivt.

---

## Del 1: Versionshantering med Git

Vi inleder med lite härlig versionshantering. I den här delen får du testa på att använda git i terminalen för att få en känsla för hur git verkligen fungerar. Längre fram i labben kommer du att få använda git genom Atom.

### Lokal git-använding

Det är i regel en bra idé att samla projekt som hör ihop på ett ställe. Jag har exempelvis skapat en katalog som heter *projekt/git-test*.

![En ny katalog](../images/new-directory.png)

#### Skapa ett nytt repository

Börja med att navigera till din nyskapade katalog. Här utgår jag från att jag står i min hemkatalog:

``` bash
$ cd projekt/git-test
$ pwd
/home/johan/projekt/git-test
```

Gott. Här ska vi skapa vårt först git-repository. Det gör du genom att skriva `git init`, och det ser ut så här:

``` bash
$ git init
Initierade tomt Git-arkiv i /home/johan/projekt/git-test/.git/
$ ls -la
totalt 12
drwxr-xr-x  3 johan  johan   4096 maj 9 00:21 .
drwxr-xr-x  3 johan  johan   4096 maj 9 00:20 ..
drwxr-xr-x  7 johan  johan   4096 maj 9 00:21 .git
```

Den där nya, spännande katalogen *.git* innehåller all information om ditt git-repository. **Rör inte den!** Överens? Bra.

Nu har du ett git-repository som väntar på att få användas. Vi ska inte låta det vänta särskilt länge.

#### Skapa en fil och versionshantera den

Vi skapar en fil här. Varför inte fortsätta på ingånget spår och skriva lite dålig poesi?

``` bash
$ touch vogonpoesi.txt
```

Öppna filen med valfri texteditor och kopiera in följande litterära mästerverk:

> Oooo fläskige fontanell, din smet bestryker mig.  
> Med slibbfalusker ur en guttubral skrafån,  
> Vid mina förfäders polyper vill jag skåda,  
> hur mjälla kakakläckans ögon smäktar i sin låda,  
> och eljest dränk min grämjelses garott med lim av torsk som aldrig förr.

Vogonpoesi är verkligen fruktansvärt.

Vi har nu en fil som finns i vår *arbetskopia*, men som ännu inte är versionshanterad. Detta kan vi se genom att köra kommandot `git status`:

``` bash
$ git status
På grenen master

Inga incheckningar ännu

Ospårade filer:
  (använd "git add <fil>..." för att ta med i det som skall checkas in)

        vogonpoesi.txt

inget köat för incheckning, men ospårade filer finns (spåra med "git add")
```

Säg till git att börja versionshantera filen genom att använda `git add`:

```bash
$ git add vogonpoesi.txt
$ git status
På grenen master

Inga incheckningar ännu

Ändringar att checka in:
  (använd "git rm --cached <fil>..." för att ta bort från kö)

        ny fil:        vogonpoesi.txt
```

Här hade vi även kunnat skriva `git add .` för att lägga till alla filer i den aktuella katalogen (glöm inte att `.` betyder *den här katalogen*).

Slutligen vill vi *checka in* filen så att den verkligen sparas som en *revision*:

``` bash
$ git commit -m "Lite vogonpoesi"
[master (rotincheckning) e6404b2] Lite vogonpoesi
  1 file changed, 5 insertions(+)
  create mode 100644 vogonpoesi.txt
$ git status
På grenen master
inget att checka in, arbetskatalogen ren
```

Så där. Nu är poesin sparad. Växeln `-m` anger att du vill lägga till ett meddelande till din incheckning.

#### Skapa en fil och undvik att versionshantera den

Ibland vill vi inte versionshantera filer. Det kan vara konfigurationsfiler med inloggningsuppgifter (dessa ska du aldrig versionshantera, det är att be om säkerhetsproblem), onödiga filer (som *node_modules* som vi kommer att stöta på senare) eller filer som ditt operativsystem eller din IDE skapar (exempelvis *.DS_Store* på macOS eller *.project* i Eclipse). Här ska vi dock skriva lite poesi som är lite för fin för att sparas. Vi skapar en ny fil:

``` bash
$ touch boye.txt
```

Öppna filen i valfri texteditor och skriv:

> Den mätta dagen, den är aldrig störst.  
> Den bästa dagen är en dag av törst.<br><br>
> Nog finns det mål och mening i vår färd -  
> men det är vägen, som är mödan värd.<br><br>
> Det bästa målet är en nattlång rast,  
> där elden tänds och brödet bryts i hast.<br><br>
> På ställen, där man sover blott en gång,  
> blir sömnen trygg och drömmen full av sång.<br><br>
> Bryt upp, bryt upp! Den nya dagen gryr.  
> Oändligt är vårt stora äventyr.  

Oerhört vackert. Dock, inget som vi vill versionshantera. Git kommer dock att tycka att vi borde göra det:

```bash
$ git status
På grenen master
Ospårade filer:
  (använd "git add <fil>..." för att ta med i det som skall checkas in)

    boye.txt

inget köat för incheckning, men ospårade filer finns (spåra med "git add")
```

Git sparar en lista över alla filer som den inte ska versionshantera i en fil som heter *.gitignore*. Lägg märke till den inledande punkten i filnamnet. Den finns inte från början, utan du måste skapa den för hand:

``` bash
$ touch .gitignore
```

Nu kan vi berätta för git att inte versionshantera *boye.txt* genom att skriva

``` bash
$ echo "boye.txt" >> .gitignore
$ cat .gitignore
boye.txt
```

Om vi nu kör en `git status` kommer git inte längre tycka att du ska versionshantera boye.txt, men däremot att den där *.gitignore* ser intressant ut:

``` bash
$ git status
På grenen master
Ospårade filer:
  (använd "git add <fil>..." för att ta med i det som skall checkas in)

    .gitignore

inget köat för incheckning, men ospårade filer finns (spåra med "git add")
```

Nu kan vi lägga till *.gitignore* och undvika att lägga till *boye.txt* genom att skriva

``` bash
$ git add .
$ git status
På grenen master
Ändringar att checka in:
  (använd "git reset HEAD <fil>..." för att ta bort från kö)

        ny fil:        .gitignore
```

Märk väl att boye.txt inte nämns längre. Git ignorerar helt enkelt den.

Vi checkar in och går vidare:

``` bash
$ git commit -m "Lade till .gitignore"
```

#### Uppdatera en fil

Nu har vi tre filer: en som versionshanteras, en som ignoreras och en som håller koll på vilka filer vi ignorerar. Om vi nu vill förbättra/försämra vogonpoesin öppnar vi *vogonpoesi.txt* i en texteditor och skrider till verket. Jag drar mitt strå till stacken och lägger till följande rad sist i dikten:

> I mina händer - enhörning.

Du gör förstås vilken förändring du vill. Det spelar ingen roll vad du gör (ändra en rad, lägg till en rad, ta bort en rad), så länge du faktiskt förändrar filens innehåll. Rör inte första raden dock, för den ska vi ändra tillsammans senare. Spara filen och stäng din texteditor igen. Om vi kör `git status` kommer git att påpeka att *vogonpoesi.txt* är förändrad:

``` bash
$ git status
På grenen master
Ändringar ej i incheckningskön:
  (använd "git add <fil>..." för att uppdatera vad som skall checkas in)
  (använd "git checkout -- <fil>..." för att förkasta ändringar i arbetskatalogen)

    ändrad:        vogonpoesi.txt

inga ändringar att checka in (använd "git add" och/eller "git commit -a")
```

Lägg till och checka in förändringarna:

``` bash
$ git add .
$ git commit -m "Förbättrade vogonpoesin"
[master 9af0168] Förbättrade vogonpoesin
  1 file changed, 2 insertions(+)
```

#### Jobba med grenar

Git är väldigt bra på att hantera parallella arbetsspår, kallade *grenar* eller *branches*. Här ska vi titta på hur vi jobbar med två spår.

Ponera att du får en potentiellt fantastisk idé kring hur du ska förbättra poesin, men att du inte riktigt vill göra dig av med den ursprungliga dikten. Då kan du skapa en *avgrening* med hjälp av `git branch`. Vi testar:

``` bash
$ git branch nytt_infall
```

Kommandot skapar en ny gren, som vi döper till *nytt_infall*. Märk väl att du fortfarande är kvar på grenen *master*, vilket vi ser om vi kör `git status`:

``` bash
$ git status
På grenen master
inget att checka in, arbetskatalogen ren
```

För att växla till en annan gren använder vi kommandot `git checkout`:

``` bash
$ git checkout nytt_infall
Växlade till grenen "nytt_infall"
$ git status
På grenen nytt_infall
inget att checka in, arbetskatalogen ren
```

Så där. Nu har vi två grenar, och kan bli lite kreativa. Öppna upp *vogonpoesi.txt* igen och lägg till lite mer text. Så här blev mina nya tillägg:

> Ehuru fröken Dingelfjas ämnar  
> Blåklocka

Lägg till förändringarna och checka in dem:

``` bash
$ git add .
$ git commit -m "Lade till två nya rader poesi"
```

Säkerställ att allt är rätt genom att köra `git status`.

Växla tillbaka till grenen *master*:

``` bash
$ git checkout master
Växlade till grenen "master"
```

Öppna *vogonpoesi.txt* i din texteditor. Lägg märke till att de två raderna som vi nyss skrev är borta.

![gif2](../images/giphy2.gif)

No worries! De finns så klart kvar, men i grenen *nytt_infall*.

Nu inser vi att den första raden i originaldikten inte har riktigt rätt klang. Öppna upp filen *vogonpoesi.txt* igen och byt ut punkten på första raden mot ett utropstecken. Så där ja. Perfektion. Spara filen och stäng din editor. Checka in förändringen:

``` bash
$ git add .
$ git commit -m "Perfektion."
[master 36cdbdf] Perfektion.
  1 file changed, 1 insertion(+), 1 deletion(-)
```

Nu har vi två versioner av samma dikt. Bra, fast vill vi egentligen inte slå samman dem till en?

#### Slå samman två grenar

Det är klart att vi vill! Som tur är, är git väldigt bra på att göra det. Vi använder kommandot `git merge` för att slå samman dem. Säkerställ att du står på grenen *master* och skriv sedan

``` bash
$ git merge nytt_infall
```

Nu blir det lite intressant. Du kommer att få upp ett fönster där du ska skriva in ett merge-meddelande. Det fungerar som incheckningsmeddelandena (eftersom sammanslagningen skapar en ny incheckning). Du kommer att få skriva ett meddelande i en annan texteditor än den du är van vid. Det här kan vara lite lurigt. Behöver du hjälp - glöm inte att du har handledare på plats!

---

##### Windows

Du kommer troligen att sitta med en mystisk texteditor som heter *vi*. Den är... Spännande. Skriv in ditt meddelande, och tryck sedan på `ESC`-tangenten. Skriv sedan *!wq* och tryck enter. Det betyder på *vi*-språk *skriv förändringar till filen och avsluta programmet*. Får du inte rätt på det, hojta till!

##### macOS

Du kommer troligen att sitta med en mystisk texteditor som heter *vi*. Den är... Spännande. Skriv in ditt meddelande, och tryck sedan på `ESC`-tangenten. Skriv sedan *!wq* och tryck enter. Det betyder på *vi*-språk *skriv förändringar till filen och avsluta programmet*. Får du inte rätt på det, hojta till!

##### Ubuntu

Du kommer troligen att sitta med texteditorn nano. Ändra meddelandet till vad du vill och tryck sedan `ctrl + o`för att skriva förändringarna till filen. Tryck sedan `ctrl + x` för att avsluta programmet.

---

När du sparat ditt meddelande får du upp följande meddelande:

``` bash
Slår ihop vogonpoesi.txt automatiskt
Merge made by the 'recursive' strategy.
  vogonpoesi.txt | 2 ++
  1 file changed, 2 insertions(+)
```

Dikten är nu sammanslagen och du kan öppna den i din texteditor. Säkerställ att alla förändringar du gjort finns i filen.

#### Ta bort en fil

Slutligen vill vi ta bort dikten. Det är ju trots allt riktigt dålig. Vi tar bort filen med `rm`:

``` bash
$ rm vogonpoesi.txt
$ git status
På grenen master
Ändringar ej i incheckningskön:
  (använd "git add/rm <fil>..." för att uppdatera vad som skall checkas in)
  (använd "git checkout -- <fil>..." för att förkasta ändringar i arbetskatalogen)

        borttagen:     vogonpoesi.txt

inga ändringar att checka in (använd "git add" och/eller "git commit -a")
```

I vanlig ordning måste vi checka in vår förändring:

``` bash
$ git add .
$ git status
På grenen master
Ändringar att checka in:
  (använd "git reset HEAD <fil>..." för att ta bort från kö)

        borttagen:     vogonpoesi.txt

$ git commit -m "Tog bort den fruktansvärda dikten"
master d9aacf2] Tog bort den fruktansvärda dikten
  1 file changed, 9 deletions(-)
  delete mode 100644 vogonpoesi.txt
```

Puh! Skönt, nu har vi bara [Karin Boyes](http://www.karinboye.se/verk/dikter/dikter/i-rorelse.shtml) vackra *I rörelse* kvar.

#### Vad hände egentligen?

Ja, vad hände? Vi skrev en dikt som vi versionshanterade och skrev en till som vi valde att inte versionshantera. Därefter fick vi ett kreativt infall och gjorde två olika versioner av dikten som vi sedan slog samman till en igen. Rörigt! Hur ska vi komma ihåg det? Det behövs inte, git gör det åt oss. Vi testar:

``` bash
$ git log
commit d9aacf2073de42268fb6348d7cdcddfe2c16d022 (HEAD -> master)
Author: Johan Holmberg <johan@idioti.se>
Date:   Thu May 9 01:51:49 2019 +0200

    Tog bort den fruktansvärda dikten

commit 56df78423de783584c15294f39825b0e28957bcd
Merge: 36cdbdf 8f8b24e
Author: Johan Holmberg <johan@idioti.se>
Date:   Thu May 9 01:37:20 2019 +0200

    Slog samman dikterna

commit 8f8b24eaefae37606367b164afd302b93a7dfcf7 (nytt_infall)
Author: Johan Holmberg <johan@idioti.se>
Date:   Thu May 9 01:35:11 2019 +0200

    Lade till två nya rader poesi

commit 36cdbdf122097ad30bbedf5e3093e28c2709fc36
Author: Johan Holmberg <johan@idioti.se>
Date:   Thu May 9 01:32:20 2019 +0200

    Perfektion.

commit 9af0168a055d92ca314affcf5948330160e34569
Author: Johan Holmberg <johan@idioti.se>
Date:   Thu May 9 01:10:29 2019 +0200

    Förbättrade vogonpoesin

commit 11128318c4188fd9901e8b74ac5e8d80de9f249d
Author: Johan Holmberg <johan@idioti.se>
Date:   Thu May 9 01:09:06 2019 +0200

    Lade till .gitignore

commit e6404b27cb4ffd8711bca7495a0bc7ebe916d5c9
Author: Johan Holmberg <johan@idioti.se>
Date:   Thu May 9 00:37:32 2019 +0200

    Lite vogonpoesi
```

Vackert, men svårläst. Vi kan även få git att rita en fin *graf* åt oss. Låtom oss testa:

``` bash
$ git log --graph
* commit d9aacf2073de42268fb6348d7cdcddfe2c16d022 (HEAD -> master)
| Author: Johan Holmberg <johan@idioti.se>
| Date:   Thu May 9 01:51:49 2019 +0200
| 
|     Tog bort den fruktansvärda dikten
|   
*   commit 56df78423de783584c15294f39825b0e28957bcd
|\  Merge: 36cdbdf 8f8b24e
| | Author: Johan Holmberg <johan@idioti.se>
| | Date:   Thu May 9 01:37:20 2019 +0200
| | 
| |     Slog samman dikterna
| | 
| * commit 8f8b24eaefae37606367b164afd302b93a7dfcf7 (nytt_infall)
| | Author: Johan Holmberg <johan@idioti.se>
| | Date:   Thu May 9 01:35:11 2019 +0200
| | 
| |     Lade till två nya rader poesi
| | 
* | commit 36cdbdf122097ad30bbedf5e3093e28c2709fc36
|/  Author: Johan Holmberg <johan@idioti.se>
|   Date:   Thu May 9 01:32:20 2019 +0200
|   
|       Perfektion.
| 
* commit 9af0168a055d92ca314affcf5948330160e34569
| Author: Johan Holmberg <johan@idioti.se>
| Date:   Thu May 9 01:10:29 2019 +0200
| 
|     Förbättrade vogonpoesin
| 
* commit 11128318c4188fd9901e8b74ac5e8d80de9f249d
| Author: Johan Holmberg <johan@idioti.se>
| Date:   Thu May 9 01:09:06 2019 +0200
| 
|     Lade till .gitignore
| 
* commit e6404b27cb4ffd8711bca7495a0bc7ebe916d5c9
  Author: Johan Holmberg <johan@idioti.se>
  Date:   Thu May 9 00:37:32 2019 +0200

      Lite vogonpoesi
```

![gif3](../images/giphy3.gif)

---

### GitHub

Nu kan du hantera git lokalt. Vi ska även titta på GitHub, sedan går vi över till testning och pakethantering.

#### Skapa ett konto

Om du inte redan har ett konto hos GitHub är det hög tid att du skapar ett sådant. Gå in på [GitHub](https://github.com/) och registrera dig. Fyll helt smidigt i formuläret på startsidan och gå vidare. Glöm inte att komma ihåg ditt lösenord!

![Signup for GitHub](../images/sign-up-github.png)

När du är klar får du ett mail som du måste öppna för att bekräfta ditt nya konto. Gör det.

#### Skapa ett repository

När du loggat in på GitHub möts du av din dashboard. Längst uppe till höger kan du välja att skapa ett nytt repository. Knappen ser ut så här:

![Knappen New](../images/new-button.png)

Klicka på den för att komma till nästa steg. Här får du ange lite uppgifter om ditt repository och projekt. Ge ditt repository namnet *testing-with-jest* (det kan egentligen heta vad som helst, men det blir enklare att hänga med i anvisningarna med det namnet). Gör det publikt (du kan ta bort det igen efter labben om du vill) och lägg till .gitignore *Node* (nu skapas en .gitignore som är väl anpassat för Node.js och npm). Du kan ocksÃ¥ välja en licens. Jag valde MIT, för att jag är en fin och altruistisk människa. Lägg till en beskrivning om du vill. **Var noga med att *INTE* klicka i *Initialize this repository with a README*!** Det ska se ut ungefär så här när du är klar:

![Johans nya repository](../images/create-repo.png)

Klicka på *Create repository* och vänta. Nu kommer du att skickas till ditt nya repository, som ser ut så här:

![Johans nya repository, steg 2](../images/repo-init.png)

Du ser två nya filer: *.gitignore* och *LICENSE*. Det är en bra start. Märk väl att GitHub tycker att du ska lägga till en README-fil. Det ska vi göra senare, men inte just nu.

#### Klona ditt repository

Gå tillbaka till din terminal och säkerställ att du står i din projektkatalog. Står du kvar i poesi-katalogen går du upp en nivå. Nu ska vi nämligen skapa ett nytt lokalt repository genom att klona vårt repository från GitHub. Börja med att kopiera webaddressen till ditt repository. Mitt, exempelvis, finns på [https://github.com/koddas/testing-with-jest](https://github.com/koddas/testing-with-jest). Var noga med att använda ditt egna repository, och inte använda mitt. Nu klonar du ner ditt repository genom att skriva

``` bash
$ git clone https://github.com/koddas/testing-with-jest
Klonar till "testing-with-jest"...
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Packar upp objekt: 100% (4/4), klart.
```

Nu har du en ny katalog att leka med:

``` bash
$ ls
git-test  testing-with-jest
$ cd testing-with-jest
$ ls -la
totalt 20
drwxr-xr-x  3 johan  johan   4096 maj 9 02:25 .
drwxr-xr-x  4 johan  johan   4096 maj 9 02:25 ..
drwxr-xr-x  8 johan  johan   4096 maj 9 02:25 .git
-rw-r--r--  1 johan  johan    914 maj 9 02:25 .gitignore
-rw-r--r--  1 johan  johan   1071 maj 9 02:25 LICENSE
```

#### Skapa en fil och hämta hem den

Lite tidigare konstaterade vi att GitHub tyckte att vi skulle ha en README-fil. Det är en bra idé. Gå tillbaka till GitHub och klicka på knappen *Add a README*.

![Här finns knappen Add a README](../images/repo-init.png)

Skriv någon text. Jag försöker föregå med gott föredöme och skriver inte bara dumheter:

![Johans README.md](../images/add-readme.png)

Den här filen versionshanteras också, så du kommer att behöva ange ett incheckningsmeddelande. Lyckligtvis har GitHub ett förvalt sådant: *Create README.md*. Det duger alldeles utmärkt, så klicka på *Commit new file*.

Så här ser det ut:

![Johans incheckningsmeddelande](../images/commit-message.png)

Nu har du en extra fil och en ny revision:

![En ny fil](../images/with-readme.png)

Gå nu tillbaka till din terminal och gör dig beredd på att hämta hem den nya filen med hjälp av `git pull`. Det som kommer att hända är att git kommer att kontakta GitHub för att se om det finns några nya revisioner som du inte har. Gör det till en vana att köra det här kommandot innan du själv skickar upp nya förändringar till ditt GitHub-repository. Det kommer att spara dig mycket huvudvärk.

``` bash
$ git pull
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Packar upp objekt: 100% (3/3), klart.
Från https://github.com/koddas/testing-with-jest
    baefd5d..496ecab  master     -> origin/master
Uppdaterar baefd5d..496ecab
Fast-forward
  README.md | 5 +++++
  1 file changed, 5 insertions(+)
  create mode 100644 README.md
```

Om vi nu listar våra filer kommer du att se att du har fått en ny:

``` bash
$ ls
LICENSE  README.md
```

#### Uppdatera en fil och skicka upp den

Öppna filen README.md i en texteditor och skriv någon ny text. När du är klar sparar du ändringarna och avslutar programmet. Checka in förändringarna i vanlig ordning:

``` bash
$ git add .
$ git commit -m "Små förändringar till README.md"
[master 30e2c10] Små förändringar till README.md
  1 file changed, 1 insertion(+), 1 deletion(-)
```

Så där. Nu har du gjort förändringar i ditt lokala git-repository, men fortfarande inte skickat upp det till GitHub. Börja med att göra en `git pull` för att vara säker på att det inte gjorts några förändringar. Skriv sedan `git push` för att skicka dina förändringar. Nu måste du ange dina inloggningsuppgifter till GitHub. Jag hoppas att du inte glömt bort ditt lösenord. Så här ser det ut när jag gör min push:

``` bash
$ git pull
$ git push
Username for 'https://github.com': koddas
Password for 'https://koddas@github.com':
Räknar objekt: 3, klart.
Delta compression using up to 4 threads.
Komprimerar objekt: 100% (3/3), klart.
Skriver objekt: 100% (3/3), 360 bytes | 360.00 KiB/s, klart.
Total 3 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/koddas/testing-with-jest
    496ecab..30e2c10  master -> master
```

Öppna din GitHub-sida, ladda om den och klicka på *README.md*. Säkerställ att dina förändringar finns där.

---

## Del 2: Testning, paketering och pakethantering

I den här delen installerar vi några paket och använder dem för att skriva lite roliga tester.

### Förbered vårt projekt

Vi vill arbeta lite strukturerat, så vi börjar med att skapa tre nya kataloger: *dist* för vår leveransklara kod, *src* för vår kod och *tests* för våra tester:

``` bash
$ mkdir dist
$ mkdir src
$ mkdir tests
$ ls
dist  src  tests
```

### Skapa ett npm-projekt

Vi börjar i stor stil med att skapa ett npm-projekt. Vi fortsätter i projektet som vi skapade i del 1 (därav namnet *testing-with-jest*). Öppna terminalen och säkerställ att du står i *projects/testing-with-jest*. Skriv sedan `npm init` och fyll i uppgifterna. Ett par saker måste fyllas i exakt, annars är du fri att fylla i bäst du vill:
* package name: Tryck bara enter, så får du det förvalda *testing-with-jest*
* entry-point: src/index.js
* test command: jest tests
* git repository: Tryck bara enter, så snappar npm upp informationen från git direkt.

``` bash
$ npm init
This utility will walk you through creating a package.json file.
It only covers the most common items, and tries to guess sensible defaults.

See `npm help json` for definitive documentation on these fields
and exactly what they do.

Use `npm install <pkg>` afterwards to install a package and
save it as a dependency in the package.json file.

Press ^C at any time to quit.
package name: (testing-with-jest) 
version: (1.0.0) 
description: A Jest + npm lab session
entry point: (index.js) src/index.js
test command: jest tests
git repository: (https://github.com/koddas/testing-with-jest) 
keywords: 
author: Johan Holmberg
license: (ISC) MIT
About to write to /home/johan/projekt/testing-with-jest/package.json:

{
  "name": "testing-with-jest",
  "version": "1.0.0",
  "description": "A Jest + npm lab session",
  "main": "src/index.js",
  "scripts": {
    "test": "jest tests"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/koddas/testing-with-jest.git"
  },
  "author": "Johan Holmberg",
  "license": "MIT",
  "bugs": {
    "url": "https://github.com/koddas/testing-with-jest/issues"
  },
  "homepage": "https://github.com/koddas/testing-with-jest#readme"
}

Is this OK? (yes)
```

Det var mycket, men det är värt det. Testa att se vad som hänt genom att lista filerna:

``` bash
$ ls
dist  LICENSE  package.json  README.md  src  tests
```

Filen *package.json* innehåller projektinformationen och kommer snart att innehålla information om paketen. Det här är ett stort och viktigt steg som vi tagit, så vi passar på att checka in förändringarna:

``` bash
$ git add .
$ git commit -m "Skapade ett npm-projekt"
```

Vi behöver inte skicka upp något till GitHub just nu, så vi väntar med det. Ändringarna finns ändå sparade lokalt just nu.

### Importera en modul

Vi kommer att skapa en enkel webbsida som hanterar en stack i JavaScript. För att göra det enkelt för oss, vill vi använda oss av modulen [Underscore](https://underscorejs.org), som är en modul som bland annat ger oss ett gäng funktioner för att förenkla arbete med arrays. Installera den med

``` bash
$ npm install underscore
npm notice created a lockfile as package-lock.json. You should commit this file.
+ underscore@1.9.1
added 1 package from 1 contributor and audited 1 package in 0.931s
found 0 vulnerabilities
```

npm tycker att vi ska checka in filen *package-lock.json*, så det får vi göra. Den här filen håller koll på förändringar i våra installerade moduler. Checkar vi inte in den, kan npm senare börja bete sig dåligt, och det vill vi så klart inte.

Innan vi checkar in förändringarna, tar vi och tittar på vad vi faktiskt har gjort. Kör en `ls` och se vad osm hänt:

``` bash
$ ls
dist  LICENSE  node_modules  package.json  package-lock.json  README.md  src  tests
```

Vi ser att vi har en ny fil *package-lock.json*, som vi redan pratat om, och *node_modules*. Den här katalogen innehåller alla nyinstallerade moduler. Den vill vi definitivt inte versionshantera. Eftersom vi tidigare valde att skapa en *.gitignore* för Node behöver vi inte bry oss om det; git struntar redan i det:

``` bash
$ git status
På grenen master
Din gren är à jour med "origin/master".

Ospårade filer:
  (använd "git add <fil>..." för att ta med i det som skall checkas in)

        package-lock.json
        package.json

inget köat för incheckning, men ospårade filer finns (spåra med "git add")
```

Checka in förändringarna innan vi går vidare:

``` bash
$ git add .
$ git commmit -m "Lade till Underscore"
[master 9faed26] Lade till Underscore
  2 files changed, 35 insertions(+)
  create mode 100644 package-lock.json
  create mode 100644 package.json
```

### Installera Webpack

Vi kommer att använda oss av Webpack för att paketera vår applikation. Först måste vi förstås installera det, så vi går till vår kära terminal och skriver

``` bash
$ npm install webpack --save-dev
$ npm install webpack-cli --save-dev
```

Växeln `--save-dev` berättar för npm att webpack inte är en del av själva projektet, utan bara ett hjälpmedel som behövs under utvecklingen.

Nu skapar vi en konfigurationsfil för Webpack så att vi senare kan bygga vår applikation. Den heter *webpack.config.js* och innehåller följande:

``` js
const path = require('path');

module.exports = {
    entry: './src/index.js',
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'bundle.js'
    }
};
```

Direktivet *entry* berättar vi för webpack att vi kommer att ha en huvudfil som heter *src/index.js*. Det är från denna som Webpack kommer att utgå när den bygger den färdiga leverabeln. Vi berättar också med direktivet *output* att vi vill spara leverabeln i katalogen *dist* med filnamnet *bundle.js*.

När vi är klara checkar vi in förändringarna:

``` bash
$ git add .
$ git commit -m "Lade till Webpack"
[master ab52a7f] Lade till Webpack
  3 files changed, 4091 insertions(+)
  create mode 100644 webpack.config.js
```

---

### Gå över till Atom

Tidigare i laborationstexten utlovades arbete med den eminenta editorn Atom. Nu är det dags. Starta Atom och öppna *projekt/testing-with-jest* genom att klicka på *File -> Open folder* och navigera sedan fram till katalogen. Din Atom-miljö ser nu ut ungefär så här:

![Johans Atom](../images/atom.png)

Till vänster har du en lista över projektets filer. I mitten har du en välkomstruta som du kan stänga ner. Längst ner till höger finns två intressanta knappar: *GitHub* och *Git*. Klicka på *Git*. Nu får du upp en panel där du kan hantera Git utan att använda terminalen. Neat. Du får så klart lov att fortsätta med terminalen om du vill, men det är inte längre något måste.

#### Utforska Git-panelen

Git-panelen är uppdelad i fyra delar:

* Unstaged Changes. Det här är de filer som blir rödmarkerade när du skriver `git status` i terminalen. Genom att markera dem och välja *Stage* i kontextmenyn (högerklicka på filerna) kör du samma kommand som `git add`.
* Staged Changes. Det här är de filer som blir grönmarkerade när du skriver `git status` i terminalen, vilket innebär att du kört `git add` på dem.
* Commit. Det här är incheckningsrutan. Skriv ditt incheckningsmeddelande och klicka på *Commit to master* för att checka in förändringarna till grenen *master*.
* Historiken. Här kan du se vad som gjorts tidigare, och gå tillbaka till tidigare revisioner. Klicka på en av revisionerna för att se vad som hände i den. Grönmarkerade rader är tillagda rader, rödmarkerade rader är borttagna rader.

Under Git-panelen finns två andra intressanta knappar: *master* och *Push 1*. Om du klickar på *master* kan du skapa och växla mellan grenar. Klickar du på *Push 1* kan du skicka dina förändringar till GitHub. Notera att de här knapparna byter text, beroende på vilken gren du står på och hur många incheckningar som inte skickats till GitHub än.

#### Utforska GitHub-panelen

GitHub-panelen ser intressantare ut än vad den är för oss. När du senare blir lite mer avancerad och börjar jobba med *pull requests*, kommer du att ha nytta av den här gottebiten. Under den här labben har du ingen nytta av den, dock.

---

### Skapa en enkel stack-modul

Öppna katalogen *src* genom att klicka på den i Atom. Högerklicka sedan på den och välj *New file*. Döp den nya filen till *stack.js*. Skriv in följande innehåll i den:

``` js
var _ = require('underscore');

let stack = [];

// Lägger ett element överst i stacken
exports.push = function (x) {
    stack.push(x);
};

// Returnerar det översta elementet i stacken och tar bort det
exports.pop = function () {
    return stack.pop();
}

// Returnerar det översta elementet i stacken
exports.peek = function () {
    return stack[0]; // Det här är medvetet felaktigt
}
```

Vi tar och bryter ner filen lite:

``` js
var _ = require('underscore');
```

Det här importerar modulen *Underscore.js*, som vi pratade om tidigare. Det här fungerar inte rakt av i webbläsaren, men det löser vi med hjälp av Webpack.

``` js
exports.push = function (x) {
    stack.push(x);
};
```

Moduler i JavaScript är enkla .js-filer som exponerar funktioner i en variabel som heter *exports*. Det vi gör här är helt enkelt att skapa en funktion *push* som vi exporterar. På samma sätt exporterar vi *pull* och *pop*.

Checka in *src/stack.js*, gärna med hjälp av Atom.

### Skapa en webbsida

Vi behöver så klart ha ett GUI för den också, så vi skriver ihop lite fantastisk HTML-kod till det. Skapa en fil som heter *dist/index.html* med följande innehåll:

```html
<!doctype html>
<html lang="en" dir="ltr">
    <head>
        <meta charset="utf-8">
        <script type="text/javascript" src="bundle.js"></script>
        <title>En stack</title>
    </head>
    <body>
        <h1>Här kan vi leka med en stack</h1>
        Stacken: <span id="top_of_stack">n/a</span><br>
        <button type="button" name="peek" id="peek">Vad finns överst på stacken?</button>
        <button type="button" name="pop" id="pop">Poppa stacken!</button>
        <button type="button" name="push" id="push">Pusha till stacken</button>
    </body>
</html>
```

Checka in HTML-dokumentet.

### Koppla samman stacken med HTML-dokumentet

För att få allt att snurra behöver vi bygga den där *src/index.js* som vi nämnde tidigare. Dess uppgift är att koppla samman stack-modulen med vårt HTML-dokument. Lägg särskilt märke till hur vacker uppdelningen är mellan logik och vy med den här lösningen. Som en extra bonus gör vi det här utan några ramverk. Yay us!

``` js
import * as stack from './stack.js';

window.onload = function () {
    console.log("done");

    var pop = document.getElementById('pop');
    var push = document.getElementById('push');
    var peek = document.getElementById('peek');
    var display = document.getElementById('top_of_stack');

    pop.addEventListener("click", function() {
        var text = "Tog bort " + stack.pop();
        alert(text);
    });

    push.addEventListener("click", function() {
        var x = prompt("Vad ska vi lägga på stacken?");
        stack.push(x);
        display.innerHTML = x;
    });

    peek.addEventListener("click", function() {
        display.innerHTML = stack.peek();
    });
};
```

Den första raden importerar alla tre funktioner (*pop*, *push*, *peek*) från vår stack-modul så att vi kan använda dem senare. Inte heller det här fungerar i webbläsaren, utan kräver en paketering. Testa ändå att öppna *dist/index.html* i en webbläsare och se vad som händer.

När du är klar, checka in filen.

### Bygg med Webpack

Nu ska vi äntligen bygga! Att bygga projekt med Webpack är förbaskat enkelt. Öppna upp din terminal och skriv `webpack` från projektroten:

``` bash
$ pwd
/home/johan/projekt/testing-with-jest
$ webpack
Hash: f99e49f9e7caecaff16c
Version: webpack 4.30.0
Time: 1164ms
Built at: 2019-05-09 05:19:16
    Asset      Size  Chunks             Chunk Names
bundle.js  19.3 KiB       0  [emitted]  main
Entrypoint main = bundle.js
[0] ./src/stack.js 456 bytes {0} [built]
[1] ./src/index.js 618 bytes {0} [built]
[3] (webpack)/buildin/global.js 472 bytes {0} [built]
[4] (webpack)/buildin/module.js 497 bytes {0} [built]
    + 1 hidden module
```

**Om du kör Windows:** Har du otur, kommer du inte att kunna köra `webpack`. Då får du skriva `node_modules/webpack-cli/bin/cli.js` istället för `webpack`.

Du ha nu fått en ny fil som heter *dist/bundle.js*, med vilken vårt projekt kommer att fungera. Gå till webbläsaren och ladda om *dist/index.html*. Testa att klicka på knapparna och se vad som händer. Fungerar den? Visst gör den det!

Men vänta lite nu... Vill vi versionshantera den där *bundle.js*? Är det inte bara något som genereras vid byggen? Helt rätt, den vill vi inte checka in. Därför:

### Ignorera bundle.js

Innan du gör något annat: titta under *Unstaged Changes* i Atom. Ser du *bundle.js* där? Bra, då har du gjort rätt.

Öppna upp *.gitignore*. Filen är full med en massa saker som vi vill ignorera, men inte just *dist/bundle.js*. Det löser vi genom att allra sist i filen skriva

``` bash
dist/bundle.js
```

Spara filen. Titta tillbaka under *Unstaged Changes*. Om du skrivit rätt har *bundle.js* nu ersatts av *.gitignore*. Flytta den till *Staged Changes* och checka in förändringen.

Puh! Nu har vi byggt en hel applikation med en extern modul, en intern modul och paketerat det med Webpack. Inte illa!

![gif4](../images/giphy4.gif)

### Importera testverktyget Jest

Nu är vi på slutspurten! Nu ska vi bara testa och se så att allt är rätt. Märkte du att knappen *Vad finns överst på stacken?* i själva verket visar vad som finns *underst* i stacken? Helt värdelöst! Det här borde vi ju ha testat innan.

För att kunna skriva enhetstester, den typ av tester som verifierar att en funktion eller liknande fungerar korrekt, måste vi först installera verktyget [Jest](https://jestjs.io).

``` bash
$ npm install --save-dev jest
```

Checka in förändringarna.

### Skriv två enhetstester

Jest är ett kompetent verktyg som kan göra en massa saker. Vi kommer dock bara att titta på enkla *assertions*. I princip innebär detta att vi skriver vad vi förväntar oss att utfallet från en operation ska vara med hjälp av *matchers*. Jest har [ett flertal sådana](https://jestjs.io/docs/en/using-matchers) som vi kan använda oss av.

Vi skapar en fil som heter *tests/stack.test.js*. Innehållet ser ut som följer:

``` js
const stack = require('../src/stack');

test('peek on empty stack returns undefined', () => {
    expect(stack.peek()).toBeUndefined();
});

test('peek on stack with one element returns that element', () => {
    stack.push(1);
    expect(stack.peek()).toBeDefined();
    expect(stack.peek()).toBe(1);
});

test('peek on stack with two or more elements returns the top element', () => {
    stack.push(1);
    stack.push("wow");
    stack.push(42);
    expect(stack.peek()).toBeDefined();
    expect(stack.peek()).toBe(42);
});
```

Vi ser här tre tester på funktionen *peek()*. Det första testar om funktionen returnerar *undefined* om stacken är tom. Det andra testar om en stack med minst ett element returnerar något annat än *undefined*. Det tredje testar om en stack med minst två element returnerar det översta elementet i stacken. Vi kör testerna genom att köra `npm run test`:

``` bash
$ pwd
/home/johan/projects/testing-with-jest
$ npm run test
```

Du kommer att få ett felmeddelande. Det är rätt! Titta noga på utskriften:

``` bash
FAIL  tests/stack.test.js
 ✓ peek on empty array returns undefined (6ms)
 ✓ peek on array with one element returns that element (2ms)
 ✕ peek on array with two or more elements returns the last element (4ms)
 
 ● peek on array with two or more elements returns the last element

   expect(received).toBe(expected) // Object.is equality

   Expected: 42
   Received: 1
   
     16 |   stack.push(42);
     17 |   expect(stack.peek()).toBeDefined();
   > 18 |   expect(stack.peek()).toBe(42);
        |                        ^
     19 | });
     20 | 
   
     at Object.toBe (tests/stack.test.js:18:24)

Test Suites: 1 failed, 1 total
Tests:       1 failed, 2 passed, 3 total
Snapshots:   0 total
Time:        2.345s
Ran all test suites matching /tests/i.
npm ERR! code ELIFECYCLE
npm ERR! errno 1
npm ERR! testing-with-jest@1.0.0 test: `jest tests`
npm ERR! Exit status 1
npm ERR! 
npm ERR! Failed at the testing-with-jest@1.0.0 test script.
npm ERR! This is probably not a problem with npm. There is likely additional logging output above.

npm ERR! A complete log of this run can be found in:
npm ERR!     /home/johan/.npm/_logs/2019-05-09T03_58_12_043Z-debug.log
```

Testutskriften säger att det tredje testfallet inte gick igenom. Jest har alltså hittat ett fel i vår kod. Mer specifikt är det rad 18 i testskriptet som fallerar, vilket låter oss veta att vår *peek()* inte alls hämtar det översta värdet i stacken. Det är bra.

Checka in testkoden, det är bra kod som vi definivt vill spara.

### Fixa till koden

Nu ska vi bara fixa till felet. Genom att titta på vad som händer i *peek()* i *stack.js*, ser vi att där minsann är ett fel:

``` js
exports.peek = function () {
    return stack[0]; // Det här är medvetet felaktigt
}
```

Vi vill ju egentligen skriva

``` js
exports.peek = function () {
    return _.last(stack);
}
```

Så klart.

Kör testerna igen:

``` bash
$ pwd
/home/johan/projects/testing-with-jest
$ npm run test
PASS  tests/stack.test.js
 ✓ peek on empty stack returns undefined (4ms)
 ✓ peek on stack with one element returns that element (1ms)
 ✓ peek on stack with two or more elements returns the top element (1ms)

Test Suites: 1 passed, 1 total
Tests:       3 passed, 3 total
Snapshots:   0 total
Time:        1.214s
Ran all test suites matching /tests/i.
```

Ja, men titta! Nu fungerar det ju! Gör ett nytt bygge med webpack:

``` bash
Hash: 7dc96d2add0abf15faca
Version: webpack 4.30.0
Time: 1327ms
Built at: 2019-05-09 06:11:41
    Asset      Size  Chunks             Chunk Names
bundle.js  19.3 KiB       0  [emitted]  main
Entrypoint main = bundle.js
[0] ./src/stack.js 389 bytes {0} [built]
[1] ./src/index.js 638 bytes {0} [built]
[3] (webpack)/buildin/global.js 472 bytes {0} [built]
[4] (webpack)/buildin/module.js 497 bytes {0} [built]
    + 1 hidden module
```

Testa i webbläsaren med, verifiera att det fungerar.

Checka in förändringarna i *src/stack.js*.

### Publicera resultatet på GitHub

Nu har vi varit förbaskat duktiga! Innan du får gå och äta lunch, ska du förstås publicera det här på GitHub. Du kan redan göra det från terminalen, men nu ska du göra det från Atom! Klicka på knappen *Push 9* under Git-historiken. Du kommer att få ange dina inloggningsuppgifter i vanlig ordning, men sen kommer det att hända saker. När Atom jobbat färdigt, byts *Push 9* ut mot *Fetch*, vilket är det samma som *pull*.

Vad gör du allra sist? Du går till ditt repository på GitHub. Nu är det vackert!

![Najs!](../images/github-finalized.png)