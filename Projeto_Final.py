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
            personagem.tira_vida(grupo_inimigo,personagem,dano)
            if personagem.vida<=0:
                grupo_amigo.remove(personagem)
        else:
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
torre2 = Torre("Torre2.png", 795,50)
torre_group=pygame.sprite.Group()
torre_group.add(torre, torre2)

rodando = True
mana_max=300
mana=0
contador=0
while rodando:
    if mana<=mana_max:
        mana+=1
    else:
        mana+=0
    contador+=1
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
            elif (event.key==pygame.K_z):
                Sasuke=Boneco(['sasuke1.png','sasuke2.png','sasuke3.png'],1100,300)
                Sasuke.ativa_boneco('sasuke1.png')
                Sasuke.vida=200
                inimigo_group.add(Sasuke)

            elif (event.key==pygame.K_m):
                if mana>=50:
                    maximo+=100
    
    acao(inimigo_group,todos_amigos,0,-4,5)
    acao(todos_amigos,inimigo_group,0,5,5)

    tela.blit(fundo, (0,0))
    torre_group.draw(tela)
    if contador==5:
        todos_amigos.update()
        inimigo_group.update()
        contador=0
    todos_amigos.draw(tela)
    inimigo_group.draw(tela)
 
    pygame.display.flip()   
pygame.mixer.music.stop()
pygame.display.quit()