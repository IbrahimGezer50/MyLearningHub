# FizzBuzz Task

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for i in items :
    if i %3 == 0 and i %5 == 0 :
        print(f"{i} FizzBuzz")
    elif i %3 == 0 :
        print(f"{i} Fizz")
    elif i %5 == 0:
        print(f"{i} Buzz")
    