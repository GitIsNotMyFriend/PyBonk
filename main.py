from engine.Graphics.DisplayManager import *
from engine import Constants

def main():
    # Initialize game
    pygame.init()
    pygame.event.set_allowed([pygame.KEYDOWN, pygame.KEYUP])
    pygame.display.set_caption("Bonk.IO")
    pygame.display.set_mode([Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT])

    # Start game loop
    dm = DisplayManager()
    dm.start()


if __name__ == '__main__':
    main()
