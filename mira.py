import pygame


def Mira(janela: pygame.display):
    pos = pygame.mouse.get_pos()
    mira = pygame.image.load('images\mira.png')
    mirarect = mira.get_rect(center=pos)
    janela.blit(mira,mirarect)
    