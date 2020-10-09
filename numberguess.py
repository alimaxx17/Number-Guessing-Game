import random

number = random.randint(1,9)

chance = 0

print("Guess a number (between 1 and 9): ")

while chance < 5:

    guess = int(input())

    if guess == number:

        print("You Win!")
        break

    elif guess < number:

        print("Your guess is too low: Guess again: ", guess)

    else:

        print("Your guess is too high: Guess again: ", guess)

    chance += 1

if not chance < 5:
    print("You Lose! The number is", number ,"LOSER")
