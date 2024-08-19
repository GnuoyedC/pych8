WIDTH,HEIGHT = (64,32) # pixels
BLACK,WHITE = ((0,0,0),(255,255,255))
import pygame

class Display:
    def __init__(self,):
        self.grid = self.clear()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        return
    def clear(self):
        self.grid = self.create_empty()
    def create_empty(self):
        return [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]  # Create a 2D list with distinct rows
