import pygame

def handle_quit_events():
    """Return True if ESC or QUIT event is detected."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return True
    return False
