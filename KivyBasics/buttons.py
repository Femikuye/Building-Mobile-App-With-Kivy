from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (1,1,1,1)

class ButtonApp(App):
    def build(self):
        button = Button(
            text="Custom Buton",
            size_hint=(0.3,0.1),
            font_size='20sp',
            pos_hint={'center_x':0.5, 'center_y': 0.5},
            on_press=self.button_press,
            on_release=self.button_release
        )
        return button
    def button_press(self, obj):
        print("Button Presses")
    def button_release(self, obj):
        print("Button Released")


ButtonApp().run()