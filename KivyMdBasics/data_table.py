from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.list import OneLineListItem
class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        table = MDDataTable(
            check=True,
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(0.9,0.6),
            rows_num=15,
            column_data=[
                ("No.", dp(30)),
                ("Food", dp(30)),
                ("Calories", dp(30))
            ],
            row_data=[
                ("1", "Rice", "300"),
                ("2", "Beans", "350"),
                ("3", "Banana", "200"),
                ("4", "Beans", "350"),
                ("5", "Beans", "350"),
                ("6", "Beans", "350"),
                ("7", "Beans", "350"),
                ("8", "Beans", "350"),
                ("9", "Beans", "350"),
                ("10", "Beans", "350"),
                ("11", "Beans", "350"),
                ("12", "Beans", "350"),
                ("13", "Beans", "350"),
            ]
        )
        table.bind(on_check_press=self.table_check_press)
        table.bind(on_row_press=self.row_check_press)
        screen.add_widget(table)
        return screen
    def table_check_press(self, instance_table, current_row):
        print("Table Event", instance_table, current_row)
    def row_check_press(self, instance_table, instance_row):
        print("Row Event", instance_table, instance_row)



DemoApp().run()