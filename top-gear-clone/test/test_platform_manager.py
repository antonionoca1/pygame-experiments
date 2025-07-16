import unittest
import pygame
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from platform_manager import PlatformManager

class TestPlatformManager(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.pm = PlatformManager()
        self.pm.generate_strips(screen_width=800, screen_height=600)

    def test_generate_strips(self):
        self.pm.generate_strips(num_strips=10, screen_width=800, screen_height=600)
        self.assertEqual(len(self.pm.strips), 10)
        y0, w0 = self.pm.strips[0]
        y9, w9 = self.pm.strips[-1]
        self.assertTrue(w9 > w0)

    def test_update(self):
        strips_before = list(self.pm.strips)
        self.pm.update(10)
        for (y_before, _), (y_after, _) in zip(strips_before, self.pm.strips):
            self.assertEqual(y_after, y_before + 10 if y_before + 10 <= self.pm.screen_height else self.pm.horizon_y)

    def tearDown(self):
        pygame.quit()
