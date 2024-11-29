import unittest

class TestThreatScoreCalculation(unittest.TestCase):
    
    def test_uniform_threat(self):
        # Все отделы имеют одинаковый уровень угроз
        data = [generate_random_data(30, 10, 50) for _ in range(5)]
        score = calculate_aggregated_threat_score(data)
        self.assertTrue(0 <= score <= 90)

    def test_one_high_threat_department(self):
        # Один отдел с высоким уровнем угроз
        data = [
            generate_random_data(10, 5, 50),
            generate_random_data(15, 5, 50),
            generate_random_data(70, 10, 50)  # Высокий уровень угроз
        ]
        score = calculate_aggregated_threat_score(data)
        self.assertTrue(0 <= score <= 90)

    def test_individual_high_threat(self):
        # Один отдел с аномально высокими индивидуальными угрозами
        data = [
            generate_random_data(30, 10, 50),
            generate_random_data(35, 15, 70),
            np.concatenate([generate_random_data(30, 5, 90), [90, 85, 88]])  # Аномалии
        ]
        score = calculate_aggregated_threat_score(data)
        self.assertTrue(0 <= score <= 90)

    def test_no_threats(self):
        # Все отделы имеют нулевой уровень угроз
        data = [generate_random_data(0, 0, 50) for _ in range(5)]
        score = calculate_aggregated_threat_score(data)
        self.assertEqual(score, 0)
