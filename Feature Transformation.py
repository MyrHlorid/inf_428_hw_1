import math
import unittest

def cyclic_time_difference(time1, time2):
    """
    Рассчитывает циклическую разницу между двумя временными точками (в часах),
    корректно обрабатывая случаи перехода через полночь.
    """
    # Преобразуем каждый временной момент в циклические признаки (x, y)
    radians1 = (2 * math.pi * time1) / 24
    radians2 = (2 * math.pi * time2) / 24
    x1, y1 = math.cos(radians1), math.sin(radians1)
    x2, y2 = math.cos(radians2), math.sin(radians2)
    
    # Вычисляем угол между двумя точками на окружности
    angle_diff = math.acos(x1 * x2 + y1 * y2)
    return (angle_diff * 24) / (2 * math.pi)  # Преобразуем радианы обратно в часы

# Unit-тесты
class TestCyclicTimeFeatures(unittest.TestCase):

    def test_cyclic_time_difference(self):
        # Разница между 23 и 1 часом - 2 часа
        self.assertAlmostEqual(cyclic_time_difference(23, 1), 2, delta=1e-5)
        # Разница между 1 и 23 часом - тоже 2 часа
        self.assertAlmostEqual(cyclic_time_difference(1, 23), 2, delta=1e-5)
        # Разница между 12 и 6 часами - 6 часов
        self.assertAlmostEqual(cyclic_time_difference(12, 6), 6, delta=1e-5)
        # Разница между одинаковыми временем - 0 часов
        self.assertAlmostEqual(cyclic_time_difference(5, 5), 0, delta=1e-5)

if __name__ == '__main__':
    unittest.main()
