import pygame
import os
from player import *


pygame.init()

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280


screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('Ventana Mamalona')



Running = True
jugador = Player('Valentina', 'Mentiras', "./Graphics/player")
print(jugador.name, jugador.weapon)
fuente = './font/joystix.ttf'
clock = pygame.time.Clock()

def main():
    global Running
    font = pygame.font.Font(fuente,16)
    while Running:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                Running = False
        screen.fill('black')
        key = pygame.key.get_pressed()

        text_surface = font.render(jugador.name, True, (255,255,255))
        text_rect = text_surface.get_rect(center=(jugador.rect.centerx, jugador.rect.top - 10))
        
        screen.blit(jugador.animations[jugador.current_animation_key][jugador.current_frame_index], jugador.rect.topleft)
        screen.blit(text_surface, text_rect)


        jugador.move(key)
        clock.tick(60)
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
