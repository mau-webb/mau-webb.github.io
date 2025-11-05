---
id: da354b-ht25
title: "Modul 5 - Fil- och felhantering i Python"
---

# Modul 5 - Fil- och felhantering i Python

## 1. Fil- och felhantering i program

### Inledning

I denna övning ska vi bygga ett program, som ska fungera som övning 1 i förra modulen - alltså en filmsamling! Det är alltså dags att leta upp koden från förra veckans modul (eller skriva ny - det är upp till er). Vad progammet ska kunna göra (med exempel) hittar ni [här](/resurser/da354b-ht25/4-listor-och-lexikon/ex-1/#övningar), men kort sammanfattat ska man:

- Kunna lista alla filmer i filmsamlingen
- Kunna lägga till en ny film i filmsamlingen
- Kunna ta bort en film från filmsamlingen
- Kunna sortera filmerna i filmsamlingen

Dessutom tillsammans den **nya funktionen** att alla filmer sparas i en text-fil och läses in i programmet, när det startas upp.

Hur ni vill spara filmerna är upp till er - det kan vara med semikolon som separator, t.ex.

```
Star Wars;Fight club;American Beauty
```

Med radbrytningar som separator, t.ex.

```
Star Wars
Fight club
American Beauty
```

Eller varför inte spana in [JSON som format](https://www.w3schools.com/python/python_json.asp) - något som används flitigt idag för att strukturera upp data, t.ex.

```
[
    "Star Wars",
    "Fight club",
    "American Beauty"
]
```

### Förbättring av programmet

När ni är klara med den första delen så kan ni lägga in mer information om varje film, lämpligen **vilket år** filmer släpptes, samet vem som **regisserade** filmen. Återigen får ni välja hur ni vill spara filmernas information, men lämligen genom semikolon i kombination med radbrytningar:

```
Star Wars;1977;George Lucas
Fight club;1999;David Fincher
American Beauty;1999;Sam Mendes
```


Eller genom JSON, t.ex. på följade sätt:

```
[
    {
        "title": "Star Wars",
        "year": 1977,
        "director": "George Lucas"
    },
    {
        "title": "Fight club",
        "year": 1999,
        "director": "David Fincher"
    },
    {
        "title": "American Beauty",
        "year": 1999,
        "director": "Sam Mendes"
    }
]
```

### Exempellösningar

- [Förbättring av programmet, med ";" som separerare](../ex-solutions/Ö3.py)