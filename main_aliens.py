import sys

import pygame 

class aliens_invade():

    def __init__(self):

        pygame.init()

        self.window = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("UAP Invasion 2025")

    def run_game(self):

        while True:
            #looks for mouse keyboard & events


            for event in pygame.QUIT:
                sys.exit

                pygame.display.flip()


if __name__ == '__main__':
    ai = aliens_invade()
    ai.run_game()