import pygame
from settings import SCREEN_HEIGHT, SCREEN_WIDTH

class Background(pygame.sprite.Sprite):

  def __init__(self, y, imageType):
    pygame.sprite.Sprite.__init__(self)
    self.images = {}
    self.images['dirt'] = pygame.transform.scale(pygame.image.load('assets/background.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))
    self.images['florest'] = pygame.transform.scale(pygame.image.load('assets/florest.png'), (600, 337))
    self.images['sky'] = pygame.transform.scale(pygame.image.load('assets/skyBackground.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))

    self.image = self.images[imageType]
    self.rect = self.image.get_rect()
    self.rect.topleft = 0, y
  def update(self, playerY, ySpeed):
    if playerY < SCREEN_HEIGHT/2+10:
      self.rect.move_ip(0, -ySpeed) 