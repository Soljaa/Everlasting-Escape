import pygame
import random
import math


def start_pos(RES:tuple) -> tuple:
    side = random.randint(1,4)
    match side:
        case 1:
            return (0, random.randint(0,RES[1]))
        case 2:
            return (random.randint(0,RES[0]), 0)
        case 3:
            return (RES[0], random.randint(0,RES[1]))
        case 4:
            return (random.randint(0,RES[0]), RES[1])
    

class Bat():
    sprite = 'images\\bat.png'

    def __init__(self, janela:pygame.surface):
        self.bat = pygame.image.load(Bat.sprite)
        self.janela_size = janela.get_size()
        self.pos = start_pos(janela.get_size())
        self.speed = 200
        self.rect = self.bat.get_rect(center = self.pos)
        self.dano = 5
        self.xp = 5
                
                      
    def draw(self:pygame.surface, janela:pygame.surface, dt:float):
        # draw
        self.rect = self.bat.get_rect(center = self.pos)
        janela.blit(self.bat, self.rect)

        # direction 
        self.x_diff, self.y_diff = self.janela_size[0]/2-self.pos[0], self.janela_size[1]/2-self.pos[1]
        ang = math.atan2(self.y_diff, self.x_diff)
        dist = int(math.hypot(self.x_diff,self.y_diff))
        if dist > 0:
            self.pos = self.pos[0] + math.cos(ang)*self.speed*dt, self.pos[1] + math.sin(ang)*self.speed*dt
        if dist < 200:  
            self.pos = self.pos[0] + math.cos(ang)*self.speed*dt*1.1, self.pos[1] + math.sin(ang)*self.speed*dt*1.1
    def resize(self, size:tuple):
        self.bat = pygame.transform.smoothscale(self.bat, size)

        
class Lacraia():
    sprite = 'images\\lacraia.png'
    sprite_tiro = 'images\\acid_shot.png'
    sprite_area = 'images\\acid_floor.png'     

    def __init__(self, janela: pygame.surface, min:int):
        self.lac = pygame.image.load(Lacraia.sprite)
        self.janela_size = janela.get_size()
        self.pos = start_pos(janela.get_size())
        self.speed = 100
        self.rect = self.lac.get_rect(center = self.pos)
        self.vida = 15*(1+min)
        self.xp = 15
        # acido
        self.acido_pos = self.pos
        self.acido = pygame.image.load(Lacraia.sprite_tiro)
        self.acido_area = pygame.image.load(Lacraia.sprite_area)
        self.acido_rect = self.acido.get_rect(center = self.acido_pos)
        self.acido_speed = 150
        self.atirou = 1
        self.acido_x_diff, self.acido_y_diff = 0,0
        self.stop = 0
        self.timer = 0
        self.dano = 15
    
    def resize(self, size:tuple):
        self.lac = pygame.transform.smoothscale(self.lac, size)

    def draw(self:pygame.surface, janela:pygame.surface, dt:float):
        # draw
        self.rect = self.lac.get_rect(center = self.pos)
        janela.blit(self.lac, self.rect)

        # direction 
        self.x_diff, self.y_diff = self.janela_size[0]/2-self.pos[0], self.janela_size[1]/2-self.pos[1]
        ang = math.atan2(self.y_diff, self.x_diff)
        dist = int(math.hypot(self.x_diff,self.y_diff))
        if dist > 250:
            self.pos = self.pos[0] + math.cos(ang)*self.speed*dt, self.pos[1] + math.sin(ang)*self.speed*dt

    def tiro(self:pygame.surface, janela:pygame.surface, dt:float, player:pygame.surface):
        if self.atirou:
            self.acido_rect = self.acido.get_rect(center = self.acido_pos)
            janela.blit(self.acido, self.acido_rect)
            self.acido_x_diff, self.acido_y_diff = self.janela_size[0]/2-self.acido_pos[0], self.janela_size[1]/2-self.acido_pos[1]
            ang = math.atan2(self.acido_y_diff, self.acido_x_diff)
            self.atirou = 0
            
        if not self.atirou and not self.stop: 

            if self.acido_rect.colliderect(player.player_rect):
                self.acido_rect = self.acido_area.get_rect(center = self.acido_pos)
                janela.blit(self.acido_area, self.acido_rect)
                player.vida -= self.dano
                self.stop = 1

            else:
                ang = math.atan2(self.acido_y_diff, self.acido_x_diff)
                self.acido_pos = self.acido_pos[0] + math.cos(ang)*self.acido_speed*dt, self.acido_pos[1] + math.sin(ang)*self.acido_speed*dt
                self.acido_rect = self.acido.get_rect(center = self.acido_pos)
                janela.blit(self.acido, self.acido_rect)
                if self.acido_pos[0] < 0 or self.acido_pos[0] > janela.get_width() or self.acido_pos[1] < 0 or self.acido_pos[1] > janela.get_height():
                    self.acido_pos = self.pos
                    self.atirou = 1
                    self.stop = 0
        if self.stop:
            self.acido_rect = self.acido_area.get_rect(center = self.acido_pos)
            janela.blit(self.acido_area, self.acido_rect)
            self.timer = self.timer + dt 
            if self.timer > 5:
                self.acido_pos = self.pos
                self.atirou = 1
                self.stop = 0
                self.timer = 0 
        
 
class Polvo():
    sprite = 'Images\\Cthunu.png'

    def __init__(self, janela:pygame.surface, min:int):
        self.polvo = pygame.image.load(Polvo.sprite)
        self.janela_size = janela.get_size()
        self.pos = start_pos(janela.get_size())
        self.speed = 75
        self.rect = self.polvo.get_rect(center = self.pos)
        self.dano = 2
        self.xp = 600
        self.vida = 100*(min)
        self.timer = 0
        self.atual = 0       
                      
    def draw(self:pygame.surface, janela:pygame.surface, dt:float, player:pygame.surface):
        # draw
        self.rect = self.polvo.get_rect(center = self.pos)
        janela.blit(self.polvo, self.rect)

        # direction 
        self.x_diff, self.y_diff = self.janela_size[0]/2-self.pos[0], self.janela_size[1]/2-self.pos[1]
        ang = math.atan2(self.y_diff, self.x_diff)
        dist = int(math.hypot(self.x_diff,self.y_diff))
        if dist > 200:
            self.pos = self.pos[0] + math.cos(ang)*self.speed*dt, self.pos[1] + math.sin(ang)*self.speed*dt
            self.timer = 0
        else:
            player.speed = 200
            self.timer += dt
            if int(self.timer*10) % 2 == 0 and int(self.timer*10) != self.atual:
                self.atual = int(self.timer*10)
                player.vida -= self.dano 

    def resize(self, size:tuple):
        self.polvo = pygame.transform.smoothscale(self.polvo, size)


class Zwarrior():
    sprite = 'images\\zombie_warrior.png'

    def __init__(self, janela:pygame.surface, min:int):
        self.zw = pygame.image.load(Zwarrior.sprite)
        self.janela_size = janela.get_size()
        self.pos = start_pos(janela.get_size())
        self.speed = 180
        self.rect = self.zw.get_rect(center = self.pos)
        self.dano = 10
        self.xp = 10
        self.vida = 20*(1+min)
        self.timer = 0
        self.atual = 0
                
                      
    def draw(self:pygame.surface, janela:pygame.surface, dt:float, player:pygame.surface):
        # draw
        self.rect = self.zw.get_rect(center = self.pos)
        janela.blit(self.zw, self.rect)

        # direction 
        self.x_diff, self.y_diff = self.janela_size[0]/2-self.pos[0], self.janela_size[1]/2-self.pos[1]
        ang = math.atan2(self.y_diff, self.x_diff)
        dist = int(math.hypot(self.x_diff,self.y_diff))
        if dist > 50:
            self.pos = self.pos[0] + math.cos(ang)*self.speed*dt, self.pos[1] + math.sin(ang)*self.speed*dt
            self.timer = 0
        else:
            self.timer += dt
            if int(self.timer*10) % 5 == 0 and int(self.timer*10) != self.atual:
                self.atual = int(self.timer*10)
                player.vida -= self.dano
            

    def resize(self, size:tuple):
        self.zw = pygame.transform.smoothscale(self.zw, size)


class Zking():
    sprite = 'images\\zombie_king.png'
    sprite_tiro = 'images\\acid_shot.png'

    def __init__(self, janela:pygame.surface):
        self.zking = pygame.image.load(Zking.sprite)
        self.janela_size = janela.get_size()
        self.pos = start_pos(janela.get_size())
        self.speed = 100
        self.rect = self.zking.get_rect(center = self.pos)
        self.dano = 50
        self.xp = 10000
        self.vida = 1000
        self.timer = 0
        self.atual = 0
        self.timer_tiro = 0
        self.atual_tiro = 0
        # tiros
        self.tiros = []
       
        

    def draw(self:pygame.surface, janela:pygame.surface, dt:float, player:pygame.surface):
        self.timer_tiro += dt
        # draw
        self.rect = self.zking.get_rect(center = self.pos)
        janela.blit(self.zking, self.rect)

        # direction 
        self.x_diff, self.y_diff = self.janela_size[0]/2-self.pos[0], self.janela_size[1]/2-self.pos[1]
        ang = math.atan2(self.y_diff, self.x_diff)
        dist = int(math.hypot(self.x_diff,self.y_diff))
        if dist > 130:
            self.pos = self.pos[0] + math.cos(ang)*self.speed*dt, self.pos[1] + math.sin(ang)*self.speed*dt
            self.timer = 0
            if not int(self.timer_tiro*10) % 3 and int(self.timer_tiro*10) != self.atual_tiro:
                self.atual_tiro = int(self.timer_tiro*10)
                self.tiros.append(Zbullet(janela, self))
            
        else:
            self.timer += dt
            if int(self.timer*10) % 10 == 0 and int(self.timer*10) != self.atual:
                self.atual = int(self.timer*10)
                player.vida -= self.dano
            self.timer_tiro = 0

    def resize(self, size:tuple):
        self.zking = pygame.transform.smoothscale(self.zking, size)


class Zbullet:
    sprite_tiro = 'images\\acid_shot.png'

    def __init__(self, janela:pygame.surface, zking:pygame.surface):
        self.bullet = pygame.image.load(Zbullet.sprite_tiro)
        self.rect = self.bullet.get_rect(center = zking.pos)
        self.speed = 3
        self.angle = math.atan2(janela.get_height()/2 - zking.pos[1], janela.get_width()/2 - zking.pos[0])
        self.vel_x = int(math.cos(self.angle) * self.speed)
        self.vel_y = int(math.sin(self.angle) * self.speed)
        self.dano = 5
        self.timer = 0
        
        
    def shot(self, dt:float, player:pygame.surface):
        self.timer += dt
        # self.rect_bullet.x += self.vel_x*dt
        # self.rect_bullet.y += self.vel_y*dt
        self.rect.move_ip(self.vel_x,self.vel_y)
        if self.rect.colliderect(player.player_rect):
            return 1
        else:
            return 0


class Manowar():
    sprite = 'images\\manowar.png'

    def __init__(self, janela:pygame.surface, min):
        self.manowar = pygame.image.load(Manowar.sprite)
        self.janela_size = janela.get_size()
        self.pos = start_pos(janela.get_size())
        self.speed = 120
        self.rect = self.manowar.get_rect(center = self.pos)
        self.dano = 30
        self.xp = 50
        self.vida = 30*(min)
                
                      
    def draw(self:pygame.surface, janela:pygame.surface, dt:float, player:pygame.surface):
        # draw
        self.rect = self.manowar.get_rect(center = self.pos)
        janela.blit(self.manowar, self.rect)

        # direction 
        self.x_diff, self.y_diff = self.janela_size[0]/2-self.pos[0], self.janela_size[1]/2-self.pos[1]
        ang = math.atan2(self.y_diff, self.x_diff)
        dist = int(math.hypot(self.x_diff,self.y_diff))
        if dist > 70:
            self.pos = self.pos[0] + math.cos(ang)*self.speed*dt, self.pos[1] + math.sin(ang)*self.speed*dt
        else:
            player.speed = 0
          

    def resize(self, size:tuple):
        self.manowar = pygame.transform.smoothscale(self.manowar, size)