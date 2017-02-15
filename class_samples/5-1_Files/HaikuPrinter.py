import time
# opens the first haiku to let the Haiku printer read the text inside.  
myFirstHaiku = open('haiku1.txt', 'r')
 
print('Here is the first haiku:')
# reads the haiku in its interity.
print(myFirstHaiku.read())
 
print('I will give you the second haiku line by line.')
print('How many seconds should I wait between lines?')
# this is asking the user to inout a number to make the computer what a certain amount of time to run a line. 
seconds = int(raw_input())
 
mySecondHaiku = open('haiku2.txt', 'r')
# reads one line at a time so that it waits for the amount of seconds the user needs.
lineToPrint = mySecondHaiku.readline()
while lineToPrint != "":
    print(lineToPrint)
    lineToPrint = mySecondHaiku.readline()
    time.sleep(seconds)
# closes the program so that the haikus are not open. 
myFirstHaiku.close()
mySecondHaiku.close()
