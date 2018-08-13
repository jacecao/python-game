# 64格棋盘游戏
# 电脑和电脑玩

import random
import sys

SPACE = ' ' * 5
SPACE_3 = ' ' * 3

# 记录上一个落子的坐标
# 第一个元素记录x坐标，第二个元素记录y坐标，第三个元素记录是什么落子‘x’'o'
MOVED_X_Y = []

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
			if len(MOVED_X_Y) == 2 and MOVED_X_Y[0] == x and MOVED_X_Y[1] == y:
				# 如果有上一次落子信息记录，那么对上一次落子信息作特殊标记
				VLINE += ( '|.%s' % board[x][y] ) + '.'
			else:

				VLINE += ( '| %s' % board[x][y] ) + ' '

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

# 执行棋盘落子
def makeMove(board, tile, xstart, ystart):
	# 计算落子是否有效
	tilesToFlip = isValidMove(board, tile, xstart, ystart)
	# 如果无效（也就是没有翻转对方棋子）
	# 那么直接返回False
	if tilesToFlip == False:
		return False
	# 如果落子有效
	# 执行落子，并标记当前落子
	board[xstart][ystart] = tile
	# 检查上一回标记落子的坐标
	if len(MOVED_X_Y) == 2:
		# 如果已经有上一次落子的记录
		# 更新为当前落子坐标
		MOVED_X_Y[0] = xstart
		MOVED_X_Y[1] = ystart
	else:
		# 如果没有记录上一次落子情况
		# 那么这里第一次添加落子信息
		MOVED_X_Y.append(xstart)
		MOVED_X_Y.append(ystart)

	# 并翻转对方的落子
	for x, y in tilesToFlip:
		board[x][y] = tile

	return True	

# 判断落子坐标是否在棋盘四个角上
def isOnCorner(x, y):
	return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)


# 获取计算机落子
def getComputerMove(board, computerTile):
	possibleMoves = getValidMoves(board, computerTile)
	# print(possibleMoves)
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
	print('           ***** POINT ******')
	print('    %s has %s points, %s has %s points.' % (playerTile, scores[playerTile], computerTile, scores[computerTile]))


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
		showHints = False
		if whoGosFirst() == 'player':
			turn = 'X'
		else:
			turn = 'O'	

		print()
		print('The [' + turn + '] will go first')

		while True:
			if turn == 'X':
				otherTile = 'O'
				x, y = getComputerMove(mainBoard, turn)
				makeMove(mainBoard, turn, x, y)

				# 检查电脑是否有落子的机会，如果没有就跳出程序
				# 如果有就轮到电脑落子	
				if getValidMoves(mainBoard, otherTile) == []:
					break
				else:
					turn = 'O'				

			else:
				# 电脑落子
				# 显示棋盘
				turn = 'O'
				otherTile = 'X'
				x, y = getComputerMove(mainBoard, turn)
				makeMove(mainBoard, turn, x, y)

				if getValidMoves(mainBoard, otherTile) == []:
					break
				else:
					turn = 'X'	

		drawBoard(mainBoard)
		scores = getScoreOfBoard(mainBoard)
		showPoints(mainBoard, 'X', 'O')

		if not playAgin():
			break


init()				