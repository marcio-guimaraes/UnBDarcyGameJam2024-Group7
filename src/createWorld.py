from .Island import Island
from settings import SCREEN_HEIGHT, SCREEN_WIDTH

def createWorld(spriteGroup):

  midIsland = Island('mid', 100, SCREEN_HEIGHT)
  leftIsland = Island('left', 100, SCREEN_HEIGHT)
  rightIsland = Island('right', 100, SCREEN_HEIGHT)
  numberOfIslands = SCREEN_WIDTH/midIsland.rect.width
  for i in range (int(numberOfIslands)+2):
    for j in range(int(SCREEN_HEIGHT/midIsland.rect.height)):
      type = 'mid' if j == 0 else 'ground'
      island = Island(type, i*midIsland.rect.width, SCREEN_HEIGHT+j*midIsland.rect.height)
      spriteGroup.add(island)

  spriteGroup.add(Island('mid', midIsland.rect.width, SCREEN_HEIGHT-130))
  spriteGroup.add(Island('right', midIsland.rect.width*2, SCREEN_HEIGHT-130))
  spriteGroup.add(Island('mid', 600, SCREEN_HEIGHT -110))
  spriteGroup.add(Island('left', 550, SCREEN_HEIGHT -110))

  island = Island('right', SCREEN_WIDTH-300, SCREEN_HEIGHT-100)

  spriteGroup.add(Island('left', 300, SCREEN_HEIGHT - 250))
  spriteGroup.add(Island('right', 350, SCREEN_HEIGHT -250 ))

  spriteGroup.add(Island('left', 600, SCREEN_HEIGHT - 350))

  #bigisland
  spriteGroup.add(Island('left', 150, SCREEN_HEIGHT - 450))
  spriteGroup.add(Island('mid', 200, SCREEN_HEIGHT - 450))
  spriteGroup.add(Island('mid', 250, SCREEN_HEIGHT - 450))
  spriteGroup.add(Island('right', 300, SCREEN_HEIGHT - 450))

  spriteGroup.add(Island('mid', midIsland.rect.width, SCREEN_HEIGHT -600))
  spriteGroup.add(Island('right', midIsland.rect.width*2, SCREEN_HEIGHT -600))
  
  spriteGroup.add(Island('left', 400, SCREEN_HEIGHT -670))
  spriteGroup.add(Island('mid', 450, SCREEN_HEIGHT -670))
  spriteGroup.add(Island('mid', 500, SCREEN_HEIGHT -670))
  spriteGroup.add(Island('mid', 550, SCREEN_HEIGHT -670))
  spriteGroup.add(Island('mid', 600, SCREEN_HEIGHT -670))