# Imports
import arcade

class AsteroidSprite(arcade.Sprite):
    """Base class for all asteroid sprites
    Asteroid sprites include asteroids
    """

    def update(self, delta_time: float = 1/60):
        """Update the position of the sprite
        When it moves off screen to the bottom, remove it
        """

        # Move the sprite
        super().update()

        # Remove if off the screen
        if self.bottom < 0:
            self.remove_from_sprite_lists()