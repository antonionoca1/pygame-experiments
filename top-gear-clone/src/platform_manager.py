import pygame

class PlatformManager:
    def __init__(self, horizon_y=100, road_color=(80, 80, 80)):
        self.horizon_y = horizon_y
        self.road_color = road_color
        self.strips = []  # List of road strips for perspective

    def generate_strips(self, num_strips=30, screen_width=800, screen_height=600):
        self.strips = []
        self.num_strips = num_strips
        self.screen_height = screen_height
        self.screen_width = screen_width
        for i in range(num_strips):
            y = self.horizon_y + i * ((screen_height - self.horizon_y) // num_strips)
            width = int(screen_width * (0.2 + 0.8 * (i / num_strips)))
            self.strips.append((y, width))

    def update(self, player_speed):
        # Move strips downward based on player speed
        new_strips = []
        for i, (y, width) in enumerate(self.strips):
            y += player_speed
            # If strip goes off screen, reset to horizon
            if y > self.screen_height:
                y = self.horizon_y
            new_strips.append((y, width))
        self.strips = new_strips

    def draw(self, screen):
        center_x = screen.get_width() // 2
        for i, (y, width) in enumerate(self.strips):
            rect = pygame.Rect(center_x - width // 2, y, width, 8)
            pygame.draw.rect(screen, self.road_color, rect)
            # Draw simple trees and signposts as colored circles/rects
            if i % 5 == 0:
                tree_x = center_x - width // 2 - 20
                pygame.draw.circle(screen, (34, 139, 34), (tree_x, y + 4), 10)
            if i % 7 == 0:
                sign_x = center_x + width // 2 + 10
                pygame.draw.rect(screen, (255, 255, 0), (sign_x, y, 8, 16))
