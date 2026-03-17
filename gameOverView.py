import arcade

class GameOverView(arcade.View):

    def on_show_view(self):
        self.background = arcade.load_texture("images/Background-2.png")

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
            "Game Over",
            self.window.width / 2,
            self.window.height / 2 + 40,
            arcade.color.RED,
            50,
            anchor_x="center"
        )

        arcade.draw_text(
            "Press ENTER to return to Menu or Q to quit the game",
            self.window.width / 2,
            self.window.height / 2 - 40,
            arcade.color.WHITE,
            20,
            anchor_x="center"
        )

    def on_key_press(self, symbol, modifiers):

        if symbol == arcade.key.ENTER:
            from menuView import MenuView

            menu = MenuView()
            self.window.show_view(menu)
        
        if symbol == arcade.key.Q:
            # Quit immediately
            arcade.close_window()