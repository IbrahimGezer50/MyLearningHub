# Notes

Python uses **indentation** to define blocks of code (e.g., inside loops or functions). Usually, it's 4 spaces.

→ Indentation bedeutet Einrückung. Einrückungen werden gemacht, um ein Code Block aufzubauen. Jede Einrückung gehört zum Code der darüber ist.

Beispiel für eine Einrückung:

```jsx
def greet():
    print("Hello")   # indented — this is inside the function

print("Bye")         # not indented — this is outside the function
```

- Einrückungen werden nicht überall akzeptiert. ⤵ der erste Print ist bspw. keine korrekte Einrückung, da er nicht ins Syntax des Codegefüges passt.

```
# Learn how to use Variables

name = "Ibrahim" 
age = 40
height = 1.75
    print(height)
print("Hello, my name is " + name + " and I am " + str(age) + " years old. I am " + str(height) + " meters tall.")
```

- Python doesn’t use `{}` like many other languages to group code — it uses **indentation (spaces)**.
- Usually, we indent using **4 spaces**.
- If your indentation is off, Python will throw an `IndentationError`.

Weiteres Beispiel:

```jsx
# Define variables globally

name = "Ibrahim"
age = 40
height = 1.75   

def introduce():
    print(f"Hello, my name is {name}, I am {age} years old and my height is {height} meters.")

# Call the function to introduce
introduce()

Ergebnis: Hello, my name is Ibrahim, I am 40 years old and my height is 1.75 meters.
```

- Python uses indentation to know that the `print()` and variable assignments belong to the `introduce()` function.
- Without indentation, Python would throw an error.
- Keeping your code **organized** with functions + comments is already a pro habit.

# Files

# Tasks

- [x]  Try a function with correct and incorrect indentation
