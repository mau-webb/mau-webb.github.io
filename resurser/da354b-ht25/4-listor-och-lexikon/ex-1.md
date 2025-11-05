---
id: da354b-ht25
title: "Modul 4 - Listor & Lexikon"
---

# Modul 4 - Listor & Lexikon

## Introduktion till listor

### Inledning

När man bygger lite större program än vad vi hittills gjort behövs smidiga sätt att spara all data som används i programmet. Ett bra alternativ är att göra detta är listor i Python. För att snabbt se värdet av listor inom programmering kan vi titta på ett snabbt exempel. Låt säga att vi vill spara fem (5) tal i vårt program. Det skulle kunna se ut så här:

```python
# Spara varje tal i en variabel
number1 = 5
number2 = 7
number3 = 2
number4 = 12
number5 = 4

# Spara alla tal i en lista
numbers = [5, 7, 2, 12, 4]
```

Som ni kan se så krävs det många fler rader kod om man ska spara varje tal individuellt i en variabel, jämfört med om vi sparar alla tal i en lista. Men den kanske största vinsten med listor är när vi vill skriva ut våra tal ovan:

```python
# Skriver ut varje tal
print(number1)
print(number2)
print(number3)
print(number4)
print(number5)

# Skriver ut alla tal i listan
for number in numbers:
    print(number)
```

Som ni kan se ovan behövde vi fem rader kod för att skriva ut talen när de ligger i separata variabler, men bara två rader när de låg i en lista. Tänk på att ju fler nummer vi vill spara - ju mer effektiv blir listan! Med andra ord - tänk om vi vill skriva ut alla studenter i denna kurs. Är de sparade i en lista kan vi med två rader kod skriva ut alla namn, det är smidigt!

Man kan naturligtvis också hämta bara ett värde från vår lista med nummer. Då måste vi dock veta på vilken plats i listan som värdet vi vill skriva ut på finns:

```python
# Spara alla tal i en lista
numbers = [5, 7, 2, 12, 4]

print(numbers[0]) # Skriver ut, 5
print(numbers[1]) # Skriver ut, 7
print(numbers[2]) # Skriver ut, 2
print(numbers[3]) # Skriver ut, 12
print(numbers[4]) # Skriver ut, 4
```

**Glöm inte!** Ni kommer väl ihåg att vi börjar räkna från **0** när det kommer till programmering?
{: .info}


### Listor och for-iteration

Något som går hand i hand i programmering är listor och for-iterationer. Som ni kan se ovan så använder vi oss utav en for-iteration när vi *gå igenom hela listan*, alltså varje sak som finns i listan. Hur fungerar då detta? Titta på följande exempel igen:

```python
# Spara alla tal i en lista
numbers = [5, 7, 2, 12, 4]

# Skriver ut alla tal i listan
for number in numbers:
    print(number)
```

- Varje gång for-iterationen går ett varv representerar variabeln **number** det värde som finns på nuvarande plats i listan (*numbers*), alltså:
    - Första varvet: number är *5*
    - Andra varvet: number är *7*
    - Tredje varvet: number är *2*
    - Fjärde varvet: number är *12*
    - Femte varvet: number är *4*
- Vi kan sedan för varje nummer som finns i listan göra vad vi vill i for-iterationen, t.ex. skriva ut numret, beräkna totalsumma, hitta högsta/lägsta värde osv.

### Bra funktioner vid listor

Det finns en del funktioner som är bra att känna till när man arbetar med listor i Pyhton, här presenteras några. *list* i rubrikerna nedan representerar en lista med saker, *x*, *i* representerar ett argument..

#### list.append(x)

Att lägga till saker sist i en lista. Det är inte alltid vi vet hur många saker vår lista ska innehålla, därför är det bra att kunna lägga till saker i efterhand, exempel:

```python
# Skapar en lista
students = []

# Lägger till tre studenter
students.append("Anton")
students.append("Fredrik")
students.append("Johanna")

# Skriver ut alla studenter i listan students
for student in students:
    print(student)
```

#### list.insert(i, x)

Ibland vill vi inte lägga till vår sak sist i listan, utan på en specifik plats som vi anger. Det gör vi genom funktionen *insert*. *i* avser platsen i listan där vi vill lägga till något och *x* avser det vi vill lägga till, exempel:

```python
# Skapar en lista med två studenter
students = ["Anton", "Johanna"]

# Lägger till "Fredrik" på plats [1] i listan (mellan "Anton" och "Johanna")
students.insert(1, "Fredrik")

# Skriver ut alla studenter i listan students
for student in students:
    print(student)
```

#### list.remove(x)

Vi vill ju naturligtvis också kunna ta bort saker från vår lista. Genom funktionen *remove* så anger vi värdet i listan som vi vill ta bort (t.ex. "Fredrik"). Skulle värdet man anger finnas fler än en gång i listan så tas endast det första värdet.

```python
# Skapar en lista med tre studenter
students = ["Anton", "Fredrik", "Johanna"]

# Tar bort "Fredrik" från vår lista
students.remove("Fredrik")

# Skriver ut alla studenter i listan students
for student in students:
    print(student)
```

#### list.pop()

Funktionen *pop* tar bort (och returnerar) det sista värdet i  vår lista.

```python
# Skapar en lista med tre studenter
students = ["Anton", "Fredrik", "Johanna"]

# Tar bort sista saken i vår lista ("Johanna") och berättar detta
removed_student = students.pop()
print("Raderat " + removed_student + " från listan")

# Skriver ut alla studenter i listan students
for student in students:
    print(student)
```

Testkör koden ovan med de olika list-exemplen. Det är viktigt att ni vet vad ni kan göra med listor och hur ni kan göra det i kommande övningar i denna modul. Ni kan se denna första övning som en *referens* till olika funktioner som kopplas till listor.
{: .info}

#### Fler funktioner

Det finns många fler bra funktioner att läsa på om kring listor. En bra start är att läsa [Pythons dokumentation](https://docs.python.org/2/tutorial/datastructures.html) kring listor.

Modulen `random` innehåller även flera hjälpsamma funktioner för just listor, till exempel:

```python
import random

# En exempellista att jobba med
data = list(range(10)) # Skapar en lista med 10 tal: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Väljer ut ett slumpmässigt valt element från listan
print(random.choice(data))

# Väljer ut tre slumpmässigt valda element från listan
print(random.sample(data, 3))

# Slumpar fram en ny ordning för elementen i listan
random.shuffle(data)

# Skriver ut listan
print(data)
```

### Övningar

Det kommer här att finnas fyra övningar som bygger på varandra, som till slut kommer att resultera i ett litet program som håller koll på vår filmsamling (med hjälp av en lista) - så gör övningarna i ordning för bästa resultat.

#### Del 1 - En filmsamling

Den första övningen går ut på att ni ska skapa en lista med filmer. Börja med att skapa en lista där ni lägger in fem filmtitlar. Ni ska sedan göra en funktion, `print_movies`, som som skriver ut alla filmer som ni har i er filmsamling. Utskriften ska se ut på följande sätt:

![Idle](../images/en-filmsamling.png)

#### Del 2 - Lägga/Ta bort till filmer

Börja med att skapa en meny med fyra alternativ:

1. Visa filmerna
2. Lägg till en film
3. Ta bort en film
4. Avsluta

Nu ska vi ge användaren möjlighet att lägga till/ta bort filmer i listan. Detta ska ske genom att ni skapar funktionerna `add_movie(title)` och `remove_movie(title)`vars syfte är att lägga till/ta bort en i listan.

- `add_movie(title)` ska lägga till filmen sist i listan
- `remove_movie(title)` ska ta bort angiven film från er lista

Exempelkörning:

![Idle](../images/till-och-fran-filmsamlingen.png)

#### Del 3 - Sortera utskrifen av filmerna alfabetiskt

Vi ska nu förbättra funktionen `print_movies` så att man kan välja i vilken ordning som filmerna ska skrivas ut i, användaren ska få tre val:

1. Kronologisk (i den ordning de blivit tillagda i listan)
2. Alfabetist - stigande
3. Alfabetist - fallande

Det kan vara bra att läsa på om Pythons funktion [sort()](https://wiki.python.org/moin/HowTo/Sorting) till denna delen.

Exempelkörning:

![Idle](../images/sortera-filmsamling.png)

#### Del 4 - Förbättrad "Lägga till film"-funktion

Ni ska nu förbättra er funktion `add_movie` så att denna funktion frågar användaren om man vill:

1. Lägga till filmen sist i listan
2. Lägga in filmen på en specifik plats i listan

När ni gjort detta har vi byggt en egen filmhanterare - och dessutom lärt oss grunderna kring listor!