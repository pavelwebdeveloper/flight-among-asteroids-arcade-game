# Basic arcade car ride with obstacles

# Imports
import arcade
import random
from spaceFlight import SpaceFlight
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE, SCALING


if __name__ == "__main__":
    # Create a new Space Flight window
    car_ride_game = SpaceFlight(
        int(SCREEN_WIDTH * SCALING), int(SCREEN_HEIGHT * SCALING), SCREEN_TITLE
    )
    # Setu to play
    car_ride_game.setup()

    # Run the game
    arcade.run()
