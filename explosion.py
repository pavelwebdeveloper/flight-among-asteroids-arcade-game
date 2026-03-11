import arcade

class Explosion(arcade.Sprite):
    def __init__(self, texture_list):
        super().__init__()

        self.textures = texture_list
        self.current_texture = 0
        self.texture = self.textures[0]

    def update(self, delta_time=0):
        self.current_texture += 0

        if self.current_texture < len(self.textures):
            self.texture = self.textures[self.current_texture]
        else:
            self.remove_from_sprite_lists()
