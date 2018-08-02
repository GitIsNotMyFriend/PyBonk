from engine.Graphics import GameCamera
from engine.Physics import MathFuncs
from engine.Objects import Entity
from typing import List

import pygame


class PlayerObject:
    """
    An Object for a player
    """
    MAX_FREEFALL_SPEED = 55

    def __init__(self, name: str, x: float, y: float, color: tuple):
        self.name = name
        self.color = color

        self.image = pygame.Surface((11*2, 11*2), pygame.SRCALPHA).convert_alpha()
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.jumping = False
        self.in_air = False
        self.velocity_x = 0
        self.velocity_y = 0

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def render(self, screen: pygame.Surface, camera: GameCamera):
        screen.blit(self.image, (self.rect.x - camera.x_pos, self.rect.y - camera.y_pos))

    def update(self, keys, sprites) -> None:
        """
        Updates the player state
        :param keys:
        :type keys: List[pygame.key]
        :return: None
        """
        # reset goals
        goal_velocity_x = 0

        if keys:
            if keys[pygame.K_w] and not self.jumping:
                self.velocity_y = -20.0
                self.jumping = True
                self.in_air = True
            if keys[pygame.K_d]:
                goal_velocity_x = 10.0
            if keys[pygame.K_a]:
                goal_velocity_x = -10.0

        # still working on smoothing movement using interpolation
        if not (-1 < self.velocity_x < 1 and goal_velocity_x == 0):
            self.velocity_x = MathFuncs.lerp(self.velocity_x, goal_velocity_x, 0.05)
        else:
            self.velocity_x = 0

        if self.in_air:
            if self.velocity_y < PlayerObject.MAX_FREEFALL_SPEED:
                self.velocity_y += 1
        else:
            self.jumping = False
            self.velocity_y = 0

        self.rect.x += self.velocity_x

        hit_list = pygame.sprite.spritecollide(self, sprites, False)

        for hit in hit_list:
            if self.velocity_x > 0:
                self.rect.right = hit.rect.left
            else:
                self.rect.left = hit.rect.right

        self.rect.y += self.velocity_y

        hit_list = pygame.sprite.spritecollide(self, sprites, False)
        if not hit_list:
            self.in_air = True

            if self.rect.y > 1000:
                self.rect.y = -200
                self.rect.x = 0
                self.velocity_y = 0
        else:
            for hit in hit_list:

                if self.velocity_y > 0:
                    self.in_air = False
                    self.rect.bottom = hit.rect.top
                else:
                    self.rect.top = hit.rect.bottom
