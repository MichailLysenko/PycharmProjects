import json
import csv
import sys


class FileHandler:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = []

    def read(self):
        raise NotImplementedError("Metoda read() musi być zaimplementowana w klasie pochodnej.")

    def write(self, output_path):
        raise NotImplementedError("Metoda write() musi być zaimplementowana w klasie pochodnej.")

    def apply_changes(self, changes):
        for column, row, value in changes:
            try:
                self.data[row][column] = value
            except IndexError:
                print(f"Nie można zastosować zmiany w wierszu {row}, kolumnie {column} - poza zakresem.")


class CSVHandler(FileHandler):
    def read(self):
        with open(self.filepath, mode='r') as file:
            reader = csv.reader(file)
            self.data = list(reader)

    def write(self, output_path):
        with open(output_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.data)


class JSONHandler(FileHandler):
    def read(self):
        with open(self.filepath, mode='r') as file:
            self.data = json.load(file)

    def write(self, output_path):
        with open(output_path, mode='w') as file:
            json.dump(self.data, file, indent=4)


class TXTHandler(FileHandler):
    def read(self):
        with open(self.filepath, mode='r') as file:
            self.data = [line.strip().split() for line in file]

    def write(self, output_path):
        with open(output_path, mode='w') as file:
            for line in self.data:
                file.write(" ".join(line) + "\n")


def parse_args():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    changes = []

    for change in sys.argv[3:]:
        x, y, value = change.split(',')
        changes.append((int(x), int(y), value))

    return input_file, output_file, changes


def main():
    input_file, output_file, changes = parse_args()

    if input_file.endswith('.csv'):
        handler = CSVHandler(input_file)
    elif input_file.endswith('.json'):
        handler = JSONHandler(input_file)
    elif input_file.endswith('.txt'):
        handler = TXTHandler(input_file)
    else:
        raise ValueError("Nieobsługiwany format pliku.")

    handler.read()
    handler.apply_changes(changes)
    handler.write(output_file)

    print("Zawartość po zmianach:")
    for line in handler.data:
        print(line)


if __name__ == "__main__":
    main()