from kivy.core.window import Window
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


# Window.clearcolor = (1,1,1,1)

class InputApp(App):
    def build(self):
        layout = GridLayout(cols=2, spacing=10, padding=25, row_force_default=True, row_default_height=40)
        self.first_name = TextInput(text="Enter Your First Name Here")
        self.last_name = TextInput(text="Enter Your Last Name Here")
        button = Button(text="Submit",
                        on_press=self.submit_form,
                        )

        layout.add_widget(self.first_name)
        layout.add_widget(self.last_name)
        layout.add_widget(button)

        return layout

    def submit_form(self, obj):
        print("First Name:" + self.first_name.text)
        print("First Name:" + self.last_name.text)

InputApp().run()