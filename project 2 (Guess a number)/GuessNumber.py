import random

n = random.randint(1, 100)
a = -1
guesses = 1


while n != a:
    a = int(input("Enter a number: "))
    if n > a:
        print("Higher number please")
        guesses += 1
    elif n < a:
        print("Lower number please")
        guesses += 1
print(f"You guess the right number {n} with {guesses} guesses.")
