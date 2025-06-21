# Notes

- A **list** is a collection of items stored in a single variable. → Statt also in einer Variable nur eine Sache zu speichern, können wir mit Listen, mehrere Dinge auf einmal abspeichern.

```jsx
my_list = ["apple", "banana", "cherry"]
```

- Items are separated by **commas**
- Lists are enclosed in **square brackets** `[]`
- You can store:
    - Strings (`"apple"`)
    - Numbers (`1`, `2.5`)
    - Even **mixed types** or **other lists**

### 🛠️ Common List Operations:

| Operation | Example | Result |
| --- | --- | --- |
| 1 Access item | `my_list[0]` | `'apple'` (0 is first) |
| 2 Change item | `my_list[1] = "orange"` | `["apple", "orange", "cherry"]` |
| 3 Add item (end) | `my_list.append("grape")` | Adds to the end |
| 4 Remove item | `my_list.remove("banana")` | Removes `"banana"` |
| 5 Length of list | `len(my_list)` | Number of items |
| 6 Slice List | my_list[start:stop] 
Think of it as: `from index X **up to but not including** index Y` | Print part of a list |
| 7 Reverse List | `my_list.reverse()`

`reversed_list = my_list[::-1]` | Reverses the List |

Beispiel für 1 (Element aufrufen)

```python
# How to work with lists

Obstsorten = ["Apfel", "Banane", "Orange", "Traube"]

print(Obstsorten[0])

Ergebnis: Apfel
```

Beispiel für 2 (Element austauschen)

```python
# How to work with lists

Obstsorten = ["Apfel", "Banane", "Orange", "Traube"]

Obstsorten[1] = "Kiwi"
print(Obstsorten)

Ergebnis: ['Apfel', 'Kiwi', 'Orange', 'Traube']
```

Beispiel für 3 (Element am Ende hinzufügen)

```python
# How to work with lists

Obstsorten = ["Apfel", "Banane", "Orange", "Traube"]

Obstsorten.append("Apfel")
print(Obstsorten)

Ergebnis: ['Apfel', 'Banane', 'Orange', 'Traube', 'Apfel']
```

Beispiel für 4 (Elemente entfernen)

```python
Obstsorten = ["Apfel", "Banane", "Orange", "Traube"]

Obstsorten.remove("Apfel")  # Remove "Apfel" from the list
print(Obstsorten)

Ergebnis: ['Banane', 'Orange', 'Traube']
```

Beispiel für 5 (Länge der Liste abrufen)

```python
# How to work with lists

Obstsorten = ["Apfel", "Banane", "Orange", "Traube"]

len(Obstsorten)  # Returns the number of items in the list
print(len(Obstsorten))

Ergebnis: 4
```

Beispiel für 6 (bestimmten Bereich der Liste)

```python
# How to work with lists

cities = ["Berlin", "Istanbul", "Cairo", "London", "New York"]
print(cities[3:4]) 

Ergebnis: ['London']
```

- Python lists are **zero-indexed**, which means:
    - `cities[0]` → First item
    - `cities[1]` → Second item
    - `cities[4]` → Fifth item

### 🧠 Bonus Insight: Why Use `append()`?

- `.append()` is the most common way to add to a list.
- It always adds the new item to the **end** of the list.

If you ever want to insert an item at a specific position, you'd use:

```python
cities.insert(1, "Paris")  # Adds "Paris" at index 1 -> which is the 2nd position
```

# Files

# Tasks

- [ ]  Create a list of 5 fruits and print the third one
