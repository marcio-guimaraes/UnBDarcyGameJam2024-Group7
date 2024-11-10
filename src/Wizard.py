import pygame
from .Enemy import Enemy
from settings import FPS

class Wizard(Enemy):
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

    self.deathSound = pygame.mixer.Sound('song/EnemySonds/DeathWizard.wav')
    self.deathSound.set_volume(1.0)
    self.attackSound = pygame.mixer.Sound('song/EnemySonds/AttackWizard.wav')
    self.attackSound.set_volume(1.0)

    self.sprites['idle'] = []
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Idle/Idle_1.png'), (24*2.4, 39*2.4)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Idle/Idle_2.png'), (24*2.4, 39*2.4)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Idle/Idle_3.png'), (24*2.4, 39*2.4)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Idle/Idle_4.png'), (24*2.4, 39*2.4)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Idle/Idle_5.png'), (24*2.4, 39*2.4)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Idle/Idle_6.png'), (24*2.4, 39*2.4)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Idle/Idle_7.png'), (24*2.4, 39*2.4)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Idle/Idle_8.png'), (24*2.4, 39*2.4)))

    self.sprites['walking'] = []
    self.sprites['walking'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Run/Run_1.png'), (24*2.4, 39*2.4)))
    self.sprites['walking'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Run/Run_2.png'), (24*2.4, 39*2.4)))
    self.sprites['walking'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Run/Run_3.png'), (24*2.4, 39*2.4)))
    self.sprites['walking'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Run/Run_4.png'), (24*2.4, 39*2.4)))
    self.sprites['walking'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Run/Run_5.png'), (24*2.4, 39*2.4)))
    self.sprites['walking'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Run/Run_6.png'), (24*2.4, 39*2.4)))
    self.sprites['walking'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Run/Run_7.png'), (24*2.4, 39*2.4)))
    self.sprites['walking'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Run/Run_8.png'), (24*2.4, 39*2.4)))

    self.sprites['attack'] = []
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Attack/Attack1_1.png'), (24*2.4, 39*2.6)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Attack/Attack1_2.png'), (24*2.4, 39*2.6)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Attack/Attack1_3.png'), (24*2.4, 39*2.6)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Attack/Attack1_4.png'), (24*2.4, 39*2.6)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Attack/Attack1_5.png'), (24*2.4, 39*2.6)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Attack/Attack1_6.png'), (24*2.4, 39*2.6)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Attack/Attack1_7.png'), (24*2.4, 39*2.6)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Attack/Attack1_8.png'), (24*2.4, 39*2.6)))


    self.sprites['hurt'] = []
    self.sprites['hurt'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Hurt/Hurt_1.png'), (24*2.4, 39*2.4)))
    self.sprites['hurt'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Hurt/Hurt_2.png'), (24*2.4, 39*2.4)))
    self.sprites['hurt'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Hurt/Hurt_3.png'), (24*2.4, 39*2.4)))


    self.sprites['death'] = []
    self.sprites['death'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Death/Death_1.png'), (24*2.4, 38*2.4)))
    self.sprites['death'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Death/Death_2.png'), (24*2.4, 38*2.4)))
    self.sprites['death'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Death/Death_3.png'), (24*2.4, 38*2.4)))
    self.sprites['death'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Death/Death_4.png'), (24*2.4, 38*2.4)))
    self.sprites['death'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Death/Death_5.png'), (24*2.4, 38*2.4)))
    self.sprites['death'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Death/Death_6.png'), (24*2.4, 38*2.4)))
    self.sprites['death'].append(pygame.transform.scale(pygame.image.load('assets/Wizard/Death/Death_7.png'), (24*2.4, 38*2.4)))

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
    if self.currentStatus != "hurt" and self.currentStatus != "idle":
      self.image = pygame.transform.flip(self.image, True, False)
  
  def changeStatus(self, newStatus):
    if newStatus == self.currentStatus: return
    if newStatus == 'death':
      print("Death")
      self.deathSound.play()
    if newStatus == 'attack':
      self.attackSound.play()
    super().changeStatus(newStatus)
