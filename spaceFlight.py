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
        arcade.set_background_color(arcade.color.BLACK)

        # Spawn a new enemy every 0.25 seconds
        arcade.schedule(self.add_obstacle, 0.25)

        # Unpause the game
        self.paused = False

        # Set up the planet
        self.planet = arcade.Sprite("images/planet03.png", SCALING)
        self.planet.center_x = self.width * 1.8
        self.planet.bottom = -500
        self.all_sprites.append(self.planet)

        # Set up the player
        self.player = arcade.Sprite("images/playerShip1_green.png", SCALING/4)
        self.player.center_x = self.width // 2
        self.player.bottom = 80
        self.all_sprites.append(self.player)


    def add_obstacle(self, delta_time: float):
        """Adds a new obstacle to the screen

        Arguments:
            delta_time {float} -- How much time has passed since the last call
        """

        # First, create the new obstacle sprite
        obstacle = ObstacleSprite("images/meteorGrey_tiny2.png", SCALING)

        # Set its position to a random height and off screen right
        obstacle.left = random.randint(10, self.width - 10)
        obstacle.top = random.randint(self.height, self.height + 80)

        # Set its speed to a random speed heading left
        obstacle.velocity = (0, random.randint(-20, -5))

        # Add it to the enemies list
        self.obstacles_list.append(obstacle)
        self.all_sprites.append(obstacle)

    def on_update(self, delta_time: float):
        """
            Update the positions and statuses of all game objects
        """

        if self.paused:
            return

        # Update everything
        self.all_sprites.update()

        # Check if player is on the road
        if self.player.top > self.height:
            self.player.top = self.height
        if self.player.right > self.width:
            self.player.right = self.width
        if self.player.bottom < 0:
            self.player.bottom = 0
        if self.player.left < 0:
            self.player.left = 0

    def on_draw(self):
        """
            Draw all game objects
        """
        self.clear()
        self.all_sprites.draw()
        