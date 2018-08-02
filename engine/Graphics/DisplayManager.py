import pygame
from engine.Objects import PlayerObject
from engine.Graphics import GameCamera
from engine.Objects import Platform

class DisplayManager:
    """
    Class to manage the whole game
    Manages the pygame screen rendering and main game loop
    """

    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()
        self.fps = 70
        self.done = False
        self.current_time = 0.0
        self.pressed_keys = []
        self.player = PlayerObject.PlayerObject("shahar", 20, -200, color=(255, 0, 0))
        self.camera = GameCamera.GameCamera(offset_x=0, offset_y=0, dt=0.20, player=self.player)
        self.platforms = pygame.sprite.Group(Platform.Platform(-100, 100, 250, 100))
        self.platforms.add(Platform.Platform(150, 250, 250, 100))

    def check_event(self):
        """
        Check all the events and update everything correspondingly
        :return: None
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                self.pressed_keys = pygame.key.get_pressed()
            elif event.type == pygame.KEYUP:
                self.pressed_keys = pygame.key.get_pressed()

    def start(self):
        """
        Start game loop
        :return: None
        """
        while not self.done:
            self.check_event()
            self.blit_game()
            self.player.update(self.pressed_keys, self.platforms)
            self.camera.update()
            self.clock.tick(self.fps)
            pygame.display.set_caption("{} - {:.2f} FPS".format("Bonk.IO", self.clock.get_fps()))
            pygame.display.flip()

    def blit_game(self):
        """
        Render every object in game
        :return: None
        """
        self.screen.fill((0, 0, 0))
        for platform in self.platforms.sprites():
            platform.render(self.screen, self.camera)

        self.player.render(self.screen, self.camera)
