print('Welcome to PumaPix!')
print('Enter your 5 favorite TV shows.')
print('Remeber: Capitalize the first letter of the TV show.')
#I have created this reminder because it makes the code go smoother when sorting.
list = 0
tv = []
#This part is for the user to input their answers.
while list < 5:
        print('Enter a show name:')
        show = raw_input()
        tv.append(show)
        list = list + 1

print('Here is what you entered:')
print(tv)
print('I have added a couple of important ones.')
tv.append("Breaking Bad")
tv.append('The Wire')
tv.sort()
#This second part is to sort out the shows by alphabetical order. 
number = 1
for entertainment in tv:
        print( str(number) + '.' + entertainment)
        number += 1
