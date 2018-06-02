from engine.Graphics.DisplayManager import *


def main():
    # Initialize game
    pygame.init()
    pygame.event.set_allowed([pygame.KEYDOWN, pygame.KEYUP])
    pygame.display.set_caption("Game Project")
    pygame.display.set_mode([640, 480])

    # Start game loop
    dm = DisplayManager()
    dm.start()


if __name__ == '__main__':
    main()
