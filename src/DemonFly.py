import pygame
from settings import SCREEN_HEIGHT

class DemonFly(pygame.sprite.Sprite):
  def __init__(self, y, xa, xb):
    pygame.sprite.Sprite.__init__(self)
    self.currentStatus = 'flying'
    self.sprites = {}
    self.falling = False
    self.xSpeed = 0
    self.xa = xa
    self.xb = xb
    self.y = y
    self.life = 100
    self.sprites['idle'] = []
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Idle/Demon_Fly_Idle_0.png'), (79, 69)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Idle/Demon_Fly_Idle_1.png'), (79, 69)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Idle/Demon_Fly_Idle_2.png'), (79, 69)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Idle/Demon_Fly_Idle_3.png'), (79, 69)))

    self.sprites['hurt'] = []
    self.sprites['hurt'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Hurt/Demon_Fly_Hurt_0.png'), (79, 69)))
    self.sprites['hurt'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Hurt/Demon_Fly_Hurt_1.png'), (79, 69)))
    self.sprites['hurt'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Hurt/Demon_Fly_Hurt_2.png'), (79, 69)))
    self.sprites['hurt'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Hurt/Demon_Fly_Hurt_3.png'), (79, 69)))

    self.sprites['flying'] = []
    self.sprites['flying'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Flying/Demon_Fly_Flying_0.png'), (79, 69)))
    self.sprites['flying'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Flying/Demon_Fly_Flying_1.png'), (79, 69)))
    self.sprites['flying'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Flying/Demon_Fly_Flying_2.png'), (79, 69)))
    self.sprites['flying'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Flying/Demon_Fly_Flying_3.png'), (79, 69)))

    self.sprites['death'] = []
    self.sprites['death'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Death/Demon_Fly_Death_0.png'), (79, 69)))
    self.sprites['death'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Death/Demon_Fly_Death_1.png'), (79, 69)))
    self.sprites['death'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Death/Demon_Fly_Death_2.png'), (79, 69)))
    self.sprites['death'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Death/Demon_Fly_Death_3.png'), (79, 69)))
    self.sprites['death'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Death/Demon_Fly_Death_4.png'), (79, 69)))
    self.sprites['death'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Death/Demon_Fly_Death_5.png'), (79, 69)))
    self.sprites['death'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Death/Demon_Fly_Death_6.png'), (79, 69)))

    self.sprites['attack'] = []
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Attack/Demon_Fly_Attack_0.png'), (79, 69)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Attack/Demon_Fly_Attack_1.png'), (79, 69)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Attack/Demon_Fly_Attack_2.png'), (79, 69)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Attack/Demon_Fly_Attack_3.png'), (79, 69)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Attack/Demon_Fly_Attack_4.png'), (79, 69)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Attack/Demon_Fly_Attack_5.png'), (79, 69)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Attack/Demon_Fly_Attack_6.png'), (79, 69)))

    self.currentSpriteIndex = 0
    self.image = self.sprites[self.currentStatus][self.currentSpriteIndex]

    self.rect = self.image.get_rect()
    self.rect.topleft = xa, y


  def update(self, playerY, ySpeed): 
    if self.currentStatus == 'death' and int(self.currentSpriteIndex) == 6:
      self.delete();

    if self.currentStatus == 'hurt' and int(self.currentSpriteIndex) == 3:
      self.changeStatus('flying')
    self.currentSpriteIndex = self.currentSpriteIndex +0.2 if self.currentSpriteIndex < len(self.sprites[self.currentStatus])-1 else 0;
    self.image = self.sprites[self.currentStatus][int(self.currentSpriteIndex)]
    moveInY = ySpeed if playerY < SCREEN_HEIGHT/2+10 else 0
    self.move(moveInY)
    if self.xSpeed > 0:
      self.image = pygame.transform.flip(self.image, True, False)

  def changeStatus(self, newStatus):
    if newStatus == self.currentStatus: return
    self.currentStatus = newStatus
    self.currentSpriteIndex = 0
  
  def move(self, ySpeed = 0):
    if self.rect.x <= self.xa: 
      self.xSpeed = 1
    elif self.rect.x >= self.xb:
      self.xSpeed = -1
    
    self.rect.move_ip(self.xSpeed, -ySpeed)
  
  def hit(self, damage, left):
    if self.currentStatus == 'death': return
    if self.currentStatus != "hurt":
      self.changeStatus('hurt')
      knockback = 0;
      if left == 1:
        knockback = -20
      else: 
        knockback = 20
      self.rect.move_ip(knockback, 0)
      self.currentSpriteIndex = 0
      self.life -= damage
    if self.life < 0:
      self.initDeath()

  def initDeath(self):
    self.changeStatus('death')
  
  def delete(self):
    self.kill()