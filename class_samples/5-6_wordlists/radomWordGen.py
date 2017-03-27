import random
#Opend the file for the computer to read.
wordsFile = open('words.txt', 'r')
#Creates an empty list so the words can all go into the list.
wordsList = []
myWord = wordsFile.readline()
#this while loop reads all the words in the 'words.txt' file.
while myWord != '':
	wordsList.append(myWord)
	myWord = wordsFile.readline()

#this picks a random word of the list and prints it.
myRandWord = random.choice(wordsList)
print(myRandWord)


