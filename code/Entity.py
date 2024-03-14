import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)  # Inicializa la clase base con los grupos proporcionados
        self.frame_index = 0  # Índice del fotograma actual de la animación
        self.animation_speed = 0.15  # Velocidad de la animación
        self.direction = pygame.math.Vector2()  # Vector de dirección de movimiento
        
    def move(self, speed):
        if self.direction.magnitude() != 0:  # Verifica si hay movimiento
            self.direction = self.direction.normalize()  # Normaliza el vector de dirección

        self.hitbox.x += self.direction.x * speed  # Actualiza la posición horizontal
        self.collision('horizontal')  # Maneja las colisiones horizontales
        self.hitbox.y += self.direction.y * speed  # Actualiza la posición vertical
        self.collision('vertical')  # Maneja las colisiones verticales
        self.rect.center = self.hitbox.center  # Actualiza el rectángulo del sprite
        
    def collision(self, direction):
        # Maneja las colisiones según la dirección especificada
        if direction == 'horizontal':  # Si se trata de una colisión horizontal
            for sprite in self.obstacle_sprites:  # Itera sobre los sprites de obstáculos
                if sprite.hitbox.colliderect(self.hitbox):  # Si hay colisión con otro sprite
                    if self.direction.x > 0:  # Si el movimiento es hacia la derecha
                        self.hitbox.right = sprite.hitbox.left  # Corrige la posición a la izquierda del obstáculo
                    if self.direction.x < 0:  # Si el movimiento es hacia la izquierda
                        self.hitbox.left = sprite.hitbox.right  # Corrige la posición a la derecha del obstáculo

        if direction == 'vertical':  # Si se trata de una colisión vertical
            for sprite in self.obstacle_sprites:  # Itera sobre los sprites de obstáculos
                if sprite.hitbox.colliderect(self.hitbox):  # Si hay colisión con otro sprite
                    if self.direction.y > 0:  # Si el movimiento es hacia abajo
                        self.hitbox.bottom = sprite.hitbox.top  # Corrige la posición arriba del obstáculo
                    if self.direction.y < 0:  # Si el movimiento es hacia arriba
                        self.hitbox.top = sprite.hitbox.bottom  # Corrige la posición abajo del obstáculo
