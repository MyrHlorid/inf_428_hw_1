# Генерация данных для отделов
departments_data = [
    {"name": "Engineering", "scores": generate_random_data(30, 10, 50)},
    {"name": "Marketing", "scores": generate_random_data(25, 15, 70)},
    {"name": "Finance", "scores": generate_random_data(40, 20, 100)},
    {"name": "HR", "scores": generate_random_data(20, 5, 30)},
    {"name": "Science", "scores": generate_random_data(35, 10, 80)}
]

# Загрузка данных в Elasticsearch
upload_to_elasticsearch("threat_scores", departments_data)

# Чтение данных из Elasticsearch
department_data_from_es = read_from_elasticsearch("threat_scores")

# Расчёт агрегированного уровня угроз
aggregated_score = calculate_aggregated_threat_score(department_data_from_es)
print(f"Aggregated Threat Score: {aggregated_score}")

# Построение графиков
department_names = ["Engineering", "Marketing", "Finance", "HR", "Science"]
plot_department_threats(department_data_from_es, department_names)
plot_individual_threats(department_data_from_es, "Finance")
