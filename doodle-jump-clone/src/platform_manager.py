import pygame
import random

class PlatformManager:
    def __init__(self, width, height, player_rect=None):
        self.platforms = []
        # First platform just below the player
        if player_rect:
            self.platforms.append(pygame.Rect(player_rect.x, player_rect.y + player_rect.height + 5, 60, 10))
        # Remaining platforms
        for i in range(6):
            self.platforms.append(
                pygame.Rect(random.randint(0, width - 60), height - (i + 1) * 100, 60, 10)
            )
        self.width = width
        self.height = height

    def update(self, player):
        offset = 0
        if player.rect.y < self.height // 2:
            offset = self.height // 2 - player.rect.y
            player.rect.y = self.height // 2
            for plat in self.platforms:
                plat.y += offset
        self.platforms = [plat for plat in self.platforms if plat.y < self.height]
        while len(self.platforms) < 7:
            new_y = self.platforms[-1].y - 100
            self.platforms.append(
                pygame.Rect(random.randint(0, self.width - 60), new_y, 60, 10)
            )
        return offset

    def draw(self, screen):
        for plat in self.platforms:
            pygame.draw.rect(screen, (200, 200, 0), plat)
