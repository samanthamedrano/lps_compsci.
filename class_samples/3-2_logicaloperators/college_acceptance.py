print('How old are you?')
age = int(raw_input())

print('What is your GPA?')
GPA = float(raw_input())

if GPA > 3.0 and age > 16:
	print('Congrats, welcome to Columbia!')
if GPA <= 3.0 or age <= 16:
	print('Sorry, good luck at Harvard.')





print("How old are you?")
age = int(input())

print("How many inches tall are you?")
height = int(input())

if age > 10 and height > 50:
	print("Hooray! You're old enough and tall enough to ride.")
else:
	print("Sorry, you can't ride.")
