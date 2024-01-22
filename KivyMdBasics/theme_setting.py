"""
1) What is a theme?
2) primary_palette on buttons

3) Color Options in primary_palette - Available options are: ‘Red’, ‘Pink’, ‘Purple’, ‘DeepPurple’, ‘Indigo’, ‘Blue’, ‘LightBlue’, ‘Cyan’, ‘Teal’, ‘Green’, ‘LightGreen’, ‘Lime’, ‘Yellow’, ‘Amber’, ‘Orange’, ‘DeepOrange’, ‘Brown’, ‘Gray’, ‘BlueGray’.

4) Primary hue option - ‘50’, ‘100’, ‘200’, ‘300’, ‘400’, ‘500’, ‘600’, ‘700’, ‘800’, ‘900’, ‘A100’, ‘A200’, ‘A400’, ‘A700’.

4) theme_style - Dark or Light two options
"""

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton

class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"
        lounch_btn = MDRectangleFlatButton(
            text="Lounch App",
            pos_hint={"center_x":0.5, "center_y":0.5}
        )
        screen.add_widget(lounch_btn)
        return screen


DemoApp().run()