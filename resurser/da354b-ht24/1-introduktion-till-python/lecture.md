---
id: da354b-ht24
title: "Modul 1 - Introduktion till Python"
---

# Modul 1 - Introduktion till Python

## Introduktion till programmering

Publiceras när tillfället varit.



<div class="frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.2696%; padding-top: 58px;"><iframe src="https://www.slideshare.net/slideshow/embed_code/key/HTU9WmsnMMLwDN" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no"></iframe></div>
</div>

<!--
<div class="video-frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.25%;"><iframe src="https://www.youtube.com/embed/sWT6SBbBArw?rel=0" style="top: 0; left: 0; width: 100%; height: 100%; position: absolute; border: 0;" allowfullscreen scrolling="no" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share;"></iframe></div>
</div>
-->

### Dagens exempel

#### En miniräknade

```python
x = input("Tal 1: ")
y = input("Tal 2: ")

result = int(x) + int(y)

print("Summan av " + x + " och " + y + " är: " + str(result))
```


#### En miniräknare (lite större program)

```python
# Skriver ut en rubrik till vårt program
print("-------------")
print("Miniräknare")
print("-------------")

# Frågar efter användarens namn, sparar det i variabeln "name"
name = input("Vad heter du? ")

# Skriver ut en beskrivning av vad som kommer att ske
print("Vi kommer ni att göra en beräkning, vänligen ange tal nedan")
# Frågar efter det första talet, sparar det i variabeln "nr_1"
nr_1 = input("Ange tal 1: ")
# Frågar efter det andra talet, sparar det i variabeln "nr_2"
nr_2 = input("Ange tal 2: ")

# Beräknar summan av talen (gör både talen till datatypen nummer)
result = float(nr_1) + float(nr_2)

# Skriver ut resultatet till användaren
print(name + ", summan blir: " + str(result))
```

<!--

#### En moms-räknare

```python
print("-------------")
print("Momsberäknare")
print("-------------")

moms = 0.3

user_money = input("Vilken summa vill du räkna moms på? ")

result = float(user_money) * moms

print("Momsen på " + str(user_money) + " är " + str(result))

```

-->

---

Ni kan även ladda ner PDF-versionen av presentationen [här](../pdf/ht24-intro.pdf).
