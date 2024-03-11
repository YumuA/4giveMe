import pygame
import sys
from player import *
from Settings import *


SCREEN_HEIGHT = screen_height - 400
SCREEN_WIDTH = screen_width - 400

class Game:
    def __init__(self):
 
        pygame.init()       
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        pygame.display.set_caption('Ventana Mamalona')
        self.clock = pygame.time.Clock()
        #main_sound = pygame.mixer.Sdound('asdasd')
        #main_sound.play(loops = -1)
        self.jugador = Player('MainCharacter', 'asd', "./Graphics/player")
        self.level = Level()
        self.fuente = './font/joystix.ttf'

    def update(self, keys):
            self.level.create_map()
            self.jugador.move(keys)
            
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    def render(self):
            
            self.screen.fill('black')
            text_surface = pygame.font.Font(self.fuente,16).render(self.jugador.name, True, (255,255,255))
            text_rect = text_surface.get_rect(center=(self.jugador.rect.centerx, self.jugador.rect.top - 10))
            self.screen.blit(self.jugador.animations[self.jugador.current_animation_key][self.jugador.current_frame_index], self.jugador.rect.topleft)
            self.screen.blit(text_surface, text_rect)
            
    
    def main(self):
        
        self.font = pygame.font.Font(self.fuente,16)
        while True:
            
            self.handle_events()
            keys = pygame.key.get_pressed()
            self.update(keys)
            self.render()
            pygame.display.flip()
            cloc = self.clock.tick(30)
            print(f'FPS: {cloc}')


if __name__ == '__main__':
    game =  Game()
    game.main()
    