import sys, pygame
from tittle_snail import Follow_mouse
from ingame import *
from conquistas import *




def fade_in(image, speed, janela, pos):
    image.set_alpha(image.get_alpha() + speed)

    # Draw the image
    janela.blit(image, pos)
    pygame.time.delay(10)

def tela_menu():
    pygame.init()
    # janela
    RES_ini = 1366, 768
    janela_menu = pygame.display.set_mode(RES_ini)
    pygame.display.set_caption('Everlasting Escape')
    logo = pygame.image.load('images\\title.png')
    pygame.mouse.set_visible(True)

    bg = pygame.image.load('images\mapa.png') 
    bg = pygame.transform.scale(bg, RES_ini)
    bg.set_alpha(0)

    jogar = pygame.image.load('images\jogar.png')
    jogar.set_alpha(0)
    jogar_rect = jogar.get_rect(topleft =(RES_ini[0]/2 - jogar.get_width()/2, 3*RES_ini[1]/10 + jogar.get_height()))

    conquistas = pygame.image.load('images\conquistas.png')
    conquistas.set_alpha(0)
    conquistas_rect = conquistas.get_rect(topleft =(RES_ini[0]/2 - conquistas.get_width()/2, 3*RES_ini[1]/10 + 2*conquistas.get_height()))

    sair = pygame.image.load('images\sair.png')
    sair.set_alpha(0)
    sair_rect = sair.get_rect(topleft = (RES_ini[0]/2 - sair.get_width()/2, 3*RES_ini[1]/10 + 3*sair.get_height()))

    run = True
    while run:
        # event check
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and jogar_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    Iniciar(game = True)
                    tela_menu()
                if event.button == 1 and conquistas_rect.collidepoint(pygame.mouse.get_pos()):
                    Conquistas()
                if event.button == 1 and sair_rect.collidepoint(pygame.mouse.get_pos()):
                    sys.exit()
        

        # anti-ghost
        fade_in(bg, 1, janela_menu, (0,0))

        # displays
        janela_menu.blit(logo, (RES_ini[0]/2 - logo.get_width()/2, 3*RES_ini[1]/10 - logo.get_height()/2))
        fade_in(jogar, 50, janela_menu, (RES_ini[0]/2 - jogar.get_width()/2, 3*RES_ini[1]/10 + jogar.get_height()))
        fade_in(conquistas, 20, janela_menu, (RES_ini[0]/2 - conquistas.get_width()/2, 3*RES_ini[1]/10 + 2*conquistas.get_height()))
        fade_in(sair, 8, janela_menu, (RES_ini[0]/2 - sair.get_width()/2, 3*RES_ini[1]/10 + 3*sair.get_height()))
        
        

        pygame.display.flip()


if __name__ == '__main__':
    tela_menu()