# 64格棋盘游戏
# 相比Tic Tac Toe更厉害的AI
# 
# 游戏玩法：
# X O 代表双方落子，在不同方向中只要一方中间的对方落子就会变为己方落子
# 例如 X O O X  => X X X X
# 最终谁的棋子多谁获胜

import random
import sys

SPACE = ' ' * 5
SPACE_3 = ' ' * 3

# 绘制棋盘数据
def drawBoard(board):
	HLINE = '+' + '---+' * 8

	print(SPACE + '  1   2   3   4   5   6   7   8')
	print()
	print(SPACE + HLINE)

	for y in range(8):
		
		VLINE = ''
		print(y+1, end=' ')

		for x in range(8):
			VLINE += ('| %s' % board[x][y]) + ' '

		print(SPACE_3 + VLINE + '|')
		print(SPACE + HLINE)	

# 重设棋盘数据
def resetBoard(board):
	for x in range(8):
		for y in range(8):
			board[x][y] = ' '

	board[3][3] = 'X'
	board[3][4] = 'O'
	board[4][3] = 'O'
	board[4][4] = 'X'

# 创建一个新的棋盘数据
def createNewBoard():
	board = []
	for i in range(8):
		board.append([' '] * 8)

	return board

def getBoardCopy(board):
	dupeBoard = createNewBoard()

	for x in range(8):
		for y in range(8):
			dupeBoard[x][y] = board[x][y]

	return dupeBoard		


# 检查当前坐标落子是否有效
# 也就是判断当前落子是否能翻转对方落子
def isValidMove(board, tile, xstart, ystart):
	if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
		return False
	# 暂时赋值	
	board[xstart][ystart] = tile

	if tile == 'X':
		otherTile = 'O'
	else:
		otherTile = 'X'

	# 检查会被翻转（将对方落子变为我方的落子）的落子，将坐标存入列表	
	tilesToFlip = []
	# 检查落子点的 ‘上 下 左 右  左上 右上 左下 右下’ 8个方向的落子情况
	_direction = [ [0, 1], [1, 1], [1, 0], [1, -1], [0, -1],[-1, -1], [-1, 0],[-1, 1] ]
	
	for xdirection, ydirection in _direction:
		x, y = xstart, ystart
		x += xdirection
		y += ydirection
		# 这里实现的是一个类递归循环
		# 目的寻找落子四周有多少对方的落子
		# 直到在同一方向上出现我方落子或为空的棋盘
		
		# 如果落子在该方向的下一个落子为对方落子
		if isOnBoard(x, y) and board[x][y] == otherTile:
			# 那么继续按照该方向搜寻有没有对方的落子
			x += xdirection
			y += ydirection
			if not isOnBoard(x, y):
				continue
			while board[x][y] == otherTile:
				x += xdirection
				y += ydirection
				# 直到该方向的落子搜寻完毕 退出寻找
				if not isOnBoard(x, y):
					break
			# 如果该方向棋盘格找完退出本次循环，进入下一个循环
			# 也就是结束该方向的寻找，进入下一个方向搜索
			if not isOnBoard(x, y):
				continue

			# 如果最终在同一方向发现我方落子
			# 那么递归该方向落子，并存入tilesToFlip列表里
			if board[x][y] == tile:
				while True:
					x -= xdirection
					y -= ydirection
					if x == xstart and y == ystart:
						break
					tilesToFlip.append([x, y])
	# 清空落子点
	board[xstart][ystart] = ' '	
	if len(tilesToFlip) == 0:
		return False
	return tilesToFlip						

# 检查落子是否在棋盘内
def isOnBoard(x, y):
	return x >= 0 and x <=7 and y >=0 and y <=7


# 获取落子提示棋盘数据
# 也就是这里返回的棋盘数据包含下一步的落子提示
def getBoardWithValidMoves(board, tile):
	dupeBoard = getBoardCopy(board)

	for x, y in getValidMoves(dupeBoard, tile):
		dupeBoard[x][y] = '.'

	return dupeBoard

# 获取有效落子坐标
def getValidMoves(board, tile):
	validMoves = []

	for x in range(8):
		for y in range(8):
			if isValidMove(board, tile, x, y) != False:
				validMoves.append([x, y])

	return validMoves

# 计算双方棋盘落子分数
def getScoreOfBoard(board):
	x_scroe = 0
	o_scroe = 0

	for x in range(8):
		for y in range(8):
			if board[x][y] == 'X':
				x_scroe += 1
			if board[x][y] == 'O':
				o_scroe += 1

	return {'X': x_scroe, 'O': o_scroe}	

# 输入玩家棋子显示方式
def enterPlayerTile():
	tile = ''
	while not (tile == 'X' or tile == 'O'):
		print('Do you want to be X or O ?')
		tile = input().upper()	

	# [代表玩家落子, 代表电脑落子]	
	if tile == 'X':
		return ['X', 'O']
	if tile == 'O':
		return ['X', 'O']	

# 执行棋盘落子
def makeMove(board, tile, xstart, ystart):
	# 计算落子是否有效
	tilesToFlip = isValidMove(board, tile, xstart, ystart)
	# 如果无效（也就是没有翻转对方棋子）
	# 那么直接返回False
	if tilesToFlip == False:
		return False
	# 如果落子有效
	# 执行落子
	board[xstart][ystart] = tile
	# 并翻转对方的落子
	for x, y in tilesToFlip:
		board[x][y] = tile

	return True	

# 判断落子坐标是否在棋盘四个角上
def isOnCorner(x, y):
	return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)

# 获取和处理玩家落子
def getPlayerMove(board, playerTile):
	
	DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()

	while True:
		# 玩家完整需要执行的操作
		# 1. 输入落子坐标  
		# 2. 输入 quit / q 退出游戏   
		# 3. 输入hints / h 显示提示 
		print('Enter your move, or type "quit" to end the game, or type "hints" turn off/on hints.')
		move = input().lower()
		if move == 'quit' or move == 'q':
			return 'quit'
		if move == 'hints' or move == 'h':
			return 'hints'	
		# 检查输入的坐标值是否正确	
		if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
			# 玩家输入的坐标范围是1-8，而实际程序中是1-7
			# 所以这里需要减1
			x = int(move[0]) - 1
			y = int(move[1]) - 1

			if isValidMove(board, playerTile, x, y) == False:
				continue
			else:
			 	break
		else:
			print('!!!!!!!!!!!')
			print('That is not a valid move, Type the x digit (1-8) the y digit(1-8).')
			print('For example , 81 will be the top-right corner.')

	return [x, y]

# 获取计算机落子
def getComputerMove(board, computerTile):
	possibleMoves = getValidMoves(board, computerTile)
	print(possibleMoves)
	# 对可以落子的点进行随机排序
	random.shuffle(possibleMoves)

	for x, y in possibleMoves:
		if isOnCorner(x, y):
			return [x, y]

	# 寻找最优落子
	bestScore = -1
	for x, y in possibleMoves:
		dupeBoard = getBoardCopy(board)
		makeMove(dupeBoard, computerTile, x, y)
		score = getScoreOfBoard(dupeBoard)[computerTile]

		if score > bestScore:
			bestMove = [x, y]
			bestScore = score

	return bestMove


# 显示得分
def showPoints(board, playerTile, computerTile):
	scores = getScoreOfBoard(board)
	print()
	print('***** POINT ******')
	print('You have %s points, the computer has %s points.' % (scores[playerTile], scores[computerTile]))


# 随机选择起始落子方
def whoGosFirst():
	if random.randint(0, 1) == 0:
		return 'computer'
	else:
		return 'player'	

# 是否再来一局
def playAgin():
	print('Do you want to play again?(yes or no)')
	return input().lower().startswith('y')											 
# 初始程序
def init():
	print('WELCOME TO REVERS!')

	while True:
		mainBoard = createNewBoard()
		resetBoard(mainBoard)
		playerTile, computerTile = enterPlayerTile()
		showHints = False
		turn = whoGosFirst()

		print()
		print('The [' + turn + '] will go first')

		while True:
			if turn == 'player':
				# 玩家落子执行代码
				if showHints:
					validMovesBoard = getBoardWithValidMoves(mainBoard, playerTile)
					drawBoard(validMovesBoard)
				else:
					drawBoard(mainBoard)
				showPoints(mainBoard, playerTile, computerTile)	

				move = getPlayerMove(mainBoard, playerTile)
				if move == 'quit' or move == 'q':
					print('Thanks for playing!')
					sys.exit()
				elif move == 'hints' or move == 'h':
					showHints = not showHints
					continue
				else:
					makeMove(mainBoard, playerTile, move[0], move[1])

				# 检查电脑是否有落子的机会，如果没有就跳出程序
				# 如果有就轮到电脑落子	
				if getValidMoves(mainBoard, computerTile) == []:
					break
				else:
					turn = 'computer'				

			else:
				# 电脑落子
				drawBoard(mainBoard)
				showPoints(mainBoard, playerTile, computerTile)
				input('Press [ENTER] to see the computer\'s move.')
				x, y = getComputerMove(mainBoard,computerTile)
				makeMove(mainBoard, computerTile, x, y)

				if getValidMoves(mainBoard, playerTile) == []:
					break
				else:
					turn = 'player'	

		drawBoard(mainBoard)
		scores = getScoreOfBoard(mainBoard)
		showPoints(mainBoard, playerTile, computerTile)

		if scores[playerTile] > scores[computerTile]:
			print('You beat the computed by %s points! Great Job' % (scores[playerTile] - scores[computerTile]))
		elif scores[playerTile] < scores[computerTile]:
			print('You lost. the computed beat you by %s points! ' % (scores[computerTile] - scores[playerTile]))
		else:
			print('The Game was a tie !')

		if not playAgin():
			break


init()				