import sys
import pygame
from player import Player
from platform_manager import PlatformManager
from hud import draw_hud
from events import handle_quit_events
from menu import show_main_menu, show_game_over
from init_utils import init_pygame, WIDTH, HEIGHT
FPS = 60

def main():
    screen, clock = init_pygame()
    if not show_main_menu(screen):
        pygame.quit()
        sys.exit()
    while True:
        player = Player(WIDTH // 2, HEIGHT - 100)
        platforms = PlatformManager(WIDTH, HEIGHT, player.rect)
        score = 0
        running = True
        while running:
            clock.tick(FPS)
            if handle_quit_events():
                return
            keys = pygame.key.get_pressed()
            offset = platforms.update(player)
            player.update(keys, platforms, offset)
            score = player.get_score()
            screen.fill((135, 206, 250))
            platforms.draw(screen)
            player.draw(screen)
            draw_hud(screen, score, clock)
            pygame.display.flip()
            if player.is_game_over(HEIGHT):
                running = False
        restart = show_game_over(screen, score)
        if not restart:
            break
    pygame.quit()


if __name__ == "__main__":
    main()
