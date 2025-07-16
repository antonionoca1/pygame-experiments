import pygame

def create_game_window(width=800, height=600):
    pygame.init()
    return pygame.display.set_mode((width, height))

def initialize_display(width=800, height=600):
    pygame.display.set_caption("Top Gear SNES Clone")
    screen = pygame.display.set_mode((width, height))
    return screen

from player import Player

def main():
    screen = initialize_display()
    clock = pygame.time.Clock()
    player = Player()
    running = True
    while running:
        running = handle_quit_event()
        player.handle_input()
        player.update()
        screen.fill((0, 0, 0))
        player.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

def handle_quit_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

if __name__ == "__main__":
    main()
