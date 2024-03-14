import pygame
from Setting import *
from support import import_folder
from Entity import * 

class Player(Entity):
	def __init__(self,pos,groups,obstacle_sprites,create_attack,destroy_weapon):
		super().__init__(groups)
		self.image = pygame.image.load('graphics/test/player.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(0,-26)
		self.import_player_assets()
		self.status = 'down'
		
		self.weapon_attack_sound = pygame.mixer.Sound('audio/sword.wav')
		self.weapon_attack_sound.set_volume(0.4)


		self.speed = 5
		self.attacking = False
		self.attack_cooldown = 400
		self.attack_time = None
		self.create_attack = create_attack
		self.destroy_weapon = destroy_weapon

		self.obstacle_sprites = obstacle_sprites
		self.weapon_index = 0
		self.can_switch_weapon = True
		self.weapon_switch_time = None
		self.switch_duration_cooldown = 200
		self.weapon = list (weapon_data.keys())[self.weapon_index]

	def import_player_assets(self):
		character_path = 'graphics/player/'
		self.animations = {'up': [],'down': [],'left': [],'right': [],
			'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
			'right_attack':[],'left_attack':[],'up_attack':[],'down_attack':[]}

		for animation in self.animations.keys():
			full_path = character_path + animation
			self.animations[animation] = import_folder(full_path)

	def input(self):
		if not self.attacking:
			keys = pygame.key.get_pressed()


			if keys[pygame.K_UP]:
				self.direction.y = -1
				self.status = 'up'
			elif keys[pygame.K_DOWN]:
				self.direction.y = 1
				self.status = 'down'
			else:
				self.direction.y = 0

			if keys[pygame.K_RIGHT]:
				self.direction.x = 1
				self.status = 'right'
			elif keys[pygame.K_LEFT]:
				self.direction.x = -1
				self.status = 'left'
			else:
				self.direction.x = 0


			if keys[pygame.K_SPACE]:
				self.attacking = True
				self.attack_time = pygame.time.get_ticks()
				self.create_attack()
				self.weapon_attack_sound.play()

			if keys[pygame.K_q] and self.can_switch_weapon:
				self.can_switch_weapon = False
				self.weapon_switch_time = pygame.time.get_ticks()
				if self.weapon_index < len(list(weapon_data.keys()))-1:
					self.weapon_index += 1
				else:
					self.weapon_index = 0
				self.weapon = list (weapon_data.keys())[self.weapon_index]

	def get_status(self):

		if self.direction.x == 0 and self.direction.y == 0:
			if not 'idle' in self.status and not 'attack' in self.status:
				self.status = self.status + '_idle'

		if self.attacking:
			self.direction.x = 0
			self.direction.y = 0
			if not 'attack' in self.status:
				if 'idle' in self.status:
					self.status = self.status.replace('_idle','_attack')
				else:
					self.status = self.status + '_attack'
		else:
			if 'attack' in self.status:
				self.status = self.status.replace('_attack','')

	def cooldowns(self):
		current_time = pygame.time.get_ticks()

		if self.attacking:
			if current_time - self.attack_time >= self.attack_cooldown:
				self.attacking = False
				self.destroy_weapon()
		if not self.can_switch_weapon:
			if current_time - self.weapon_switch_time >= self.switch_duration_cooldown:
				self.can_switch_weapon = True

	def animate(self):
		animation = self.animations[self.status]

		self.frame_index += self.animation_speed
		if self.frame_index >= len(animation):
			self.frame_index = 0

		self.image = animation[int(self.frame_index)]
		self.rect = self.image.get_rect(center = self.hitbox.center)

	def update(self):
		self.input()
		self.cooldowns()
		self.get_status()
		self.animate()
		self.move(self.speed)