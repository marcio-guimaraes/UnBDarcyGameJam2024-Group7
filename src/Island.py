import pygame
from settings import SCREEN_HEIGHT

class Island(pygame.sprite.Sprite):
  def __init__(self, type, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.sprites = {}
    
    self.sprites['left'] = pygame.transform.scale(pygame.image.load('assets/Island/left.png'), (128/2.5, 128/2.5))
    self.sprites['mid'] = pygame.transform.scale(pygame.image.load('assets/Island/mid.png'), (128/2.5, 128/2.5))
    self.sprites['right'] = pygame.transform.scale(pygame.image.load('assets/Island/right.png'), (128/2.5, 128/2.5))
    self.sprites['leftGrass'] = pygame.transform.scale(pygame.image.load('assets/Island/leftGrass.png'), (128/2.5, 128/2.5))
    self.sprites['midGrass'] = pygame.transform.scale(pygame.image.load('assets/Island/midGrass.png'), (128/2.5, 128/2.5))
    self.sprites['rightGrass'] = pygame.transform.scale(pygame.image.load('assets/Island/rightGrass.png'), (128/2.5, 128/2.5))
    self.sprites['ground'] = pygame.transform.scale(pygame.image.load('assets/Island/ground.png'), (128/2.5, 128/2.5))
    
    self.image = self.sprites[type]
    self.rect = self.image.get_rect()
    self.rect.topleft = x-self.rect.width, y-self.rect.height

  def update(self, playerY, ySpeed):
    if playerY < SCREEN_HEIGHT/2+10:
      self.rect.move_ip(0, -ySpeed)
  