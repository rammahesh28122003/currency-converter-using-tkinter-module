import tkinter as tk
from tkinter import ttk

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        self.currency_options = {
            "USD": "United States Dollar (USD)",
            "EUR": "Euro (EUR)",
            "INR": "Indian Rupee (INR)",
            "AUD": "Australian Dollar (AUD)",
            "CAD": "Canadian Dollar (CAD)",
            "GBP": "British Pound (GBP)",
            "JPY": "Japanese Yen (JPY)"
        }

        self.amount_label = tk.Label(root, text="Enter Amount:")
        self.amount_label.grid(row=0, column=0, padx=10, pady=10)

        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

        self.from_currency_label = tk.Label(root, text="From Currency:")
        self.from_currency_label.grid(row=1, column=0, padx=10, pady=10)

        self.from_currency_combobox = ttk.Combobox(root, values=list(self.currency_options.values()))
        self.from_currency_combobox.grid(row=1, column=1, padx=10, pady=10)
        self.from_currency_combobox.set("United States Dollar (USD)")

        self.to_currency_label = tk.Label(root, text="To Currency:")
        self.to_currency_label.grid(row=2, column=0, padx=10, pady=10)

        self.to_currency_combobox = ttk.Combobox(root, values=list(self.currency_options.values()))
        self.to_currency_combobox.grid(row=2, column=1, padx=10, pady=10)
        self.to_currency_combobox.set("Euro (EUR)")

        self.convert_button = tk.Button(root, text="Convert", command=self.convert)
        self.convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def convert(self):
        try:
            amount = float(self.amount_entry.get())
            from_currency = self.get_currency_code(self.from_currency_combobox.get())
            to_currency = self.get_currency_code(self.to_currency_combobox.get())

            # Conversion rates for USD, EUR, INR, AUD, CAD, GBP, and JPY (modify as needed)
            conversion_rates = {
                "USD": 1.0,
                "EUR": 0.85,
                "INR": 74.7,
                "AUD": 1.35,
                "CAD": 1.25,
                "GBP": 0.72,
                "JPY": 110.5
            }

            converted_amount = amount * (conversion_rates[to_currency] / conversion_rates[from_currency])
            result_str = f"{amount:.2f} {self.currency_options[from_currency]} = {converted_amount:.2f} {self.currency_options[to_currency]}"
            self.result_label.config(text=result_str)
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a valid amount.")

    def get_currency_code(self, currency_name):
        return [code for code, name in self.currency_options.items() if name == currency_name][0]

# Create the main application window
root = tk.Tk()
currency_converter_app = CurrencyConverterApp(root)
root.mainloop()
