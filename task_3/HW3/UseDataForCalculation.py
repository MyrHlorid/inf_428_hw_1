import math

def calculate_time_differences(data):
    differences = []
    for record in data:
        time1 = record["time_of_day"]
        threat = record["threat_score"]
        # Например, сравниваем с фиксированным временем 12:00
        diff = cyclic_time_difference(time1, 12)
        differences.append({"time_diff": diff, "threat_score": threat})
    return differences

# Пример использования
if elastic_data:
    time_differences = calculate_time_differences(elastic_data)
    print("Time differences calculated:", time_differences)
