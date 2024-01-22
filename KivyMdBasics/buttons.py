from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton , MDIconButton , MDFloatingActionButton
from kivymd.uix.screen import Screen

class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        btn_flat = MDFlatButton(
            text="My Flat Button",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        icon_btn = MDIconButton(
            text="Icon Button",
            icon="apple-ios",
            pos_hint={"center_x": 0.5, "center_y": 0.4}
        )
        rec_flat_btn = MDRectangleFlatButton(
            text="Rectangle Button",
            pos_hint={"center_x": 0.5, "center_y": 0.2}
        )

        float_btn = MDFloatingActionButton(
            text="Floating Button",
            pos_hint={"center_x": 0.5, "center_y": 0.1},
            icon="apple-ios",
        )
        screen.add_widget(btn_flat)
        screen.add_widget(icon_btn)
        screen.add_widget(rec_flat_btn)
        screen.add_widget(float_btn)
        return screen


DemoApp().run()