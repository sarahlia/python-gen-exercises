import random

num = random.randint(1, 99)
# print(num)

guesses = 0

username = input("What is your name? ")
print(f"Hello {username}, welcome to Sarah's Guessing Game!")

ans = input("Do you want to start the game? [y/n]")

guessing = True

if ans.lower() == "y":
    guessing = True
else:
    print("Have a nice day!")
    guessing = False

while guessing:
    ans = int(input("Guess a number between 1 and 99: "))
    guesses += 1
    print(f"You have guessed {guesses} time(s)")

    if ans == num:
        print(f"It is {ans}! Congrats, you guessed correctly!!")
        print(f"It took you {guesses} tries. ")
        guessing = False
    elif ans > num:
        print("Go lower..")
    else:
        print("Go higher....")
