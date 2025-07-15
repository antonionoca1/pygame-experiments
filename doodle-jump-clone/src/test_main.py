import unittest
import pygame
from main import init_pygame

# Mock Player class for testing
class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
    def is_game_over(self, screen_height):
        return self.rect.y > screen_height

# Mock PlatformManager class for testing
class PlatformManager:
    def __init__(self, screen_width, screen_height):
        self.platforms = [pygame.Rect(0, i * 80, 60, 10) for i in range(7)]

class TestMain(unittest.TestCase):
    def test_init_pygame(self):
        screen, clock = init_pygame()
        self.assertIsInstance(screen, pygame.Surface)
        self.assertIsInstance(clock, pygame.time.Clock)

    def test_player(self):
        player = Player(100, 500)
        self.assertEqual(player.rect.x, 100)
        self.assertEqual(player.rect.y, 500)
        self.assertFalse(player.is_game_over(600))
        player.rect.y = 601
        self.assertTrue(player.is_game_over(600))

    def test_platform_manager(self):
        pm = PlatformManager(400, 600)
        self.assertEqual(len(pm.platforms), 7)
        for plat in pm.platforms:
            self.assertIsInstance(plat, pygame.Rect)

if __name__ == "__main__":
    unittest.main()
