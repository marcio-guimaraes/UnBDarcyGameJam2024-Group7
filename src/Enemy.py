import pygame
from settings import SCREEN_HEIGHT, FPS

class Enemy(pygame.sprite.Sprite):

  def __init__(self):
    pygame.sprite.Sprite.__init__(self)

  def update(self, playerY, ySpeed, player):
    if self.attackDelay > 0 and self.currentStatus != "attack":
      self.attackDelay-=1
    if self.currentStatus == 'death' and int(self.currentSpriteIndex) == len(self.sprites['death'])-1:
      self.delete()
    if self.currentStatus == 'hurt' and int(self.currentSpriteIndex) == len(self.sprites['hurt'])-1:
      self.changeStatus('walking')
    if self.currentStatus == 'attack' and int(self.currentSpriteIndex) == len(self.sprites['attack'])-1:
      self.attackDelay = FPS
      self.changeStatus('walking')

    self.currentSpriteIndex = self.currentSpriteIndex +0.2 if self.currentSpriteIndex < len(self.sprites[self.currentStatus])-1 else 0;
    self.image = self.sprites[self.currentStatus][int(self.currentSpriteIndex)]
    x = self.rect.x
    y = self.rect.y
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    moveInY = ySpeed if playerY < SCREEN_HEIGHT/2+10 else 0

    if self.currentStatus == 'death': return

    playerIsInRange = self.testIfPlayerInRange(player)
    playerIsInAttackRange = self.testIfPlayerInAttackRange(player)

    if self.currentStatus == 'attack':
      if player.rect.x > self.rect.x:
        self.image = pygame.transform.flip(self.image, True, False)
      self.xSpeed = 0
    elif playerIsInAttackRange and self.currentStatus != "hurt":
      self.changeStatus('idle' if self.sprites['idle'] else 'walking')
      self.xSpeed = 0
      if self.currentStatus != "attack" and self.attackDelay <= 0:
        self.changeStatus('attack')
    elif playerIsInRange and self.currentStatus != "hurt":
      self.changeStatus("walking")
      if player.rect.x > self.rect.x:
        self.xSpeed = 1
      else:
        self.xSpeed = -1
    elif self.rect.x <= self.xa and self.currentStatus != "hurt":
      self.xSpeed = 1
    elif self.rect.x >= self.xb and self.currentStatus != "hurt":
      self.xSpeed = -1
    elif self.xSpeed == 0 and self.currentStatus != "hurt":
      self.xSpeed = 1
    elif self.currentStatus == "hurt":
      self.xSpeed = 0
    elif self.currentStatus != "hurt":
      self.changeStatus("walking")
    
    self.move(moveInY )
    if self.xSpeed > 0:
      self.image = pygame.transform.flip(self.image, True, False)

  def changeStatus(self, newStatus):
    if newStatus == self.currentStatus: return
    self.currentStatus = newStatus
    self.currentSpriteIndex = 0
  
  def move(self, ySpeed = 0 ):
    self.ysAttack -= ySpeed
    self.yeAttack -= ySpeed
    self.rect.move_ip(self.xSpeed, -ySpeed)
  
  def hit(self, damage, left):
    if self.currentStatus == 'death': return
    if self.currentStatus != "hurt":
      self.attackDelay = FPS
      self.changeStatus('hurt')
      knockback = 0;
      if left == 1:
        knockback = -self.knockback
      else: 
        knockback = self.knockback
      self.rect.move_ip(knockback, 0)
      self.currentSpriteIndex = 0
      self.life -= damage
    if self.life < 0:
      self.initDeath()

  def initDeath(self):
    self.changeStatus('death')
  
  def delete(self):
    self.kill()
  
  def testIfPlayerInRange(self, player):
    playerMid = player.rect.y-player.rect.height/2
    return player.rect.x > self.xa and player.rect.x < self.xb and playerMid < self.rect.y and playerMid > self.rect.y-self.rect.height
  
  def testIfPlayerInAttackRange(self, player): 
    playerMidY = player.rect.y
    playerMidX = player.rect.x  
    return(playerMidX + self.attackRange > self.rect.x and playerMidX - self.attackRange < self.rect.x ) and (
      playerMidY + self.attackRange > self.rect.y and playerMidY - self.attackRange < self.rect.y
    )