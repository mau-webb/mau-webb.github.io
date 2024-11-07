---
id: da354b-ht24
title: "Modul 2 - Funktioner"
---

# Modul 2 - Funktioner

## Introduktion till funktioner

#### Rekommenderad läsning

- [Think Python - Chapter 3  Functions](http://greenteapress.com/thinkpython2/html/thinkpython2004.html)

### Inledning

```python
def my_function():
    # Do something
    return
```

__Notera__ att man inte (som t.ex. i JavaScript) använder `{` och `}` för att deklarera vad som tillhör en funktion, utan istället så bestämmer _indenteringen_ vilken kod som tillhör vilken funktion. Studerar vi exemplet ovan så ser vi att den kod som tillhör funktionen `my_function` är indenterad med 4st blankslag. Det är därför mycket viktigt att man har koll på sin indentering, inte bara för att man vill skriva tydlig och lättläst kod - utan för att det annars blir syntaxfel när man vill köra sitt program.

### En första funktion

För att se hur det fungerar att både skapa, och sedan köra en funktion, kommer här ett exempel. Funktion vi skapar döper vi till `welcome` och syftet med funktionen är helt enkelt att skriva ut en välkomnshälsning. Koden för funktionen är följande:

```python
def welcome():
    print("--------------------------------")
    print("  Välkommen till mitt program!  ")
    print("--------------------------------")
```

När man vill köra en funktion i Python skriver man namnet på den funktion som man vill köra. Vill vi köra funktionen `welcome` skriver vi alltså:

```python
welcome()
```

__Övning:__ Testa att kopiera in koden ovan i en egen Python-fil och kör sedan programmet i IDLE för att se så att funktionen körs som förväntat.

### Dokumentera sina funktioner

Det är ofta bra att dokumentera sin kod i form utav kommentarer, så att man har koll på vad en viss del kod gör i sitt program. I Python kan man även dokumentera vad en funktion gör, vilket är smidigt när man snabbt behöver kolla upp en funktion (utan att behöva gå igenom koden). Detta gör man genom tre enkla citat-tecken `'''` följt av en kommentar och avslutar sedan med ytterliggare `'''`. Skulle vi kommentera vår funktion som vi skrev ovan skulle det kunna se ut såhär:

```python
def welcome():
    '''
        Funktionen skriver ut ett välkomstmeddelande till besökaren
    '''
    print("--------------------------------")
    print("  Välkommen till mitt program!  ")
    print("--------------------------------")
```

Vill vi sedan (när vi kör programmet i IDLE) ta reda på vad vi skrivt för kommentar för vår funktion `welcome` så skriver vi:

```python
help(welcome)
```

Då visas vår dokumentation kring funktionen att visas på detta sätt:

![IDLE](../images/idle1.png)

## Övningar

### Övning 1

I denna övningen ska vi utgå från befinglig kod och "lägga in" koden i en funktion. Funktionen ska heta `multiply`, och bestå utan koden nedan:

```python
print("I detta program beräknas produkten av två tal")
num_1 = int(input("Ange tal 1: "))
num_2 = int(input("Ange tal 2: "))
product = num_1 * num_2
print("Produkten av " + str(num_1) + " och " + str(num_2) + " är: " + str(product))
print("--------------------------------")
```

När ni skrivit klart funktionen så ska den köras __tre__ gånger. Funktionen ska även dokumenteras enligt beskrivningen ovan (genom `''' dina kommentarer '''`). __Tänk på__ att vara noga med indenteringen för funktionen.

Fungerar det som förväntat när du kör funktionen `help` för din funktion? Skrivs funktionens beskrivning ut på ett tydligt sätt?
{: .info}

### Övning 2

Hittills har vi nu gjort två funktioner.

1. En funktion som välkomnar användaren till vårt program
2. En funktion som beräknar produkten av två tal

I denna övningen ska vi lägga in båda funktionerna (som ju nu är väldokumenterade) i samma Python-fil och sedan köra båda funktionerna (som bildar vårt program) enligt:

```python
welcome()
multiply()
```

Funktionsanropen ska i detta läget ligga _efter_ att funktionerna är definierade. Annars kommer ni få ett meddelande som säger att funktionerna som ni försöker köra inte är definierade (tänk på att datorn läser koden uppifrån och ner). Om allt fungerar som det ska bör resultatet se ut något i stil med:

![](../images/idle2.png)

Testa även så att din dokumentation fungerar som förväntat till dina funktioner:

```python
help(welcome)
help(multiply)
```

Resultatet bör bli liknande:

![](../images/idle3.png)
