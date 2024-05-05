import pygame

from goal import Goal
from player import Player
from information import Information

class Game():

    def __init__(self) -> None:
        self.dt = 0
        self.running = False
        self.winning_count = 0
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 600))
        self.screen.fill("black")
        
        pygame.display.set_caption('Reinforcement Learning Game')

    def game_start(self):
        pygame.init()
        self.running = True

        info = Information()
        goal = Goal(self.screen.get_width(), self.screen.get_height())
        player = Player(self, self.screen.get_width(), self.screen.get_height(), self.dt)
        font = pygame.font.SysFont('Comic Sans MS', 18)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_finish()
                    
            self.screen.fill("black")
            collide = goal.rect.colliderect(player.rect)
            goal_color = (0, 255, 0) if collide else (0, 0, 255)

            if info.min_distance == 0:
                info.min_distance = player.position.distance_to(goal.position)

            info.current_distance = player.position.distance_to(goal.position)
            info.distance += player.move(pygame.key.get_pressed(), self.dt)

            points_text = font.render(f'Points: {round(info.points, 0)}', False, (255, 255, 255))
            distance_text = font.render(f'Distance: {round(info.distance, 0)}', False, (255, 255, 255))
            min_distance_text = font.render(f'Mininum distance: {round(info.min_distance, 0)}', False, (255, 255, 255))
            current_distance = font.render(f'Current distance: {round(info.current_distance, 0)}', False, (255, 255, 255))
            
            self.screen.blit(points_text, (0, 0))
            self.screen.blit(distance_text, (0, 25))
            self.screen.blit(min_distance_text, (0, 50))
            self.screen.blit(current_distance, (0, 75))

            pygame.draw.rect(self.screen, "red", player.rect, 20)
            pygame.draw.rect(self.screen, goal_color, goal.rect, 20)

            pygame.display.flip()

            if collide:
                info.points += 1
                info.print_results()
                info.reset_distance()
                info.reset_min_distance()
                goal = Goal(self.screen.get_width(), self.screen.get_height())

            self.dt = self.clock.tick(30) / 1000

    def game_finish(self):
        self.running = False
        pygame.quit()

if  __name__ == "__main__":
    Game().game_start()
