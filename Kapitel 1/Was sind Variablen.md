# Notes

## Variables:

A **variable** stores data so you can reuse or manipulate it later. → Variablen sind also Beschreibungen, die eine Information in sich enthalten, die man später wiederverwenden kann. Einer Variable kann ein Wert zugeordnet werden, indem man das = Zeichen nutzt.

```jsx
name = "Alice"       # a string
age = 25             # an integer
height = 5.6         # a float

print("Hello, my name is " + name + " and I am " + str(age) + " years old.")
```

- Variable names should start with a letter (oder mit Unterstrich __) and be descriptive. → Daher kann eine Variable nicht mit einer Zahl starten.
- Wenn man beim Print nicht definiert, dass es sich um eine Zahl handelt, dann gibt es einen Error. Daher wurde “age” zu einem string umgewandelt, indem es so definiert wurde → str(age)

### Feedback von ChatGPT

Da ich für die Definition der integers jeweils alle integers zu einem string umgewandelt habe schlägt mir ChatGPT vor:

- Python doesn’t allow mixing strings and numbers directly, so using `str(age)` and `str(height)` is perfect.
- You could also use **f-strings**, which are cleaner and more modern (available since Python 3.6). Here’s how your print line would look with f-strings (not required, just educational):

```jsx
print(f"Hello, my name is {name} and I am {age} years old. I am {height} meters tall.")
```

→ Das ist tatsächlich einfacher und schneller.

# Files

# Tasks

- [x]  Create and print variables with different types: string, int, float
