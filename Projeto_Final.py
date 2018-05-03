'Projeto de Desoft'
import pygame
import sys
from pygame.locals import *

class Boneco(pygame.sprite.Sprite):
    def __init__(self, imagem, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        
        self.image=pygame.image.load(imagem)
        self.rect=self.image.get_rect()
        self.rect.x=posx
        self.rect.y=posy

        
    def ativa_boneco(self, imagem):
        self.image=pygame.image.load(imagem)
    
    def move(self, velocidade):
        self.rect.x += velocidade

class Torre(pygame.sprite.Sprite):
    
    def __init__(self,imagem, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        
        self.image=pygame.image.load(imagem)
        self.rect=self.image.get_rect()
        self.rect.x=posx
        self.rect.y=posy
        
    def ativa_torre(self,imagem):
        self.image=pygame.image.load(imagem)
    
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


fundo= pygame.image.load("cenario.jpeg").convert()

personagem1 = Boneco('goku.png', 10,250)
personagem_group = pygame.sprite.Group()
inimigo1=Inimigo('Naruto.png',1100,351)
inimigo_group=pygame.sprite.Group()



rodando = True
while rodando:
    relogio=pygame.time.Clock()
    tempo=relogio.tick(50)
    
    pressed_keys=pygame.key.get_pressed()
    if pressed_keys[K_w]:
        personagem1.ativa_boneco('goku.png')
        personagem_group.add(personagem1)
    elif pressed_keys[K_q]:
        inimigo1.ativa_inimigo('Naruto.png')
        inimigo_group.add(inimigo1)
    if pygame.sprite.spritecollide(personagem1,inimigo_group, False):
        personagem1.move(0)
        inimigo1.move_inimigo(0)
    else:
        personagem1.move(1)
        inimigo1.move_inimigo(-3)
    for event in pygame.event.get():
        if event.type == QUIT:
            rodando = False
        
    tela.blit(fundo, (0,0))
    personagem_group.draw(tela)
    inimigo_group.draw(tela)
    
    pygame.display.update()   

pygame.display.quit()