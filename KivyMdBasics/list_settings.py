"""
1) Example of List - https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/lists.png
2) Create -> OneLineListItem
https://raw.githubusercontent.com/HeaTTheatR/KivyMD-data/master/gallery/kivymddoc/lists.gif

3) Flow to create a list : OneLineListItem-> MDList -> ScrollView -> Screen
4) Create a for loop to add more items
5) Create a TwoLineListItem(secondary_text), ThreeLineListItem (tertiary_text)

- Flow to Icon/Avatar list : IconLeftWidget/IconRightWidget -> OneLineListItem-> MDList -> ScrollView -> Screen
6) Add a OneLineIconListItem
7) Add a OneLineAvatarListItem

8) Use the Builder method to create a list
"""
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import (MDList, OneLineListItem , TwoLineListItem
,ThreeLineListItem , ThreeLineIconListItem, OneLineIconListItem , TwoLineIconListItem,
OneLineAvatarListItem, IconLeftWidget , ImageLeftWidget)
from kivymd.uix.scrollview import ScrollView
class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        scroll_view = ScrollView()
        list_view = MDList()
        self.theme_cls.primary_palette = "Purple"

        left_icon = IconLeftWidget(icon="language-python")
        left_icon2 = IconLeftWidget(icon="language-python")
        left_icon3 = IconLeftWidget(icon="language-python")

        one_line_list_item = OneLineListItem(text="Single Line List Item Without Icon")
        one_line_list_item_with_icon = OneLineIconListItem(text="Single Line List Item With Icon")
        one_line_list_item_with_icon.add_widget(left_icon)

        right_image = ImageLeftWidget(source="python2.png")
        one_line_list_item_with_avatar = OneLineAvatarListItem(text="Single Line List Item With Avatar")
        one_line_list_item_with_avatar.add_widget(right_image)

        two_lines_list_item = TwoLineListItem(
            text="Double Lines No Icon",
            secondary_text="This Is Two Lines List Item Without Icon"
        )
        two_lines_list_item_with_icon = TwoLineIconListItem(
            text="Double Lines Yes Icon",
            secondary_text="This Is Two Lines List Item With Icon"
        )
        two_lines_list_item_with_icon.add_widget(left_icon2)

        three_line_list_item = ThreeLineListItem(
            text="Three Lines List Item",
            secondary_text="This three lines list item without icon",
            tertiary_text= "No Icon List"
        )
        three_line_list_item_with_icon = ThreeLineIconListItem(
            text="Three Lines List Item",
            secondary_text="This three lines list item with icon",
            tertiary_text="It Has Icon List"
        )
        three_line_list_item_with_icon.add_widget(left_icon3)

        list_view.add_widget(one_line_list_item)
        list_view.add_widget(one_line_list_item_with_icon)

        list_view.add_widget(one_line_list_item_with_avatar)

        list_view.add_widget(two_lines_list_item)
        list_view.add_widget(two_lines_list_item_with_icon)

        list_view.add_widget(three_line_list_item)
        list_view.add_widget(three_line_list_item_with_icon)

        scroll_view.add_widget(list_view)

        screen.add_widget(scroll_view)
        return screen


DemoApp().run()