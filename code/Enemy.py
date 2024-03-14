# import pygame
# from Setting import * 
# from Entity import Entity
# from support import *

# class Enemy(Entity):  # Define la clase Enemy, que hereda de Entity
#     def __init__(self, monster_name, pos, groups, obstacle_sprites):
#         super().__init__(groups)  # Llama al constructor de la clase padre Entity
#         self.sprite_type = 'enemy'
#         self.import_graphics(monster_name)  # Importa los gráficos del enemigo
#         self.status = 'idle'
#         self.image = self.animations[self.status][self.frame_index]  # Define la imagen inicial del enemigo
#         self.rect = self.image.get_rect(topleft=pos)  # Define el rectángulo de colisión
#         self.hitbox = self.rect.inflate(0, -10)  # Define la hitbox del enemigo
#         self.obstacle_sprites = obstacle_sprites  # Define los sprites de obstáculos
#         self.monster_name = monster_name  # Define el nombre del monstruo
#         monster_info = monster_data[self.monster_name]  # Obtiene información del monstruo desde monster_data
#         self.health = monster_info['health']  # Define la salud del enemigo
#         self.exp = monster_info['exp']  # Define la experiencia que otorga el enemigo al ser derrotado
#         self.speed = monster_info['speed']  # Define la velocidad de movimiento del enemigo
#         self.attack_damage = monster_info['damage']  # Define el daño de ataque del enemigo

#     def import_graphics(self, name):
#         self.animations = {'idle': [], 'move': [], 'attack': []}  # Inicializa el diccionario de animaciones
#         main_path = f'../graphics/monster/{name}/'  # Ruta principal para las animaciones del enemigo
#         for animation in self.animations.keys():
#             self.animations[animation] = import_folder(main_path + animation)  # Importa las animaciones del enemigo

#     def update(self):
#         self.move(self.speed)  # Actualiza la posición del enemigo