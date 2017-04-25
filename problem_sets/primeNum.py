# Function that tells if it is a prime number.
def Prime(ugh, list):
        wow = range(1,int(ugh))
        num = ugh - 2
        y = 0
        for number in wow:
                yeah = int(ugh) % int(number)
#Checks if it is a prime number.
                if yeah != 0:   
                        y = y + 1
# remainder must  equal to 0 to continue.
                        if y == num:
                                print(ugh)
                                list.append(ugh)
 
#creats a empty list
primosList = []

# ranges from 2 to 10,001, because it covers from start to end 
rangeList = range(2, 10001)

#print out the prime numbers.
for stop in rangeList:
        gg = Prime(stop, primosList)

