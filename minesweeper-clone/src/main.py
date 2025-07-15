
import pygame
import sys
from .game import MinesweeperGame

BOARD_SIZES = [(9, 9), (16, 16), (30, 16)]
MINES_COUNT = [10, 40, 99]
CELL_SIZE = 32
MARGIN = 40

def main():
    pygame.init()
    board_size = BOARD_SIZES[0]
    mines = MINES_COUNT[0]
    width = board_size[0] * CELL_SIZE + MARGIN * 2
    height = board_size[1] * CELL_SIZE + MARGIN * 2 + 60
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Minesweeper')
    clock = pygame.time.Clock()
    game = MinesweeperGame(board_size, mines)

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
