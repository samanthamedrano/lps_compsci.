import random
mynum = random.randint(1, 1000)
print("I'm thinking of a number between 1 and 1000. Enter your guess!")
guess = raw_input()
while guess != mynum:
	print("I'm thinking of a number between 1 and 1000. Enter your guess!")
	guess = int(raw_input())
	if guess < mynum:
		print('Nope, your number was too low.')
	if guess > mynum:
		print('Nope, your number was too high.')
	if guess == mynum:
		break
if guess == mynum:
	print('Hooray, you won!')
