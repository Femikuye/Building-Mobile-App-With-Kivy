from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton , MDFlatButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from helpers import username_helper

class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Purple"
        button = MDRectangleFlatButton(
            text="Show",
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            on_release=self.show_data
        )
        self.username = Builder.load_string(username_helper)
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen

    def show_data(self, obj):
        if len(self.username.text) > 1:
            close_btn = MDFlatButton(
                text="Close",
                on_release=self.close_dialog
            )
            more_btn = MDFlatButton(text="More")
            self.dialog = MDDialog(
                text=self.username.text,
                title="Username Check",
                #size_hint=(0.5, 1),
                buttons=[close_btn, more_btn]
            )
            self.dialog.open()
    def close_dialog(self, obj):
        self.dialog.dismiss()
DemoApp().run()