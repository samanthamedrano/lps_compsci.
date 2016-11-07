#number 1 

myVar = str('3')
myVar2 = 'blind mice'

print(myVar + myVar2)

# number 2

age = 72
age_str = str(age)
name = "Esme"
print('Name:' +'esme' + "," + age_str)


# number 3

grade = 79
extra_credit = 8
total = (grade + extra_credit)
print("The overall grade is " + str(total))

# number 4

num1 = 90
num2 = 82

avg = (num1 + num2) / 2
print("The average is " + str(avg)) 

# number 5

print("Which month is it? Enter only the number, like 8 for August.")
month = raw_input()

print("Great, you've entered month " + month + ".")
months_left = 12 - int (month)
print("Woot, only " + str(months_left) + " months till the New Year!")
