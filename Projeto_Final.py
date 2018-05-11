'Projeto de Desoft'
#comandos iniciais vbaseados no jogo feito em sala: helloPongSpriteBase
#animações baseadas na fonte:https://stackoverflow.com/questions/14044147/animated-sprite-from-few-images
import pygame
import sys
from pygame.locals import *

class Boneco(pygame.sprite.Sprite):
    def __init__(self,lista_imagens):
        pygame.sprite.Sprite.__init__(self)
        
        self.imagens=[]
        for img in lista_imagens:
            self.imagens.append(pygame.image.load(img))
        self.index=0
        self.image=self.imagens[self.index]
        self.rect=pygame.Rect(5,280,120,120)

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
    
class Inimigo(pygame.sprite.Sprite):
    
    def __init__(self, imagem, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(imagem)
        self.rect=self.image.get_rect()
        self.rect.x=posx
        self.rect.y=posy
    
    def ativa_inimigo(self, imagem):
        self.image = pygame.image.load(imagem)
        
    def move_inimigo(self, velocidade):
        self.rect.x += velocidade
# início
    
pygame.init()
tela = pygame.display.set_mode((1238,491), 0, 32)
pygame.display.set_caption('Tower defense')
pygame.mixer.music.load('Música_pygame.mp3')
pygame.mixer.music.play()


fundo= pygame.image.load("cenario.jpeg").convert()

Goku_group = pygame.sprite.Group()
Naruto_group=pygame.sprite.Group()
inimigo1=Inimigo('Naruto.png',1100,351)
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
                 Goku = Boneco(['1.png','2.png'])
                 Goku.ativa_boneco('1.png')
                 Goku.vida=100
                 Goku_group.add(Goku)
            elif (event.key==pygame.K_w):
                 Naruto = Boneco(['naruto1.png','naruto2.png','naruto3.png'])
                 Naruto.ativa_boneco('naruto1.png')
                 Naruto.vida=100
                 Naruto_group.add(Naruto)
            elif (event.key==pygame.K_z):
                inimigo1.ativa_inimigo('Naruto.png')
                inimigo_group.add(inimigo1)
    for personagem in  Goku_group:
        if pygame.sprite.spritecollide(personagem,inimigo_group, False):
            personagem.move(0)
            personagem.ativa_boneco('3.png')
        else:
            personagem.move(3)
    for personagem in  Naruto_group:
        if pygame.sprite.spritecollide(personagem,inimigo_group, False):
            personagem.move(0)
            personagem.ativa_boneco('naruto3.png')
        else:
            personagem.move(3)
    for inimigo in inimigo_group:
        if pygame.sprite.spritecollide(inimigo, Goku_group, False):
            inimigo.move_inimigo(0)
        else:
            inimigo.move_inimigo(-2)
        
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