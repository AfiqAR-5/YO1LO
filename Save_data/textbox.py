import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("YO1LO")
font = pygame.font.SysFont("Georgia", 100)
message = 'what the hellllllllllllll'
snip = font.render('', True, 'white')
counter = 0
speed = 3
done = False


bg = pygame.image.load('Save_data/prisoncell.png')
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

button_surface = pygame.image.load("Save_data/textbox.png")
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
		if counter < speed * len(message):
			done = True
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		
		snip = font.render(message[0: counter//speed], True, 'white')
		screen.blit(snip, (10, 310))
		
	button.update()
	button.changeColor(pygame.mouse.get_pos())
	pygame.display.update()