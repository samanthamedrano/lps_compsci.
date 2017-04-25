# Function that tells if it is a prime number.
def Prime(ugh, list):
        wow = range(1,int(ugh))
        num = ugh - 2
        o = 0
        for number in wow:
                yeah = int(ugh) % int(number)
#Checks if it is a prime number.
                if yeah != 0:   
                        o = o + 1
# remainder must not equal to 0 to continue.
                        if o == num:
                                print(ugh)
                                list.append(ugh)
 
#creats a empty list
primosList = []

# ranges from 2 to 100,001.
rangeList = range(2, 10001)

for stop in rangeList:
        gg = Prime(stop, primosList)

