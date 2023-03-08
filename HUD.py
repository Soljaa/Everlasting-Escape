import pygame


class HUD_element():

    def __init__(self, file:str, pos:tuple):
        self.pos = pos
        self.hud_element = pygame.image.load(file)
        self.rect = self.hud_element.get_rect(center = self.pos)
                   
    def draw(self:pygame.surface, janela:pygame.surface):
        self.rect = self.hud_element.get_rect(center = self.pos)
        janela.blit(self.hud_element, self.rect)
    
    def resize(self, size:tuple):
        self.hud_element = pygame.transform.smoothscale(self.hud_element, size)

# hide
# posicionar
# desenhar
# resize