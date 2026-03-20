# Basic arcade spacecraft flight among asteroids game

# Imports
import arcade
import random
from menuView import MenuView
from gameView import GameView
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE, SCALING

"""Space Flight Among Asteroids game
    Spacecraft starts on the bottom center of the game view
    The spacecraft can move right, left, forward, backward
    Many asteroids appear from the top of the game view at variable speeds
    And fly to the bottom of the game view
    There is one big asteroid that stayes in the middle of the game view all the time
    Collision of the spacecraft with any of the asteroids ends the game
    """

if __name__ == "__main__":
    # Generate a menu view
    window = arcade.Window(
        int(SCREEN_WIDTH * SCALING), int(SCREEN_HEIGHT * SCALING), SCREEN_TITLE
    )
    menu = MenuView()
    window.show_view(menu)

    # Run the game
    arcade.run()
