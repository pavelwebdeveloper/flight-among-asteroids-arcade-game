# Basic arcade spacecraft flight among asteroids game

# Imports
import arcade
import random
from menuView import MenuView
from gameView import GameView
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE, SCALING


if __name__ == "__main__":
    # Create a new Space Flight game
    #spacecraft_flight_among_asteroids_game = SpaceFlight(
    #    int(SCREEN_WIDTH * SCALING), int(SCREEN_HEIGHT * SCALING), SCREEN_TITLE
    #)
    # Set up to play
    #spacecraft_flight_among_asteroids_game.setup()

    window = arcade.Window(
        int(SCREEN_WIDTH * SCALING), int(SCREEN_HEIGHT * SCALING), SCREEN_TITLE
    )
    menu = MenuView()
    window.show_view(menu)

    # Run the game
    arcade.run()
