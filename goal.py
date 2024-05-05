import pygame
import random

class Goal():

    def __init__(self, screen_width, screen_height) -> None:
        self.width = 20
        self.height = self.width
        self.position = pygame.Vector2(random.randint(0, screen_width - self.width), random.randint(0, screen_height - self.width))
        self.rect = pygame.Rect((round(self.position.x - (self.width / 2)), round(self.position.y  - (self.height / 2)), self.width, self.height))
