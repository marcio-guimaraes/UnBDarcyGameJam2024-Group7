import pygame
from .Island import Island
from .Killer import Killer
from .Player import Player
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, FPS


class History():
  def __init__(self, screen):
    self.screen = screen
    self.step = 1
    self.subStep = 0
    self.endded = 0

    self.winsound = pygame.mixer.Sound('song/GameWinner.wav')
    self.winsound.set_volume(1.0)

    self.well = pygame.transform.scale(pygame.image.load('assets/history/scene1/Well.png'), (480/3, 480/3))
    self.lantern = pygame.transform.scale(pygame.image.load('assets/history/scene1/Street_Lantern.png'), (480/2.5, 480/2))
    self.barrel = pygame.transform.scale(pygame.image.load('assets/history/scene1/Wooden_Barrel.png'), (128/2.5, 128/2.5))
    self.cart = pygame.transform.scale(pygame.image.load('assets/history/scene1/Cart.png'), (256/2, 256/2))
    self.midIsland = pygame.transform.scale(pygame.image.load('assets/Island/mid.png'), (128/2.5, 128/2.5))
    self.dirt = pygame.transform.scale(pygame.image.load('assets/Island/ground.png'), (128/2.5, 128/2.5))
    self.sky = pygame.transform.scale(pygame.image.load('assets/skyBackground.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))
    self.dialogueBlock = pygame.transform.scale(pygame.image.load('assets/dialogueBlock.svg'), (1214/2, 321/2))
    self.logoGame = pygame.transform.scale(pygame.image.load('assets/logoGame.png'), (400, 390))


    self.playerName = "Alistair"
    

    killerBase = Killer(0, 0)
    playerBase= Player(0,0)
    self.personsGroup = pygame.sprite.Group()
    self.killer = Killer(-100, SCREEN_HEIGHT/1.5-killerBase.rect.height)
    self.player = Player(270, SCREEN_HEIGHT/1.5-playerBase.rect.height, True)
    self.personsGroup.add(self.killer)
    self.personsGroup.add(self.player)
    self.delay = FPS


  def dialogue(self, author, line1, line2=""):
    fonte = pygame.font.SysFont('arial', 20, True, False)

    self.screen.blit(self.dialogueBlock, (0, SCREEN_HEIGHT-200))
    fonte = pygame.font.SysFont('arial', 20, True, False)
    texto_formatado = fonte.render(line1, False, (48, 47, 42))
    self.screen.blit(texto_formatado, (20, SCREEN_HEIGHT-140))
    texto_formatado = fonte.render(line2, False, (48, 47, 42))
    self.screen.blit(texto_formatado, (20, SCREEN_HEIGHT-110))
    texto_formatado = fonte.render(author, False, (233, 233, 233))
    self.screen.blit(texto_formatado, (110, SCREEN_HEIGHT-183))
    

  def scene1(self, events, paused =False):

    midIsland = Island('mid', 0, 0)
    numberOfIslands = SCREEN_WIDTH/midIsland.rect.width
    self.screen.blit(self.sky, (0,0))

    for i in range (int(numberOfIslands)+2):
      for j in range (int(numberOfIslands)+2):
        self.screen.blit(self.midIsland if j == 0 else self.dirt, (i*120/2.5, SCREEN_HEIGHT/1.5+j*120/2.5))

    self.screen.blit(self.well, (SCREEN_WIDTH-200,SCREEN_HEIGHT/1.5-self.well.get_rect().height))
    self.screen.blit(self.lantern, (SCREEN_WIDTH-self.lantern.get_rect().width, SCREEN_HEIGHT/1.5-self.lantern.get_rect().height))
    self.screen.blit(self.barrel, (SCREEN_WIDTH-self.barrel.get_rect().width, SCREEN_HEIGHT/1.5-self.barrel.get_rect().height))
    self.screen.blit(self.cart, (0, SCREEN_HEIGHT/1.5-self.cart.get_rect().height))
    self.screen.blit(self.logoGame, (100, 10))

    if not self.endded:
      self.personsGroup.update()
      self.personsGroup.draw(self.screen)

    if not paused:
      if self.subStep == 0:
        if self.killer.rect.x<200:
          self.killer.currentStatus = "run"
          self.killer.rect.move_ip(3, 0)
        else:
          self.killer.currentStatus = "idle"
          self.subStep += 1
      elif self.subStep == 1:
        self.dialogue("Aegir:", "Finalmente encontrei você… desertor")

        for event in events:
          if event.type == pygame.KEYDOWN:
            self.subStep+=1
      elif self.subStep == 2:
        self.dialogue(self.playerName, "Quem é você?")
        for event in events:
          if event.type == pygame.KEYDOWN:
            self.subStep+=1
      elif self.subStep == 3:
        self.dialogue("Aegir", "Você realmente não se lembra de mim?", "Estive ao seu lado na Batalha de Azincourt.")
        for event in events:
          if event.type == pygame.KEYDOWN:
            self.subStep+=1
      elif self.subStep == 4:
        self.dialogue("Aegir", "Enquanto você fugia com o seu batalhão,", "nós fomos deixados para morrer! Covarde!")
        for event in events:
          if event.type == pygame.KEYDOWN:
            self.subStep+=1
      elif self.subStep == 5:
        self.dialogue(self.playerName, "Aquela batalha estava perdida. Permanecer seria", "uma sentença de morte. Não havia esperança…")
        for event in events:
          if event.type == pygame.KEYDOWN:
            self.subStep+=1
      elif self.subStep == 6:
        self.dialogue("Aegir", "Não havia esperança para você, talvez.", "Para nós, havia honra. Fomos massacrados…")
        for event in events:
          if event.type == pygame.KEYDOWN:
            self.subStep+=1
      elif self.subStep == 7:
        self.dialogue("Aegir", "Eu sobrevivi por um milagre apenas para ser preso.", "Hoje, vim cobrar a dívida que você deixou para trás.")
        for event in events:
          if event.type == pygame.KEYDOWN:
            self.subStep+=1
      elif self.subStep == 8:
        self.dialogue(self.playerName, "Foi há anos… Não pode entender o peso que carrego.", "Tentei viver, mas o passado nunca me deixou em paz.")
        for event in events:
          if event.type == pygame.KEYDOWN:
            self.subStep+=1
      elif self.subStep == 9:
        self.dialogue("Aegir", "Então sabe o que deve fazer. A dívida de um desertor", "só se paga com sangue. A escolha é sua… ")
        for event in events:
          if event.type == pygame.KEYDOWN:
            self.subStep+=1
      elif self.subStep == 10:
        self.dialogue("Aegir", "irá encarar seu fim com ou sem honra?")
        for event in events:
          if event.type == pygame.KEYDOWN:
            self.subStep+=1
      elif self.subStep == 11:
        self.dialogue(self.playerName, "Minha vida foi marcada pela fuga e pelo medo…", "mas não agora. Aceito meu destino.")
        for event in events:
          if event.type == pygame.KEYDOWN:
            self.subStep+=1
      elif self.subStep == 12:
        if self.killer.rect.x<240:
          self.killer.currentStatus = "run"
          self.killer.rect.move_ip(3, 0)
        else:
          self.subStep += 1
          self.killer.currentSpriteIndex = 0
          self.killer.currentStatus = "attack"
      elif self.subStep == 13:
        if int(self.killer.currentSpriteIndex) >= 3:
          self.killer.currentStatus = "idle"
          self.subStep+=1
          self.delay = FPS*2
      elif self.subStep == 14:
        self.screen.fill((0, 0, 0))
        if self.delay < 0:
          self.subStep +=1
        else: self.delay-=1
      elif self.subStep == 15:
        self.screen.fill((0, 0, 0))
        self.dialogue("Guia", "Ah, veja só… seja bem-vindo ao seu destino final.")
        for event in events:
          if event.type == pygame.KEYDOWN:
            self.subStep+=1
      elif self.subStep == 16:
        self.screen.fill((0, 0, 0))
        self.dialogue("Guia", "Ou… será que é só o começo?.")
        for event in events:
          if event.type == pygame.KEYDOWN:
            self.subStep+=1
      elif self.subStep == 17:
        self.screen.fill((0, 0, 0))
        self.dialogue("Guia", "Quem diria… um \"grande cavaleiro\", reduzido a isso.", "Parece que o passado finalmente cobrou o seu preço, não é?")
        for event in events:
          if event.type == pygame.KEYDOWN:
            self.subStep+=1
      elif self.subStep == 18:
        self.screen.fill((0, 0, 0))
        self.dialogue("Guia", "Mas, como você parece alguém determinado a lutar até o ", "último suspiro, vou te dar uma chance.")
        for event in events:
          if event.type == pygame.KEYDOWN:
            self.subStep+=1
      elif self.subStep == 19:
        self.screen.fill((0, 0, 0))
        self.dialogue("Guia", "Dizem que se você escalar o suficiente,", "há uma saída lá em cima…")
        for event in events:
          if event.type == pygame.KEYDOWN:
            self.subStep+=1
      elif self.subStep == 20:
        self.screen.fill((0, 0, 0))
        self.dialogue("Guia", "embora eu não apostasse muito nisso,", "se fosse você")
        for event in events:
          if event.type == pygame.KEYDOWN:
            self.subStep+=1
      elif self.subStep == 21:
        self.screen.fill((0, 0, 0))
        self.dialogue("Guia", "Agora, ouça com atenção. Seu caminho é simples:", "Use as teclas A e D para se mover")
        for event in events:
          if event.type == pygame.KEYDOWN:
            self.subStep+=1
      elif self.subStep == 22:
        self.screen.fill((0, 0, 0)) 
        self.dialogue("Guia", "E espaço para pular")
        for event in events:
          if event.type == pygame.KEYDOWN:
            self.subStep+=1
      elif self.subStep == 23:
        self.screen.fill((0, 0, 0)) 
        self.dialogue("Guia", "Mas neste caminho também terão inimigos,", "então é melhor você se preparar")
        for event in events:
          if event.type == pygame.KEYDOWN:
            self.subStep+=1
      elif self.subStep == 24:
        self.screen.fill((0, 0, 0)) 
        self.dialogue("Guia", "Use sua espada pressionando L", "E seu escudo pressionando K")
        for event in events:
          if event.type == pygame.KEYDOWN:
            self.subStep+=1
      elif self.subStep == 25:
        self.screen.fill((0, 0, 0)) 
        self.dialogue("Guia", "Então, boa sorte… herói. Suba o mais alto que puder." )
        for event in events:
          if event.type == pygame.KEYDOWN:
            self.subStep+=1
      elif self.subStep == 26:
        self.screen.fill((0, 0, 0)) 
        self.dialogue("Guia", "Quem sabe você chegue lá em cima… e encontre a grande", "surpresa que te espera.!" )
        for event in events:
          if event.type == pygame.KEYDOWN:
            self.subStep+=1
      elif self.subStep == 28:
        self.screen.fill((0, 0, 0))
        self.player.rect.move_ip(0, -10)
        if self.delay < 0:
          self.subStep +=1
        else: self.delay-=1
        return False
      elif self.subStep == 29:
        self.dialogue("Guia", "Parabens! Você conquistou a eternidade no paraiso!" )
        self.winsound.play()
        for event in events:
          if event.type == pygame.KEYDOWN:
            self.endded = True
      else: 
        return True
      
      # 
    if not paused: pygame.display.flip()
    return False
      
  def end(self):
    self.delay = 10
    self.subStep = 28

  def update(self, events, paused =False):

    if self.step == 1:
      return self.scene1(events, paused) 