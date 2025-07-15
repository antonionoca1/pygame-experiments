import pygame
import random
import sys
import time

# Game settings
BOARD_SIZES = [(9, 9), (16, 16), (30, 16)]
MINES_COUNT = [10, 40, 99]
CELL_SIZE = 32
MARGIN = 40

class Minesweeper:
    def __init__(self, board_size=(9, 9), mines=10):
        self.board_size = board_size
        self.mines = mines
        self.reset_game()

    def reset_game(self):
        self.state = 'playing'
        self.start_time = None
        self.elapsed = 0
        self.flags = 0
        self.mine_counter = self.mines
        self.first_click = True
        self.board = self.create_board()
        self.place_mines()
        self.calculate_numbers()

    def create_board(self):
        w, h = self.board_size
        return [[{'mine': False, 'revealed': False, 'flagged': False, 'question': False, 'number': 0} for _ in range(w)] for _ in range(h)]

    def place_mines(self, safe_x=None, safe_y=None):
        # Place mines, avoiding the first clicked cell
        w, h = self.board_size
        positions = [(x, y) for x in range(w) for y in range(h)]
        if safe_x is not None and safe_y is not None:
            positions.remove((safe_x, safe_y))
            for nx, ny in self.neighbors(safe_x, safe_y):
                if (nx, ny) in positions:
                    positions.remove((nx, ny))
        mines = random.sample(positions, self.mines)
        for x, y in mines:
            self.board[y][x]['mine'] = True

    def calculate_numbers(self):
        w, h = self.board_size
        for y in range(h):
            for x in range(w):
                if self.board[y][x]['mine']:
                    continue
                self.board[y][x]['number'] = self.count_adjacent_mines(x, y)

    def count_adjacent_mines(self, x, y):
        return sum(1 for nx, ny in self.neighbors(x, y) if self.board[ny][nx]['mine'])

    def neighbors(self, x, y):
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
            self.place_mines(x, y)
            self.calculate_numbers()
            self.start_time = time.time()
            self.first_click = False
        cell['revealed'] = True
        if cell['mine']:
            self.state = 'lost'
        elif cell['number'] == 0:
            self.flood_fill(x, y)
        self.check_win()

    def flood_fill(self, x, y):
        for nx, ny in self.neighbors(x, y):
            cell = self.board[ny][nx]
            if not cell['revealed'] and not cell['mine'] and not cell['flagged']:
                cell['revealed'] = True
                if cell['number'] == 0:
                    self.flood_fill(nx, ny)

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
        flags = sum(1 for nx, ny in self.neighbors(x, y) if self.board[ny][nx]['flagged'])
        if flags == cell['number']:
            for nx, ny in self.neighbors(x, y):
                ncell = self.board[ny][nx]
                if not ncell['flagged'] and not ncell['revealed']:
                    self.reveal_cell(nx, ny)

    def check_win(self):
        for row in self.board:
            for cell in row:
                if not cell['mine'] and not cell['revealed']:
                    return
        if self.state == 'playing':
            self.state = 'won'

    def update_timer(self):
        if self.start_time:
            self.elapsed = int(time.time() - self.start_time)

    def draw(self, screen):
        self.draw_hud(screen)
        self.draw_board(screen)
        if self.state == 'lost':
            self.draw_message(screen, 'Game Over')
        elif self.state == 'won':
            self.draw_message(screen, 'You Win!')

    def draw_hud(self, screen):
        font = pygame.font.SysFont(None, 36)
        timer = font.render(f'Time: {self.elapsed}', True, (0,0,0))
        mines = font.render(f'Mines: {self.mine_counter}', True, (0,0,0))
        screen.blit(timer, (MARGIN, 5))
        screen.blit(mines, (MARGIN + 200, 5))

    def draw_board(self, screen):
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

    def draw_message(self, screen, msg):
        font = pygame.font.SysFont(None, 48)
        text = font.render(msg, True, (255,0,0))
        rect = text.get_rect(center=(screen.get_width()//2, 40))
        screen.blit(text, rect)

    def handle_event(self, event):
        if self.state not in ['playing']:
            return
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = self.get_cell_from_mouse(event.pos)
            if x is None or y is None:
                return
            if event.button == 1:
                self.reveal_cell(x, y)
            elif event.button == 3:
                mods = pygame.key.get_mods()
                if mods & pygame.KMOD_SHIFT:
                    self.toggle_question(x, y)
                else:
                    self.toggle_flag(x, y)
            elif event.button == 2:
                self.chord_click(x, y)

    def get_cell_from_mouse(self, pos):
        mx, my = pos
        mx -= MARGIN
        my -= MARGIN + 60
        if mx < 0 or my < 0:
            return None, None
        x = mx // CELL_SIZE
        y = my // CELL_SIZE
        w, h = self.board_size
        if 0 <= x < w and 0 <= y < h:
            return x, y
        return None, None

def main():
    pygame.init()
    board_size = BOARD_SIZES[0]
    mines = MINES_COUNT[0]
    width = board_size[0] * CELL_SIZE + MARGIN * 2
    height = board_size[1] * CELL_SIZE + MARGIN * 2 + 60
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Minesweeper')
    clock = pygame.time.Clock()
    game = Minesweeper(board_size, mines)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                game.handle_event(event)
        game.update_timer()
        screen.fill((200, 200, 200))
        game.draw(screen)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
