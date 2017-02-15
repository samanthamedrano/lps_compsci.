# this opens both of the haiku files so they are ready to be used.
myThirdHaiku = open('haiku3.txt', 'r')
myFourthHaiku = open('haiku4.txt', 'r')


print('Hello, welcome to Haiku reader!')
print('Choose between the following:')
print('(3):A haiku about food.')
print('(4):A haiku about Supernatural.')
# this is for when the program asks the user what they need to put.
response = raw_input()
# when the user puts 3 or 4 they will be displayed the Haiku they choose.
if response == '3':
	print(myThirdHaiku.read())
elif response == '4':
	print(myFourthHaiku.read()) 

# Lastly, this closes the haikus. 
myThirdHaiku.close()
myFourthHaiku.close()
