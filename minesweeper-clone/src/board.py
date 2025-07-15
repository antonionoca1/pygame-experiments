import random
import pygame
import time

CELL_SIZE = 32
MARGIN = 40

class Board:
    def __init__(self, board_size, mines):
        self.board_size = board_size
        self.mines = mines
        self.reset()

    def reset(self):
        self.state = 'playing'
        self.start_time = None
        self.elapsed = 0
        self.flags = 0
        self.mine_counter = self.mines
        self.first_click = True
        self.board = self._create_board()
        self._place_mines()
        self._calculate_numbers()

    def _create_board(self):
        w, h = self.board_size
        return [[{'mine': False, 'revealed': False, 'flagged': False, 'question': False, 'number': 0} for _ in range(w)] for _ in range(h)]

    def _place_mines(self, safe_x=None, safe_y=None):
        w, h = self.board_size
        positions = [(x, y) for x in range(w) for y in range(h)]
        if safe_x is not None and safe_y is not None:
            positions.remove((safe_x, safe_y))
            for nx, ny in self._neighbors(safe_x, safe_y):
                if (nx, ny) in positions:
                    positions.remove((nx, ny))
        mines = random.sample(positions, self.mines)
        for x, y in mines:
            self.board[y][x]['mine'] = True

    def _calculate_numbers(self):
        w, h = self.board_size
        for y in range(h):
            for x in range(w):
                if self.board[y][x]['mine']:
                    continue
                self.board[y][x]['number'] = self._count_adjacent_mines(x, y)

    def _count_adjacent_mines(self, x, y):
        return sum(1 for nx, ny in self._neighbors(x, y) if self.board[ny][nx]['mine'])

    def _neighbors(self, x, y):
        w, h = self.board_size
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < w and 0 <= ny < h:
                    yield nx, ny

    def reveal_cell(self, x, y):
        cell = self.board[y][x]
        if cell['revealed'] or cell['flagged']:
            return
        if self.first_click:
            self._place_mines(x, y)
            self._calculate_numbers()
            self.start_time = time.time()
            self.first_click = False
        cell['revealed'] = True
        if cell['mine']:
            self.state = 'lost'
        elif cell['number'] == 0:
            self._flood_fill(x, y)
        self._check_win()

    def _flood_fill(self, x, y):
        for nx, ny in self._neighbors(x, y):
            cell = self.board[ny][nx]
            if not cell['revealed'] and not cell['mine'] and not cell['flagged']:
                cell['revealed'] = True
                if cell['number'] == 0:
                    self._flood_fill(nx, ny)

    def toggle_flag(self, x, y):
        cell = self.board[y][x]
        if cell['revealed']:
            return
        if not cell['flagged']:
            cell['flagged'] = True
            cell['question'] = False
            self.flags += 1
        else:
            cell['flagged'] = False
            self.flags -= 1
        self.mine_counter = self.mines - self.flags

    def toggle_question(self, x, y):
        cell = self.board[y][x]
        if cell['revealed']:
            return
        if not cell['question']:
            cell['question'] = True
            cell['flagged'] = False
            if self.flags > 0:
                self.flags -= 1
        else:
            cell['question'] = False

    def chord_click(self, x, y):
        cell = self.board[y][x]
        if not cell['revealed'] or cell['number'] == 0:
            return
        flags = sum(1 for nx, ny in self._neighbors(x, y) if self.board[ny][nx]['flagged'])
        if flags == cell['number']:
            for nx, ny in self._neighbors(x, y):
                ncell = self.board[ny][nx]
                if not ncell['flagged'] and not ncell['revealed']:
                    self.reveal_cell(nx, ny)

    def _check_win(self):
        for row in self.board:
            for cell in row:
                if not cell['mine'] and not cell['revealed']:
                    return
        if self.state == 'playing':
            self.state = 'won'

    def draw(self, screen):
        w, h = self.board_size
        font = pygame.font.SysFont(None, 28)
        for y in range(h):
            for x in range(w):
                cell = self.board[y][x]
                rect = pygame.Rect(MARGIN + x * CELL_SIZE, MARGIN + 60 + y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                color = (180, 180, 180) if cell['revealed'] else (100, 100, 100)
                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, (50, 50, 50), rect, 2)
                if cell['revealed']:
                    if cell['mine']:
                        pygame.draw.circle(screen, (0,0,0), rect.center, CELL_SIZE//4)
                    elif cell['number'] > 0:
                        num = font.render(str(cell['number']), True, (0,0,255))
                        screen.blit(num, (rect.x + 8, rect.y + 2))
                elif cell['flagged']:
                    pygame.draw.polygon(screen, (255,0,0), [(rect.x+8,rect.y+24),(rect.x+24,rect.y+16),(rect.x+8,rect.y+8)])
                elif cell['question']:
                    q = font.render('?', True, (0,128,0))
                    screen.blit(q, (rect.x + 8, rect.y + 2))
