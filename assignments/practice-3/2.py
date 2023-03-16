from random import randint

num = randint(0, 10)
attempt = 1

while int(input("Guess: ")) != num:
    attempt += 1
    if attempt > 3:
        print("You lose")
        exit()

print("You win")
