# Расчет агрегированного уровня угроз
def calculate_aggregated_threat_score(department_data):
    total_threat = 0
    total_users = 0

    for dept in department_data:
        total_threat += np.sum(dept)
        total_users += len(dept)

    # Нормализация до диапазона 0 - 90
    aggregated_score = total_threat / total_users
    return min(max(aggregated_score, 0), 90)
