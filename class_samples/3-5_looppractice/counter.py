# counter.py

print('What number do you want to count by?')
num = int(raw_input())
my_sum = 0

while my_sum < 100:
	my_sum = my_sum + num
	print(my_sum)
