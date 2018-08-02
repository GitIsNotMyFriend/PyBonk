import pygame
from engine.Objects import Entity
from engine.Graphics import GameCamera


class Platform(Entity.Entity):

    def __init__(self, x: float, y: float, width: float, height: float):
        super(Platform, self).__init__(x, y, width, height)
        self.draw = pygame.draw.rect(self.image, (255, 255, 255), self.image.get_rect())

    def render(self, screen: pygame.Surface, camera: GameCamera):
        screen.blit(self.image, (self.rect.x - camera.x_pos, self.rect.y - camera.y_pos))
