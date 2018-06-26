import random

guesseTimes = 0

print('...GUESS A  NUMBER...')

print('hello! whate is your name?')

myName = input()

number = random.randint(1, 20)
print('well,' +myName + ', i am thinking of a number between 1 and 20.')

while guesseTimes < 6:
	print('Take a guess.')
	guess = int(input())
	
	guesseTimes = guesseTimes + 1
	
	if guess < number:
		print('Your guess is too low.')
	if guess > number:
		print('Your guess is too high.')
	if guess == number:
		break

if guess == number:
	print('Good job,' + myName + '! you guessed my bumber in' + str(guesseTimes) + 'times.')
	
if guess != number:
	print('the number i was thinking of was ' + str(nnumber))