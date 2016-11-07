print("Welcome to Sloth's Quest!")
print('Enter the name of your character:')
name = raw_input()

print('Enter strength (1-10):')
strength = int(raw_input())

print('Enter health (1-10):')
health = int(raw_input())

print('Enter luck (1-10):')
luck = int(raw_input())

total = int(strength + health + luck)

if total > 15:
	print('You have given your character too many points!')
	print('Default values have been assigned, ' + name + ':')
	strength = 5
	health = 5
	luck = 5
	print('strength = ' + str(strength) + ', health = ' + str(health) + ', luck = ' + str(luck))
if total <= 15:
	print(name + ', ' + str(strength) + ', ' + str(health) + ',' + str(luck)) 

print(name + ', you have come to a fork in the road. Do you want to go right or left? Enter \'right\' or \'left\'.')
fork = raw_input()

if fork == 'left' and health < 6:
	print('Aww you lost, you have been clawed to death by a Ostrich!')
elif fork == 'left' and health >=6:
	print('Congratulations you have won the game by befriending and ostrich!')

if fork == 'right' and strength < 10:
	print('You have been killed by Shrek! Ogres have layers. You have lost.')
elif fork == 'right' and strength == 10:
	print('Congratulations you have won the game by hitting off with Shrek!')
	
