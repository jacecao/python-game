# 友好版
# 添加更加友好的探测坐标说明，能更加快速猜测宝箱位置

# sonar treasure hunt game
# 一个坐标识别游戏

import random
import sys

# 绘制游戏面板
def drawBoard(board):
	hline = ''
	space = '    '

	for i in range(1, 6):
		if i > 1:
			hline += ('+' * 9) + str(i)
		else:
			hline += ('+' * 10) + str(i)

	hline += ('+' * 9)	
	print()	
	print(space + hline)
	print(space + ('0123456789' * 6))

	for i in range (15):
		if i < 10:
			extraSpace = '  '
		else:
			extraSpace = ' '
		print('%s%s %s %s' % (extraSpace, i, getRow(board, i), i))
	
	print(space + ('0123456789' * 6))
	print(space + hline)

# 绘制一列的数据信息
def getRow(board, row):
	boardRow = ''
	for i in range(60):
		boardRow += board[i][row]
	return boardRow
	
# 绘制二维数据信息（也就是一张笛卡尔坐标数据）
def createNewBoard():
	board = []

	for x in range(60):
		board.append([])
		for y in range(15):
			if random.randint(0, 1) == 0:
				board[x].append('~')
			else:
				board[x].append('`')

	return board				

# 获取指定数量的随机坐标[沉入海底的箱子坐标值]
def getRandomChests(numChests):
	chests = []
	for i in range(numChests):
		chests.append([random.randint(0, 59), random.randint(0, 14)])
	return chests

# 检查给的坐标是否在已定的坐标范围内	
def isRightMove(x, y):
	return x >= 0 and x <= 59 and y >= 0 and y <= 14

# 移动坐标
def sonarWorking(board, chests, x, y):
	# 难度设置（可探测的范围设置）
	level = 30

	if not isRightMove(x, y):
		return False
	# 预设距离沉入海底箱子的最小距离	
	smallestDistance = 100
	# 坐标距离提示
	tip = ''
	# 检查输入的坐标值是否解决chests[箱子]的坐标
	for cx, cy in chests:
		if abs(cx - x) > abs(cy - y):
			distance = abs(cx - x)
			tip = 'X'
		else:
			distance = abs(cy - y)
			tip = 'Y'

		if distance < smallestDistance:
			smallestDistance = distance

	if smallestDistance == 0:
		chests.remove([x, y])
		return {
					'status': 'get',
					'info': '''
**************************************
You have found a sunken treasure chest
**************************************	
					'''
				}	
	else:
		if smallestDistance < level:
			if x != 0:
				board[x-1][y] = tip
			if len(str(smallestDistance)) == 2:
				if x + 1 > 59:
					board[x-2][y] = tip
					board[x-1][y] = str(smallestDistance)[0]
					board[x][y] = str(smallestDistance)[1]
				else:
					board[x-1][y] = tip
					board[x][y] = str(smallestDistance)[0]
					board[x+1][y] = str(smallestDistance)[1]	
			else:			
				board[x][y] = str(smallestDistance)
			return {
						'status': 'detected',
						'info': 'treasure detected at a distance of %s from the sonar device.' % (smallestDistance)
					}
		else:
			board[x][y] = 'N'
			return {
						'status': 'fail',
						'info': 'Sonar did\'t detect anything.'
					}

# 接收玩家输入的坐标（也就是sonar的坐标值）
def enterPlayerMove():
	print()
	print('Where do you want to drop the next sonar device ?')
	print('X: (0 - 59) | Y: (0 - 14)')
	print('You can input quit exit the game!')

	while True:
		move = input()
		if move.lower().startswith('q'):
			print('Thanks for playing!')
			sys.exit()

		move = move.split()
		# isdigit() 检查字符串是否是数字组成
		if len(move) == 2 and move[0].isdigit() and	move[1].isdigit() and isRightMove(int(move[0]), int(move[1])):
			return [int(move[0]), int(move[1])]

		print()
		print('Enter a number from 0 to 59, a space, then a number from 0 to 14')	

def playAgain():
	print()
	print('Do you want to play again?(yes or no)')
	return input().lower().startswith('y')

def showInstructions():
	print('this game instructions:')


def init(sonar_num, chest_num):
	print()
	print('S O N A R !')
	print()
	print('Would you want to view the instructions? (yes/no)')

	if input().lower().startswith('y'):
		showInstructions()

	while True:
		theBoard = createNewBoard()
		theChests = getRandomChests(chest_num)
		drawBoard(theBoard)
		# 记录成功获取宝箱的位置
		successMoves = []

		while sonar_num > 0:
			if sonar_num > 1:
				extraSsonar = 's'
			else:
				extraSsonar = ''

			if len(theChests) > 1:
				extraSchest = 's'
			else:
				extraSchest = ''

			print()
			print('You have %s sonar device%s left. %s treasure chest%s remaining.' % (sonar_num, extraSsonar, len(theChests), extraSchest))

			x, y = enterPlayerMove()
			theBoard = createNewBoard()
			moveResult = sonarWorking(theBoard, theChests, x, y)
			if moveResult == False:
				continue
			else:
				if	moveResult['status'] == 'get':
					successMoves.append([x, y])

				if len(successMoves) > 0:
					for _x, _y in successMoves:
						theBoard[_x][_y] = 'V' # success symbol

				drawBoard(theBoard)
				print()
				print(moveResult['info'])
				print('You drop here: [%s, %s]' % (str(x), str(y)))	

			if len(theChests) == 0:
				print()
				print('You have found all the sunken treasure chests! good game!')
				# 询问是否再来一局
				if playAgain():
					break
				else:
					print('Thanks for Playing!')
					sys.exit()

			sonar_num -= 1	

			if sonar_num == 0:
				print()
				print('GAME OVER!')
				print('The remaining chests were here: ')
				for x, y in theChests:
					print('X: %s, Y: %s' % (x, y))

				if not playAgain():
					sys.exit()

init(8, 2)												



