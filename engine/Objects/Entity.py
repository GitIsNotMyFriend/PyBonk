import pygame
from abc import ABC, abstractmethod


class Entity(pygame.sprite.Sprite, ABC):
    """
    Abstract entity class
    """
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y

    @abstractmethod
    def render(self, offset_x, offset_y):
        pass
