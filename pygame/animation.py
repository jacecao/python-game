import pygame, sys, time
from pygame.locals import *

pygame.init()

W_WIDTH = 400
W_HEIGHT = 400
windowSurface = pygame.display.set_mode((W_WIDTH, W_HEIGHT), 0, 32)

pygame.display.set_caption('Python-Animation')

DOWN_LEFT = 1
DOWN_RIGHT = 3
UP_LEFT = 7
UP_RIGHT = 9

MOVE_SPEED = 4

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def create_block (x, y, w, h, color_name, director):
	return {
		'rect': pygame.Rect(x, y, w, h),
		'color': color_name,
		'dir': director
	}

block_1 = create_block(300, 80, 50, 100, RED, UP_RIGHT)
block_2 = create_block(200, 200, 20, 20, GREEN, UP_LEFT)
block_3 = create_block(100, 150, 60, 60, BLUE, DOWN_LEFT)

blocks = [block_1, block_2, block_3]

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	windowSurface.fill(BLACK)
	
	for b in blocks:
		if b['dir'] == DOWN_LEFT:
			b['rect'].left -= MOVE_SPEED
			b['rect'].top += MOVE_SPEED

		if b['dir'] == DOWN_RIGHT:
			b['rect'].left += MOVE_SPEED
			b['rect'].top += MOVE_SPEED	

		if b['dir'] == UP_LEFT:
			b['rect'].left -= MOVE_SPEED
			b['rect'].top -= MOVE_SPEED

		if b['dir'] == UP_RIGHT:
			b['rect'].left += MOVE_SPEED
			b['rect'].top -= MOVE_SPEED

		if b['rect'].top < 0:
			if b['dir'] == UP_LEFT:
				b['dir'] = DOWN_LEFT

			if b['dir'] == UP_RIGHT:
				b['dir'] = DOWN_RIGHT

		if b['rect'].bottom > W_HEIGHT:
			if b['dir'] == DOWN_LEFT:
				b['dir'] = UP_LEFT

			if b['dir'] == DOWN_RIGHT:
				b['dir'] = UP_RIGHT

		if b['rect'].left < 0:
			if b['dir'] == DOWN_LEFT:
				b['dir'] = DOWN_RIGHT

			if b['dir'] == UP_LEFT:
				b['dir'] = UP_RIGHT

		if b['rect'].right > W_WIDTH:
			if b['dir'] == DOWN_RIGHT:
				b['dir'] = DOWN_LEFT

			if b['dir'] == UP_RIGHT:
				b['dir'] = UP_LEFT

		pygame.draw.rect(windowSurface, b['color'], b['rect'])
		
	pygame.display.update()
	time.sleep(0.02)									

