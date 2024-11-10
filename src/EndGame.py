import pygame
from settings import SCREEN_HEIGHT, SCREEN_WIDTH

class EndGame(pygame.sprite.Sprite):

  def __init__(self, y):
    pygame.sprite.Sprite.__init__(self)
    self.images = {}
    self.image = pygame.transform.scale(pygame.image.load('assets/skyBackground.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))

    self.rect = self.image.get_rect()
    self.rect.topleft = 0, y
  def update(self, playerY, ySpeed):
    if playerY < SCREEN_HEIGHT/2+10:
      self.rect.move_ip(0, -ySpeed) 