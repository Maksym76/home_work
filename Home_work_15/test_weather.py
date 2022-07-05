import unittest

from get_weather import pressure, temperature


class TestWeather(unittest.TestCase):

    @unittest.skipIf(pressure() > 1013, 'pressure biggest then 1013 hPa')
    def test_lowe_pressure(self):
        self.assertLess(pressure(), 1013)

    @unittest.skipIf(pressure() < 1013, 'pressure lowest then 1013 hPa')
    def test_high_pressure(self):
        self.assertGreater(pressure(), 1013)

    @unittest.skipIf(temperature() > 0, 'temperature lowest then 0 C')
    def test_negative_temperature(self):
        self.assertLess(temperature(), 0)

    @unittest.skipIf(temperature() < 0, 'temperature biggest then 0 C')
    def test_positive_temperature(self):
        self.assertGreater(temperature(), 0)


if __name__ == '__mani__':
    unittest.main()
