from model import CSVModel
from view import CSVView
import tkinter as tk

class CSVController:
    def __init__(self, file_path, root):
        self.model = CSVModel(file_path)
        self.view = CSVView(root, self)
        self.data = self.model.get_data()

    def get_cow_by_id(self, cow_id):
        for row in self.data:
            if row['id'] == cow_id:
                return row
        return None

    def get_cow_details(self, cow_id):
        result = self.get_cow_by_id(cow_id)
        if result:
            years = int(result['age_years'])
            months = int(result['age_months'])
            
            if result['color'] == 'white':
                calculated_value = 120 - (years * 12 + months)
                return (result, calculated_value)
            elif result['color'] == 'brown':
                calculated_value =40  - years 
                return (result, calculated_value)
            elif result['color'] == 'pink':
                calculated_value = 30 - months
                return (result, calculated_value)
        return None, None

if __name__ == "__main__":
    file_path = "Cows.csv"  

    root = tk.Tk()
    app = CSVController(file_path, root)
    root.mainloop()