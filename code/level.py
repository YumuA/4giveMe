import pygame
from Setting import *
from tile import Tile
from player import Player
from support import *
from random import choice
from weapon import Weapon
# from Enemy import Enemy
class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()  # Obtiene la superficie de visualización
        self.visible_sprites = YSortCameraGroup()  # Grupo de sprites visibles
        self.obstacle_sprites = pygame.sprite.Group()  # Grupo de sprites de obstáculos
        self.create_map()  # Crea el mapa del nivel
        self.current_attack = None  # Inicializa el ataque actual como nulo

    def create_map(self):
        # Definición de los diseños del mapa y los gráficos
        layouts = {
            'boundary': import_csv_layout('map/map_FloorBlocks.csv'),
            'grass': import_csv_layout('map/map_Grass.csv'),
            'object': import_csv_layout('map/map_Objects.csv'),
            'entities': import_csv_layout('map/map_Entities.csv')
        }
        graphics = {
            'grass': import_folder('graphics/grass'),
            'objects': import_folder('graphics/objects')
        }

        for style, layout in layouts.items():  # Itera sobre los diseños del mapa
            for row_index, row in enumerate(layout):  # Itera sobre las filas del diseño
                for col_index, col in enumerate(row):  # Itera sobre las columnas del diseño
                    if col != '-1':  # Verifica si el valor de la celda es diferente de '-1'
                        x = col_index * TILESIZE  # Calcula la coordenada x del sprite
                        y = row_index * TILESIZE  # Calcula la coordenada y del sprite
                        if style == 'boundary':  # Si es un borde
                            Tile((x, y), [self.obstacle_sprites], 'invisible')  # Crea un sprite invisible
                        elif style == 'grass':  # Si es pasto
                            random_grass_image = choice(graphics['grass'])  # Selecciona un gráfico de pasto al azar
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'grass', random_grass_image)  # Crea un sprite de pasto
                        elif style == 'object':  # Si es un objeto
                            surf = graphics['objects'][int(col)]  # Obtiene el gráfico del objeto
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)  # Crea un sprite de objeto
                        elif style == 'entities':  # Si son entidades
                            if col == '394':  # Si es el jugador
                                self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites, self.create_attack, self.destroy_weapon)  # Crea el jugador
                            else:
                                if col == '390': monster_name = 'bamboo'  # Si es un enemigo de tipo 'bamboo'
                                elif col == '391': monster_name = 'spirit'  # Si es un enemigo de tipo 'spirit'
                                elif col == '392': monster_name = 'raccon'  # Si es un enemigo de tipo 'raccon'
                               # Enemy(monster_name, (x, y), [self.visible_sprites], self.obstacle_sprites)  # Crea un enemigo

    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.visible_sprites])  # Crea un nuevo ataque del jugador

    def destroy_weapon(self):
        if self.current_attack:  # Si hay un ataque actual
            self.current_attack.kill()  # Elimina el ataque actual
        self.current_attack = None  # Reinicia el ataque actual como nulo

    def run(self):
        self.visible_sprites.custom_draw(self.player)  # Dibuja los sprites visibles
        self.visible_sprites.update()  # Actualiza los sprites visibles



class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()  # Inicializa el grupo de sprites
        self.display_surface = pygame.display.get_surface()  # Obtiene la superficie de visualización
        self.half_width = self.display_surface.get_size()[0] // 2  # Calcula la mitad del ancho de la pantalla
        self.half_height = self.display_surface.get_size()[1] // 2  # Calcula la mitad de la altura de la pantalla
        self.offset = pygame.math.Vector2()  # Inicializa un vector de desplazamiento
        self.floor_surf = pygame.image.load('graphics/tilemap/ground.png').convert()  # Carga la imagen del suelo
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))  # Obtiene el rectángulo del suelo

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width  # Calcula el desplazamiento horizontal
        self.offset.y = player.rect.centery - self.half_height  # Calcula el desplazamiento vertical
        floor_offset_pos = self.floor_rect.topleft - self.offset  # Calcula la posición del suelo con respecto al desplazamiento
        self.display_surface.blit(self.floor_surf, floor_offset_pos)  # Dibuja el suelo en la pantalla
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):  # Itera sobre los sprites ordenados por su posición vertical
            offset_pos = sprite.rect.topleft - self.offset  # Calcula la posición del sprite con respecto al desplazamiento
            self.display_surface.blit(sprite.image, offset_pos)  # Dibuja el sprite en la pantalla
