'Projeto de Desoft'
#comandos iniciais vbaseados no jogo feito em sala: helloPongSpriteBase
#animações baseadas na fonte:https://stackoverflow.com/questions/14044147/animated-sprite-from-few-images
import pygame
import sys
from pygame.locals import *

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
    
class Torre(pygame.sprite.Sprite):
    
    def __init__(self,imagem, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        
        self.image=pygame.image.load(imagem)
        self.rect=self.image.get_rect()
        self.rect.x=posx
        self.rect.y=posy
    
    def Vida_torre(self,dano):
        vida = 10000
        vida -= dano
        
        return vida
def acao(grupo_amigo, grupo_inimigo,move1,move2,imagem,dano):
    for personagem in grupo_amigo:
        if pygame.sprite.spritecollide(personagem,grupo_inimigo, False):
            personagem.move(move1)
            personagem.ativa_boneco(imagem)
            if personagem.vida<=0:
                grupo_amigo.remove(personagem)
        else:
            personagem.move(move2)
    for inimigo in grupo_inimigo:
        if contador==2:
            inimigo.vida-=dano    
# início
    
pygame.init()
tela = pygame.display.set_mode((1238,491), 0, 32)
pygame.display.set_caption('Tower defense')
pygame.mixer.music.load('Música_pygame.mp3')
pygame.mixer.music.play()


fundo= pygame.image.load("cenario.jpeg").convert()

Goku_group = pygame.sprite.Group()
Naruto_group=pygame.sprite.Group()
inimigo_group=pygame.sprite.Group()
torre=Torre("Torre.png", -100,100)
torre_group=pygame.sprite.Group()
torre_group.add(torre)

rodando = True
contador=0
while rodando:
    contador+=1
    relogio=pygame.time.Clock()
    tempo=relogio.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            rodando = False
        if (event.type==pygame.KEYDOWN):
            if (event.key==pygame.K_q):
                 Goku = Boneco(['1.png','2.png'],5,275)
                 Goku.ativa_boneco('1.png')
                 Goku.vida=100
                 Goku_group.add(Goku)
            elif (event.key==pygame.K_w):
                 Naruto = Boneco(['naruto1.png','naruto2.png','naruto3.png'],5,370)
                 Naruto.ativa_boneco('naruto1.png')
                 Naruto.vida=200
                 Naruto_group.add(Naruto)
            elif (event.key==pygame.K_z):
                Sasuke=Boneco(['sasuke1.png','sasuke2.png','sasuke3.png'],1100,300)
                Sasuke.ativa_boneco('sasuke1.png')
                Sasuke.vida=200
                inimigo_group.add(Sasuke)
    acao(Goku_group,inimigo_group,0,3,'3.png',1)
    acao(Naruto_group,inimigo_group,0,2,'naruto_parado.png',2)
    acao(inimigo_group,Naruto_group or Goku_group,0,-2,'sasuke_parado.png',2) 
        
    tela.blit(fundo, (0,0))
    torre_group.draw(tela)
    if contador==6:
        Goku_group.update()
        Naruto_group.update()
        contador=0
    Naruto_group.draw(tela)
    Goku_group.draw(tela)
    inimigo_group.draw(tela)
 
    pygame.display.flip()   
pygame.mixer.music.stop()
pygame.display.quit()