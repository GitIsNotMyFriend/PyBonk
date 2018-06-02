import pygame
from engine.Objects import PlayerObject
from engine.Graphics import GameCamera


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
        self.player = PlayerObject.PlayerObject("shahar", 10, 10, color=(255, 0, 0))
        self.camera = GameCamera.GameCamera(offset_x=0, offset_y=0, dt=1, player=self.player)

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
            self.player.update(self.pressed_keys)
            self.camera.update()
            self.clock.tick(self.fps)
            pygame.display.set_caption("{} - {:.2f} FPS".format("Game Project", self.clock.get_fps()))
            pygame.display.flip()

    def blit_game(self):
        """
        Render every object in game
        :return: None
        """
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, (255, 255, 255), [200 - self.camera.x_pos, 10 - self.camera.y_pos, 100, 20])
        self.player.render(self.screen, self.camera)
