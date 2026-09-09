import csv
file_path="C:\\Users\\sulta\\Documents\\Training Session\\Python\\test.csv"

with open(file_path, "r") as f:
    data = csv.reader(f)
    for row in data:
        print(row)