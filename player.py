from Settings import import_folder
import pygame
import os

PLAYER_HEIGHT = 50
PLAYER_WIDTH = 50

class Player():
    def __init__(self, name, weapon, image_path_player):
        self.name = name
        self.health = 100
        self.weapon = weapon
        self.armor = None
        self.magicResist = None
        self.speed = None
        self.maxHealth = None
        self.stamin = None
        self.animations = {'up': [],'down': [],'left': [],'right': [],}
        self.load_animations(image_path_player)

        self.rect = pygame.Rect(280, 300, PLAYER_HEIGHT, PLAYER_WIDTH)
        self.current_animation_key = 'down'
        self.current_frame_index = 0

    def load_animations(self, character_path):
        for animation in self.animations.keys():
            full_path = os.path.join(character_path, animation)
            self.animations[animation] = import_folder(full_path)

    def attack(self, enemy):
        if enemy.health == 0:
            print("Haz matado a un enemigo, has recibido +10 de experiencia")
        elif enemy.health > 0:
            print("Has hecho tanto de daño, el enemigo tiene tanta vida")

    def move(self, key):
        if key[pygame.K_w]:
            self.rect.y -= 5
            if pygame.key.get_pressed()[pygame.K_w]:
                self.current_animation_key = 'up'
                self.current_frame_index += 1
                if self.current_frame_index >= len(self.animations[self.current_animation_key]):
                    self.current_frame_index = 0
            print("w")
        if key[pygame.K_s]:
            if pygame.key.get_pressed()[pygame.K_s]:
                self.current_animation_key = 'down'
                self.current_frame_index += 1
                if self.current_frame_index >= len(self.animations[self.current_animation_key]):
                    self.current_frame_index = 0
            self.rect.y += 5
            print("s")
        if key[pygame.K_a]:
            self.rect.x -= 5
            if pygame.key.get_pressed()[pygame.K_a]:
                self.current_animation_key = 'left'
                self.current_frame_index += 1
                if self.current_frame_index >= len(self.animations[self.current_animation_key]):
                    self.current_frame_index = 0
            print("a")
        if key[pygame.K_d]:
            self.rect.x += 5
            if pygame.key.get_pressed()[pygame.K_d]:
                self.current_animation_key = 'right'
                self.current_frame_index += 1
                if self.current_frame_index >= len(self.animations[self.current_animation_key]):
                    self.current_frame_index = 0
            print("d")