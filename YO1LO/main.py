import pygame
from SaveLoadManager import SaveLoadSystem
pygame.init()


saveloadmanager = SaveLoadSystem(" .save", "save_data")

entities = saveloadmanager.load_game_data(["entities"])