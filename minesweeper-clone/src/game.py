import pygame
import time
from .board import Board
from .hud import Hud
from .input_handler import InputHandler

class MinesweeperGame:
    def __init__(self, board_size, mines):
        self.board = Board(board_size, mines)
        self.hud = Hud(self.board)
        self.input_handler = InputHandler(self.board)
        self.state = 'playing'
        self.start_time = None
        self.elapsed = 0

    def update_timer(self):
        if self.start_time:
            self.elapsed = int(time.time() - self.start_time)

    def draw(self, screen):
        self.hud.draw(screen, self.elapsed)
        self.board.draw(screen)
        if self.state == 'lost':
            self.hud.draw_message(screen, 'Game Over')
        elif self.state == 'won':
            self.hud.draw_message(screen, 'You Win!')

    def handle_event(self, event):
        self.input_handler.handle_event(event)
        self.state = self.board.state
        if not self.start_time and not self.board.first_click:
            self.start_time = time.time()
