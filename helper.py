import pygame

class Helper():

    @staticmethod
    def screen_limit_reached(coord: int, position: pygame.Vector2, game, player) -> bool:
        if coord == 12 and player.position.y <= (0  + (player.width / 2)):
            return True
        elif coord == 6 and player.position.y >= game.screen.get_height() - (player.width / 2):
            return True
        elif coord == 9 and player.position.x <= (0  + (player.height / 2)):
            return True
        elif coord == 3 and player.position.x >= game.screen.get_width() - (player.height / 2):
            return True
        else:
            return False
