from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton , MDFlatButton
from kivy.lang import Builder
from helpers import username_helper

class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Purple"
        button = MDRectangleFlatButton(
            text="Show",
            pos_hint={"center_x": 0.5, "center_y": 0.4},
        )
        self.username = Builder.load_string(username_helper)
        screen.add_widget(self.username)
        return screen

DemoApp().run()