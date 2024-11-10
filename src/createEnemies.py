from .DemonFly import DemonFly
from .DemonAxe import DemonAxe
from .Wizard import Wizard
from settings import SCREEN_HEIGHT

def createEnemies(spriteGroup):
  spriteGroup.add(DemonFly(550, 0, 100))
  demonAxeBase = DemonAxe(0, 0, 0)

  spriteGroup.add(DemonFly(230, 100, 200 ))
  spriteGroup.add(DemonFly(10, 350, 550))
  spriteGroup.add(DemonFly(-470, 300, 450))

  spriteGroup.add(DemonAxe(-790, 350, 550 ))

  spriteGroup.add(DemonFly(-1070, 0, 100))
  spriteGroup.add(DemonAxe(-1290, 200, 350))

  spriteGroup.add(DemonFly(-1820, 200, 300))

  spriteGroup.add(Wizard(-2140, 150, 400))
  spriteGroup.add(DemonFly(-2290, 0, 100))
  spriteGroup.add(DemonFly(-2270, 500, 590))

  spriteGroup.add(Wizard(-2760, 50, 300))

  spriteGroup.add(DemonFly(-3705, 450, 550))

  spriteGroup.add(DemonAxe(-3330, 250, 450))
  spriteGroup.add(Wizard(-3860, 0, 200))

  spriteGroup.add(DemonFly(-4140, 200, 250))