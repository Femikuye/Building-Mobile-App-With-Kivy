from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = (1,1,1,1)
class BasicApp(App):
    def build(self):
        label = Label(text="This is a basic app",
                      font_size='25sp',
                      color=(0,0,0,1),
                      bold=True, italic=True)
        return label

BasicApp().run()