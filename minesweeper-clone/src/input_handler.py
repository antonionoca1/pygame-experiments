import pygame
from .board import CELL_SIZE, MARGIN

class InputHandler:
    def __init__(self, board):
        self.board = board

    def handle_event(self, event):
        if self.board.state != 'playing':
            return
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = self._get_cell_from_mouse(event.pos)
            if x is None or y is None:
                return
            if event.button == 1:
                self.board.reveal_cell(x, y)
            elif event.button == 3:
                mods = pygame.key.get_mods()
                if mods & pygame.KMOD_SHIFT:
                    self.board.toggle_question(x, y)
                else:
                    self.board.toggle_flag(x, y)
            elif event.button == 2:
                self.board.chord_click(x, y)

    def _get_cell_from_mouse(self, pos):
        mx, my = pos
        mx -= MARGIN
        my -= MARGIN + 60
        if mx < 0 or my < 0:
            return None, None
        x = mx // CELL_SIZE
        y = my // CELL_SIZE
        w, h = self.board.board_size
        if 0 <= x < w and 0 <= y < h:
            return x, y
        return None, None
