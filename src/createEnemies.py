from .DemonFly import DemonFly
from .DemonAxe import DemonAxe
from settings import SCREEN_HEIGHT

def createEnemies(spriteGroup):
  spriteGroup.add(DemonFly(550, 0, 100))
  spriteGroup.add(DemonAxe(610, 0, 100))
