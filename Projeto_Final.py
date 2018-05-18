'Projeto de Desoft'
#comandos iniciais vbaseados no jogo feito em sala: helloPongSpriteBase
#animações baseadas na fonte:https://stackoverflow.com/questions/14044147/animated-sprite-from-few-images
import pygame
import sys
from pygame.locals import *
import random
import numpy as np
class Boneco(pygame.sprite.Sprite):
    def __init__(self,lista_imagens,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        
        self.imagens=[]
        for img in lista_imagens:
            self.imagens.append(pygame.image.load(img))
        self.index=0
        self.image=self.imagens[self.index]
        self.rect=pygame.Rect(posx,posy,120,120)

    def ativa_boneco(self, imagem):
        self.image=pygame.image.load(imagem)
    
    def move(self, velocidade):
        self.rect.x += velocidade
    
    def update(self):
        self.index+=1
        if self.index>=len(self.imagens):
            self.index=0
        self.image=self.imagens[self.index]
                    

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
        
def acao(grupo_amigo, grupo_inimigo,move1,move2,dano):
     for personagem in grupo_amigo:
        if pygame.sprite.spritecollide(personagem,grupo_inimigo, False):
            if personagem!=torre and personagem!=torre2:
                personagem.move(move1)
            try:
                if personagem==Goku:
                    personagem.ativa_boneco('3.png')
                elif personagem==Naruto:
                    personagem.ativa_boneco('naruto_parado.png')
                elif personagem==Sasuke:
                    personagem.ativa_boneco('sasuke_parado.png')
            except NameError:
                True
            if personagem!=torre and personagem!=torre2:
                personagem.tira_vida(grupo_inimigo,personagem,dano)
            if personagem.vida<=0:
                grupo_amigo.remove(personagem)
        else:
            if personagem!=torre and personagem!=torre2:
                personagem.move(move2)
# classe do botão retirada de: http://www.dreamincode.net/forums/topic/401541-buttons-and-sliders-in-pygame/
cor_fundo = (255, 235, 215)
cor_letra = (0,0,0)
cinza = (200,200,200)
class Botao():

   def __init__(self, txt, location, bg=cor_fundo, fg=cor_letra, size=(50, 50), font_name="Comic sans", font_size=20):
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
pygame.mixer.music.load('Música_pygame.mp3')
pygame.mixer.music.play()
tela_intro=pygame.image.load("cenario.jpeg").convert()
start = Botao("Start",(1238/2, 491/2))

intro = True
while intro:
    for event in pygame.event.get():
        if event.type == QUIT:
            intro = False
            rodando = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            clicou = start.clique() 
            if clicou:
                intro = False
    start.mouseover()       
    tela.blit(tela_intro,(0,0))
    start.draw(tela)
    pygame.display.flip()

fundo= pygame.image.load("cenario.jpeg").convert()

todos_amigos=pygame.sprite.Group()
inimigo_group=pygame.sprite.Group()
torre=Torre("Torre.png", -100,100)
torre.vida(200)
torre2 = Torre("Torre2.png", 795,50)
torre2.vida(2000)
inimigo_group.add(torre2)
todos_amigos.add(torre)

rodando = True
mana_max=300
mana=0
contador=0
contador2=0
wave = 0
while rodando:
    if mana<=mana_max:
        mana+=1
    else:
        mana+=0
    contador+=1
    contador2+=1
    relogio=pygame.time.Clock()
    tempo=relogio.tick(40)

    for event in pygame.event.get():
        if event.type == QUIT:
            rodando = False
        if (event.type==pygame.KEYDOWN):
            if (event.key==pygame.K_q):
                if mana>=50:
                    Goku = Boneco(['1.png','2.png'],5,275)
                    Goku.ativa_boneco('1.png')
                    Goku.vida=100
                    todos_amigos.add(Goku)
                    mana-=50
            elif (event.key==pygame.K_w):
                if mana>=30:
                    Naruto = Boneco(['naruto1.png','naruto2.png','naruto3.png'],5,370)
                    Naruto.ativa_boneco('naruto1.png')
                    Naruto.vida=100
                    todos_amigos.add(Naruto)
                    mana-=30

            elif (event.key==pygame.K_m):
                if mana>=50:
                    maximo+=100
    
    acao(inimigo_group,todos_amigos,0,-4,5)
    acao(todos_amigos,inimigo_group,0,5,5)
    x = random.randint(0,100)
    if x > 50 and x < 75:
        if contador2 == 5:
            Sasuke=Boneco(['sasuke1.png','sasuke2.png','sasuke3.png'],1100,300)
            Sasuke.ativa_boneco('sasuke1.png')
            Sasuke.vida=200
            inimigo_group.add(Sasuke)
    if contador2 == 15:
        contador2 = 0
        wave += 1
    if wave == 10:
        contador2 = 0

    tela.blit(fundo, (0,0))
    if contador==5:
        todos_amigos.update()
        inimigo_group.update()
        contador=0
    inimigo_group.draw(tela)
    todos_amigos.draw(tela)
    pygame.display.flip()
    if torre.vida<=0:
        fundo= pygame.image.load("gameover.jpg").convert()
        inimigo_group=pygame.sprite.Group()
        todos_amigos=pygame.sprite.Group()
        pygame.display.update()
        pygame.mixer.music.stop()
        if (event.type==pygame.KEYDOWN):
            if event.key==K_ESCAPE:
                rodando=False
            elif event.key==K_BACKSPACE:
                intro=True
            else:
                True
pygame.display.quit()