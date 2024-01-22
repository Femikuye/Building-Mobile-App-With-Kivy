#Icons Definations:  https://github.com/kivymd/KivyMD/blob/master/kivymd/icon_definitions.py
# Styles: https://raw.githubusercontent.com/HeaTTheatR/KivyMD-data/master/gallery/kivymddoc/md-label-font-style.gif
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon

class DemoApp(MDApp):
    def build(self):
        label = MDLabel(text="Simple Text", halign="center",
                        theme_text_color="Error")
        label_custom_color = MDLabel(text="Simple Text",
                                     halign="center",
                        theme_text_color="Custom",
                                     text_color=(80/255.0,60/255.0,125/255.0,1),
                                     font_style='Caption'
                                     )
        icon_label = MDIcon(
            icon='language-python',
            halign='center'
        )
        return icon_label


DemoApp().run()