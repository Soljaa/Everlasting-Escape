import pygame


def Follow_mouse(snail:pygame.surface, dt:float):
    speed = 2
    mouse_pos = pygame.mouse.get_pos()
    dirx = mouse_pos[0] - snail.x
    diry = mouse_pos[1] - snail.y
    snail.x += dirx * speed * dt
    snail.y += diry * speed * dt
    