import pygame
import math

def rot_center(image, angle):
    
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

class Player:
    sprite = 'Images\dola.png'


    def __init__(self, janela:pygame.surface):
        self.player = pygame.image.load(Player.sprite)
        self.vida = 100
        self.xp = 0
        self.nivel = 0
        self.player_rect = self.player.get_rect(center = (janela.get_width()/2, janela.get_height()/2))
        self.speed = 400
        self.arma = 'arco'
        self.balas = []
        self.dano = 5*(1+self.nivel)
        # pega direção do mouse e usar para mudar o sprite no draw
    
    def draw(self:pygame.surface, janela:pygame.surface):
        self.player_rect = self.player.get_rect(center = (janela.get_width()/2, janela.get_height()/2))
        janela.blit(self.player, self.player_rect)
        self.dano = 5*(1+self.nivel)
    
    def resize(self, size:tuple):
        self.player = pygame.transform.smoothscale(self.player, size)
        


class PlayerBullet:
    flecha = 'images\\flecha.png'
    magia = 'images\\fire_ball.png'
    lanca = 'images\\lança.png'
    arco_lanca = ''
    arco_cajado = ''
    cajado_lanca = ''

    def __init__(self, mouse_pos:tuple, janela:pygame.surface, arma:str, dano:int):
        # basicos
        if arma == 'arco':
            self.bullet = pygame.image.load(PlayerBullet.magia)
            self.angle = math.atan2(mouse_pos[1]-janela.get_height()/2, mouse_pos[0]-janela.get_width()/2)
            self.bullet = rot_center(self.bullet, self.angle)
            self.rect = self.bullet.get_rect(center = (janela.get_width()/2, janela.get_height()/2))            
            self.speed = 6
        elif arma == 'cajado':
            self.bullet = pygame.image.load(PlayerBullet.magia)
            self.rect = self.bullet.get_rect(center = (janela.get_width()/2, janela.get_height()/2))
            self.angle = math.atan2(mouse_pos[1]-janela.get_height()/2, mouse_pos[0]-janela.get_width()/2)
            self.speed = 3
        elif arma == 'lanca':
            self.bullet = pygame.image.load(PlayerBullet.lanca)
            self.rect = self.bullet.get_rect(center = (janela.get_width()/2, janela.get_height()/2))
            self.angle = math.atan2(mouse_pos[1]-janela.get_height()/2, mouse_pos[0]-janela.get_width()/2)
            self.speed = 6
        # misturados
        elif arma == 'arco_lanca':
            self.bullet = pygame.image.load(PlayerBullet.arco_lanca)
            self.rect = self.bullet.get_rect(center = (janela.get_width()/2, janela.get_height()/2))
            self.angle = math.atan2(mouse_pos[1]-janela.get_height()/2, mouse_pos[0]-janela.get_width()/2)
            self.speed = 6
        elif arma == 'arco_cajado':
            self.bullet = pygame.image.load(PlayerBullet.flecha)
            self.rect = self.bullet.get_rect(center = (janela.get_width()/2, janela.get_height()/2))
            self.angle = math.atan2(mouse_pos[1]-janela.get_height()/2, mouse_pos[0]-janela.get_width()/2)
            self.speed = 6
        elif arma == 'cajado_lanca':
            self.bullet = pygame.image.load(PlayerBullet.cajado_lanca)
            self.rect = self.bullet.get_rect(center = (janela.get_width()/2, janela.get_height()/2))
            self.angle = math.atan2(mouse_pos[1]-janela.get_height()/2, mouse_pos[0]-janela.get_width()/2)
            self.speed = 6
        
        self.vel_x = int(math.cos(self.angle) * self.speed)
        self.vel_y = int(math.sin(self.angle) * self.speed)
        self.dano = dano
        
        
    def shot(self):
        # self.rect.x += self.vel_x*dt
        # self.rect.y += self.vel_y*dt
        self.rect.move_ip(self.vel_x,self.vel_y)
        

    