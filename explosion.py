import arcade

class Explosion(arcade.Sprite):
    def __init__(self, texture_list):
        super().__init__()

        self.textures = texture_list
        self.current_texture = 0
        self.texture = self.textures[0]

        self.frame_timer = 0
        self.frame_delay = 6 # number of updates before changing frame

    def update(self, delta_time=0):

        self.frame_timer += 1

        if self.frame_timer >= self.frame_delay:
            self.frame_timer = 0
            self.current_texture += 1

            if self.current_texture < len(self.textures):
                self.texture = self.textures[self.current_texture]
            else:
                self.remove_from_sprite_lists()
