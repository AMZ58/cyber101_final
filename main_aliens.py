import sys

import pygame 

class aliens_invade():

    def __init__(self):

        pygame.init()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("UAP Invasion 2025")

        self.color = (100,150,100,100)

        pygame.display.set_mode((1200,800))

    def run_game(self):

        while True:
            #looks for mouse keyboard & events


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


            self.window.fill(self.color)
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    ai = aliens_invade()
    ai.run_game()