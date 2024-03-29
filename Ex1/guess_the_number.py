# This is guess the number game.
import random
print("Hello, what's your name?")
name = input()

print("Well, " + name + ", I'm thinking of a number between 1 and 20.")
# Generate secret number
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
	print("Take a guess.")
	guess = int(input())

	if guess < secretNumber:
		print("Your guess is too low.")
	elif guess > secretNumber:
		print("Your guess is too high.")
	else:
		break # This condition is for the correct guess!

if guess == secretNumber:
	print("Good job, " + name + "! You guessed my number in " + str(guessesTaken) + " tries.")
else:
	print("Nope. The number I was thinking of was " + str(secretNumber) + ".")