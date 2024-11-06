import pygame
from settings import SCREEN_HEIGHT

class Player(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.currentStatus = 'idle'
    self.life = 100
    self.bottomCollide = False
    self.topCollide = False
    self.leftCollide = False
    self.rightCollide = False
    self.xSpeed = 0;
    self.ySpeed = 0;
    self.lastMove = 1
    self.sprites = {}
    self.falling = False
    self.sprites['idle'] = []
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Idle/HeroKnight_Idle_0.png'), (44*1.7, 40*1.7)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Idle/HeroKnight_Idle_1.png'), (44*1.7, 40*1.7)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Idle/HeroKnight_Idle_2.png'), (44*1.7, 40*1.7)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Idle/HeroKnight_Idle_3.png'), (44*1.7, 40*1.7)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Idle/HeroKnight_Idle_4.png'), (44*1.7, 40*1.7)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Idle/HeroKnight_Idle_5.png'), (44*1.7, 40*1.7)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Idle/HeroKnight_Idle_6.png'), (44*1.7, 40*1.7)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Idle/HeroKnight_Idle_7.png'), (44*1.7, 40*1.7)))

    self.sprites['run'] = []
    self.sprites['run'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Run/HeroKnight_Run_1.png'), (44*1.7, 40*1.7)))
    self.sprites['run'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Run/HeroKnight_Run_2.png'), (44*1.7, 40*1.7)))
    self.sprites['run'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Run/HeroKnight_Run_3.png'), (44*1.7, 40*1.7)))
    self.sprites['run'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Run/HeroKnight_Run_4.png'), (44*1.7, 40*1.7)))
    self.sprites['run'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Run/HeroKnight_Run_5.png'), (44*1.7, 40*1.7)))
    self.sprites['run'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Run/HeroKnight_Run_6.png'), (44*1.7, 40*1.7)))
    self.sprites['run'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Run/HeroKnight_Run_7.png'), (44*1.7, 40*1.7)))
    self.sprites['run'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Run/HeroKnight_Run_8.png'), (44*1.7, 40*1.7)))
    self.sprites['run'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Run/HeroKnight_Run_9.png'), (44*1.7, 40*1.7)))

    self.sprites['fall'] = []
    self.sprites['fall'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Fall/HeroKnight_Fall_0.png'), (44*1.7, 40*1.7)))
    self.sprites['fall'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Fall/HeroKnight_Fall_1.png'), (44*1.7, 40*1.7)))
    self.sprites['fall'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Fall/HeroKnight_Fall_2.png'), (44*1.7, 40*1.7)))
    self.sprites['fall'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Fall/HeroKnight_Fall_3.png'), (44*1.7, 40*1.7)))

    self.sprites['attack'] = []
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Attack1/HeroKnight_Attack1_0.png'), (44*1.7, 40*1.7)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Attack1/HeroKnight_Attack1_1.png'), (32*1.7, 40*1.7)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Attack1/HeroKnight_Attack1_2.png'), (75*1.7, 40*1.7)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Attack1/HeroKnight_Attack1_3.png'), (49*1.7, 39*1.7)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Attack1/HeroKnight_Attack1_4.png'), (38*1.7, 39*1.7)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/HeroKnight/Attack1/HeroKnight_Attack1_5.png'), (28*1.7, 39*1.7)))

    self.currentSpriteIndex = 0
    self.image = self.sprites[self.currentStatus][self.currentSpriteIndex]

    self.rect = self.image.get_rect()
    self.rect.topleft = 100, 500

  def update(self): 
    print(self.life)
    currentTypeOfImage = self.currentStatus
    if not self.currentStatus == "attack" and not self.bottomCollide:
      currentTypeOfImage = 'fall'


    if self.currentStatus == 'attack' and not self.currentSpriteIndex < len(self.sprites[currentTypeOfImage])-1:
      self.endAttack()
    
    if self.currentStatus == 'attack' and int(self.currentSpriteIndex) == 2 and self.lastMove < 0: 
      self.rect.move_ip(-4, 0)

    self.currentSpriteIndex = self.currentSpriteIndex +0.2 if self.currentSpriteIndex < len(self.sprites[currentTypeOfImage])-1 else 0;
    self.image = self.sprites[currentTypeOfImage][int(self.currentSpriteIndex)]

    if self.topCollide and self.ySpeed < 0:
      self.ySpeed = 0
    
    if self.rightCollide and self.xSpeed > 0:
      self.xSpeed = 0
      if self.ySpeed < 0:
        self.ySpeed = 0
    if self.leftCollide and self.xSpeed < 0: 
      self.xSpeed = 0
      if self.ySpeed < 0:
        self.ySpeed = 0

    if not self.bottomCollide:
      self.ySpeed += 0.2
    else: 
      self.ySpeed = 0;

    if self.lastMove < 0:
      self.image = pygame.transform.flip(self.image, True, False)

    if self.ySpeed != 0 and self.rect.y > SCREEN_HEIGHT/2:
      self.rect.move_ip(0, self.ySpeed)

    if self.xSpeed < 0 and self.rect.x < 5: return # Limite  esquerdo
    if self.xSpeed > 0 and self.rect.x > 600-self.rect.width: return # Limite  direito
    self.rect.move_ip(self.xSpeed if self.ySpeed == 0 else self.xSpeed/1.5, 0)

  def changeStatus(self, newStatus):
    if newStatus == self.currentStatus: return
    self.currentStatus = newStatus
    self.currentSpriteIndex = 0

  def run(self, speed):
    self.lastMove = 1 if speed > 0 else -1

    self.xSpeed = speed
    if not self.currentStatus == 'fall': self.changeStatus('run')
  
  def jump(self):
    if not self.bottomCollide: return
    self.ySpeed = -9
    self.bottomCollide = False
  
  def attack(self):
    if self.bottomCollide:
      self.xSpeed = 0
    self.changeStatus('attack')
  
  def endAttack(self):
    self.changeStatus('idle')
