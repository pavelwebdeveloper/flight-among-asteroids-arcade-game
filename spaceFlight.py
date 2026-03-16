# Imports
import arcade
import random
from asteroidSprite import AsteroidSprite
from explosion import Explosion
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

        # Set up the background image
        self.background = arcade.Sprite("images/purple.png", SCALING * 2.5)
        self.background.center_x = self.width // 2
        self.background.center_y = self.height // 2
        self.all_sprites.append(self.background)

        # Set the game to unpaused status
        self.paused = False

        # Spawn a new asteroid every 0.25 seconds
        arcade.schedule(self.add_flying_asteroid, 0.25)

        # Setting up sounds
        self.collision_sound = arcade.load_sound("sounds/Collision.wav");
        self.move_up_sound = arcade.load_sound("sounds/Rising_putter.wav");
        self.move_down_sound = arcade.load_sound("sounds/Falling_putter.wav");

        # Set up the planet
        self.planet = arcade.Sprite("images/planet03.png", SCALING*1.5)
        self.planet.center_x = self.width * 2.2
        self.planet.bottom = -1300
        self.planet_rotation_speed = 0.2 # Add rotation to the planet in degrees per frame
        self.all_sprites.append(self.planet)

        # Set up stationary asteroid
        self.static_asteroid = arcade.Sprite("images/meteorGrey_big4.png", SCALING/2)
        self.static_asteroid.center_x = self.width // 2
        self.static_asteroid.center_y = self.height // 2
        self.static_asteroid.change_angle = random.uniform(5,-5) # Add rotation to the stationary asteroid
        self.all_sprites.append(self.static_asteroid)

        # Set up the player
        self.player = arcade.Sprite("images/playerShip1_green.png", SCALING/4)
        self.player.center_x = self.width // 2
        self.player.bottom = 80
        self.all_sprites.append(self.player)

        # Set up explosion for spacecraft
        self.spacecraft_explosion_textures = []
        for i in range(1,9):
            texture = arcade.load_texture(f"images/explosion/explosion0{i}.png")
            self.spacecraft_explosion_textures.append(texture)

        # Set up explosion between asteroids
        self.asteroid_explosion_textures = []
        for i in range(1,3):
            texture = arcade.load_texture(f"images/explosion/scorch_0{i}.png")
            self.asteroid_explosion_textures.append(texture)


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

        # Set its speed to a random speed
        flying_asteroid.velocity = (0, random.randint(-20, -5))

        # Add rotation to the flying asteroid
        flying_asteroid.change_angle = random.uniform(-2,2)

        # Add it to the list of flying asteroids
        self.flying_asteroids.append(flying_asteroid)
        self.all_sprites.append(flying_asteroid)

    def on_update(self, delta_time: float):
        """
            Update the positions and statuses of all game objects
        """

        if self.paused:
            return
        
        # Checking if the space ship collided with any asteroid
        if self.player.collides_with_list(self.flying_asteroids) or self.player.collides_with_sprite(self.static_asteroid):

            arcade.play_sound(self.collision_sound)

            explosion = Explosion(self.spacecraft_explosion_textures)
            explosion.center_x = self.player.center_x
            explosion.center_y = self.player.center_y

            self.all_sprites.append(explosion)

            self.paused = True
            arcade.unschedule(self.add_flying_asteroid)

        # check for collisions between asteroids
        for asteroid in list(self.flying_asteroids):
            hit_list = arcade.check_for_collision_with_list(asteroid, self.flying_asteroids)

            for other in hit_list:
                if other is asteroid:
                    continue # skip oneself

                if asteroid.width == other.width:
                    #print("2 small asteroids collided !!!!!!!")
                    self._create_explosion_remove_small_asteroids(asteroid, other)

                    break
            
            if arcade.check_for_collision(asteroid, self.static_asteroid):
                    #print("samall asteroid collided with the big one !!!!!!!")
                    self._create_explosion_remove_small_asteroids(asteroid)

                    break

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
        self.planet.angle -= self.planet_rotation_speed

    def _create_explosion_remove_small_asteroids(self, first_small_asteroid, second_small_asteroid = None):

        arcade.play_sound(self.collision_sound)

        collision_x = first_small_asteroid.center_x
        collision_y = first_small_asteroid.center_y

        explosion = Explosion(self.asteroid_explosion_textures)
        explosion.center_x = collision_x
        explosion.center_y = collision_y

        self.all_sprites.append(explosion)

        first_small_asteroid.remove_from_sprite_lists()
        if second_small_asteroid is not None:
            second_small_asteroid.remove_from_sprite_lists()

        

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
            if self.paused == False:
                self.paused = True
                # Stop spawning a new asteroid every 0.25 seconds
                arcade.unschedule(self.add_flying_asteroid)
            else:
                # Resume spawning a new asteroid every 0.25 seconds
                arcade.schedule(self.add_flying_asteroid, 0.25)
                self.paused = False

        if symbol == arcade.key.I or symbol == arcade.key.UP:
            arcade.play_sound(self.move_up_sound)
            self.player.change_y = 5  

        if symbol == arcade.key.K or symbol == arcade.key.DOWN:
            arcade.play_sound(self.move_down_sound)
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
        