import pygame

def create_game_window(width=800, height=600):
    pygame.init()
    return pygame.display.set_mode((width, height))

def initialize_display(width=800, height=600):
    pygame.display.set_caption("Top Gear SNES Clone")
    screen = pygame.display.set_mode((width, height))
    return screen


from player import Player
from platform_manager import PlatformManager

def main():
    screen = initialize_display()
    clock = pygame.time.Clock()
    player = Player()
    platform_manager = PlatformManager()
    platform_manager.generate_strips(screen_height=screen.get_height(), screen_width=screen.get_width())
    running = True
    while running:
        running = handle_quit_event()
        player.handle_input()
        player.update()
        platform_manager.update(player.speed)
        screen.fill((0, 0, 0))
        # Draw road and roadside objects
        platform_manager.draw(screen)
        # Draw player car
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
