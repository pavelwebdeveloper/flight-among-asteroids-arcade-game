# Imports
import arcade
import random
import math
from asteroidSprite import AsteroidSprite
from constants import SCALING



class SpaceFlight(arcade.Window):
    """Space Shooter side scroller game
    Player starts on the left, enemies appear on the right
    Player can move anywhere, but not off screen
    Enemies fly to the left at variable speed
    Collisions end the game
    """

    """Space Flight Among Asteroids game
    Player starts on the center and moves along a road
    Player can move within the road, but not off road
    Asteroids appear on the road at variable speed
    Collisions end the game
    """

    def __init__(self, width, height, title):
        """Initialize the game
        """
        super().__init__(width, height, title)

        # Set up the empty sprite lists
        self.flying_asteroids = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()

        



    def setup(self):
        """Get the game ready to play
        """

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

        # Unpause the game
        self.paused = False

        # Spawn a new enemy every 0.25 seconds
        arcade.schedule(self.add_flying_asteroid, 0.25)

        # Set up the planet
        #self.planet = arcade.Sprite("images/planet03.png", SCALING)
        #self.planet.center_x = self.width * 1.8
        #self.planet.bottom = -500
        #self.planet_rotation_speed = 0.2 # degrees per frame
        #self.all_sprites.append(self.planet)

        self.static_asteroid = arcade.Sprite("images/meteorGrey_big4.png", SCALING/2)
        self.static_asteroid.center_x = self.width // 2
        self.static_asteroid.center_y = self.height // 2
        self.all_sprites.append(self.static_asteroid)

        # Set up the player
        self.player = arcade.Sprite("images/playerShip1_green.png", SCALING/4)
        self.player.center_x = self.width // 2
        self.player.bottom = 80
        self.all_sprites.append(self.player)


    def add_flying_asteroid(self, delta_time: float):
        """Adds a new asteroid to the screen

        Arguments:
            delta_time {float} -- How much time has passed since the last call
        """

        # First, create the new asteroid sprite
        flying_asteroid = AsteroidSprite("images/meteorGrey_tiny2.png", SCALING)

        # Set its position to a random height and off screen right
        flying_asteroid.left = random.randint(10, self.width - 10)
        flying_asteroid.top = random.randint(self.height, self.height + 80)

        # Set its speed to a random speed heading left
        flying_asteroid.velocity = (0, random.randint(-20, -5))

        # Add it to the enemies list
        self.flying_asteroids.append(flying_asteroid)
        self.all_sprites.append(flying_asteroid)

    def on_update(self, delta_time: float):
        """
            Update the positions and statuses of all game objects
        """

        if self.paused:
            return
        
        # Checking if anything the space ship collided with any asteroid
        if self.player.collides_with_list(self.flying_asteroids) or self.player.collides_with_sprite(self.static_asteroid):
            print("Colliding with planet!")
            self.paused = not self.paused
            arcade.unschedule(self.add_flying_asteroid)
            

        # Update everything
        self.all_sprites.update()

        # Check if space ship is within the screen
        if self.player.top > self.height:
            self.player.top = self.height
        if self.player.right > self.width:
            self.player.right = self.width
        if self.player.bottom < 0:
            self.player.bottom = 0
        if self.player.left < 0:
            self.player.left = 0

        # Rotating the planet
        #self.planet.angle -= self.planet_rotation_speed

    def on_draw(self):
        """
            Draw all game objects
        """
        self.clear()
        self.all_sprites.draw()

    def on_key_press(self, symbol, modifiers):
        """
            Handle user keyboard input 
            Q: Quit the game
            P: Pause/Unpause the game
            I/J/K/L: Move Up, Left, Down, Right
            Arrows: Move Up, Left, Down, Right
        """
        if symbol == arcade.key.Q:
            # Quit immediately
            arcade.close_window()

        if symbol == arcade.key.P:
            # Quit immediately
            self.paused = not self.paused

        if symbol == arcade.key.P:
            # Quit immediately
            self.paused = not self.paused

        if symbol == arcade.key.I or symbol == arcade.key.UP:
            self.player.change_y = 5  

        if symbol == arcade.key.K or symbol == arcade.key.DOWN:
            self.player.change_y = -5  

        if symbol == arcade.key.J or symbol == arcade.key.LEFT:
            self.player.change_x = -5  

        if symbol == arcade.key.L or symbol == arcade.key.RIGHT:
            self.player.change_x = 5 
    
    def on_key_release(self, symbol, modifiers):
        """
            Stop movement when movement keys are realeased
        """

        if(
            symbol == arcade.key.I
            or symbol == arcade.key.K
            or symbol == arcade.key.UP
            or symbol == arcade.key.DOWN
        ):
            self.player.change_y = 0

        if(
            symbol == arcade.key.J
            or symbol == arcade.key.L
            or symbol == arcade.key.LEFT
            or symbol == arcade.key.RIGHT
        ):
            self.player.change_x = 0
        