# Tic Tac Toe

import random

'''
	打印棋盘画面
'''
def drawBoard(board):
	print('     |     |')
	print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9])
	print('     |     |')
	print('-----------------')
	print('     |     |')
	print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6])
	print('     |     |')
	print('-----------------')
	print('     |     |')
	print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3])
	print('     |     |')
	
#drawBoard(''.join(['1','2','3','4','5','6','7','8','9','0']))	

# 选择哪种符号代表你的棋子
def inputPlayerLetter():
	letter = ''
	
	while not (letter == 'X' or letter == 'O'):
		print('Do you want to be X or O ?')
		letter = input().upper()
		
	if letter == 'X':
		return ['X', 'O']
	else:
		return ['O', 'X']
		
# 决定谁先开始		
def whoGoesFirst():
	if random.randint(0, 1) == 0:
		return 'computer'
	else:
		return 'player'
		

def playAgain():
	print('Do you want to play again?(yes or no)')
	return input().lower().startswith('y')
	
# 标记落子的位置
def makeMove(board, letter, move):
	board[move] = letter	

# 判断是否胜利
# _board  当前棋盘棋子状态
# _symbol 代表玩家的棋子	
def isWinner(_board, _symbol):
	# 这里采取硬检查手段
	return (
	(_board[7] == _symbol and _board[8] == _symbol and _board[9] == _symbol)or
	(_board[7] == _symbol and _board[4] == _symbol and _board[1] == _symbol)or
	(_board[7] == _symbol and _board[5] == _symbol and _board[3] == _symbol)or
	(_board[8] == _symbol and _board[5] == _symbol and _board[2] == _symbol)or
	(_board[9] == _symbol and _board[5] == _symbol and _board[1] == _symbol)or
	(_board[9] == _symbol and _board[6] == _symbol and _board[3] == _symbol)or
	(_board[4] == _symbol and _board[5] == _symbol and _board[6] == _symbol)or
	(_board[1] == _symbol and _board[2] == _symbol and _board[3] == _symbol)
	)	

# 复制棋盘状态	
def geBoardCopy(board):
	dupeBoard = []
	
	for i in board:
		dupeBoard.append(i)
	
	return dupeBoard	

# 检查移动位置是否有空间	
def isSpaceFree(board, move):	
	return board[move] == ' '

def getPlayerMove(board):	
	move = ' '
	
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
		print('what is your next move?(1-9)')
		move = input()
		
	return int(move)
	
def chooseRandomMoveFromList(board, movesList):
	#记录当前为空的位置
	possibleMoves = []	
	
	for i in movesList:
		if isSpaceFree(board, i):
			possibleMoves.append(i)
	
	if len(possibleMoves) != 0:
		return random.choice(possibleMoves)
	else:
		return None
		
def getComputerMove(board, computerLetter):
	if computerLetter == 'X':
		playerLetter = '0'
	else:
		playerLetter = 'X'

	# 检索能够获取胜利的位置，并返回	
	for i in range(1, 10):
		_copyBoard = geBoardCopy(board)
		if isSpaceFree(_copyBoard, i):
			makeMove(_copyBoard, computerLetter, i)
			if isWinner(_copyBoard, computerLetter):
				return i
				
	# 检索玩家可能获取胜利的位置，并返回	
	for i in range(1, 10):
		_copyBoard = geBoardCopy(board)
		if isSpaceFree(_copyBoard, i):
			makeMove(_copyBoard, playerLetter, i)
			if isWinner(_copyBoard, playerLetter):
				return i
				
	move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
	if move != None:
		return move
		
	if isSpaceFree(board, 5):
		return 5
		
	return chooseRandomMoveFromList(board, [2, 4, 6, 8])	
		
def isBoardFull(board):
	for i in range(1, 10):
		if isSpaceFree(board, i):
			return False
	
	return True 	
	

def init():
	print('Welcome to Tic Tac Toe!')	
		
	while True:
		theBoard = [' '] * 10
		playerLetter, computerLetter = inputPlayerLetter()
		turn = whoGoesFirst()
		
		print('The ' + turn + ' will go first.')
		gameIsPlaying = True
		
		while gameIsPlaying:
			if turn == 'player':
			# 玩家落子
				drawBoard(theBoard)
				move = getPlayerMove(theBoard)
				makeMove(theBoard, playerLetter, move)
				
				if isWinner(theBoard, playerLetter):
					drawBoard(theBoard)
					print('Hooray! You have won the game!')
					gameIsPlaying = False
				else:
					if isBoardFull(theBoard):
						drawBoard(theBoard)
						print('the game is a tie1')
						break
					else:
						turn = 'computer'
		
			else:
			# 该电脑落子
				move = getComputerMove(theBoard, computerLetter)
				makeMove(theBoard, computerLetter, move)
			
				if isWinner(theBoard, computerLetter):
					drawBoard(theBoard)
					print('The computer has beaten you! you lose.')
					gameIsPlaying = False
				else:
					if isBoardFull(theBoard):
						drawBoard(theBoard)
						print('the game is a tie1')
						break
					else:
						turn = 'player'
		
		if not playAgain():
			break


# 启动游戏
init()			