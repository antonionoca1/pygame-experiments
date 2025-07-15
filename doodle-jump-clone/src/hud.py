import pygame

def draw_hud(screen, score, clock):
    font = pygame.font.Font(None, 24)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    fps_text = font.render(f"FPS: {clock.get_fps():.1f}", True, (0, 0, 0))
    screen.blit(fps_text, (10, 40))
