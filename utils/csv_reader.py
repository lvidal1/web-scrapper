import csv


def syncFile(path):
    with open(path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
