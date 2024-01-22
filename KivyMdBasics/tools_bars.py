from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (380, 600)

screen_helper = """
Screen:
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Pataskity Voice'
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
            right_action_items: [["language-python", lambda x: app.navigation_draw()]]
            elevation:2
        MDLabel:
            text: 'Listen To Your Favorite Books From Your Favorite Authors'
            halign: 'center'
        MDBottomAppBar:
            MDTopAppBar:
                title: 'Copright 2023'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                mode: 'end'
                on_action_button: app.navigation_draw()
                type: 'bottom'
                icon: 'language-php'
"""
class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.primary_hue = "900"
        screen = Builder.load_string(screen_helper)
        return screen
    def navigation_draw(self):
        print("Navigation")


DemoApp().run()