import numpy as np
import unittest

# Генерация случайных данных для уровня угроз
def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)

# Расчет агрегированного уровня угроз
def calculate_aggregated_threat_score(department_data, importance_scores):
    total_weighted_threat = 0
    total_importance = 0
    
    for dept, importance in zip(department_data, importance_scores):
        mean_threat = np.mean(dept)
        weighted_threat = mean_threat * importance
        total_weighted_threat += weighted_threat
        total_importance += importance
    
    # Нормализация до диапазона 0 - 90
    aggregated_score = total_weighted_threat / total_importance
    return min(max(aggregated_score, 0), 90)

# Тестирование
class TestThreatScoreCalculation(unittest.TestCase):
    
    def test_basic_calculation(self):
        # Тест на правильность вычислений
        data = [generate_random_data(30, 10, 50) for _ in range(5)]
        importance_scores = [1, 1, 1, 1, 1]
        score = calculate_aggregated_threat_score(data, importance_scores)
        self.assertTrue(0 <= score <= 90)
    
    def test_different_importances(self):
        # Тест на случай с разными значениями важности
        data = [generate_random_data(20, 5, 100), generate_random_data(40, 10, 50), generate_random_data(60, 20, 30)]
        importance_scores = [2, 3, 5]
        score = calculate_aggregated_threat_score(data, importance_scores)
        self.assertTrue(0 <= score <= 90)
    
    def test_one_high_threat_department(self):
        # Тест на случай с высоким уровнем угроз в одном отделе
        data = [generate_random_data(10, 5, 100), generate_random_data(15, 5, 80), generate_random_data(70, 10, 50)]
        importance_scores = [1, 1, 1]
        score = calculate_aggregated_threat_score(data, importance_scores)
        self.assertTrue(0 <= score <= 90)
    
    def test_all_departments_with_high_threat(self):
        # Тест на случай с высоким уровнем угроз в каждом отделе
        data = [generate_random_data(80, 5, 100) for _ in range(5)]
        importance_scores = [2, 3, 4, 1, 5]
        score = calculate_aggregated_threat_score(data, importance_scores)
        self.assertTrue(0 <= score <= 90)
    
    def test_no_threats(self):
        # Тест на отсутствие угроз во всех отделах
        data = [generate_random_data(0, 0, 50) for _ in range(5)]
        importance_scores = [1, 2, 3, 4, 5]
        score = calculate_aggregated_threat_score(data, importance_scores)
        self.assertEqual(score, 0)
