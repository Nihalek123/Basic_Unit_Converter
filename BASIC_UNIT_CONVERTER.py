import tkinter as tk
from tkinter import ttk


# Conversion functions
def convert_distance(value, from_unit, to_unit):
    distance_units = {"Meters": 1, "Kilometers": 1000, "Miles": 1609.34, "Feet": 0.3048}
    return (value * distance_units[from_unit]) / distance_units[to_unit]


def convert_weight(value, from_unit, to_unit):
    weight_units = {"Grams": 1, "Kilograms": 1000, "Pounds": 453.592, "Ounces": 28.3495}
    return (value * weight_units[from_unit]) / weight_units[to_unit]


def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return value if to_unit == "Celsius" else (value * 9 / 5) + 32 if to_unit == "Fahrenheit" else value + 273.15
    if from_unit == "Fahrenheit":
        return value if to_unit == "Fahrenheit" else (value - 32) * 5 / 9 if to_unit == "Celsius" else (
                                                                                                                   value - 32) * 5 / 9 + 273.15
    if from_unit == "Kelvin":
        return value if to_unit == "Kelvin" else value - 273.15 if to_unit == "Celsius" else (
                                                                                                         value - 273.15) * 9 / 5 + 32


# GUI Application
class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")

        # Conversion category selection
        self.category_label = ttk.Label(root, text="Conversion Category:")
        self.category_label.grid(row=0, column=0)

        self.category_combobox = ttk.Combobox(root, values=["Distance", "Weight", "Temperature"], state="readonly")
        self.category_combobox.grid(row=0, column=1)
        self.category_combobox.bind("<<ComboboxSelected>>", self.update_units)

        # Input value
        self.value_label = ttk.Label(root, text="Enter Value:")
        self.value_label.grid(row=1, column=0)

        self.value_entry = ttk.Entry(root)
        self.value_entry.grid(row=1, column=1)

        # From unit
        self.from_unit_label = ttk.Label(root, text="From Unit:")
        self.from_unit_label.grid(row=2, column=0)

        self.from_unit_combobox = ttk.Combobox(root, state="readonly")
        self.from_unit_combobox.grid(row=2, column=1)

        # To unit
        self.to_unit_label = ttk.Label(root, text="To Unit:")
        self.to_unit_label.grid(row=3, column=0)

        self.to_unit_combobox = ttk.Combobox(root, state="readonly")
        self.to_unit_combobox.grid(row=3, column=1)

        # Convert button
        self.convert_button = ttk.Button(root, text="Convert", command=self.convert_units)
        self.convert_button.grid(row=4, column=1)

        # Result display
        self.result_label = ttk.Label(root, text="Result:")
        self.result_label.grid(row=5, column=0)

        self.result_display = ttk.Label(root, text="")
        self.result_display.grid(row=5, column=1)

    def update_units(self, event):
        category = self.category_combobox.get()
        if category == "Distance":
            units = ["Meters", "Kilometers", "Miles", "Feet"]
        elif category == "Weight":
            units = ["Grams", "Kilograms", "Pounds", "Ounces"]
        else:
            units = ["Celsius", "Fahrenheit", "Kelvin"]

        self.from_unit_combobox.config(values=units)
        self.to_unit_combobox.config(values=units)

    def convert_units(self):
        try:
            value = float(self.value_entry.get())
            from_unit = self.from_unit_combobox.get()
            to_unit = self.to_unit_combobox.get()
            category = self.category_combobox.get()

            if category == "Distance":
                result = convert_distance(value, from_unit, to_unit)
            elif category == "Weight":
                result = convert_weight(value, from_unit, to_unit)
            else:
                result = convert_temperature(value, from_unit, to_unit)

            self.result_display.config(text=f"{result:.2f} {to_unit}")
        except ValueError:
            self.result_display.config(text="Invalid input. Please enter a number.")


# Running the app
root = tk.Tk()
app = UnitConverterApp(root)
root.mainloop()
