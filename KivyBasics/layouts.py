from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.core.window import Window

Window.clearcolor = (1,1,1,1)
Window.size = (360,600)
class LayoutApp(App):
    def build(self):
        box_layout = BoxLayout(orientation="vertical", spacing=100, padding=80)
        image = Image(source="python2.png")
        box_layout.add_widget(image)
        btn4 = Button(text="Login", size_hint=(None,None),
                      width=150, height=50,
                      pos_hint={"center_x":0.5}
                      )
        box_layout.add_widget(btn4)

        return box_layout

LayoutApp().run()