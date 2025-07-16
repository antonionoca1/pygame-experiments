import unittest
import pygame
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.player = Player()

    def test_accelerate(self):
        self.player.speed = 0
        self.player.accelerate()
        self.assertEqual(self.player.speed, 1)
        self.player.accelerate(30)
        self.assertEqual(self.player.speed, 20)  # capped at 20

    def test_brake(self):
        self.player.speed = 10
        self.player.brake()
        self.assertEqual(self.player.speed, 9)
        self.player.brake(20)
        self.assertEqual(self.player.speed, 0)  # capped at 0

    def test_steer(self):
        self.player.steer(-1)
        self.assertEqual(self.player.direction, -1)
        self.player.steer(1)
        self.assertEqual(self.player.direction, 1)
        self.player.steer(0)
        self.assertEqual(self.player.direction, 0)

    def test_update_position(self):
        self.player.x = 400
        self.player.y = 500
        self.player.direction = 1
        self.player.speed = 5
        self.player.update()
        self.assertEqual(self.player.x, 405)
        self.assertEqual(self.player.y, 495)
        self.player.x = -10
        self.player.y = -10
        self.player.update()
        self.assertGreaterEqual(self.player.x, 0)
        self.assertGreaterEqual(self.player.y, 0)
        self.player.x = 800
        self.player.y = 600
        self.player.update()
        self.assertLessEqual(self.player.x, 760)
        self.assertLessEqual(self.player.y, 520)

    def tearDown(self):
        pygame.quit()
