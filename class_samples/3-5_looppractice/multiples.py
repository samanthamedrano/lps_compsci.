# multiples.py

print('For what number would you like multiples?')
num = float(raw_input())
number= int(1)
multi = int(num * number)

 
while multi < 1000:
	print( str(number) + ' times ' + str(num) + ' equals ' + str(multi) + '.')
	number = number + 1
	multi = float(num * number)

