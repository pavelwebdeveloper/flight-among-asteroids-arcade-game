import arcade
from gameView import GameView
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE, SCALING

class MenuView(arcade.View):

    def on_show_view(self):
        #arcade.set_background_color(arcade.color.BLACK)

        self.background = arcade.load_texture("images/Background-3.png")

    def on_draw(self):
        self.clear()

        arcade.draw_texture_rect(
            self.background,
            arcade.XYWH(
                self.window.width // 2,
                self.window.height // 2,
                self.window.width,
                self.window.height
            )
        )

        arcade.draw_text(
            "Flight Among Asteroids",
            self.window.width / 2,
            self.window.height / 2 + 80,
            arcade.color.WHITE,
            40,
            anchor_x="center"
        )

        arcade.draw_text(
            "Press ENTER to start or Q to exit",
            self.window.width / 2,
            self.window.height / 2 - 20,
            arcade.color.WHITE,
            20,
            anchor_x="center"
        )

    def on_key_press(self, symbol, modifiers):

        if symbol == arcade.key.ENTER:
            #game_view = SpaceFlight(
                #int(SCREEN_WIDTH * SCALING), int(SCREEN_HEIGHT * SCALING), SCREEN_TITLE
            #)
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)

        if symbol == arcade.key.Q:
            # Quit immediately
            arcade.close_window()