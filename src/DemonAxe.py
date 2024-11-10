import pygame
from .Enemy import Enemy
from settings import FPS



class DemonAxe(Enemy):
  def __init__(self, y, xa, xb, xsAttack = None, xeAttack=None, ysAttack=None, yeAttack=None):
    pygame.sprite.Sprite.__init__(self)
    self.currentStatus = 'walking'
    self.xSpeed = 0
    self.xa = xa
    self.xb = xb
    self.y = y
    self.life = 200
    self.attackRange = 40
    self.damage = 0.75 #0.5
    self.attackDelay = FPS
    self.knockback = 5
    self.sprites = {}

    self.deathSound = pygame.mixer.Sound('song/EnemySonds/DeathDemonAxe.wav')
    self.deathSound.set_volume(1.0)
    self.attackSound = pygame.mixer.Sound('song/EnemySonds/AttackDemonAxe.wav')
    self.attackSound.set_volume(1.0)

    self.sprites['idle'] = []
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/DemonAxe/Idle/idle_1.png'), (24*2.4, 39*2.4)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/DemonAxe/Idle/idle_2.png'), (24*2.4, 39*2.4)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/DemonAxe/Idle/idle_3.png'), (24*2.4, 39*2.4)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/DemonAxe/Idle/idle_4.png'), (24*2.4, 39*2.4)))

    self.sprites['hurt'] = []
    self.sprites['hurt'].append(pygame.transform.scale(pygame.image.load('assets/DemonAxe/Hurt/hurt_1.png'), (24*2.4, 39*2.4)))
    self.sprites['hurt'].append(pygame.transform.scale(pygame.image.load('assets/DemonAxe/Hurt/hurt_2.png'), (24*2.4, 39*2.4)))
    self.sprites['hurt'].append(pygame.transform.scale(pygame.image.load('assets/DemonAxe/Hurt/hurt_3.png'), (24*2.4, 39*2.4)))

    self.sprites['walking'] = []
    self.sprites['walking'].append(pygame.transform.scale(pygame.image.load('assets/DemonAxe/Walk/walk_1.png'), (24*2.4, 39*2.4)))
    self.sprites['walking'].append(pygame.transform.scale(pygame.image.load('assets/DemonAxe/Walk/walk_2.png'), (24*2.4, 39*2.4)))
    self.sprites['walking'].append(pygame.transform.scale(pygame.image.load('assets/DemonAxe/Walk/walk_3.png'), (24*2.4, 39*2.4)))
    self.sprites['walking'].append(pygame.transform.scale(pygame.image.load('assets/DemonAxe/Walk/walk_4.png'), (24*2.4, 39*2.4)))
    self.sprites['walking'].append(pygame.transform.scale(pygame.image.load('assets/DemonAxe/Walk/walk_5.png'), (24*2.4, 39*2.4)))
    self.sprites['walking'].append(pygame.transform.scale(pygame.image.load('assets/DemonAxe/Walk/walk_6.png'), (24*2.4, 39*2.4)))

    self.sprites['death'] = []
    self.sprites['death'].append(pygame.transform.scale(pygame.image.load('assets/DemonAxe/Death/death_1.png'), (24*2.4, 38*2.4)))
    self.sprites['death'].append(pygame.transform.scale(pygame.image.load('assets/DemonAxe/Death/death_2.png'), (24*2.4, 38*2.4)))
    self.sprites['death'].append(pygame.transform.scale(pygame.image.load('assets/DemonAxe/Death/death_3.png'), (24*2.4, 38*2.4)))
    self.sprites['death'].append(pygame.transform.scale(pygame.image.load('assets/DemonAxe/Death/death_4.png'), (24*2.4, 38*2.4)))

    self.sprites['attack'] = []
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/DemonAxe/Attack1/attack1_1.png'), (24*2.4, 39*2.4)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/DemonAxe/Attack1/attack1_2.png'), (24*2.4, 39*2.4)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/DemonAxe/Attack1/attack1_3.png'), (24*2.4, 39*2.4)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/DemonAxe/Attack1/attack1_4.png'), (40*2.4, 39*2.4)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/DemonAxe/Attack1/attack1_5.png'), (24*2.4, 39*2.4)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/DemonAxe/Attack1/attack1_6.png'), (24*2.4, 39*2.4)))

    self.currentSpriteIndex = 0
    self.image = self.sprites[self.currentStatus][self.currentSpriteIndex]

    self.rect = self.image.get_rect()
    self.rect.topleft = xa, y

    self.xsAttack = xsAttack if xsAttack else xa
    self.xeAttack = xeAttack if xeAttack else xb
    self.ysAttack = ysAttack if ysAttack else y
    self.yeAttack = yeAttack if yeAttack else y

  def update(self, playerY, ySpeed, player):
    super().update(playerY, ySpeed, player)
    self.image = pygame.transform.flip(self.image, True, False)
  
  def changeStatus(self, newStatus):
    if newStatus == self.currentStatus: return
    if newStatus == 'death':
      self.deathSound.play()
    if newStatus == 'attack':
      self.attackSound.play()
    super().changeStatus(newStatus)
