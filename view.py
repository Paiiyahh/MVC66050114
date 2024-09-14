import tkinter as tk
from tkinter import messagebox

class CSVView:
    def __init__(self, root, controller):
        self.controller = controller

        self.root = root
        self.root.title("Cow Lookup")

        self.label = tk.Label(root, text="Enter Cow ID:")
        self.label.pack(pady=30)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=30)

        self.submit_button = tk.Button(root, text="Submit", command=self.submit)
        self.submit_button.pack(pady=30)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=30)

    def submit(self):
        cow_id = self.entry.get()
        if cow_id:
            result, calculated_value = self.controller.get_cow_details(cow_id)
            if result:
                if calculated_value is not None:  # If the color is white
                    self.result_label.config(
                        text=f"ID: {result['id']}, Color: {result['color']}, Age: {result['age_years']} years and {result['age_months']} months, Calculation: {calculated_value}"
                    )
                else:
                    self.result_label.config(
                        text=f"ID: {result['id']}, Color: {result['color']}, Age: {result['age_years']} years and {result['age_months']} months"
                    )
            else:
                messagebox.showerror("Error", "Cow ID not found.")
        else:
            messagebox.showerror("Error", "Please enter a valid ID.")
