class TestAggregatedThreatScore(unittest.TestCase):

    def test_generate_random_data(self):
        data = generate_random_data(45, 10, 20)
        self.assertTrue(len(data) == 20)
        self.assertTrue(np.all(data >= 0) and np.all(data <= 90))

    def test_calculate_aggregated_threat(self):
        department_threat_scores = [[30, 40, 50], [20, 25, 30], [10, 15, 20]]
        department_importances = [3, 3, 3]
        result = calculate_aggregated_threat(department_threat_scores, department_importances)
        self.assertAlmostEqual(result, 27.5, delta=0.5)

    def test_functional_case_similar_threats_and_importance(self):
        # Похожие уровни угрозы и важности
        department_threat_scores, department_importances = generate_department_data(
            num_departments=5,
            user_range=(10, 50),
            mean_range=(30, 40),
            variance_range=(5, 10)
        )
        result = calculate_aggregated_threat(department_threat_scores, department_importances)
        self.assertTrue(0 <= result <= 90)

    def test_functional_case_high_threat_low_importance(self):
        department_threat_scores = [[80]*20, [20]*30, [10]*40, [30]*50, [40]*60]
        department_importances = [1, 3, 3, 4, 5]
        result = calculate_aggregated_threat(department_threat_scores, department_importances)
        self.assertTrue(0 <= result <= 90)

    def test_functional_case_varied_importances(self):
        department_threat_scores = [[60]*15, [30]*25, [25]*10, [55]*30, [10]*20]
        department_importances = [1, 5, 3, 4, 2]
        result = calculate_aggregated_threat(department_threat_scores, department_importances)
        self.assertTrue(0 <= result <= 90)
        
if __name__ == '__main__':
    unittest.main()
