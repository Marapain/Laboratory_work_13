import csv
import json

# 1. Створення CSV файлу
csv_file = 'students_data.csv'
data = [
    ["ID", "Name", "Age", "Grade"],
    ["1", "Alice", "20", "A"],
    ["2", "Bob", "22", "B"],
    ["3", "Charlie", "19", "C"]
]

try:
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print(f"CSV файл '{csv_file}' успішно створено.")
except Exception as e:
    print(f"Помилка при створенні CSV файлу: {e}")

# 2. Конвертація CSV у JSON
json_file = 'students_data.json'

try:
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]

    with open(json_file, mode='w') as file:
        json.dump(data, file, indent=4)
    print(f"JSON файл '{json_file}' успішно створено.")
except Exception as e:
    print(f"Помилка при конвертації: {e}")