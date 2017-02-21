print('Welcome to the Haiku generator!')

# the follow asks the user to input the haikus in different lines.
print('Provide the first line of your Haiku:')
firstLine = raw_input()

print('Provide the second line of your haiku:')
secondLine = raw_input()

print('Provide the third line of your haiku:')
thirdLine = raw_input()
#This asks the user to name the file
print('What file name would you like to write your haiku to? Psh. Add the .txt into your name')
file = raw_input()
#this opens the user file and sets it to writing.
userHaiku = open((file), "w")
#this writes the user Haiku in different lines.
userHaiku.write(firstLine + "\n" + secondLine + "\n" + thirdLine + "\n")


print("Done! To view your haiku, type 'cat' and the name of your file at the command line.")
#Closes the file so that it doesn't keep running.
userHaiku.close()
