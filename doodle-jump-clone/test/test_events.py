import unittest
import pygame
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from events import handle_quit_events

class TestEvents(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((100, 100))

    def tearDown(self):
        pygame.quit()

    def test_handle_quit_events_quit(self):
        quit_event = pygame.event.Event(pygame.QUIT)
        pygame.event.post(quit_event)
        self.assertTrue(handle_quit_events())

    def test_handle_quit_events_escape(self):
        esc_event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_ESCAPE)
        pygame.event.post(esc_event)
        self.assertTrue(handle_quit_events())

    def test_handle_quit_events_none(self):
        # Clear event queue
        pygame.event.clear()
        self.assertFalse(handle_quit_events())

if __name__ == "__main__":
    unittest.main()
