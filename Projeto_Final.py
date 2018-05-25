'Projeto de Desoft'
#comandos iniciais vbaseados no jogo feito em sala: helloPongSpriteBase
#animações baseadas na fonte:https://stackoverflow.com/questions/14044147/animated-sprite-from-few-images
import pygame
import sys
from pygame.locals import *
import random
import numpy as np
class Boneco(pygame.sprite.Sprite):
    def __init__(self,lista_imagens,posx,posy,tipo):
        pygame.sprite.Sprite.__init__(self)
        
        self.imagens=[]
        for img in lista_imagens:
            self.imagens.append(pygame.image.load(img))
        self.index=0
        self.image=self.imagens[self.index]
        self.rect=pygame.Rect(posx,posy,120,120)
        self.tipo=tipo

    def ativa_boneco(self, imagem):
        self.image=pygame.image.load(imagem)
    
    def move(self, velocidade):
        self.rect.x += velocidade
    
    def update(self):
        self.index+=1
        if self.index>=len(self.imagens):
            self.index=0
        self.image=self.imagens[self.index]

    def altera_boneco(self,lista_imagens):
        self.imagens=[]
        for imagem in lista_imagens:
            self.imagens.append(pygame.image.load(imagem))             

    def vida(self,life):
        self.vida=life
    
    def tira_vida(self,inimigo_grupo,personagem,dano):
        for inimigo in inimigo_grupo and pygame.sprite.spritecollide(personagem,inimigo_grupo, False):
            inimigo.vida-=dano

class Torre(pygame.sprite.Sprite):
    
    def __init__(self,imagem, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        
        self.image=pygame.image.load(imagem)
        self.rect=self.image.get_rect()
        self.rect.x=posx
        self.rect.y=posy
    
    def vida(self,life):
        self.vida=life
        
def acao(grupo_amigo, grupo_inimigo):
     for personagem in grupo_amigo:
        if pygame.sprite.spritecollide(personagem,grupo_inimigo, False):
            punch = pygame.mixer.Sound('smack.wav')
            punch.play()
            if personagem!=torre and personagem!=torre2:
                personagem.move(0)
                if personagem.tipo=='Goku':
                    personagem.altera_boneco(['1.png','3.png'])
                    dano=5
                elif personagem.tipo=='Naruto':
                    personagem.altera_boneco(['naruto_1.png','naruto_2.png','naruto_3.png',\
                                                'naruto_4.png','naruto_5.png','naruto_6.png','naruto_7.png',\
                                                'naruto_8.png'])
                    dano=30
                elif personagem.tipo=='Sasuke':
                    personagem.altera_boneco(['chidori_1.png','chidori_2.png','chidori_3.png','chidori_4.png','chidori_5.png',\
                                            'chidori_6.png','chidori_7.png','chidori_8.png'])
                    dano=10
                personagem.tira_vida(grupo_inimigo,personagem,dano)
            if personagem.vida<=0:
                grupo_amigo.remove(personagem)
        else:
            if personagem!=torre and personagem!=torre2:
                if personagem.tipo=='Goku':
                    personagem.altera_boneco(['1.png','2.png'])
                    personagem.move(7)
                elif personagem.tipo=='Naruto':
                    personagem.altera_boneco(['naruto1.png','naruto2.png','naruto3.png'])
                    personagem.move(3)
                elif personagem.tipo=='Sasuke':
                    personagem.altera_boneco(['sasuke1.png','sasuke2.png','sasuke3.png'])
                    personagem.move(-4)
# classe do botão retirada de: http://www.dreamincode.net/forums/topic/401541-buttons-and-sliders-in-pygame/
cor_fundo = (255, 235, 215)
cor_letra = (0,0,0)
cinza = (200,200,200)
class Botao():

    def __init__(self, txt, location, bg=cor_fundo, fg=cor_letra, size=(100, 50), font_name="Comic sans", font_size=20):
        self.color = bg  # the static (normal) color
        self.bg = bg  # actual background color, can change on mouseover
        self.fg = fg  # text color
        self.size = size
        self.font = pygame.font.SysFont(font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])
        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(center=location)
       

    def draw(self,tela):
       self.surface.fill(self.bg)
       self.surface.blit(self.txt_surf, self.txt_rect)
       tela.blit(self.surface, self.rect)

    def mouseover(self):
        self.bg = self.color
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.bg = cinza  # mouseover color

    def clique(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True
        return False


# início
    
pygame.init()
tela = pygame.display.set_mode((1238,491), 0, 32)
pygame.display.set_caption('Tower defense')
Música_pygame = pygame.mixer.Sound('Musica_pygame.wav')
Música_pygame.play()
tela_intro=pygame.image.load("cenario.jpeg").convert()
start = Botao("Start",(1238/2, 491/2))
tela_tutorial = pygame.image.load("Tuto2.png").convert()
tutorial = Botao("Tutorial",(1238/2, 400))
fonte = myfont = pygame.font.SysFont("monospace", 30)
rodando = True
intro = True
pré_jogo = True
while pré_jogo:
    while intro:
        for event in pygame.event.get():
            if event.type == QUIT:
                intro = False
                pré_jogo=False
                rodando = False
                tuto = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                clicou = start.clique() 
                clicou2 = tutorial.clique()
                if clicou :
                    intro = False
                    pré_jogo = False
                    tuto = False
                elif clicou2 :
                    intro = False
                    tuto = True
        tutorial.mouseover()
        start.mouseover()       
        tela.blit(tela_intro,(0,0))
        start.draw(tela)
        tutorial.draw(tela)
        pygame.display.flip()
    
    while tuto :
        for event in pygame.event.get():
            if event.type == QUIT:
                pré_jogo = False
                rodando = False
                tuto = False
            elif (event.type ==pygame.KEYDOWN):
                if (event.key ==pygame.K_z):
                    tuto = False
                    intro = True
        tela.blit(tela_tutorial,(0,0))
        pygame.display.flip()


fundo= pygame.image.load("cenario.jpeg").convert()

todos_amigos=pygame.sprite.Group()
inimigo_group=pygame.sprite.Group()
torre=Torre("Torre.png", -100,100)
torre.vida(20000)
torre2 = Torre("Torre2.png", 975,105)
torre2.vida(20000  )
inimigo_group.add(torre2)
todos_amigos.add(torre)

#Controle de mana
mana_max=300
limite=800
mana=0
vel_mana=1
contador=0
contador2=0
contador3=0
valor_da_mana=50
wave = 0
while rodando:
    if mana<=mana_max:
        mana+=vel_mana
        if mana>mana_max:
            mana=mana_max
    else:
        mana+=0
    contador+=1
    contador2+=1
    contador3+=1
    relogio=pygame.time.Clock()
    tempo=relogio.tick(40)

    for event in pygame.event.get():
        if event.type == QUIT:
            rodando = False
        if (event.type==pygame.KEYDOWN):
            if (event.key==pygame.K_q):
                if mana>=40:
                    Goku = Boneco(['1.png','2.png'],5,275,'Goku')
                    Goku.vida=600
                    todos_amigos.add(Goku)
                    mana-=40

            elif (event.key==pygame.K_w):
                if mana>=100:
                    Naruto = Boneco(['naruto1.png','naruto2.png','naruto3.png'],5,370,'Naruto')
                    Naruto.vida=2000
                    todos_amigos.add(Naruto)
                    mana-=100

            elif (event.key==pygame.K_m):
                if mana>=valor_da_mana:
                    if mana_max<=limite:
                        mana_max+=100
                        vel_mana+=0.1
                        mana-=valor_da_mana
                        valor_da_mana+=10
    
    acao(inimigo_group,todos_amigos)
    acao(todos_amigos,inimigo_group)

    #Wave 
    x = random.randint(0,100)
    if x > 50 and x < 75:
        if contador2 == 5:
            Sasuke=Boneco(['sasuke1.png','sasuke2.png','sasuke3.png'],1100,300,'Sasuke')
            Sasuke.vida=5000
            inimigo_group.add(Sasuke)
    if contador2 == 15:
        contador2 = 0
        wave += 1
    if wave == 100:
        contador2 = 0
# printar o contador de mana https://stackoverflow.com/questions/19733226/python-pygame-how-to-make-my-score-text-update-itself-forever   
    manatexto = fonte.render("Mana:  {0}/{1}".format(int(mana),mana_max), 7, (250,250,250))
    quadro=pygame.image.load('quadro.jpg')
    tela.blit(fundo, (0,0))
    tela.blit(quadro,(0,0))
    tela.blit(manatexto, (20, 20))
    telinha_goku = pygame.image.load('cara_goku_bloqueada.jpg')
    telinha_naruto = pygame.image.load('Naruto_indisponivel.png')
    tela.blit(telinha_goku,(320,0))
    tela.blit(telinha_naruto,(402,0))
    if mana >= 40:
        telinha_goku = pygame.image.load('cara_goku.jpg')
        tela.blit(telinha_goku,(320,0))
    if mana >= 100:
        telinha_naruto = pygame.image.load('naruto_rosto.jpg')
        tela.blit(telinha_naruto,(402,0))
    
    if contador==2:
        inimigo_group.update()
        contador=0
    inimigo_group.draw(tela)
    if contador3==1:
        todos_amigos.update()
        contador3=0
    todos_amigos.draw(tela)
    
    def fim(torre,imagem):
        if torre.vida<=0:
            fundo= pygame.image.load(imagem).convert()
            inimigo_group=pygame.sprite.Group()
            todos_amigos=pygame.sprite.Group()
            tela.blit(fundo,(0,0))
            pygame.mixer.music.stop()
            if (event.type==pygame.KEYDOWN):
                if event.key==K_ESCAPE:
                    rodando=False
                else:
                    True
    fim(torre,"gameover.jpg")
    fim(torre2,"youwin.jpg")
   
    pygame.display.flip()
pygame.display.quit()
Música_pygame.stop()