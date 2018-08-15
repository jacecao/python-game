import pygame, sys
from pygame.locals import *

pygame.init()

windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('hello world!')

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

basicFont = pygame.font.SysFont(None, 48)

# 绘制文字对象
text = basicFont.render('Hello world!', True, WHITE, BLUE)
textRect = text.get_rect()

textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

windowSurface.fill(WHITE)

# 绘制多边形
pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# 绘制线条
pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)

# 绘制圆形
pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)

# 绘制椭圆                             （x, y, width, height）
pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)
# 绘制正方形
pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# 获取所有渲染窗口的像素点
pixArray = pygame.PixelArray(windowSurface)
# 指定坐标点的颜色
pixArray[480][380] = BLACK

# 删除像素对象，接触渲染窗口被占用
del pixArray

# 在windowSurface上面绘制textRect
windowSurface.blit(text, textRect)

# 游戏版面绘制
pygame.display.update()

while True:
	# 操作事件监听
	for event in pygame.event.get():
		if event.type == 1:
			pygame.display.update()

		if event.type == QUIT:
			pygame.quit()
			sys.exit()
