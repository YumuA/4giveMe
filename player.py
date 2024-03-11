from Settings import *
import pygame
import os
from random import choice

PLAYER_HEIGHT = 50
PLAYER_WIDTH = 50

SCREEN_HEIGHT = screen_height - 400
SCREEN_WIDTH = screen_width - 400

TILESIZE = 64

#class Tile(pygame.sprite.Sprite):
#	def __init__(self,pos,groups,sprite_type,surface = pygame.Surface((TILESIZE,TILESIZE))):
#		super().__init__(groups)
#		self.sprite = sprite_type
#		self.image = surface
#		if sprite_type == 'object':
#			self.rect = self.image.get_rect(topleft=(pos[0], pos[1] - TILESIZE))
#		else:
#			self.rect = self.image.get_rect(topleft = pos)
#		self.hitbox = self.rect.inflate(0, -10)

class Level:
    def __init__(self):
        
        
        self.display_surface = pygame.display.get_surface()
        
        self.create_map()
        self.height_Screen = screen_height - 200
        self.size_cube = 128
        
        
    def create_map(self):
        layouts = {
            'boundary': import_map_csv('map/map_FloorBlocks.csv'),
			'grass': import_map_csv('map/map_Grass.csv'),
			'object': import_map_csv('map/map_Objects.csv')
        }
        graphics = {
            'grass': import_folder('graphics_co/grass'),
			'objects': import_folder('graphics_co/objects')
        }

        for style, layout in layouts.items():
                for row_index,row in enumerate(layout):
                    for col_index, col in enumerate(row):
                        if col != '-1':
                            x = col_index * TILESIZE
                            y = row_index * TILESIZE
                            if style == 'grass':
                                random_grass_image = choice(graphics['grass'])
                            if style == 'object':
                                surf = graphics['objects'][int (col)]


        

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
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))