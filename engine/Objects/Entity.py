import pygame
from engine.Graphics import GameCamera
from abc import ABC, abstractmethod


class Entity(pygame.sprite.Sprite, ABC):
    """
    Abstract entity class
    """
    def __init__(self, x: float, y: float, width: float, height: float):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    @abstractmethod
    def render(self, screen: pygame.Surface, camera: GameCamera):
        pass
