import arcade
from gameView import GameView
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE, SCALING

class MenuView(arcade.View):

    def on_show_view(self):
        # adding an image to the background for the menu view
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

        # adding text to the menu view
        arcade.draw_text(
            "Flight Among Asteroids",
            self.window.width / 2,
            self.window.height / 2 + 80,
            arcade.color.WHITE,
            40,
            anchor_x="center"
        )

        # adding another line of text to the menu view
        arcade.draw_text(
            "Press ENTER to start or Q to exit",
            self.window.width / 2,
            self.window.height / 2 - 20,
            arcade.color.WHITE,
            20,
            anchor_x="center"
        )

    def on_key_press(self, symbol, modifiers):

        # if a user presses "Enter" key then the game view is opened and the game begins 
        if symbol == arcade.key.ENTER:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)

        # if a user presses "Q" key then the game finishes
        if symbol == arcade.key.Q:
            # Quit immediately
            arcade.close_window()