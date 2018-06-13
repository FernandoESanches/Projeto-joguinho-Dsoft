'Projeto de Desoft'
#comandos iniciais vbaseados no jogo feito em sala: helloPongSpriteBase
#Transformador de gif em imagens utilizado: https://pt.bloggif.com/gif-extract

#=========================================Imports============================================
import pygame
import sys
from pygame.locals import *
import random
import numpy as np
from firebase import firebase

#=========================================Firebase===========================================
firebase=firebase.FirebaseApplication('https://joguinho-desoft.firebaseio.com/', None)
recorde=firebase.get('Score',None)
pontuacao={'pontos':0}

# ==============================Classes========================================================
class Boneco(pygame.sprite.Sprite):
    def __init__(self,lista_imagens,posx,posy,tipo,largura,altura):
        pygame.sprite.Sprite.__init__(self)
        
        self.imagens=[]
        for img in lista_imagens:
            self.imagens.append(pygame.image.load(img))
        self.index=0
        self.image=self.imagens[self.index]
        self.rect=pygame.Rect(posx,posy,largura,altura)
        self.tipo=tipo

    def ativa_boneco(self, imagem):
        self.image=pygame.image.load(imagem)
    
    def move(self, velocidade):
        self.rect.x += velocidade
    
    def update(self): #animações baseadas na fonte:https://stackoverflow.com/questions/14044147/animated-sprite-from-few-images
        self.index+=1
        if self.index>=len(self.imagens):
            self.index=0
        self.image=self.imagens[self.index]

    def altera_boneco(self,lista_imagens):
        self.imagens=[]
        for imagem in lista_imagens:
            self.imagens.append(pygame.image.load(imagem))   

    def dano(self,dano):
        self.dano=dano          

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
        
class Portal(pygame.sprite.Sprite):
    def __init__(self,lista_imagens,posx,posy,largura,altura):
        pygame.sprite.Sprite.__init__(self)
        
        self.imagens=[]
        for img in lista_imagens:
            self.imagens.append(pygame.image.load(img))
        self.index=0
        self.image=self.imagens[self.index]
        self.rect=pygame.Rect(posx,posy,largura,altura)

    def update(self): #animações baseadas na fonte:https://stackoverflow.com/questions/14044147/animated-sprite-from-few-images
        self.index+=1
        if self.index>=len(self.imagens):
            self.index=0
        self.image=self.imagens[self.index]

# =========================================Função====================================
def powerup(uuup,dano_inicial,power):
    if mana_max >= uuup:
        dano = dano_inicial
        dano += power
    else:
        dano = dano_inicial
    return dano

def acao(grupo_amigo, grupo_inimigo,pontuacao):
    for personagem in grupo_amigo:
        colisoes=pygame.sprite.spritecollide(personagem,grupo_inimigo, False)
        if colisoes:
            punch = pygame.mixer.Sound('smack.wav')
            punch.play()
            punch.set_volume(0.3)
            if personagem!=torre:
                personagem.move(0)
                if personagem.tipo=='Goku':
                    personagem.altera_boneco(['gokuat2.png','gokuat3.png','gokuat4.png',\
                                            'gokuat5.png','gokuat6.png','gokuat7.png','gokuat8.png'])
                    dano = powerup(800,5,30)
                    dano = powerup(1200,dano,30)
                elif personagem.tipo=='Naruto':
                    personagem.altera_boneco(['naruto_1.png','naruto_2.png','naruto_3.png',\
                                                'naruto_4.png','naruto_5.png','naruto_6.png','naruto_7.png',\
                                                'naruto_8.png'])
                    dano = powerup(1000,40,50)
                    dano = powerup(1300,dano,50)
                    
                elif personagem.tipo=='Luffy':
                    personagem.altera_boneco(['luffysoco1.png','luffysoco2.png','luffysoco3.png','luffysoco4.png'])
                    dano = powerup(1100,40,50)
                    dano = powerup(1400,dano,50)
                    

                elif personagem.tipo=='Sasuke':
                    personagem.altera_boneco(['chidori_1.png','chidori_2.png','chidori_3.png','chidori_4.png','chidori_5.png',\
                                            'chidori_6.png','chidori_7.png','chidori_8.png'])
                    
                elif personagem.tipo=='Ed':
                    personagem.altera_boneco(['ed1.png','ed2.png','ed3.png','ed4.png','ed5.png','ed6.png','ed7.png','ed8.png'])
                    
                elif personagem.tipo=='Boss':
                    personagem.altera_boneco(['bossat1.png','bossat2.png','bossat3.png','bossat4.png','bossat5.png',\
                                            'bossat6.png','bossat7.png','bossat8.png'])
                    
                for inimigo in colisoes:
                    inimigo.vida-=personagem.dano
            if personagem.vida<=0:
                grupo_amigo.remove(personagem)
                if personagem!=torre:
                    if personagem.tipo=='Ed':
                        pontuacao['pontos']+=50
                    elif personagem.tipo=='Sasuke':
                        pontuacao['pontos']+=200
                    elif personagem.tipo=='Boss':
                        pontuacao['pontos']+=2000
                        BOSS['vida']+=1000
                        BOSS['dano']+=30
                        
        else:
             if personagem!=torre:
                if personagem.tipo=='Goku':
                    personagem.altera_boneco(['goku1.png','goku2.png','goku3.png','goku4.png'])
                    personagem.move(9)
                elif personagem.tipo=='Naruto':
                    personagem.altera_boneco(['naruto1.png','naruto2.png','naruto3.png'])
                    personagem.move(5)
                elif personagem.tipo=='Sasuke':
                    personagem.altera_boneco(['sasuke1.png','sasuke2.png','sasuke3.png'])
                    personagem.move(-5)
                elif personagem.tipo=='Ed':
                    personagem.altera_boneco(['af1.png','af2.png','af3.png','af4.png','af5.png','af6.png'])
                    personagem.move(-8)

                elif personagem.tipo=='Luffy':
                    personagem.altera_boneco(['luffy1.png','luffy2.png','luffy3.png','luffy4.png','luffy5.png',\
                                            'luffy6.png','luffy7.png','luffy8.png'])
                    personagem.move(4)
                elif personagem.tipo=='Boss':
                    personagem.altera_boneco(['boss1.png','boss2.png','boss3.png','boss4.png'])
                    personagem.move(-1)

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

#================================Início======================================
pygame.init()

#=====Tela=========
tela = pygame.display.set_mode((1238,491), 0, 32)
pygame.display.set_caption('Tower defense')

#====Som========== orietações pegas de https://www.pygame.org/docs/ref/mixer.html
Música_pygame = pygame.mixer.Sound('Musica_pygame.wav')
Música_pygame.play()

tela_intro=pygame.image.load("start tela.png").convert()
start = Botao("Start",(1238/2, 150))
tela_tutorial = pygame.image.load("TelaTuto.png").convert()
tutorial = Botao("Tutorial",(1238/2, 400))
fonte =  pygame.font.SysFont("monospace", 30)
fonte_score = pygame.font.SysFont("Arial", 30)
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
the_portal=pygame.sprite.Group()

portal=Portal(['portal1.png','portal2.png','portal3.png','portal4.png','portal5.png','portal6.png','portal7.png','portal8.png','portal9.png'],\
                1020,140,400,400)
torre=Torre("Torre.png", -100,100)
torre.vida(10000)
todos_amigos.add(torre)
the_portal.add(portal)

#Controle de mana
mana_max=300
limite=1000
mana=100
vel_mana=1

#Caracteristicas do Boss
BOSS={'vida':10000,'dano':100}

contador=0
contador_inimigo=0
contador_update_dos_inimigos=0
contador4=0
contador_boss=0
valor_da_mana=50
contador_final = 1
dificuldade = 0
while rodando:
    try:
        if mana<=mana_max:
            mana+=vel_mana
            if mana>mana_max:
                mana=mana_max
        else:
            mana+=0
        contador+=1
        contador_inimigo+=1
        contador_boss+=1
        contador_update_dos_inimigos+=1
        contador4+=1

        relogio=pygame.time.Clock()
        tempo=relogio.tick(40)

        for event in pygame.event.get():
            #Comandos
            if event.type == QUIT:
                rodando = False
            if (event.type==pygame.KEYDOWN):
                if (event.key==pygame.K_q):
                    if mana>=40:
                        Goku = Boneco(['goku1.png','goku2.png','goku3.png','goku4.png'],5,275,'Goku',200,158)
                        Goku.vida=2500
                        Goku.dano=5
                        todos_amigos.add(Goku)
                        mana-=40

                elif (event.key==pygame.K_w):
                    if mana>=100:
                        Naruto = Boneco(['naruto1.png','naruto2.png','naruto3.png'],5,370,'Naruto',115,146)
                        Naruto.vida=2000
                        Naruto.dano=40
                        todos_amigos.add(Naruto)
                        mana-=100
                
                elif (event.key==pygame.K_e):
                    if mana>=300:
                        Luffy = Boneco(['luffy1.png','luffy2.png','luffy3.png','luffy4.png','luffy5.png',\
                            'luffy6.png','luffy7.png','luffy8.png'],5,380,'Luffy',87,100)
                        Luffy.vida=4000
                        Luffy.dano=50
                        todos_amigos.add(Luffy)
                        mana-=300

                elif (event.key==pygame.K_m):
                    if mana>=valor_da_mana:
                        if mana_max<limite:
                            mana_max+=100
                            vel_mana+=0.5
                            mana-=valor_da_mana
                            valor_da_mana+=30
        
        acao(inimigo_group,todos_amigos,pontuacao)
        acao(todos_amigos,inimigo_group,pontuacao)

        #Wave 
        x = random.randint(0,100)
        if x > 60 - dificuldade and x < 75 + dificuldade:
            if contador_inimigo == 4:
                Sasuke=Boneco(['sasuke1.png','sasuke2.png','sasuke3.png'],1100,300,'Sasuke',157,200)
                Sasuke.vida=2000
                Sasuke.dano=30
                inimigo_group.add(Sasuke)
        elif x > 35 - dificuldade and x < 40 + dificuldade:
            if contador_inimigo == 4:
                Ed=Boneco(['af1.png','af2.png','af3.png','af4.png','af5.png','af6.png'],1100,300,'Ed',239,200)
                Ed.vida=1000
                Ed.dano=20
                inimigo_group.add(Ed)
        if contador_boss==200:
            Boss=Boneco(['boss1.png','boss2.png','boss3.png','boss4.png'],1100,250,'Boss',250,259)
            Boss.vida=BOSS['vida']
            Boss.dano=BOSS['dano']
            inimigo_group.add(Boss)
            contador_final=100
            dificuldade += 2
        
        if contador_final == 100:
            contador_inimigo = 0
        if contador_boss==800:
            contador_final = 0
            contador_boss = 0
        if contador_inimigo == 10:
            contador_inimigo = 0
            contador_final += 1
        
         
    # printar o contador de mana https://stackoverflow.com/questions/19733226/python-pygame-how-to-make-my-score-text-update-itself-forever   
        manatexto = fonte.render("Mana: {0}/{1}".format(int(mana),mana_max), 7, (250,250,250))
        quadro=pygame.image.load('quadro.jpg')
        tela.blit(fundo, (0,0))
        tela.blit(quadro,(0,0))
        tela.blit(manatexto, (20, 20))
        telinha_goku = pygame.image.load('cara_goku_bloqueada.jpg')
        telinha_naruto = pygame.image.load('Naruto_indisponivel.png')
        telinha_mana = pygame.image.load('crystal_pixel_mana_bloqueada.png')
        telinha_luffy = pygame.image.load('Cara_luffy_bloqueada.png')
        tela.blit(telinha_goku,(320,0))
        tela.blit(telinha_naruto,(402,0))
        tela.blit(telinha_mana,(566,0))
        tela.blit(telinha_luffy,(484,0))
        
        #Cooldown dos personagens
        def cooldown(mana_min, imagem,posicao):
            if mana >= mana_min:
                telinha = pygame.image.load(imagem)
                tela.blit(telinha,posicao)
        cooldown(40,"cara_goku.jpg",(320,0))
        cooldown(100,"naruto_rosto.jpg",(402,0))
        cooldown(300,"Cara_luffy.png",(484,0))
        cooldown(valor_da_mana,'crystal_pixel_mana.png',(566,0))
        cooldown(300,"Cara_luffy.png",(484,0))
        
        #Tempo para dar o update
        if contador==1:
            inimigo_group.update()
            contador=0
        if contador_update_dos_inimigos==1:
            todos_amigos.update()
            the_portal.update()
            contador_update_dos_inimigos=0
        the_portal.draw(tela)
        todos_amigos.draw(tela)
        inimigo_group.draw(tela)

        #=====Barra de vida======Retirado de https://stackoverflow.com/questions/19780411/pygame-drawing-a-rectangle
        red=(255,0,0)
        green=(0,255,0)
        torre_life=150*torre.vida/10000
        barra_vermelha=pygame.draw.rect(tela,red,(80,160,150,10))
        vida=pygame.draw.rect(tela,green,(80,160,torre_life,10))
        if torre.vida<=0:
            
            fundo= pygame.image.load("gameover.jpg").convert()
            del(inimigo_group)
            del(todos_amigos)
            del(vida)
            del(torre_life)
            tela.blit(fundo,(0,0))
            pygame.mixer.music.stop()
            if recorde<pontuacao['pontos']:
                recorde=pontuacao['pontos']
            scores = fonte_score.render("Score: {0}".format(pontuacao['pontos']), 7, (250,250,250))
            recordes= fonte_score.render("Highscore: {0}".format(recorde), 7, (250,250,250))
            tela.blit(scores,(1100/2,50))
            tela.blit(recordes,(1100/2,100))
            if (event.type==pygame.KEYDOWN):
                if event.key==K_ESCAPE:
                    rodando=False

        pygame.display.flip()
    except NameError:
        None

firebase.put('https://joguinho-desoft.firebaseio.com/','Score',recorde)
print('Pontuação:{0}. \nRecorde:{1}.'.format(pontuacao['pontos'],recorde))
pygame.display.quit()
Música_pygame.stop()
Música_pygame.fadeout