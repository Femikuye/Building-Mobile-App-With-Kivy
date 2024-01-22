from kivy.app import App
# To import image locally:
from kivy.uix.image import Image
# To import Image From URL:
from kivy.uix.image import AsyncImage
from kivy.core.window import Window

Window.clearcolor = (1,1,1,1)
class ImageApp(App):
    def build(self):
        image2 = Image(source="python2.png")
        image = AsyncImage(source="https://pataskitypublishing.com/assets/images/logos/logo.png")
        #
        return image

ImageApp().run()
