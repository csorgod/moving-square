import pygame
from helper import Helper


class Player():

    def __init__(self, game, screen_width, screen_height, dt) -> None:
        self.dt = dt
        self.width = 30
        self.game = game
        self.distance = 200
        self.height = self.width
        self.position = pygame.Vector2(screen_width / 2, screen_height / 2)
        self.rect = (round(self.position.x - (self.width / 2)), round(self.position.y  - (self.height / 2)), self.width, self.height)
        
    def move(self, keys, dt):
        self.dt = dt
        walked = False

        if keys[pygame.K_w]:
            if not Helper.screen_limit_reached(12, self.position, self.game, self):
                self.position.y -= self.distance * self.dt
                walked = True
        if keys[pygame.K_s]:
            if not Helper.screen_limit_reached(6, self.position, self.game, self):
                self.position.y += self.distance * self.dt
                walked = True
        if keys[pygame.K_a]:
            if not Helper.screen_limit_reached(9, self.position, self.game, self):
                self.position.x -= self.distance * self.dt
                walked = True
        if keys[pygame.K_d]:
            if not Helper.screen_limit_reached(3, self.position, self.game, self):
                self.position.x += self.distance * self.dt
                walked = True

        self.update()
        return (self.distance * self.dt) if walked else 0

    def update(self):
        self.rect = pygame.Rect((round(self.position.x - (self.width / 2)), round(self.position.y  - (self.height / 2)), self.width, self.height))
