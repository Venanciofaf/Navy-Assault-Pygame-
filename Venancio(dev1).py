
import pygame 
import random 
import time
import math


pygame.init() #Inicializa o framework do pygame 
pygame.mixer.init()
#---Gera tela principal 
largura = 650 # Largura da tela 
comprimento = 800 #Comprimento da tela 

window = pygame.display.set_mode((largura , comprimento)) #Inicializa o display da janela, com as suas dimensões 
pygame.display.set_caption('Navy Assault') #Coloca o título da janela 


# ---- Inicia assets (Imagem) 
#tamanho imagem oponente
largura_oponente = 80
comprimento_oponente = 100

#Tamanho imagem jogador
largura_jogador = 80
comprimento_jogador = 100

#Tamanho tiros 
largura_tiro = 35
comrpimento_tiro = 35 

#Tamanho vidas
largura_vida = 50
comprimento_vida = 50

#Tamanho do Boss
largura_boss = 250
comprimento_boss = 300

#Bala do Boss 
largura_bala_boss = 55
comprimento_bala_boss = 55 


#Imagens
assets = {}
assets['imagem_fundo'] = pygame.image.load('Imagens/Fundo.png').convert() #Inicializa a imagem no pygame 
assets['imagem_fundo'] = pygame.transform.scale(assets['imagem_fundo'] , (650,800)) #Converte a imagem para a escala 

assets['imagem_oponente'] = pygame.image.load('Imagens/Barco_inimigo/Barco_inimigo.png').convert_alpha()
assets['imagem_oponente'] = pygame.transform.scale(assets['imagem_oponente'] , (largura_oponente,comprimento_oponente))

assets['imagem_jogador'] = pygame.image.load('Imagens/Barco_jogador/Barco/Barco_amigo.png').convert_alpha()
assets['imagem_jogador'] = pygame.transform.scale(assets['imagem_jogador'] , (largura_jogador,comprimento_jogador))

assets['imagem_tiro'] = pygame.image.load('Imagens/Barco_jogador/Canhões/Canhões_jogador/Segundo_canhã_jogador/Tiro_canhão2.png')
assets['imagem_tiro'] = pygame.transform.scale(assets['imagem_tiro'] , (largura_tiro , comrpimento_tiro) )

assets['imagem_tiro_inimigo'] = pygame.image.load('Imagens/Barco_jogador/Canhões/Canhões_jogador/Quarto_canhão_jogador/Tiro_canhão4.png')
assets['imagem_tiro_inimigo'] = pygame.transform.scale(assets['imagem_tiro_inimigo'] , (largura_tiro , comrpimento_tiro))

assets['imagem_placar'] = pygame.image.load('Imagens/Foto_placar.png')
assets['imagem_placar'] = pygame.transform.scale(assets['imagem_placar'] , (100, 100))

assets['Imagem_vida'] = pygame.transform.scale(assets['imagem_jogador'], (largura_vida, comprimento_vida))

assets['fonte_placar'] = pygame.font.SysFont('cooper black' , 28 , True , False)

assets['imagem_boss']  = pygame.image.load('Imagens/Boss/Boss.png')
assets['imagem_boss'] = pygame.transform.scale(assets['imagem_boss'] , (largura_boss , comprimento_boss))

assets['imagem_bala_boss'] = pygame.image.load('Imagens/Boss/Bala_de_canhão_boss.png')
assets['imagem_bala_boss']  = pygame.transform.scale(assets['imagem_bala_boss'] , (largura_bala_boss , comprimento_bala_boss))

imagem_fundo_bg = assets['imagem_fundo'].get_width()
scroll = 0
tiles = math.ceil(comprimento / imagem_fundo_bg) + 1


anim_tiro_jogador = []

for i in range(3):
    arquivo = f'Imagens/Barco_jogador/Barco/anim_barco_jogador_{i}.png '
    imagem = pygame.image.load(arquivo).convert_alpha()
    imagem = pygame.transform.scale(imagem,(largura_jogador,comprimento_jogador))
    anim_tiro_jogador.append(imagem)

assets['anim_tiro_jogador'] = anim_tiro_jogador

anim_explosion_barco_amigo = []
for i in range(27):
    arquivo2 = f'Imagens/Barco_jogador/Barco/animação-destruição/{i}.png'

    imagem = pygame.image.load(arquivo2).convert_alpha()
    imagem = pygame.transform.scale(imagem,(110,110))
    anim_explosion_barco_amigo.append(imagem)

assets['anim_explosion_barco_amigo'] = anim_explosion_barco_amigo

anim_explod_inimigo = []

for i in range(23):
    arquivo3 = f'Imagens/Barco_inimigo/explod_inimigo/{i}.png'

    imagem = pygame.image.load(arquivo3).convert_alpha()
    imagem = pygame.transform.scale(imagem, (110,110))
    anim_explod_inimigo.append(imagem)

assets['anim_explod_inimigo'] = anim_explod_inimigo

anim_tiro_inimigo2= []

for i in range(3):
    arquivo4 = f'Imagens/Barco_inimigo/tiro_inimigo/{i}.png'

    imagem = pygame.image.load(arquivo4).convert_alpha()
    imagem = pygame.transform.scale(imagem, (80,100))
    anim_tiro_inimigo2.append(imagem)

assets['anim_tiro_inimigo'] = anim_tiro_inimigo2


#Sons 


pygame.mixer.music.load('Sons/Música_fundo.mp3')
pygame.mixer.music.set_volume(0.4)

assets['som do tiro do jogador'] = pygame.mixer.Sound('Sons/tiro_jogador.ogg')
assets['som do tiro do jogador'].set_volume(0.2)

assets['som do tiro do inimigo'] = pygame.mixer.Sound('Sons/tiro_oponente.wav')
assets['som do tiro do inimigo'].set_volume(0.2)

assets['som da explosão do jogador'] = pygame.mixer.Sound('Sons/explosão_barco.wav')
assets['som da explosão do jogador'].set_volume(0.2)

assets['som da explosão do inimigo'] = pygame.mixer.Sound('Sons/Inimigo_explodindo.ogg')
assets['som da explosão do inimigo'].set_volume(0.2)

assets['som do jogador travado'] = pygame.mixer.Sound('Sons/navio_n_atira.wav')
assets['som do jogador travado'].set_volume(0.4)

assets['jogador colidindo'] = pygame.mixer.Sound('Sons/contato_com_navio.wav')
assets['jogador colidindo'].set_volume(0.3)



assets['boss_chegando'] = pygame.mixer.Sound('Sons/som_boss_chegando.flac')
assets['boss_chegando'].set_volume(0.9)

assets['tiro_boss'] = pygame.mixer.Sound('Sons/son_explod_boss.wav')
assets['tiro_boss'].set_volume(0.2)


#Classe do navio inimigo 
class Inimigo(pygame.sprite.Sprite): #Classe dos navios inimigos 
    def __init__(self , assets , groups): #Essa classe baseia-se na entrada de uma imagem 
        pygame.sprite.Sprite.__init__(self) 
        self.image = assets['imagem_oponente']
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(1 , 560)
        self.rect.y = 1
        self.vx_oponente = random.randint(-2 , 2 )
        self.vy_oponente = 3.5
        self.all_sprites = groups['all_sprites']
        self.todos_tiros_inimigo = groups['todos_tiros_inimigo']
        self.imagem_tiro_inimigo = assets['imagem_tiro_inimigo']

    def update(self):
        #Atualizando a posição do navio 
        self.rect.x += self.vx_oponente 
        self.rect.y += self.vy_oponente

        #Condições para reposcionar o inimigo: 
        if self.rect.x > 595:
            self.rect.x = 595
            self.vx_oponente = self.vx_oponente * -1
        if self.rect.x <  -30:
            self.rect.x = -30 
            self.vx_oponente = self.vx_oponente * -1 
        if self.rect.y > comprimento:
            self.rect.y = 1
            self.rect.x = random.randint(0 , 560)

    def tiro_inimigo(self):
        novo_tiro_inimigo = Tiro_inimigo(assets['imagem_tiro_inimigo'] , self.rect.bottom  , self.rect.centerx)
        self.all_sprites.add(novo_tiro_inimigo)
        self.todos_tiros_inimigo.add(novo_tiro_inimigo)


#criando classe pro jogador
class jogador(pygame.sprite.Sprite):
    def __init__(self, assets, groups):
        pygame.sprite.Sprite.__init__(self) 
        self.image = assets['imagem_jogador']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = largura/2
        self.rect.bottom = comprimento - 10
        self.vx_jogador = 0
        self.all_sprites = groups['all_sprites']
        self.todos_tiros = groups['todos_tiros']
        self.imagem_tiro = assets['imagem_tiro']
    
    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.vx_jogador

        # Mantem dentro da tela
        if self.rect.x > 595:
            self.rect.x = 595
        if self.rect.x < -30:
            self.rect.x = -29
            
    def tiro(self):
    # A nova bala vai ser criada logo acima e no centro horizontal da nave
        novo_tiro = Tiro(self.imagem_tiro, self.rect.top, self.rect.centerx)
        self.all_sprites.add(novo_tiro)
        self.todos_tiros.add(novo_tiro)

     

    
class Tiro(pygame.sprite.Sprite):
    # Construtor da classe.

    def __init__(self, img, bottom, centerx):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = centerx
        self.rect.bottom = bottom +20
        self.speedy = -10  # Velocidade fixa para cima

    def update(self):
        # A bala só se move no eixo y
        self.rect.y += self.speedy

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()

class Tiro_inimigo(pygame.sprite.Sprite):
    # Construtor da classe.

    def __init__(self, img, bottom, centerx):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = centerx
        self.rect.bottom = bottom +20
        self.speedy = 5  # Velocidade fixa para cima

    def update(self):
        # A bala só se move no eixo y
        self.rect.y += self.speedy

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()


class Boss(pygame.sprite.Sprite):
    def __init__(self , assets , groups):
        pygame.sprite.Sprite.__init__(self)
        self.image= assets['imagem_boss'] 
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = largura/2
        self.rect.bottom = 200
        self.vx_boss = 2
        self.vy_boss = 1
        self.todos_tiros_boss = groups['todos_tiros_boss']
        self.all_sprites = groups['all_sprites']
        self.imagem_tiro_boss = assets['imagem_bala_boss']

        self.tempo = pygame.time.get_ticks()

        
    def update(self):
        self.rect.x += self.vx_boss
        self.rect.y += self.vy_boss
        
        #Condições para reposcionar o inimigo: 
        if self.rect.x > 450:
            self.rect.x = 449
            self.vx_boss = self.vx_boss * -1
        if self.rect.x <  -30:
            self.rect.x = -30 
            self.vx_boss = self.vx_boss * -1 
        if self.rect.top > 700:
            self.rect.y = 1
            self.rect.x = random.randint(0 , 300)
        if self.rect.bottom == comprimento + 10:
            self.vy_boss = - 10
            self.vx_boss = 0
        if self.rect.top == -40:
            self.vx_boss = 2
            self.vy_boss = 1
    def tiro_boss(self):
        novo_tiro_boss1 = Tiro_boss(assets['imagem_bala_boss'] , self.rect.bottom , self.rect.centerx , 0 , 10 )
        novo_tiro_boss2 = Tiro_boss(assets['imagem_bala_boss'] , self.rect.bottom , self.rect.centerx , 3, 10 )
        novo_tiro_boss3 = Tiro_boss(assets['imagem_bala_boss'] , self.rect.bottom , self.rect.centerx , -3 , 10 )
        self.todos_tiros_boss.add(novo_tiro_boss1)
        self.todos_tiros_boss.add(novo_tiro_boss2)
        self.todos_tiros_boss.add(novo_tiro_boss3)
        self.all_sprites.add(novo_tiro_boss1)
        self.all_sprites.add(novo_tiro_boss2)
        self.all_sprites.add(novo_tiro_boss3)

class Tiro_boss(pygame.sprite.Sprite):
    def __init__(self, img , bottom , centerx , vx_tiro_boss , vy_tiro_boss):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.vy_tiro_boss = vy_tiro_boss
        self.vx_tiro_boss = vx_tiro_boss
    def update(self):
        self.rect.x += self.vx_tiro_boss
        self.rect.y += self.vy_tiro_boss

        if self.rect.left > largura or self.rect.right < 0:
            self.kill()
        if self.rect.bottom > comprimento:
            self.kill()

class canhao_anim(pygame.sprite.Sprite):

    def __init__(self, centrox, velocidadex, assets):
        pygame.sprite.Sprite.__init__(self)

        self.animacao = assets['anim_tiro_jogador']
        self.frame = 0
        self.image = self.animacao[self.frame]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx =  centrox 
        self.rect.centery = comprimento - 10  #Captura a posição do centro do retangulo da imagem no eixo 'y'
        self.speedx = velocidadex #Define a velocidade da animação(para acompanhar o barco após o tiro)
        self.ultima_vez = pygame.time.get_ticks()#Captura o tempo da animação


        self.temporizador = 10 #Tempo necessário para que rode outra animação

    def update(self):#Atualiza a classe
        agora = pygame.time.get_ticks()#Captura o tempo atual 


        tempo_decorrido = agora - self.temporizador#Verifica o tempo decorrido

        if tempo_decorrido > self.temporizador:#condição para que a animação continue a rodar 

            self.ultima_vez = agora #Captura o tempo da ultima animação


            self.frame += 1 #Atualiza a imagem que será usada

        if self.frame == len(assets['anim_tiro_jogador']): #verifica se está na ultima imagem
            self.kill()#finaliza a animação

        else:
            
            centrox = self.rect.centerx + self.speedx #Atualiza a posição da animação 
            self.image = self.animacao[self.frame]#Define nova imagem
            self.rect = self.image.get_rect()#Captura o espaço retangular da imagem
            self.rect.centerx =  centrox #Define a posição do centro da imagem no eixo 'x'
            self.rect.centery = comprimento - 60 # Define a posição do centro da imagem no eixo 'y'

            if self.rect.x > 595:#Verifica se a animação passou do limite positivo da tela
                self.rect.x = 595#Reposiciona a animação
            if self.rect.x < -30:#Verifica se a animação passou do limite negativo da tela 
                self.rect.x = -29#Reposiciona a animação
                

class explo_jogador(pygame.sprite.Sprite):#Represent a explosão do jogador
    
   def __init__(self, centro, assets): #construtor da classe 
        pygame.sprite.Sprite.__init__(self)# Construtor da classe mãe 

        self.explosao = assets['anim_explosion_barco_amigo']#Atributo que armazena as imagens da animação
        self.frame = 0#Numeração da imagem da animação
        self.image = self.explosao[self.frame]#Define a imagem atual da animação
        self.rect = self.image.get_rect()#Captura a área retangular da imagem
        self.rect.center = centro #Define a posição em 'x' e 'y' do centro da imagem
        self.ultima_vez = pygame.time.get_ticks()#Captura o tempo 


        self.temporizador = 2 #Tempo necessário para que rode outra animação

   def update(self):#atualiza a classe 
        agora = pygame.time.get_ticks()#Captura o tempo atual 


        tempo_decorrido = agora - self.temporizador#Verifica o tempo decorrido

        if tempo_decorrido > self.temporizador:#condição para que a animação continue a rodar 

            self.ultima_vez = agora#Captura o tempo da ultima animação


            self.frame += 1 #atualiza a que será usada

        if self.frame == len(self.explosao):#verifica se chegou à ultima imagem
            self.kill()#finaliza a animação

        else:

            centro = self.rect.center#Atualiza a posição da animação 
            self.image = self.explosao[self.frame]#Define nova imagem
            self.rect = self.image.get_rect()#Captura o espaço retangular da imagem
            self.rect.center =  centro#Define a posição em 'x' e 'y' do centro da imagem

class explod_inimigo(pygame.sprite.Sprite):#Representa a animação de explosão do inimigo
   
   def __init__(self, centro, assets):#Construtor da classe
        
        pygame.sprite.Sprite.__init__(self)#Construtor da classe mãe 

        self.explosao = assets['anim_explod_inimigo']#atributo que armazena as imagens da animação
        self.frame = 0#numeração da imagem da animação
        self.image = self.explosao[self.frame]#Define a imagem atual da animação
        self.rect = self.image.get_rect()#Captura a área retangular da imagem
        self.rect.center = centro#Define a posição em 'x' e 'y' do centro da imagem
        self.ultima_vez = pygame.time.get_ticks()#Captura o tempo 


        self.temporizador = 22 #Tempo necessário para que rode outra animação

   def update(self):#atualiza a classe 
        agora = pygame.time.get_ticks()#Captura o tempo atual 


        tempo_decorrido = agora - self.temporizador#Verifica o tempo decorrido

        if tempo_decorrido > self.temporizador:#condição para que a animação continue a rodar 

            self.ultima_vez = agora#Captura o tempo da ultima animação


            self.frame += 1#atualiza a que será usada

        if self.frame == len(self.explosao):#verifica se chegou à ultima imagem
            self.kill()#finaliza a animação

        else:

            centro = self.rect.center#Atualiza a posição da animação 
            self.image = self.explosao[self.frame]#Define nova imagem
            self.rect = self.image.get_rect()#Captura o espaço retangular da imagem
            self.rect.center =  centro#Define a posição em 'x' e 'y' do centro da imagem



class canhao_inimigo_anim(pygame.sprite.Sprite):
    
    def __init__(self, centerx, centery, velocidadex, velocidadey, assets):    
        pygame.sprite.Sprite.__init__(self)

        self.tiro = assets['anim_tiro_inimigo']
        self.frame = 0
        self.image = self.tiro[self.frame]
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.ultima_vez = pygame.time.get_ticks()
        self.speedx = velocidadex
        self.speedy = velocidadey

        self.temporizador = 2

    def update(self):
        agora = pygame.time.get_ticks()#Captura o tempo atual 


        tempo_decorrido = agora - self.temporizador#Verifica o tempo decorrido

        if tempo_decorrido > self.temporizador:#condição para que a animação continue a rodar 

            self.ultima_vez = agora#Captura o tempo da ultima animação


            self.frame += 1 #atualiza a que será usada

        if self.frame == len(self.tiro):#verifica se chegou à ultima imagem
            self.kill()#finaliza a animação

        else:

            centrox = self.rect.centerx + self.speedx#Atualiza a posição da animação 
            centroy = self.rect.centery + self.speedy
            self.image = self.tiro[self.frame]#Define nova imagem
            self.rect = self.image.get_rect()#Captura o espaço retangular da imagem
            self.rect.centerx =  centrox#Define a posição em 'x' e 'y' do centro da imagem
            self.rect.centery = centroy

            if self.rect.x > 595:#Verifica se a animação passou do limite positivo da tela
                self.rect.x = 595#Reposiciona a animação
            if self.rect.x < -30:#Verifica se a animação passou do limite negativo da tela 
                self.rect.x = -29#Reposiciona a animação
            


            



#quantidade de vidas do jogador
vidas = 3
vidas_boss = 75
vidas_ganhas = []#Armazena quais pontuações já cederam vida ao jogador 
#placar
placar = 0 
#criando navios: 

all_sprites = pygame.sprite.Group() #Uma lista que armazena todos os sprites do jogo 

todos_tiros = pygame.sprite.Group() #Lista que armazena somente os tiros do jogador 
todos_amigo = pygame.sprite.Group()
todos_tiros_inimigo = pygame.sprite.Group()#lista que armazena todos os tiros dos inimigos 
todos_tiros_boss = pygame.sprite.Group()
n_inimigos = 4 #variável que armazena a quantidade de inimigos 
todos_boss = pygame.sprite.Group()
todos_inimigos = pygame.sprite.Group()#lista que armazena todos os inimigos

groups = {}
groups['all_sprites'] = all_sprites
groups['todos_tiros'] = todos_tiros
groups['todos_tiros_inimigo'] = todos_tiros_inimigo
groups['todos_inimigos'] = todos_inimigos
groups['todos_tiros_boss'] = todos_tiros_boss
for i in range(n_inimigos):#loop para armazenar todos os inimigos dentro do grupo

    navio = Inimigo(assets , groups)#Gerador do barco inimigo 
    all_sprites.add(navio)#adiciona o navio à lista de sprites 
    todos_inimigos.add(navio)#adiciona o navio a lista de inimigos 

navio_amigo = jogador(assets, groups)#gerador do navio do jogador 
all_sprites.add(navio_amigo)#adiciona o navio à lista de sprites 
navio_boss = Boss( assets , groups )
todos_boss.add(navio_boss)
todos_amigo.add(navio_amigo)
#Relógio que controla o loop
clock = pygame.time.Clock()

FPS = 50  #quantidade de imagens que são mostradas na tela por segundo 
tempo_inimigo = 0 #tempo em que o inimigo ira atirar 

#Estados do próprio jogador  
acabou = 0 
perdeu_vidas = 1
regenerando = 2 
playing = 3 
state = playing

#Estados do estágio do jogo 
fase_1 = 10
fase_final = 20 
status_fase = fase_1
#----Loop principal do jogo ---
pygame.mixer.music.play(loops=-1)
while state != acabou: 
    clock.tick(FPS) 
    tempo_fase1 = pygame.time.get_ticks()
    tempo_inimigo += 1 #adiciona tempo ao ocntador 
    if tempo_inimigo == 50:#verifica se já passou  o tempo necessário para o inimigo atirar 
        for i in todos_inimigos: #loop para acessar todos os inimigos dentro da lista
            i.tiro_inimigo()#faz o inimigo atirar 
            assets['som do tiro do inimigo'].play()#roda o som do tiro 
            anim_tiro2 = canhao_inimigo_anim(i.rect.centerx, i.rect.centery, i.vx_oponente,i.vy_oponente,  assets)
            all_sprites.add(anim_tiro2)
        tempo_inimigo = 0 #reinicia o contador de tempo após atirar 
    
    # ----- Trata eventos
    for event in pygame.event.get(): #pygame.evente.get devolve uma lista com todos os eventos que ocorreram desde a última janela 
        # ----- Verifica consequências
        if event.type == pygame.QUIT: #Se o comando do evento for igual a pygame.quit, o loop acaba 
            state = acabou #finaliza o jogo 
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:#verifica a telca apertada 
                navio_amigo.vx_jogador -= 8#Faz o jogador se movimenta para a esquerda 
            if event.key == pygame.K_RIGHT:#verifica a tecla apertada 
                navio_amigo.vx_jogador += 8#faz o jogador se movimentar para a direita 
            if event.key == pygame.K_SPACE:#verifica a tecla apertada 
                if state == playing:
                    navio_amigo.tiro()#Faz o navio do jogador atirar 
                    assets['som do tiro do jogador'].play()#roda o som do tiro do jogador 
                    tiro = canhao_anim(navio_amigo.rect.centerx,navio_amigo.vx_jogador, assets)#realiza a animação de tiro do jogador 
                    all_sprites.add(tiro)#Adiciona a animação no grupo de sprites 
                if state == regenerando:
                    assets['som do jogador travado'].play()   
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:#verifica tecla apertada 
                navio_amigo.vx_jogador += 8#Faz o jogador parar após soltar a tecla 
            if event.key == pygame.K_RIGHT:#verifica tecla apertada 
                navio_amigo.vx_jogador -= 8#faz o jogador parar após soltar a telca 

    all_sprites.update()#atualiza todos os eventos dos sprites dentro dos grupos 
    
    if state == playing and status_fase == fase_1: 
        if pygame.sprite.spritecollide(navio_amigo, todos_inimigos, True, pygame.sprite.collide_mask):#verifica se houve colizão entre o jogador e algum inimigo
            novo_inimigo = Inimigo(assets , groups)  #cria inimigo novamente 
            all_sprites.add(novo_inimigo)  #Adiciona sprite do inimigo no grupo de todos os sprites 
            todos_inimigos.add(novo_inimigo)  #Adiciona sprite do inimigo no grupo de sprites dos inimigos 
            vidas -= 1   #Diminui a quantidade de vida do jogador 
            assets['jogador colidindo'].play()
            placar -= 1000   #Reduz a pontuação do jogador 
            assets['som da explosão do inimigo'].play() #Roda o som da explosão do inimigo
            if vidas > 0: 
                state = regenerando
                tomou_tiro = pygame.time.get_ticks()
            else:
                state = perdeu_vidas
                morreu = pygame.time.get_ticks()
        hit_navio = pygame.sprite.groupcollide(groups['todos_inimigos'], groups['todos_tiros'], True, True, pygame.sprite.collide_mask)#Armazena todos os inimigos que foram acertados por tiros 
        for navio in hit_navio:   #Acessa os inimigos 1 por 1 
            assets['som da explosão do inimigo'].play()   #roda o som de explosão do inimigo 
            novo_inimigo = Inimigo(assets , groups)   #cria inimigo novamente 
            all_sprites.add(novo_inimigo)   #Adiciona sprite do inimigo no grupo de todos os sprites 
            todos_inimigos.add(novo_inimigo)  #Adiciona sprite do inimigo no grupo de sprites dos inimigos 
            morte_inimigo = explod_inimigo(navio.rect.center, assets)   #roda animação de explosão do inimigo
            all_sprites.add(morte_inimigo)  #Adiciona animação de explosão do inimigo no grupo de todos os sprites 
            placar += 100   #adiciona os pontos do jogador 
            if placar % 500 == 0 and placar > 0:  #verifica se o jogador ganhou 500 pontos
                if placar / 500 not in vidas_ganhas:  #verifica se é a primeira vez que o jogador chegou nessa quantidade de pontos 
                    vidas += 1   #adiciona vidas ao jogador 
                    vidas_ganhas.append(placar / 500)  #acrescenta à lista de vidas ganhas essa quantidade de pontos 
        
        if pygame.sprite.spritecollide(navio_amigo, groups['todos_tiros_inimigo'], True, pygame.sprite.collide_mask):#Verifica colisão do jogdor com os tiros inimigos
            vidas -= 1     #Reduz a quantidade de vidas 
            placar -= 500 #Reduz a quantidade de pontos
            assets['jogador colidindo'].play()  
            if vidas > 0: 
                state = regenerando
                tomou_tiro = pygame.time.get_ticks()
            else:
                state = perdeu_vidas
                morreu = pygame.time.get_ticks()
    elif state == regenerando:
            now = pygame.time.get_ticks()
            if now - tomou_tiro > 3000:
                state = playing
                now = 0 
    
    
    elif state == perdeu_vidas:
        morte_jogador = explo_jogador(navio_amigo.rect.center, assets)#roda animação de explosão do navio do jogador 
        all_sprites.add(morte_jogador)#adiciona a animação no grupo de todas as sprites 
        navio_amigo.kill()#Remove o navio do grupo de sprites 
        assets['som da explosão do jogador'].play()#Roda o som de explosão do navio do jogador
        tempo_morte =  pygame.time.get_ticks()
        if tempo_morte - morreu > 1500:
            state = acabou

    
    if tempo_fase1 - (1000 * 1) > 0 and status_fase == fase_1:
        status_fase = fase_final
        assets['boss_chegando'].play()
        for tiro_inimigo2 in todos_tiros_inimigo:
            tiro_inimigo2.kill()
        for navio_inimigo_morrer in todos_inimigos:
                navio_inimigo_morrer.kill() 
        all_sprites.add(navio_boss)       
        navio_boss.tiro_boss()
        contagem_tiro_boss = 0
    
    if status_fase == fase_final:
        contagem_tiro_boss += 1
        if contagem_tiro_boss % 75 == 0:
            navio_boss.tiro_boss()
            assets['tiro_boss'].play()
        if state == playing:
            hits3 =  pygame.sprite.spritecollide(navio_amigo , todos_boss , False , pygame.sprite.collide_mask)
            if len(hits3) > 0:
                vidas -= 1 
                if vidas > 0:
                    state = regenerando
                    tomou_tiro = pygame.time.get_ticks()
                if vidas == 0:
                    state = perdeu_vidas
                    morreu = pygame.time.get_ticks()
            
            hits4 = pygame.sprite.groupcollide(todos_boss , groups['todos_tiros'] , False, True, pygame.sprite.collide_mask)
            if len(hits4) > 0:
                for chave, valor in hits4.items():
                    vidas_boss -= 1 
                    if vidas_boss == 0:
                        chave.kill()
                    for termo in valor: 
                        termo.kill()
            hits5 = pygame.sprite.groupcollide(todos_amigo , groups['todos_tiros_boss'] , False , True , pygame.sprite.collide_mask)
            if len(hits5) > 0:
                for key, value in hits5.items():
                    vidas -= 1 
                    if vidas > 0:
                        state = regenerando
                        tomou_tiro = pygame.time.get_ticks()
                    else:
                        state = perdeu_vidas
                        morreu = pygame.time.get_ticks()
            
       
    #Gera saídas 
    window.fill( (0 , 0 , 0)) 
    window.blit(assets['imagem_fundo'] , (0,0))   #Posiciona a imagem de fundo na janela window, na posição 0,0
    if status_fase == fase_1:
        window.blit(assets['imagem_placar'] , (550 , 5))  #desenha a imagem do placar na janela do jogo 
    all_sprites.draw(window)#Desenha as imagens de todos os sprites na janela do jogo 

    #Colocando placar
    if status_fase == fase_1:
        superficie_placar = assets['fonte_placar'].render("{0}".format(placar) , True , (255 , 255 , 255))#guarda a imagem da quantidade de pontos que será mostrada 
        window.blit(superficie_placar , (560 , 40))#desenha a quantidade de pontos na janela 
    #Colocando vidas
    x_vida = 25  #posição inicial da imagem de vidas no eixo 'x' 
    y_vida = 10  #posição inicial da imagem de vidas no eixo 'y'
    for i in range(vidas):#loop para gerar imagens das vidas 
        window.blit(assets['Imagem_vida'], (x_vida, y_vida))#desenha a imagem da vida na tela 
        x_vida += 25#move a posição da imagem no eixo 'x'
      
    #Autaliza estado do jogo 
    pygame.display.update() #Atualiza o estado do jogo observado a cada loop
#--- Finalização 
pygame.quit() #Finaliza o game     