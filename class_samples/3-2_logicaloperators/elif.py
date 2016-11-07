# number 2

print('How far from Richmond do you live in miles?')
mile = int(raw_input())
print('What is your GPA?')
GPA = float(raw_input())
print('What is your ACT score?')
ACT = int(raw_input()) 



if mile <= 30 and GPA >= 2.0:
	print('Congrats on being accepted to CSU Richmond!')
elif mile > 30 and GPA >= 2.5 and ACT >= 18:
	print('Congrats on being accepted to CSU Richmond!')
elif mile > 30 and GPA <= 2.5 and ACT <= 18:
	print('Sorry, but you have been rejected from CSU Richmond :(')

