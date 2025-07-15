import pygame
WIDTH, HEIGHT = 400, 600

def init_pygame():
    pygame.init()
    return pygame.display.set_mode((WIDTH, HEIGHT)), pygame.time.Clock()
