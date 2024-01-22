from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

Window.clearcolor = (1,1,1,1)

class LayoutApp(App):
    def build(self):
        layout = GridLayout(cols=2,
                            row_force_default=True,
                            row_default_height=40
                            )
        btn1 = Button(text="Register", size_hint=(None, None), width=100, height=40)
        btn2 = Button(text="Login")
        btn3 = Button(text="Register 2", size_hint=(None, None), width=100, height=40)
        btn4 = Button(text="Login 2")

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)

        return layout

LayoutApp().run()