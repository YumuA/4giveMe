import pygame, sys
from Setting import *
from level import Level


class Game:
    def __init__(self):


        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()

        # main_sound = pygame.mixer.Sound('audio/main.ogg')
        # main_sound.set_volume(0.1) 
        # main_sound.play(loops= -1)

        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()