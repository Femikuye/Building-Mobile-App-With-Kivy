from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (380, 600)

screen_helper = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: 'Pataskity Voice'
                        left_action_items: [["menu", lambda x: main_nav_drawer.set_state()]]
                        right_action_items: [["search-web", lambda x: app.navigation_draw()]]
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
        MDNavigationDrawer:
            id: main_nav_drawer
            MDBoxLayout:
                spacing: '8dp'
                padding: '8dp'
                orientation: 'vertical'

                Image:
                    source: 'python2.png'
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel: 
                    text: 'Femi Kuye'
                    font_size: '21'
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel: 
                    text: 'oluwafemiolayinka35@gmail.com'
                    font_size: '17'    
                    size_hint_y: None
                    height: self.texture_size[1]
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Login'
                            IconLeftWidget:
                                icon: 'login-variant'
                        OneLineIconListItem:
                            text: 'Logout'
                            IconLeftWidget:
                                icon: 'logout-variant'
                        OneLineIconListItem:
                            text: 'Register'
                            IconLeftWidget:
                                icon: 'account'
                        OneLineIconListItem:
                            text: 'Profile'
                            IconLeftWidget:
                                icon: 'face-man-profile'
                        OneLineIconListItem:
                            text: 'My Favorite Books'
                            IconLeftWidget:
                                icon: 'robot-love'
                        OneLineIconListItem:
                            text: 'Categories'
                            IconLeftWidget:
                                icon: 'robot-love'
                        OneLineIconListItem:
                            text: 'History'
                            IconLeftWidget:
                                icon: 'history'
                        OneLineIconListItem:
                            text: 'Settings'
                            IconLeftWidget:
                                icon: 'tools'

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