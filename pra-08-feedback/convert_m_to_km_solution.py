"""
CP1404 Week 11 Workshop - GUI program to convert miles to kilometres
Lindsay Ward, IT@JCU
06/10/2015
"""

# convert_miles_km.py

from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """
        Calculate the conversion from miles to kilometres and display the result in the output label.
        """
        # Get the value of the input field and convert it to a float
        try:
            value = float(self.root.ids.input_miles.text)
        except ValueError:
            # If the value is not a valid number, set the result to 0.0
            result = 0.0
        else:
            # Otherwise, perform the conversion and display the result
            result = value * MILES_TO_KM

        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """
        Increment or decrement the value in the input field by the specified amount.
        """
        # Get the current value of the input field and convert it to a float
        try:
            value = float(self.root.ids.input_miles.text)
        except ValueError:
            # If the value is not a valid number, assume it is 0
            value = 0

        # Increment or decrement the value
        value += change

        # Update the input field with the new value
        self.root.ids.input_miles.text = str(value)

        # Calculate and display the result
        self.handle_calculate()



MilesConverterApp().run()
