import pygame
from .board import CELL_SIZE, MARGIN

class Hud:
    def __init__(self, board):
        self.board = board

    def draw(self, screen, elapsed):
        font = pygame.font.SysFont(None, 36)
        timer = font.render(f'Time: {elapsed}', True, (0,0,0))
        mines = font.render(f'Mines: {self.board.mine_counter}', True, (0,0,0))
        screen.blit(timer, (MARGIN, 5))
        screen.blit(mines, (MARGIN + 200, 5))

    def draw_message(self, screen, msg):
        font = pygame.font.SysFont(None, 48)
        text = font.render(msg, True, (255,0,0))
        rect = text.get_rect(center=(screen.get_width()//2, 40))
        screen.blit(text, rect)
