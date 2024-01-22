import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color , Ellipse , Line
import random
Window.clearcolor = (1,1,1,1)

class PaintWindow(Widget):
    def on_touch_down(self, touch):
        colorR = random.randint(0, 255)
        colorG = random.randint(0, 255)
        colorB = random.randint(0, 255)
        self.canvas.add(Color(rgb=(colorR / 255.0 , colorG / 255.0 , colorB /255.0 )))
        d = 30
        self.canvas.add(Ellipse(pos=(touch.x - d/2, touch.y - d/2), size=(d,d)))

        touch.ud["line"] = Line(point=(touch.x,touch.y))
        self.canvas.add(touch.ud["line"])
    def on_touch_move(self, touch):
        touch.ud["line"].points += [touch.x, touch.y]

class PaintApp(App):
    def build(self):
        rootWindow = Widget()
        clearButton = Button(text="Clear")
        self.painter = PaintWindow()
        clearButton.bind(on_release=self.clear_canvas)
        rootWindow.add_widget(self.painter)
        rootWindow.add_widget(clearButton)

        return rootWindow
    def clear_canvas(self, obj):
        self.painter.canvas.clear()



PaintApp().run()


# What To Learn
# 1. Changing background color and RGBA colors
# 2. on_touch_down Effect
# 3. Color
# 4. Drawing a circle/ellipse