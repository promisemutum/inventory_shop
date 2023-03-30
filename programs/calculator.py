import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")

        # Set the size of the window
        master.geometry("500x350")

        # Center the window contents
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)
        master.grid_columnconfigure(2, weight=1)
        master.grid_columnconfigure(3, weight=1)
        master.grid_rowconfigure(0, weight=1)
        master.grid_rowconfigure(1, weight=1)
        master.grid_rowconfigure(2, weight=1)

        # Create input fields
        self.num1 = tk.Entry(master, width=10)
        self.num1.grid(row=0, column=0, padx=5, pady=5)

        self.num2 = tk.Entry(master, width=10)
        self.num2.grid(row=0, column=2, padx=5, pady=5)

        # Create buttons for calculations
        self.add_button = tk.Button(master, text="+", command=self.add)
        self.add_button.grid(row=1, column=0, padx=5, pady=5)

        self.subtract_button = tk.Button(master, text="-", command=self.subtract)
        self.subtract_button.grid(row=1, column=1, padx=5, pady=5)

        self.multiply_button = tk.Button(master, text="*", command=self.multiply)
        self.multiply_button.grid(row=1, column=2, padx=5, pady=5)

        self.divide_button = tk.Button(master, text="/", command=self.divide)
        self.divide_button.grid(row=1, column=3, padx=5, pady=5)

        # Create output field
        self.result = tk.Label(master, text="")
        self.result.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

    def add(self):
        try:
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())
            result = num1 + num2
            self.result.config(text=f"Result: {result}")
        except ValueError:
            self.result.config(text="Invalid input")

    def subtract(self):
        try:
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())
            result = num1 - num2
            self.result.config(text=f"Result: {result}")
        except ValueError:
            self.result.config(text="Invalid input")

    def multiply(self):
        try:
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())
            result = num1 * num2
            self.result.config(text=f"Result: {result}")
        except ValueError:
            self.result.config(text="Invalid input")

    def divide(self):
        try:
            num1 = float(self.num1.get())
            num2 = float(self.num2.get())
            result = num1 / num2
            self.result.config(text=f"Result: {result}")
        except ZeroDivisionError:
            self.result.config(text="Cannot divide by zero")
        except ValueError:
            self.result.config(text="Invalid input")

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
