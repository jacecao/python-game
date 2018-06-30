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
		return 'you got it!'
	
	if len(guess) != num_len:  
		return 'TIPS>>>>  it\'s a ' + str(num_len) + ' digits number!'
		
	clue = []
		
	for i in range(len(guess)):
		print(i)
		if guess[i] == secretNum[i]:
			clue.append('Right')
		elif guess[i] in secretNum:
			clue.append('Maybe')
		else:
			clue.append('Error')
	
	for tips in clue:
		if tips == 'Maybe' or tips == 'Right':
			break
		else:	
			return 'TIPS>>>> that\'s bad guess'
	# 这里需要调整一下顺序
	#clue.sort()
		
	return ' '.join(clue)
	

print(getClues('121', '243'))










