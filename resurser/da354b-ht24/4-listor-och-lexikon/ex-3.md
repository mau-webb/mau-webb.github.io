---
id: da354b-ht24
title: "Modul 4 - Listor & Lexikon"
---

# Modul 4 - Listor & Lexikon

## Introduktion till lexikon

### Inledning

I [introduktionen till listor](../ex-1) gick vi igenom hur man kunde spara data i listor, iterera över dessa listor och på så sätt underlätta hantering av större datamängder. Ett problem som ni kanske upptäckt i listor är att det inte alltid är så enkelt att plocka ut ett värde ut en lista, om man inte vet vad värdet är, eller den exakta platsen i listan som värdet har. Detta är ett av de problem som lexikon löser.

Ett lexikon är kort och gott en samling av *nycklar* och *värden*, där varje nyckel har ett värde. Ett bra och enkelt exempel är en telefonbok. I en telefonbok har man (simplifierat) ett namn (nyckel) som är kopplat till ett telefonnummer (värde). Skulle vi skapa en enkelt telefonbok (i form att ett lexikon) i Python skulle det kunna se ut såhär:

```python
# Skapar vår telefonbok
phone_book = {}

# Lägg till tre personer, med vars ett nummer
phone_book["Anton"] = "070-000000"
phone_book["Fredrik"] = "070-111111"
phone_book["Johanna"] = "070-222222"
```

Vi skapar alltså ett tomt lexikon genom `phone_book = {}` och lägger till våra kontakter genom att ange nyckel (namn på person) och värde (telefonnummer). Svårare än så är det inte att skapa ett lexikon!

Vill jag sedan skriva ut telefonnummret till Fredrik så anger jag helt enkelt bara nyckeln ("Fredrik") i vårt lexikon (phone_book), såhär:

```python
# Skriver ut det nummer som är kopplat till nyckeln "Fredrik"
print(phone_book["Fredrik"]) # Skriver ut "070-111111"
```

#### Iterera över ett lexikon

Det finns naturligtvis (precis som i listor) tillfällen när man vill skriva en alla nycklar/värden (eller både och) från ett lexikon. Detta sker på följande sätt med vår telefonbok:

```python
# Skriver ut alla nycklar som finns i vår telefonbok (alltså, namnen)
for name in phone_book:
    print(name)

# Skriver ut alla värden som finns i vår telefonbok (alltså, telefonnummer)
for name in phone_book:
    print(phone_book[name])

# Skriver ut alla nycklar och värden i vår telefonbok (namn och telefonnummer)
for name in phone_book:
    print(f"{name}: {phone_book[name]}")
```

Innan ni går vidare kan det vara bra att titta på [Pythons dokumentation](https://docs.python.org/2/tutorial/datastructures.html#dictionaries) kring just lexikon.

### Övningar

#### Övning 1 - Ett enkelt översättningslexikon

Ni ska skapa ett enkelt översättningslexikon och översätta ert favoritcitat från engelska till svenska. Ert lexikon ska då innehålla det engelska ordet som nyckel och det svenska ordet som värde. Ni ska sedan skapa funktionen `translate(words)` där man skickar in en lista med engelska ord och funktionen returnerar motsvarande ord i svenska, som en sträng. Ert lexikon behöver således endast innehålla de ord ni vill ha möjlighet att översätta (men i ett större perspektiv kanske en hel ordlista). T.ex. skulle följande körning:

```python
print(translate(["May", "the force", "be", "with", "you"]))
```

Ge följande resultat:

![Idle](../images/idle4.png)

#### Övning 2 - En filmsamling med betyg!

I förra övningen (med listor) byggde vi ett filmhanteringsprogram. Nu ska vi bygga ett liknande program, men även inkludera betygsättning. Detta genom ett lexikon där nyckeln är filmens titel och filmens betyg är värdet. Vi ska även här ha en bra struktur med en meny med följande alternativ:

1. Visa filmer
    - Sortera filmer kronologiskt
    - Sortera filmer efter bäst betyg
	- Sortera filmer efter sämst betyg
	- Sordera filmer i alfabetisk ordning
2. Lägg till en film (med betyg)
3. Ta bort en film (med betyg)
4. Avsluta programmet

I stort ser det alltså ut som ert program i förra övningen, ni kan antingen utgå från den koden och modifiera den så att den sparar filmerna i ett lexikon istället för en lista. Eller börja om från grunden om det är bekvämare.

Lycka till!