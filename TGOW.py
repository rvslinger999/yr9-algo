import random
import time

print("Yagshamash! I am a Borat, the computer! Welcome to the Game of War! Good luck trying to beat me!")
age= raw_input("How old are you? ")
name= raw_input("What's YOUR name? ")
print("Hi "+name)
print("Age "+age)

x = raw_input("Please ENTER an ACCESS CODE to continue: ")

while x != "b0rat123":
	print("ACCESS DENIED")
	x = raw_input("Please RE-ENTER an ACCESS CODE: ")

print("ACCESS GRANTED")

playerScore= 0
computerScore = 0

cardValues = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
cardSuits = ["Clubs","Diamonds","Hearts","Spades"]

rounds = int(raw_input("Please enter the amount of ROUNDS you would like to play: "))
for i in range(rounds):
	print("\n")
	raw_input("Press ENTER to draw a card")

	playerValue = random.choice(cardValues)
	playerSuit = random.choice(cardSuits)

	print("Drawing your card...")
	time.sleep(1.5)
	print("You drew the "+playerValue+" of "+playerSuit)

	computerValue = random.choice(cardValues)
	computerSuit = random.choice(cardSuits)

	print("Drawing the computer's card...")
	time.sleep(1.5)
	print("The computer drew the "+computerValue+" of "+computerSuit)

	if cardValues.index(playerValue) > cardValues.index(computerValue):
		print("You have won!")
		playerScore = playerScore + 1

	elif cardValues.index(computerValue) > cardValues.index(playerValue):
		print("OOF, you lost bruh.")
		computerScore = computerScore + 1
	else:
		if cardSuits.index(playerSuit) > cardSuits.index(computerSuit):
			print("You have won!")
			playerScore = playerScore + 1
		elif cardSuits.index(computerSuit) > cardSuits.index(playerSuit):
			print("OOF, you lost bruh.")
			computerScore = computerScore + 1
		else:
			print("You didn't win or lose. Still bad but still good...")

print("\n")

if playerScore > computerScore:
	print("Congrats bruh. YOU WIN!!!!!!")
elif computerScore > playerScore:
	print("Hah you lost! Go back to Fortnite")
else:
	print("You tied. So you didn't win or lose. Still bad but not bad...")

