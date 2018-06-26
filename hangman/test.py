'''
word = 'hello'

for s in word:
	print(s)
	

lis = [1, 3]
for i in lis:
	word = word[:i] + '_' + word[i+1:]
	print(word)
'''	
	

missLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
puzzleList = getPuzzleIndexList(secretWord)
puzzleWord = getPuzzleWord(secretWord, puzzleList)
hideWord = getHideWord(secretWord, puzzleList)
gameIsDone = False

while True:
	displayBoard(missLetters, correctLetters, guessWord)
	
	# 获取当前用户猜的字母
	guess = getGuess(missLetters + correctLetters)
	
	'''
		循环被隐藏的字母表，检查当前猜测的字母是否为正确的字母
	'''
	if guess in hideWord:
		correctLetters = correctLetters + guess
	# 修改guessWord字符串
		for _index in puzzleList:
			if secretWord[_index] == guess:
				guessWord = guessWord[:_index] + guess + guessWord[_index+1:]
		
	# 是否已经猜到全部隐藏的字母
		foundAllLetters = True
	
		for i in puzzleList:
			if secretWord[i] not in correctLetters:
				foundAllLetters = False
				break
		
		if foundAllLetters:
			print('Yes! the secret word is "' + secretWord + '"! you have won!')
			gameIsDone = True
	
	else:
		missLetters = missLetters + guess
		
		if len(missLetters) == len(HANGMAN_PICS) - 1:
			displayBoard(missLetters, correctLetters, secretWord)

			print('you have run out of guesses!\nAfter ' + str(len(missLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct quesses, the word was "' + secretWord + '"')
			
			gameIsDone = True

	# 检查当前游戏是否完成			
	if gameIsDone:
		# 如果已经完成，检查是否需要再次开始
		if playAgain():
			missLetters = ''
			correctLetters = ''
			secretWord = getRandomWord(words)
			puzzleList = getPuzzleIndexList(secretWord)
			guessWord = getPuzzleWord(secretWord, puzzleList)
			hideWord = getHideWord(secretWord, puzzleList)
		else:
			break	