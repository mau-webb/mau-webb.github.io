---
id: da354a
title: "Modul 1 - Introduktion till Python"
---

# Modul 1 - Introduktion till Python

## Introduktion till programmering

<div class="frame">
    <div style="left: 0; width: 100%; height: 0; position: relative; padding-bottom: 56.1972%;"><iframe src="https://speakerdeck.com/player/91516b7ad6794f70a134975a7ceb611f" style="border: 0; top: 0; left: 0; width: 100%; height: 100%; position: absolute;" allowfullscreen scrolling="no" allow="encrypted-media"></iframe></div>
</div>

---

<div class="video-frame">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/R8T1Qm5dENI" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

---

### Dagens exempel

#### En miniräknare

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

---

Ni kan även ladda ner PDF-versionen av presentationen [här](../pdf/introduktion-till-programmering.pdf).