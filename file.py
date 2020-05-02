import csv
import os
import pandas as pd


class CSVFile:
    def __init__(self, name, column_names=None):
        self.filename = "{}.csv".format(name)

        if not os.path.isfile(self.filename) and column_names:
            self.create(column_names)
        elif not os.path.isfile(self.filename):
            raise FileNotFoundError("Give column names to create file")

    def create(self, column_names):
        try:
            with open(self.filename, "w") as file:
                writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(column_names)
                file.close()
        except IOError:
            print("File not accessible")
            return

    def append(self, rows: list):
        try:
            with open(self.filename, "a") as file:
                writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerows(rows)
                file.close()
        except:
            pass

    def read(self, row):
        data = pd.read_csv(self.filename)
        return data[row:row+1]

    def __len__(self):
        data = pd.read_csv(self.filename)
        return len(data)