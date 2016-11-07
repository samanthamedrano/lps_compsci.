# number 3
fave = int(5) 
print('What do you think my favorite number is?')
user_fave = int(raw_input())
if user_fave > fave:
	print('Sorry, you lose. :(. Next time try a lower guess.')
	print('Here is a hint. What is 3 plus 2 equal to?')
if user_fave < fave:
	print('Sorry, you lose.:(. Next time try a higher guess.')
	print('Here is a hint. What is the square root of 25?')
if user_fave == fave:
	print('Wow, you guessed it! You must be a genius.') 


