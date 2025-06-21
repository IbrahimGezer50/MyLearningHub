# Notes

## Loops with Lists

- Loops werden mit dem Befehl `for` aufgerufen.
- Loops sind dafür da, um wiederholende Aufgaben, Berechnungen etc. wieder und wieder automatisch durchzuführen.

Der Syntax lautet

```python
for item in list:
    # do something with item (beliebigerName)
```

→ Für *element* in der Liste, tue bitte folgendes (wieder und wieder)

Beispiel:

```python
# Learn how to use loops in Python

cities = ["Berlin", "Istanbul", "Dubai", "Jakarta", "Kuala Lumpur", "Tokyo", "San Francisco"]

# Loop through each city and print a flight announcement

for city in cities:
    print(f"Now flying to: {city}")
    
Ergebnis:
Now flying to: Berlin
Now flying to: Istanbul     
Now flying to: Dubai        
Now flying to: Jakarta      
Now flying to: Kuala Lumpur 
Now flying to: Tokyo        
Now flying to: San Francisco
```

The loop:

- Goes through each item in the list
- Temporarily calls it `city` (you can name this whatever you like)
- Runs the code inside the block for each item

### Wie kann ich die Liste aus dem Loop nummerieren?

→ Um die Liste zu nummerieren oder jedem “Flug” einen index zuzuweisen, nutzen wir `enumerate()`

Beispiel:

```python
# Learn how to use loops in Python

cities = ["Berlin", "Istanbul", "Dubai", "Jakarta", "Kuala Lumpur", "Tokyo", "San Francisco"]

# Loop through each city and print a flight announcement

for index,city in enumerate(cities):
    print(f"Flight {index}: Now flying to {city}.")
    
Ergebnis:
Flight 0: Now flying to Berlin.
Flight 1: Now flying to Istanbul.
Flight 2: Now flying to Dubai.
Flight 3: Now flying to Jakarta.
Flight 4: Now flying to Kuala Lumpur.
Flight 5: Now flying to Tokyo.
Flight 6: Now flying to San Francisco.
```

Um direkt mit der `1` zu beginnen:

```python
for index, city in enumerate(cities):
    print(f"Flight {index + 1}: Now flying to {city}.")
```

oder

```python
for flight_no, city in enumerate(cities, start=1):
    print(f"Flight {flight_no}: Now flying to {city}.")
```

→ Hier sehen wir nochmal, dass wir statt `index` auch ein anderes Wort nutzen können.

# Files

# Tasks
