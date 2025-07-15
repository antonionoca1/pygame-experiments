import pygame
from events import handle_quit_events

WIDTH, HEIGHT = 400, 600

def show_main_menu(screen):
    font = pygame.font.Font(None, 32)
    title_font = pygame.font.Font(None, 52)
    title_text = title_font.render("Doodle Jump Clone", True, (0, 0, 0))
    menu_text = font.render("Press Enter to Start", True, (0, 0, 0))
    screen.fill((255, 255, 255))
    screen.blit(title_text, (WIDTH // 10, HEIGHT // 2 - 90))
    screen.blit(menu_text, (WIDTH // 4, HEIGHT // 2 - 24))
    pygame.display.flip()
    while True:
        if handle_quit_events():
            return False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            return True

def show_game_over(screen, score):
    font = pygame.font.Font(None, 48)
    over_text = font.render("Game Over", True, (200, 0, 0))
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    restart_text = font.render("Press R to Restart", True, (0, 0, 0))
    screen.fill((255, 255, 255))
    screen.blit(over_text, (100, HEIGHT // 2 - 48))
    screen.blit(score_text, (100, HEIGHT // 2))
    screen.blit(restart_text, (60, HEIGHT // 2 + 48))
    pygame.display.flip()
    while True:
        if handle_quit_events():
            return False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            return True
