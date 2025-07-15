import pygame


class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.vel_y = 0
        self.max_height = y
        self.total_ascended = 0

    def update(self, keys, platforms, offset=0):
        self.vel_y += 0.5
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        self.rect.y += int(self.vel_y)
        for plat in platforms.platforms:
            if self.rect.colliderect(plat) and self.vel_y > 0:
                self.vel_y = -13
        self.max_height = min(self.max_height, self.rect.y)
        self.total_ascended += offset

    def get_score(self):
        return self.total_ascended

    def get_height(self):
        # HEIGHT should be passed as a parameter
        raise NotImplementedError("get_height should be called with HEIGHT as a parameter, or refactored out if not needed.")

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 200, 0), self.rect)

    def is_game_over(self, screen_height):
        return self.rect.y > screen_height
