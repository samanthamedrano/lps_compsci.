print('What is the amount of the purchase you have made in cents?')
purchase = float(raw_input())
discount = purchase * 0.10
end = int(purchase - discount)

if end > 1000:
	print('You spent over $10! Your final price is ' + str(end) +  ' cents.')  
if end < 1000:
	print('You spent less than $10! Your final price is ' + str(end) + ' cents')

