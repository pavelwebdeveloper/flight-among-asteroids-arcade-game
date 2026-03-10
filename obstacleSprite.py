# Imports
import arcade

class ObstacleSprite(arcade.Sprite):
    """Base class for all obstacle sprites
    Obstacle sprites include obstacles
    """

    def update(self):
        """Update the position of the sprite
        When it moves off screen to the bottom, remove it
        """

        # Move the sprite
        super().update()

        # Remove if off the screen
        if self.bottom < 0:
            self.remove_from_sprite_lists()