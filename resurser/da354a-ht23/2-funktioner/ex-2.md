---
id: da354a-ht23
title: "Modul 2 - Funktioner"
---

# Modul 2 - Funktioner

## Argument och parametrar

#### Rekommenderad läsning

- [Think Python - Chapter 3  Functions](http://greenteapress.com/thinkpython2/html/thinkpython2004.html)

### Inledning

I den förra övningen så tittade vi på hur man skapar funktioner i Python och hur man på ett smidigt och effektivt sätt kan dokumentera funktionerna. De funktioner som vi byggde var dock statiska, i den mening att de gör exakt samma sak varje gång som de körs.

Vi ska i denna övningen titta på hur vi kan göra de funktioner som vi bygger mer dynamiska. Detta genom att _skicka med_ data till funktionerna som vi bygger. Den data som skickas från användaren när funktionen anropas kallas för _argument_ medan den data som tas emot av funktionen kallas för _parameter_. Ett snabbt exempel:

```python
def shout_out(text):
    """Tar en sträng som input och skriver ut den i versaler"""
    print(text.upper())

shout_out("Vi testar!")
shout_out("En gång till!")
```

I exemplet ovan så är `text` parametern till funktionen `shout_out` och `Vi testar` är argumentet när funktionen anropas. Variabeln/parametern `text`i funktionen representerar alltså det som skickas som argument till funktionen. Vi kör funktionen två gånger, första gången representerar `text` i funktionen strängen `"Vi testar!"` och andra gången strängen `"En gång till!"`. Kör vi koden ovan så ser det ut såhär:

![](../images/idle4.png)

## Övningar

### Övning 1 - Areafunktion

Vi ska nu bygga en funktion som räknar ut arean för en rektangel. Funktionen har två parametrar, `height` och `width` som multiplicerat med varandra resulterar i arean för rektangeln. Er uppgift är att skriva klart funktionen nedan så att den blir komplett.

```python
def area(width, height):
    """Funktionen beräknar och skriver ut arean för en rektangel"""
    # Er kod här

area(4, 5)
area(7, 12)
area(32, 23)
```

När ni skrivit klart funktionen ska resultatet vara:

![](../images/idle5.png)

### Övning 2 - Celcius till Fahrenheit

Vi ska nu bygga en funktion som omvandlar temperatur i Celcius till Fahrenheit. Formeln för detta är: `fahrenheit = celcius  *  9/5 + 32`. Er uppgift är att skriva funktionen `celcius_to_fahrenheit` som ska ta antalet grader i Celcius som en parameter och ska fungera med följande anrop:

```python
celcius_to_fahrenheit(0)
celcius_to_fahrenheit(15)
celcius_to_fahrenheit(30)
```

Och funktionens utskrifter ska se ut på följande sätt:

![](../images/idle6.png)