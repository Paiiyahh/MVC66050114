import csv

class CSVModel:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_data(self):
        try:
            with open(self.file_path, mode='r') as file:
                reader = csv.DictReader(file)
                data = [row for row in reader]
                return data
        except FileNotFoundError:
            return None
