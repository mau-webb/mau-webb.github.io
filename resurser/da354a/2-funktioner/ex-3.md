---
id: da354a
title: "Modul 2 - Funktioner"
---

# Modul 2 - Funktioner

## Att returnera värden

#### Rekommenderad läsning

- [Think Python - Chapter 3  Functions](http://greenteapress.com/thinkpython2/html/thinkpython2004.html)

### Inledning

Nu när vi kan skriva funktioner, som dessutom kan ha parametrar, så ska vi titta på hur funktioner kan returnera värden. Hittills har vi kört en funktion - funktionen har gjort någon beräkning och sedan skrivit ut resultatet. Det är inte alltid så smidigt att sjävla utskriften sker inuti funktionen - då man ibland vill variera hur utskriften ska se ut eller helt enkelt arbeta vidare med det resultat som funktionen beräknat. Detta kan man lösa genom att funktionen _returnerar_ ett värde.

Exempel: låt säga att vi vill låta användaren beräkna arean av en rektangel. Då skulle det vara smidigt om vår funktion `area` skulle göra beräkningen och sedan skicka tillbaka resultatet av beräkningen till oss - så att vi kan göra vad vi vill med resultatet, t.ex. skriva ut det. Se följande exempel:

```python
def area(height, width):
    '''
		Funktionen returnerar arean för en rektangel
     '''
    return height * width

print("-" * 20)
print("Vi beräknar arean av en rektangel")
print("-" * 20)
h = int(input("Vad är höjden på rektangeln? "))
w = int(input("Vad är bredden på rektangeln? "))
result = area(h, w)
print("Arean är: " + str(result))
```

Resultatet av beräkningen `area(h, w)` sparas i variabeln `result`. När man kör koden ovan får man följande resultat:

![](images/idle7.png)

### Övning 1 - Välkomstfunktion

Vi ska nu göra en funktion som frågar efter besökarens namn och sedan returnerar namnet (det som användaren skriver in). Funktionen ska heta `get_name` och inte ha någon parameter. Ni ska skriva funktionen så att den fungerar med följande kod:

```python
name = get_name()
print("*"*30)
print("Hej " + name + "!")
print("Vad kul att du vill köra mitt program!")
```

Resultatet kan se ut såhär:

![](../images/idle10.png)

### Övning 2 - Fahrenheit till Celcius

Vi ska nu vända på formeln (jämfört med övningen i förra avsnittet) och omvandla Fahrenheit till Celcius. Formeln för detta är `(fahrenheit  -  32)  *  5/9 = celcius`. Funktionen ska heta `fahrenheit_to_celcius` ha en parameter, `fahrenheit`. Funktionen ska omvandla de grader Fahrenheit som skickas till den, och returnera resultatet i Celcius. För att dubbelkolla så att funktionen fungerar som den ska så kan ni kalla på funktionen med följande kod:

```python
print("20° Fahrenheit är " + str(fahrenheit_to_celcius(20)) + "° Celcius")
print("50° Fahrenheit är " + str(fahrenheit_to_celcius(50)) + "° Celcius")
print("Din tur att välja")
fahrenheit = int(input("Antal grader i Fahrenheit: "))
print(str(fahrenheit) + "° Fahrenheit är " + str(fahrenheit_to_celcius(fahrenheit)) + "° Celcius")
```

Resultatet kan se ut såhär:

![](../images/idle8.png)

### Övning 3 - Yards till meter

Vi ska nu bygga en funktion som omvandlar yards till meter. En yard är 0,9144 meter. Funktionen ska heta `yards_to_meters` ha en parameter: `yards`. Funktionen ska returnera antalet meter. Ni ska (på samma sätt som övning 2) fråga användaren efter antalet yards som ska omvandlas och sedan använda er av funktion `yards_to_meters` för att göra själva omvandlingen. Resultatet ska se ut såhär:

![](../images/idle9.png)