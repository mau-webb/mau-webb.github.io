---
id: da354a-ht22
title: "Modul 4 - Listor & Lexikon"
---

# Modul 4 - Listor & Lexikon

## Listor & strängar

### Inledning

Som vi nu upptäckt så är listor väldigt smidiga att jobba med när man vill hantera större mängder data. Kunskap om listor är också väldigt bra att ha när det kommer till stränghantering. Vi kan på samma sätt som vi i övning 1 hämtade ett värde på plats x i en lista, hämta ett tecken på plats x från en sträng. Se följande exempel:

```python
name = "Anton"
print(name[0]) # Skriver ut "A"
print(name[1]) # Skriver ut "n"
print(name[2]) # Skriver ut "t"
print(name[3]) # Skriver ut "o"
print(name[4]) # Skriver ut "n"
```

Genom att ange ett index i strängen, så hämtar vi valt tecken från strängen. Detta medför vidare också att vi kan iterera över en sträng och på så sätt gå igenom alla tecken i en sträng. I följande exempel väljer vi att räkna antalet "e" i strängen "May the force be with you":

```python
quote = "May the force be with you"
nr_of_times = 0
# Itererar över alla bokstäver i strängen "quote"
for i in quote:
    # Om aktuell bokstav är "e"
    if i == "e":
        nr_of_times += 1
# Skriver ut vårt resultat
print(f"Bokstaven 'e' förekommer {nr_of_times} gånger")
```

En annan sak som också är ganska vanligt när man jobbar med strängar, är att man vill dela upp en sträng i flera bitar. Detta gör man i Python genom funktionen `split()`. Funktionen fungerar så att man delar (splittar) en sträng vid ett valt tecken. Vill man dela upp en sträng till ord så splittar man strängen vid " " (mellanslag). Det man får tillbaka av funktionen `split()` är då en lista med de uppdelade bitarna av strängen. Exempel:

```python
# Ger listan ["May", "the", "force", "be", "with", "you"]
"May the force be with you".split(" ")

# Ger listan ["gul", "blå", "röd"]
"gul, blå, röd".split(", ")

# Ger listan ["A", "to"]
"Anton".split("n")
```

Notera att de tecken som man väljer att splittra strängen vid *inte* returneras i listan. I och med att vi får tillbaka en lista med den uppdelade strängen går det utmärkt att iterara över listan om vi skulle vilja.

### Övningar

#### Övning 1 - Räkna ord i en mening

Den första uppgiften går ut på att ni ska räkna antalet ord i en mening genom funktionen `count_words(text)`. Funktionen ska som parameter ta emot en sträng (en mening förslagsvis) och funktionen ska sedan genom funktionen `split()` dela upp strängen till en lista med alla ord, och därefter returnera längden på listan. En exempelkörning skulle kunna se ut såhär:

![Ilde](../images/idle5.png)

#### Övning 2 - Rövarspråket

**Vi har gjort denna övning på en föreläsning tidigare - klarar du av att göra den själv nu?**

I denna övning så ska vi översätta en mening i svenska till [rövarspråket](http://sv.wikipedia.org/wiki/R%C3%B6varspr%C3%A5ket). Rövarspråket går kort och gått ut på att man efter varje konsonant lägger ett o (kort å-ljud) och därefter samma konsonant igen, till exempel byts b ut mot "bob" och f mot "fof". Vokalerna är förblir oförändrade. Till er hjälp får ni funktionen `isVowel(char)` där ni som argument skickar in en bokstav, så returnerar funktionen `True` om bokstaven är en vokal och `False` om det är en konsonant.

```python
def isVowel(char):
    return char.lower() in 'aeiouåäö'
```

Förväntad körning för anropet `print rovarsprak("hej på dig")` skulle kunna se ut såhär:

![Idle](../images/idle6.png)