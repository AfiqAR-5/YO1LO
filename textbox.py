import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("YO1LO")
font = pygame.font.Font("assets/ARCADE.TTF", 100)


bg = pygame.image.load('assets/prisoncell.png')
scaled_bg = pygame.transform.scale(bg, (1280,720))
bg_rect = scaled_bg.get_rect(x=0,y=0)


class Button():
	def __init__(self, image, x_pos, y_pos, text_input):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = font.render(self.text_input, True, "white")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self):
		screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			print("Button Press!")

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = font.render(self.text_input, True, "#ba2323")
		else:
			self.text = font.render(self.text_input, True, "white")

button_surface = pygame.image.load("assets/textbox.png")
button_surface = pygame.transform.scale(button_surface, (850, 200))

button = Button(button_surface, 640, 615, "")

while True:

	screen.blit(scaled_bg,bg_rect)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			button.checkForInput(pygame.mouse.get_pos())
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		
		
	button.update()
	button.changeColor(pygame.mouse.get_pos())
	pygame.display.update()