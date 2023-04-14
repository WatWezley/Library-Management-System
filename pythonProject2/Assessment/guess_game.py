day = 28
guess = 0

while guess != day:
    guess = int(input("guess my age: "))
    if guess != day:
        print("INCORRECT GUESS")
    if guess == day:
        print("CORRECT GUESS")
