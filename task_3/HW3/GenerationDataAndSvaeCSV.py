import csv
import random
import os

# Генерация случайных данных
def generate_random_data(file_path, num_records=100):
    data = []
    for _ in range(num_records):
        record = {
            "time_of_day": random.randint(0, 23),  # Время суток (0-23)
            "threat_score": random.randint(0, 100)  # Уровень угроз (0-100)
        }
        data.append(record)
    
    # Сохранение данных в .csv
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["time_of_day", "threat_score"])
        writer.writeheader()
        writer.writerows(data)
    print(f"Data generated and saved to {file_path}")

# Проверка существования файла и чтение данных
def read_data_from_csv(file_path):
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist. Please generate data first.")
        return None
    
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    print(f"Data read from {file_path}")
    return data

# Пример использования
file_path = "threat_data.csv"
if not os.path.exists(file_path):
    generate_random_data(file_path)
data = read_data_from_csv(file_path)
