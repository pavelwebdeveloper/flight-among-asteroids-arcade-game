import arcade

class Explosion(arcade.Sprite):
    def __init__(self, texture_list):
        super().__init__()

        self.textures = texture_list
        # setting the current image to the first image from the array of images
        self.current_texture = 0
        # displaying the first image from the array of images
        self.texture = self.textures[0]

        self.frame_timer = 0
        # setting the speed of changing of images to 6
        self.frame_delay = 6 # number of updates before changing frame

    def update(self, delta_time=0):

        self.frame_timer += 1

        # set to the next image only when frame_delay value is reached
        if self.frame_timer >= self.frame_delay:
            self.frame_timer = 0
            self.current_texture += 1

            # if the array of images is not over yet then continue to display the next image in the array of images
            if self.current_texture < len(self.textures):
                self.texture = self.textures[self.current_texture]
            else:
                self.remove_from_sprite_lists() # if the array of images is over then remove the images from the game view
