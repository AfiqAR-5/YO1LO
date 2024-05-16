import pygame

class CharacterPic():
    def __init__(self, image, pos, width, height, velocity):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.width = width
        self.height = height
        self.speed = [5]
        self.y_velocity = [5]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
    
    def update(self, screen):
        screen.blit(self.image, (self.x_pos, self.y_pos))	
        
    def react(self, pos, velocity):
    	if self.y_velocity == 6:
            pygame.time.wait(10)
            self.y_pos += self.y_velocity