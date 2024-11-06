import pygame
from .Enemy import Enemy
from settings import SCREEN_HEIGHT, FPS

class DemonFly(Enemy):
  def __init__(self, y, xa, xb, xsAttack = None, xeAttack=None, ysAttack=None, yeAttack=None ):
    pygame.sprite.Sprite.__init__(self)
    self.currentStatus = 'walking'

    self.xSpeed = 0
    self.xa = xa
    self.xb = xb
    self.y = y
    self.life = 100
    self.attackRange = 40
    self.damage = 0.5
    self.knockback = 20
    self.attackDelay = FPS

    self.sprites = {}
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

    self.sprites['walking'] = []
    self.sprites['walking'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Flying/Demon_Fly_Flying_0.png'), (79, 69)))
    self.sprites['walking'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Flying/Demon_Fly_Flying_1.png'), (79, 69)))
    self.sprites['walking'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Flying/Demon_Fly_Flying_2.png'), (79, 69)))
    self.sprites['walking'].append(pygame.transform.scale(pygame.image.load('assets/DemonFly/Flying/Demon_Fly_Flying_3.png'), (79, 69)))

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

    self.xsAttack = xsAttack if xsAttack else xa
    self.xeAttack = xeAttack if xeAttack else xb
    self.ysAttack = ysAttack if ysAttack else y
    self.yeAttack = yeAttack if yeAttack else y-self.rect.height
