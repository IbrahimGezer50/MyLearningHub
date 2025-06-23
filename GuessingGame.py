import random
secret = random.randint(1, 100)
count = 5

while count > 0:
    guessed_number = input("Guess the number between 1 and 100:")
    try:
        gn = int(guessed_number)
        count -= 1
    except ValueError:
        print("Please put a number!")
        continue
    if gn == secret:
        print("You got it!")
        break
    else:
        if count > 0:
            if gn > secret:
                print(f"Too high! Attempts left: {count}")
            elif gn < secret:
                print(f"Too low! Attempts left: {count}")
        else:
            print(f"Out of guesses. The number was {secret}")