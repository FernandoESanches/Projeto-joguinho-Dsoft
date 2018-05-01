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
        self.rect.x+=velocidade

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
        vida = 'a definir'
        vida += -dano
        
        return vida

# início
    
pygame.init()
tela = pygame.display.set_mode((1400,700), 0, 32)
pygame.display.set_caption('Tower defense')


fundo= 'a definir'

pressed_keys=pygame.key.get_pressed()
if pressed_keys[W]:
   personagem1 = Boneco('a definir', (10),(10))
   personagem1_group = pygame.sprite.Group()
   personagem1_group.add(personagem1)

torre1 = Torre('a definir',(10),(10))
torre1_group= pygame.sprite.Group()
torre1_group.add(torre1)

torre2 = Torre('a definir',(1300),(10))
torre2_group= pygame.sprite.Group()
torre2_group.add(torre2)


rodando = True
while rodando:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            rodando = False
            
    
    boneco.move()
    
        