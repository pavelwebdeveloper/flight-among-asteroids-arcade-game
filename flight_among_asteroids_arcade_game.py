# Basic arcade car ride with obstacles

# Imports
import arcade
import random
from spaceFlight import SpaceFlight
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE, SCALING


if __name__ == "__main__":
    # Create a new Space Flight game
    spacecraft_flight_among_asteroids_game = SpaceFlight(
        int(SCREEN_WIDTH * SCALING), int(SCREEN_HEIGHT * SCALING), SCREEN_TITLE
    )
    # Set up to play
    spacecraft_flight_among_asteroids_game.setup()

    # Run the game
    arcade.run()
