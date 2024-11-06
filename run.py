import pygame

from src.Player import Player
from src.Background import Background
from src.createWorld import createWorld
from src.createEnemies import createEnemies
from settings import *
from src.lifeBar import LifeBar

pygame.init()
pygame.display.set_caption("UnB Darcy Game Jam - Grupo 07")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
hitSound = pygame.mixer.Sound('song/hitSound.wav')

# Carregar o Game Over
game_over_image = pygame.image.load('assets/gameOver.png')
game_over_image = pygame.transform.scale(game_over_image, (400,390))
gameOverSound = pygame.mixer.Sound('song/gameOver1.wav')

# Grupos de sprites
allSprites = pygame.sprite.Group()
floorGroup = pygame.sprite.Group()
enemiesGroup = pygame.sprite.Group()
backgroundGroup = pygame.sprite.Group()
lifebarGroup = pygame.sprite.Group()

# Criando o fundo
baseBackground = Background(0)
for i in range(3):
    backgroundGroup.add(Background(-i * baseBackground.rect.height))

# Adicionando o jogador
player = Player()
allSprites.add(player)

lifebar = LifeBar()
lifebarGroup.add(lifebar)

# Criando o mundo e os inimigos
createWorld(floorGroup)
createEnemies(enemiesGroup)

# Variáveis para controle da mensagem inicial e da música
mostrar_frase = True
inicio_jogo = False
musica_de_fundo_tocando = False
morreu = False  # Variável de controle para detectar a morte do jogador

# Loop principal do jogo
running = True
while running:
    clock.tick(FPS)
    screen.fill((0, 0, 0))

    # Exibe imagem de Game Over se o jogador morreu
    if morreu:
        backgroundGroup.draw(screen)
        screen.blit(game_over_image, (90, 240))
        pygame.display.flip()
        gameOverSound.play()
        
        # Espera até que o jogador pressione uma tecla para sair
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                running = False
        continue

    # Atualiza e desenha os elementos de fundo na tela
    for background in backgroundGroup:
        background.update(player.rect.y, player.ySpeed)

    backgroundGroup.draw(screen)
    allSprites.update()
    allSprites.draw(screen)

    for floor in floorGroup:
        floor.update(player.rect.y, player.ySpeed)
    floorGroup.draw(screen)

    for enemie in enemiesGroup:
        enemie.update(player.rect.y, player.ySpeed, player)
    enemiesGroup.draw(screen)

    pygame.draw.rect(screen, (255, 0, 0), (17, 15.5, 161.5 * player.life / 100, 30))
    lifebarGroup.draw(screen)

    # Exibe a mensagem inicial antes do jogo começar
    if mostrar_frase:
        fonte = pygame.font.SysFont('arial', 40, True, False)
        mensagem = 'press enter'
        texto_formatado = fonte.render(mensagem, False, (255, 255, 255))
        screen.blit(texto_formatado, (210, 390))

    # Verifica colisões do jogador com o chão
    playerCollidesWithFloor = pygame.sprite.spritecollide(player, floorGroup, False)
    leftCollide, rightCollide, bottomCollide, topCollide = False, False, False, False

    for collide in playerCollidesWithFloor:
        playerFoot = player.rect.height + player.rect.y
        playerHead = player.rect.y
        blockBottom = collide.rect.y + collide.rect.height
        playerRight = player.rect.x + player.rect.height
        blockLeft = collide.rect.x + collide.rect.width
        if collide.rect.y - 15 < playerFoot and collide.rect.y + 15 > playerFoot:
            bottomCollide = True
        elif playerHead + 15 > blockBottom and playerHead - 15 < blockBottom:
            topCollide = True
        elif playerRight + 15 > collide.rect.x and playerRight - 15 < collide.rect.x:
            rightCollide = True
        elif blockLeft + 15 > player.rect.x and blockLeft - 15 < player.rect.x:
            leftCollide = True

    player.bottomCollide = bottomCollide
    player.topCollide = topCollide
    player.leftCollide = leftCollide
    player.rightCollide = rightCollide

    # Só processa ações do jogador se o jogo começou (Enter foi pressionado)
    if inicio_jogo:
        # Verifica se o jogador morreu
        if player.currentStatus == 'death':
            morreu = True
            continue  # Pula a atualização do jogo e exibe a tela de Game Over

        # Verifica colisões com inimigos
        playerCollidesWithEnemies = pygame.sprite.spritecollide(player, enemiesGroup, False)
        for enemie in playerCollidesWithEnemies:
            if player.currentStatus == 'attack':
                if player.lastMove > 0:
                    enemie.hit(15, 0)
                else:
                    enemie.hit(15, 1)
            elif enemie.currentStatus == 'attack':
                player.hit(enemie.damage)

        # Movimentos e ataques do jogador
        key = pygame.key.get_pressed()
        if key[pygame.K_a] and player.bottomCollide and not player.currentStatus == 'attack' and not player.currentStatus == 'death':
            player.run(-5)
        elif key[pygame.K_d] and player.bottomCollide and not player.currentStatus == 'attack' and not player.currentStatus == 'death':
            player.run(5)
        elif key[pygame.K_f] and not player.currentStatus == 'attack' and not player.currentStatus == 'death':
            player.attack()
            hitSound.set_volume(1)
            hitSound.play()
        elif player.bottomCollide and not player.currentStatus == 'attack' and not player.currentStatus == 'death':
            player.xSpeed = 0
            player.changeStatus('idle')

        if key[pygame.K_SPACE] and not player.currentStatus == 'death':
            player.jump()

        if key[pygame.K_t]:
            morreu = True

    # Eventos (teclas e fechamento do jogo)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Ao pressionar Enter, a música toca e o jogo começa
                mostrar_frase = False
                inicio_jogo = True
                if not musica_de_fundo_tocando:
                    pygame.mixer.music.set_volume(0)
                    pygame.mixer.music.load('song/Batman (NES) - Game Over Theme.mp3')
                    pygame.mixer.music.play(-1)  # Toca a música em loop
                    musica_de_fundo_tocando = True

    pygame.display.flip()

pygame.quit()
