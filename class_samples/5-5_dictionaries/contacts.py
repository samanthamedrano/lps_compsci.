# an empty dictionary so tht the user can input more people.
phoneCont = {  }

run = True
print('Welcome to Contacts!')
# the while loop helps the code keeps running until run is not equal to True.
while run: 
	print('What would you like to do?')
	print('(1): Add a phone number.')
	print('(2): Print the full list of contacts.')
	print("(3): Enter a name to retrieve that contact's phone number.")
	print('(0): Exit the Contact app.')

	
	response = raw_input()
	# the usker can input specific choices and they are taken to a different choice every time it is different.
	if response == '0':
		print('Thank you for using Contacts!')
		run = False
	elif response == '1':
		print('what is the name of you contact?')
		name = raw_input()
		print('What is the phone number of the contact?')
		number = raw_input()
			#This saves the number and name of the contact to the dictionary.
		phoneCont[name] = number
	elif response == '2':
		print(phoneCont)
	elif response == '3':
		print('Whose number would you like?')
		bring = raw_input()
 		print(phoneCont[name])
