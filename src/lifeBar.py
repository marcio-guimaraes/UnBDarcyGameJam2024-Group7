import pygame

class LifeBar(pygame.sprite.Sprite):

  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.transform.scale(pygame.image.load('assets/lifeBar.png'), (855 *0.2 , 207*0.2))
    self.rect = self.image.get_rect()
    self.rect.topleft = 10, 10