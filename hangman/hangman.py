import random

HANGMAN_PICS = ['''
	 +--+
	    |
	    |
	    |
	  ===''', '''
	 +--+
	 O  |
	    |
	    |
	  ===''', '''
	 +--+
	 O  |
	 |  |
		|
	  ===''', '''
	 +--+
	 O  |
	/|  |
		|
	  ===''', '''
	 +--+
	 O  |
	/|\ |
		|
	  ===''', '''
	 +--+
	 O  |
	/|\ |
	/   |
	  ===''', '''
	 +---+
	 O   |
	/|\  |
	/ \  |
	  ===''', '''
	 +--+
	 |
	[O   |
	/|\  |
	/ \  |
	  ===''','''
	 +--+
	 |
	[O]  |
	/|\  |
	/ \  |
	  ===''']

words = 'ant room down bat bear june come cat but'

words = words.split()

def getRandomWord(wordList):
	wordIndex = random.randint(0, len(wordList) - 1)
	return wordList[wordIndex]

#设置需要猜测的字母
'''
	secret_word  需要猜测的单词
	index_list  猜测单词中需要隐藏的字母
'''
def getPuzzleWord(secret_word, index_list):
	_secret_word = secret_word;
	
	for i in index_list:
		_secret_word = _secret_word[:i] + '_' + _secret_word[i+1:]
		
	return _secret_word;
	
def getHideWord(secret_word, index_list):
	_hide_word = ''
	for i in index_list:
		_hide_word = _hide_word + secret_word[i]
	return _hide_word
	
def getPuzzleIndexList(secret_word):
		word_len = len(secret_word);
		Level = 2; #难度级别
		puzzle_num = int(word_len/2); #计算需要隐藏的个数
		# 如果隐藏个数大于0
		if puzzle_num > 0:
			_list = []
			# 获取需要隐藏的随机索引值
			while puzzle_num > 0:
				# 获取随机值
				random_num = random.randint(0, word_len - 1)
				# 如果获取的随机值不在列表内，那么储存改值
				if random_num not in _list:
					_list.append(random_num)
					puzzle_num = puzzle_num - 1
			return _list
		else:
			return list(range(0, word_len))
			
'''
	missLetters  已猜错的字母
	correctLetters 猜正确的字母
	guessedWord  当前正在猜的词语（可能其中有些字母已经猜对）
'''	
def displayBoard(missLetters, correctLetters, guessedWord):
	print(HANGMAN_PICS[len(missLetters)])
	print()
	
	print('Missed letters: ', end=' ')
	for letter in missLetters:
		print(letter, end=' ')
	print()
	
	for letter in guessedWord:
		print(letter, end=' ')
	print()

# 获取用户猜测的字母
def getGuess(alreadyGuessed):
	while True:
		print('Guess a letter.')
		guess = input()
		guess = guess.lower()
		if len(guess) != 1:
			print('please enter a single letter')
		elif guess in alreadyGuessed:
			print('you have already guessed that letter. choose again')
		elif guess not in 'abcdefghijklmnopqrstuvwxyz':
			print('please enter a letter.')
		else:
			return guess


			
def playAgain():
	print('do you want to play again? (yes or no)')
	return input().lower().startswith('y')
	
'''
	程序主体部分 
'''
	
print('H A N G M A N')

missLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
puzzleList = getPuzzleIndexList(secretWord)
puzzleWord = getPuzzleWord(secretWord, puzzleList)
hideWord = getHideWord(secretWord, puzzleList)
gameIsDone = False

while True:
	displayBoard(missLetters, correctLetters, puzzleWord)
	
	# 获取当前用户猜的字母
	guess = getGuess(missLetters + correctLetters)
	
	'''
		循环被隐藏的字母表，检查当前猜测的字母是否为正确的字母
	'''
	if guess in hideWord:
		correctLetters = correctLetters + guess
	# 修改puzzleWord字符串
		for _index in puzzleList:
			if secretWord[_index] == guess:
				puzzleWord = puzzleWord[:_index] + guess + puzzleWord[_index+1:]
		
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
			displayBoard(missLetters, correctLetters, puzzleWord)

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
			puzzleWord = getPuzzleWord(secretWord, puzzleList)
			hideWord = getHideWord(secretWord, puzzleList)
			gameIsDone = False
		else:
			break	