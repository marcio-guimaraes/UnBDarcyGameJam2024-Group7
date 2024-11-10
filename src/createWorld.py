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
  spriteGroup.add(Island('mid', midIsland.rect.width*2, SCREEN_HEIGHT-130))
  spriteGroup.add(Island('mid', midIsland.rect.width*3, SCREEN_HEIGHT-130))
  spriteGroup.add(Island('right', midIsland.rect.width*4, SCREEN_HEIGHT-130))
  
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

  spriteGroup.add(Island('mid', 600, SCREEN_HEIGHT - 810))
  spriteGroup.add(Island('left', 550, SCREEN_HEIGHT -810))

  spriteGroup.add(Island('left', 200, SCREEN_HEIGHT -900))
  spriteGroup.add(Island('mid', 250, SCREEN_HEIGHT -900))
  spriteGroup.add(Island('right', 300, SCREEN_HEIGHT -900))

  spriteGroup.add(Island('mid', midIsland.rect.width, SCREEN_HEIGHT -1050))
  spriteGroup.add(Island('right', midIsland.rect.width*2, SCREEN_HEIGHT -1050))

  spriteGroup.add(Island('left', 350, SCREEN_HEIGHT -1150))
  spriteGroup.add(Island('mid', 400, SCREEN_HEIGHT -1150))
  spriteGroup.add(Island('mid', 450, SCREEN_HEIGHT -1150))
  spriteGroup.add(Island('right', 500, SCREEN_HEIGHT -1150))

  spriteGroup.add(Island('left', 200, SCREEN_HEIGHT -1320))
  spriteGroup.add(Island('mid', 250, SCREEN_HEIGHT -1320))
  spriteGroup.add(Island('right', 300, SCREEN_HEIGHT -1320))

  spriteGroup.add(Island('left', 400, SCREEN_HEIGHT -1450))
  spriteGroup.add(Island('mid', 450, SCREEN_HEIGHT -1450))
  spriteGroup.add(Island('mid', 500, SCREEN_HEIGHT -1450))
  spriteGroup.add(Island('mid', 550, SCREEN_HEIGHT -1450))
  spriteGroup.add(Island('mid', 600, SCREEN_HEIGHT -1450))

  spriteGroup.add(Island('left', 250, SCREEN_HEIGHT -1600 ))
  spriteGroup.add(Island('right', 300, SCREEN_HEIGHT -1600 ))

  spriteGroup.add(Island('mid', midIsland.rect.width, SCREEN_HEIGHT -1750 ))
  spriteGroup.add(Island('mid', midIsland.rect.width*2, SCREEN_HEIGHT -1750 ))
  spriteGroup.add(Island('right', midIsland.rect.width*3, SCREEN_HEIGHT -1750 ))

  
  spriteGroup.add(Island('right', midIsland.rect.width, SCREEN_HEIGHT -1870 ))
  
  spriteGroup.add(Island('left', 250, SCREEN_HEIGHT -1950 ))
  spriteGroup.add(Island('mid', 300, SCREEN_HEIGHT -1950 ))
  spriteGroup.add(Island('mid', 350, SCREEN_HEIGHT -1950 ))
  spriteGroup.add(Island('right', 400, SCREEN_HEIGHT -1950 ))

  spriteGroup.add(Island('left', 500, SCREEN_HEIGHT - 2080))
  spriteGroup.add(Island('right', 550, SCREEN_HEIGHT - 2080))

  spriteGroup.add(Island('left', 200, SCREEN_HEIGHT - 2200))
  spriteGroup.add(Island('mid', 250, SCREEN_HEIGHT - 2200))
  spriteGroup.add(Island('right', 300, SCREEN_HEIGHT - 2200))
  


  spriteGroup.add(Island('midGrass', midIsland.rect.width, SCREEN_HEIGHT - 2350))
  spriteGroup.add(Island('midGrass', midIsland.rect.width*2, SCREEN_HEIGHT - 2350))
  spriteGroup.add(Island('rightGrass', midIsland.rect.width*3, SCREEN_HEIGHT - 2350))
  spriteGroup.add(Island('midGrass', 600, SCREEN_HEIGHT - 2350))
  spriteGroup.add(Island('midGrass', 550, SCREEN_HEIGHT - 2350))
  spriteGroup.add(Island('leftGrass', 500, SCREEN_HEIGHT - 2350))


  #starsky

  spriteGroup.add(Island('leftGrass', 250, SCREEN_HEIGHT -2500))
  spriteGroup.add(Island('midGrass', 300, SCREEN_HEIGHT - 2500))
  spriteGroup.add(Island('rightGrass', 350, SCREEN_HEIGHT  -2500))

  spriteGroup.add(Island('leftGrass', midIsland.rect.width, SCREEN_HEIGHT - 2650))
  spriteGroup.add(Island('rightGrass', midIsland.rect.width*2, SCREEN_HEIGHT - 2650))

  spriteGroup.add(Island('leftGrass', 550, SCREEN_HEIGHT - 2650))
  spriteGroup.add(Island('rightGrass', 600, SCREEN_HEIGHT - 2650))

  spriteGroup.add(Island('leftGrass', 200, SCREEN_HEIGHT - 2800 ))
  spriteGroup.add(Island('midGrass', 250, SCREEN_HEIGHT - 2800 ))
  spriteGroup.add(Island('midGrass', 300, SCREEN_HEIGHT - 2800 ))
  spriteGroup.add(Island('midGrass', 350, SCREEN_HEIGHT - 2800 ))
  spriteGroup.add(Island('midGrass', 400, SCREEN_HEIGHT - 2800 ))
  spriteGroup.add(Island('rightGrass', 450, SCREEN_HEIGHT - 2800 ))

  spriteGroup.add(Island('midGrass', 600, SCREEN_HEIGHT-2950))
  spriteGroup.add(Island('leftGrass', 550, SCREEN_HEIGHT-2950))

  spriteGroup.add(Island('leftGrass', 50, SCREEN_HEIGHT - 2970))
  spriteGroup.add(Island('midGrass', 100, SCREEN_HEIGHT - 2970))
  spriteGroup.add(Island('rightGrass', 150, SCREEN_HEIGHT - 2970))

  spriteGroup.add(Island('leftGrass', 300, SCREEN_HEIGHT-3100 ))
  spriteGroup.add(Island('rightGrass', 350, SCREEN_HEIGHT-3100 ))
  
  spriteGroup.add(Island('rightGrass', 550,SCREEN_HEIGHT-3250 ))
  spriteGroup.add(Island('midGrass', 500,SCREEN_HEIGHT-3250 ))
  spriteGroup.add(Island('leftGrass', 450,SCREEN_HEIGHT-3250 ))

  spriteGroup.add(Island('leftGrass', 100, SCREEN_HEIGHT - 3420))
  spriteGroup.add(Island('midGrass', 150, SCREEN_HEIGHT - 3420))
  spriteGroup.add(Island('midGrass', 200, SCREEN_HEIGHT - 3420 ))
  spriteGroup.add(Island('midGrass', 250, SCREEN_HEIGHT - 3420 ))
  spriteGroup.add(Island('midGrass', 300, SCREEN_HEIGHT - 3420 ))
  spriteGroup.add(Island('rightGrass', 350, SCREEN_HEIGHT - 3420))

  spriteGroup.add(Island('leftGrass', 500, SCREEN_HEIGHT - 3570))
  spriteGroup.add(Island('rightGrass', 550, SCREEN_HEIGHT - 3570))

  spriteGroup.add(Island('leftGrass', 250, SCREEN_HEIGHT - 3720))
  spriteGroup.add(Island('midGrass', 300, SCREEN_HEIGHT - 3720))
  spriteGroup.add(Island('rightGrass', 350, SCREEN_HEIGHT - 3720))

  spriteGroup.add(Island('rightGrass', midIsland.rect.width, SCREEN_HEIGHT - 3840))

  spriteGroup.add(Island('leftGrass', 300, SCREEN_HEIGHT - 3990))
  spriteGroup.add(Island('midGrass', 350, SCREEN_HEIGHT - 3990))
  spriteGroup.add(Island('midGrass', 400, SCREEN_HEIGHT - 3990 ))
  spriteGroup.add(Island('midGrass', 450, SCREEN_HEIGHT - 3990 ))
  spriteGroup.add(Island('midGrass', 500, SCREEN_HEIGHT - 3990 ))
  spriteGroup.add(Island('rightGrass', 550, SCREEN_HEIGHT - 3990))

  spriteGroup.add(Island('midGrass', 600, SCREEN_HEIGHT - 4090))
  spriteGroup.add(Island('leftGrass', 550, SCREEN_HEIGHT - 4090))

  spriteGroup.add(Island('leftGrass', 250, SCREEN_HEIGHT - 4240))
  spriteGroup.add(Island('midGrass', 300, SCREEN_HEIGHT - 4240))
  spriteGroup.add(Island('rightGrass', 350, SCREEN_HEIGHT - 4240))

  spriteGroup.add(Island('midGrass', 600, SCREEN_HEIGHT - 4390))
  spriteGroup.add(Island('midGrass', 550, SCREEN_HEIGHT - 4390))
  spriteGroup.add(Island('leftGrass', 500, SCREEN_HEIGHT - 4390))

  spriteGroup.add(Island('leftGrass', 50, SCREEN_HEIGHT - 4520))
  spriteGroup.add(Island('midGrass', 100, SCREEN_HEIGHT - 4520))
  spriteGroup.add(Island('midGrass', 150, SCREEN_HEIGHT - 4520))
  spriteGroup.add(Island('midGrass', 200, SCREEN_HEIGHT - 4520))
  spriteGroup.add(Island('rightGrass', 250, SCREEN_HEIGHT - 4520))

  spriteGroup.add(Island('leftGrass', 450, SCREEN_HEIGHT - 4670))
  spriteGroup.add(Island('midGrass', 500, SCREEN_HEIGHT - 4670))
  spriteGroup.add(Island('midGrass', 550, SCREEN_HEIGHT - 4670))
  spriteGroup.add(Island('midGrass', 600, SCREEN_HEIGHT - 4670))

  spriteGroup.add(Island('leftGrass', 250, SCREEN_HEIGHT - 4820))
  spriteGroup.add(Island('midGrass', 300, SCREEN_HEIGHT - 4820))
  spriteGroup.add(Island('rightGrass', 350, SCREEN_HEIGHT - 4820))

  spriteGroup.add(Island('midGrass', midIsland.rect.width, SCREEN_HEIGHT - 4970))
  spriteGroup.add(Island('midGrass', midIsland.rect.width*2, SCREEN_HEIGHT - 4970))
  spriteGroup.add(Island('rightGrass', midIsland.rect.width*3, SCREEN_HEIGHT - 4970))
  spriteGroup.add(Island('midGrass', 600, SCREEN_HEIGHT - 4970))
  spriteGroup.add(Island('midGrass', 550, SCREEN_HEIGHT - 4970))
  spriteGroup.add(Island('leftGrass', 500, SCREEN_HEIGHT - 4970))