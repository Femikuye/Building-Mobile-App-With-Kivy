from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen , ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (380, 600)

screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:
<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: 
            root.manager.current = 'profile'
            root.manager.transition.direction = 'left'
    MDRectangleFlatButton:
        text: 'Upload'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: 
            root.manager.current = 'uploadimage'
            root.manager.transition.direction = 'left'

<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'User Profile'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Go Back'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: 
            root.manager.current = 'menu'
            root.manager.transition.direction = 'right'
<UploadScreen>:
    name: 'uploadimage'
    MDLabel:
        text: 'Upload Your Profile Here'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Go Back'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: 
            root.manager.current = 'menu'            
            root.manager.transition.direction = 'right'
"""
class MenuScreen(Screen):
    pass
class ProfileScreen(Screen):
    pass
class UploadScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(UploadScreen(name='uploadimage'))
class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.primary_hue = "900"
        screen = Builder.load_string(screen_helper)
        return screen
    def navigation_draw(self):
        print("Navigation")


DemoApp().run()