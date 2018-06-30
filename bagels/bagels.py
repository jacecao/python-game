# Bagels
# guess a hid number by tips

import random

# numDigits  需要获取几位数 数字
def getSecretNum(numDigits):
	numbers = list(range(10))
	# 打乱序列中的元素
	random.shuffle(numbers)
	secrectNum = ''
	
	for i in range(numDigits):
		secrectNum += str(numbers[i])
		
	return secrectNum

# 获取线索	
def getClues(guess, secretNum):
	
	num_len = len(secretNum)
	
	if guess == secretNum:
		return 'You Got It!'
	
	if len(guess) != num_len:  
		return 'TIPS>>>>  it\'s a ' + str(num_len) + ' digits number!'
		
	clue = []
		
	for i in range(len(guess)):
		if guess[i] == secretNum[i]:
			clue.append('Right[' + guess[i] + ']')
		elif guess[i] in secretNum:
			clue.append('Maybe[' + guess[i] + ']')
		else:
			clue.append('Error[' + guess[i] + ']')
	
	for tips in clue:
		if tips[0] == 'M' or tips[0] == 'R':
			# 这里需要调整一下顺序
			#clue.sort()
			return ' '.join(clue)
	return 'TIPS>>>> that\'s bad guess'
	
	
def isOnlyDigits(num):
	if num == '':
		return False
		
	for i in num:
		if i not in '0 1 2 3 4 5 6 7 8 9'.split():
			return False

	return True

def playAgin():
	print()
	print('Do you want to play again? (yes or no)')
	return input().lower().startswith('y')


def main(numDigits, maxGuess):
	print('B A G E L S - G A M E')
	print()
	print('This is a %s-digits number. Try to guess it' % (numDigits))
	print()
	print('Here are some clues:')
	print('-------------------------------------------------------')
	print('when i say  |             that means')
	print('-------------------------------------------------------')
	print('  Right     |      one digit is correct with right position')
	print('  Maybe     |      one digit is correct with wrong position')
	print('  bad guess |      no digit is correct')
	print('-------------------------------------------------------')
	
	while True:
		secretNum = getSecretNum(numDigits)
		print()
		print('I have thought up a number. you have %s chances to guess it'%(maxGuess))
		
		numGuesses = 1
		while numGuesses <= maxGuess:
			guess = ''
			while not isOnlyDigits(guess):
				print()
				print('Guess #%s:' % (numGuesses))
				guess = input()
				
			clue = getClues(guess, secretNum)
			print()
			print('-----------------------------------')
			print(clue)
			print('-----------------------------------')
			print()
			numGuesses += 1

			if guess == secretNum:
				break
			
			if numGuesses > maxGuess:
				print('G A M E - O V E R!')
				print()
				print('The secret number is %s.' % (secretNum))

		if not playAgin():
			break

main(3, 6)			
