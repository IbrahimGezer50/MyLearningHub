## 🔄 How to Reverse a List in Python

There are **two common ways** to reverse a list. Here's how and **why** they work:

---

### ✅ Method 1: Using `[::-1]` (List Slicing)

```python
python
reversed_list = cities[::-1]
```

**Explanation:**

- This is called **list slicing**
- The `:` syntax means: `[start:stop:step]`
- `[::-1]` tells Python to:
    - Start at the end
    - Move backward one item at a time
    - So it creates a **new, reversed list**

🧠 This does **not** change the original list — it just gives you a reversed copy.

---

### ✅ Method 2: Using `.reverse()` (In-Place)

```python
python
KopyalaDüzenle
cities.reverse()

```

**Explanation:**

- This method **modifies the original list**
- You don’t get a new list; instead, `cities` is now reversed

⚠️ Use this only when you're okay changing the original list!

---

## 🔍 Summary

| Method | Reverses in-place? | Returns a new list? |
| --- | --- | --- |
| `[::-1]` | ❌ No | ✅ Yes |
| `.reverse()` | ✅ Yes | ❌ No |
