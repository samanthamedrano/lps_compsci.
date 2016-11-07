print("Hi! What's your name?")
name = raw_input()


print("And how old are you?")
age = int(raw_input())


if age < 18:
	print("You're cool!")
else:
	if name == "Minkus":
		print("You're cool!")
	else:
		print("You're too many years old and your name isn't cool enough.")
