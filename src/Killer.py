import pygame
from settings import SCREEN_HEIGHT, FPS

class Killer(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.currentStatus = 'idle'
    self.sprites = {}

    self.dead = False;
    self.sprites['idle'] = []
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/history/killer/idle/tile000.png'), (19*2, 37*2)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/history/killer/idle/tile001.png'), (19*2, 37*2)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/history/killer/idle/tile002.png'), (19*2, 37*2)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/history/killer/idle/tile003.png'), (19*2, 37*2)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/history/killer/idle/tile004.png'), (19*2, 37*2)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/history/killer/idle/tile005.png'), (19*2, 37*2)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/history/killer/idle/tile006.png'), (19*2, 37*2)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/history/killer/idle/tile007.png'), (19*2, 37*2)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/history/killer/idle/tile008.png'), (19*2, 37*2)))
    self.sprites['idle'].append(pygame.transform.scale(pygame.image.load('assets/history/killer/idle/tile009.png'), (19*2, 37*2)))


    self.sprites['run'] = []
    self.sprites['run'].append(pygame.transform.scale(pygame.image.load('assets/history/killer/run/tile000.png'), (27*2, 37*2)))
    self.sprites['run'].append(pygame.transform.scale(pygame.image.load('assets/history/killer/run/tile001.png'), (24*2, 37*2)))
    self.sprites['run'].append(pygame.transform.scale(pygame.image.load('assets/history/killer/run/tile002.png'), (16*2, 37*2)))
    self.sprites['run'].append(pygame.transform.scale(pygame.image.load('assets/history/killer/run/tile003.png'), (17*2, 37*2)))
    self.sprites['run'].append(pygame.transform.scale(pygame.image.load('assets/history/killer/run/tile004.png'), (24*2, 37*2)))
    self.sprites['run'].append(pygame.transform.scale(pygame.image.load('assets/history/killer/run/tile005.png'), (28*2, 37*2)))
    self.sprites['run'].append(pygame.transform.scale(pygame.image.load('assets/history/killer/run/tile006.png'), (24*2, 37*2)))
    self.sprites['run'].append(pygame.transform.scale(pygame.image.load('assets/history/killer/run/tile007.png'), (16*2, 37*2)))
    self.sprites['run'].append(pygame.transform.scale(pygame.image.load('assets/history/killer/run/tile008.png'), (16*2, 37*2)))
    self.sprites['run'].append(pygame.transform.scale(pygame.image.load('assets/history/killer/run/tile009.png'), (25*2, 37*2)))

    self.sprites['attack'] = []
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/history/killer/attack/tile000.png'), (37*2, 36*2)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/history/killer/attack/tile001.png'), (64*2, 42*2)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/history/killer/attack/tile002.png'), (63*2, 35*2)))
    self.sprites['attack'].append(pygame.transform.scale(pygame.image.load('assets/history/killer/attack/tile003.png'), (57*2, 34*2)))

    self.currentSpriteIndex = 0
    self.image = self.sprites[self.currentStatus][self.currentSpriteIndex]

    self.rect = self.image.get_rect()
    self.rect.topleft = x, y

  def update(self): 
    currentTypeOfImage = self.currentStatus

    self.currentSpriteIndex = self.currentSpriteIndex + 0.2 if self.currentSpriteIndex < len(self.sprites[currentTypeOfImage])-1 else 3;
    self.image = self.sprites[currentTypeOfImage][int(self.currentSpriteIndex)]