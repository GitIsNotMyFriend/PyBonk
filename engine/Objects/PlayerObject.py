from engine.Graphics import GameCamera
from engine.Physics import MathFuncs
import pygame


class PlayerObject():
    """
    An Object for a player
    """
    def __init__(self, name: str, x: float, y: float, color: tuple):
        self.name = name
        self.color = color

        self.image = pygame.Surface((11*2, 11*2), pygame.SRCALPHA).convert_alpha()
        self.draw = pygame.draw.circle(self.image, self.color, (10, 10), 10)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.velocity_x = 0
        self.velocity_y = 0

        self.goal_velocity_x = 0
        self.goal_velocity_y = 0

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def render(self, screen: pygame.Surface, camera: GameCamera):
        screen.blit(self.image, (self.rect.x - camera.x_pos, self.rect.y - camera.y_pos))

    def update(self, keys) -> None:
        """
        Updates the player state
        :param keys:
        :type keys: List[pygame.key]
        :return: None
        """
        # reset goals
        self.goal_velocity_x = 0
        self.goal_velocity_y = 0

        if keys:
            if keys[pygame.K_w]:
                self.goal_velocity_y = -12.0
            if keys[pygame.K_d]:
                self.goal_velocity_x = 12.0
            if keys[pygame.K_s]:
                self.goal_velocity_y = 12.0
            if keys[pygame.K_a]:
                self.goal_velocity_x = -12.0

        # still working on smoothing movement using interpolation
        self.velocity_x = MathFuncs.lerp(self.velocity_x, self.goal_velocity_x, 0.05)
        self.velocity_y = MathFuncs.lerp(self.velocity_y, self.goal_velocity_y, 0.05)

        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

