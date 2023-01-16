"""
Kivy example for CP1404/CP5632, IT@JCU
Dynamically create buttons based on content of dictionary
Lindsay Ward, first version: 11/07/2016
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty

NEW_COLOUR = (1, 0, 0, 1)  # RGBA for red
ALTERNATIVE_COLOUR = (1, 0, 1, 1)  # RGBA for magenta


class DynamicWidgetsApp(App):
    """Kivy app to demo dynamic widget creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) example - dictionary of names: phone numbers
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = self.create_layout()
        self.create_widgets()
        return self.root

    def create_layout(self):
        """Create the main layout of the app."""
        main_layout = BoxLayout(orientation='vertical')

        entries_box = BoxLayout(orientation='vertical')
        main_layout.add_widget(entries_box)

        status_label = Label(size_hint_y=0.1, text=self.status_text)
        main_layout.add_widget(status_label)

        buttons_layout = BoxLayout(orientation='horizontal', size_hint_y=0.2)
        create_button = Button(text="Create Widgets", on_press=self.create_widgets)
        buttons_layout.add_widget(create_button)
        clear_button = Button(text="Clear Widgets", on_press=self.clear_all)
        buttons_layout.add_widget(clear_button)
        main_layout.add_widget(buttons_layout)

        return main_layout

    def create_widgets(self):
        """Create buttons from data and add them to the GUI."""
        for name in self.name_to_phone:
            # create a button for each data entry, specifying the text
            temp_button = Button(text=name)
            temp_button.bind(on_press=self.press_entry)
            # set the button's background colour
            temp_button.background_color = NEW_COLOUR
            # add the button to the "entries_box" layout widget
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        """Handle pressing entry buttons."""
        # get name (dictionary key) from the text of Button we clicked on
        name = instance.text
        # change the button's background colour
        instance.background_color = ALTERNATIVE_COLOUR
        # update status text
        self.status_text = f"{name}'s number is {self.name_to_phone[name]}"

    def clear_all(self):
        """Clear all widgets that are children of the "entries_box" layout widget."""
        self.root.ids.entries_box.clear_widgets()


DynamicWidgetsApp().run()
