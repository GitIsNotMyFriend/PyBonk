from engine.Objects import PlayerObject
from engine.Physics import MathFuncs

from engine import Constants


class GameCamera:
    """
    Game camera to show different parts of the game for the player
    """
    def __init__(self, offset_x: float, offset_y: float, player: PlayerObject, dt: float):
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.player = player
        self.dt = dt

        self.x_pos = self.player.get_x() - self.offset_x - Constants.WINDOW_WIDTH / 2 + player.image.get_width()
        self.y_pos = self.player.get_y() - self.offset_y - Constants.WINDOW_HEIGHT / 2 + player.image.get_height()

    def update(self):
        """
        Update the camera position to center player to screen
        :return:
        """
        self.desired_x_pos = self.player.get_x() - self.offset_x - Constants.WINDOW_WIDTH / 2 + 10
        self.desired_y_pos = self.player.get_y() - self.offset_y - Constants.WINDOW_HEIGHT / 2 + 10

        self.x_pos = MathFuncs.lerp(self.x_pos, self.desired_x_pos, self.dt)
        self.y_pos = MathFuncs.lerp(self.y_pos, self.desired_y_pos, self.dt)
