# Imports
import arcade
import random
from obstacleSprite import ObstacleSprite
from constants import SCALING



class CarRide(arcade.Window):
    """Space Shooter side scroller game
    Player starts on the left, enemies appear on the right
    Player can move anywhere, but not off screen
    Enemies fly to the left at variable speed
    Collisions end the game
    """

    """Car Ride game
    Player starts on the center and moves along a road
    Player can move within the road, but not off road
    Obstacles appear on the road at variable speed
    Collisions end the game
    """

    def __init__(self, width, height, title):
        """Initialize the game
        """
        super().__init__(width, height, title)

        # Set up the empty sprite lists
        self.obstacles_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()

    def setup(self):
        """Get the game ready to play
        """

        # Set the background color
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Set up the player
        self.player = arcade.Sprite("images/jet.png", SCALING)
        self.player.center_x = self.width / 2
        self.player.bottom = 10
        self.all_sprites.append(self.player)

        # Spawn a new enemy every 0.25 seconds
        arcade.schedule(self.add_obstacle, 0.25)

    def add_obstacle(self, delta_time: float):
        """Adds a new obstacle to the screen

        Arguments:
            delta_time {float} -- How much time has passed since the last call
        """

        # First, create the new obstacle sprite
        obstacle = ObstacleSprite("images/missile.png", SCALING)

        # Set its position to a random height and off screen right
        obstacle.left = random.randint(10, self.width - 10)
        obstacle.top = random.randint(self.height, self.height + 80)

        # Set its speed to a random speed heading left
        obstacle.velocity = (0, random.randint(-20, -5))

        # Add it to the enemies list
        self.obstacles_list.append(obstacle)
        self.all_sprites.append(obstacle)