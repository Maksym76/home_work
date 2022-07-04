from unittest import TestCase, main


from get_weather import information_about_weather, pressure, temperature


class TestWeather(TestCase):

    def test_lowe_pressure(self):
        self.assertLess(pressure(), '1013.25')

    def test_high_pressure(self):
        self. assertGreater(pressure(), '1013.25')

    def test_negative_temperature(self):
        self.assertLess(temperature(), '0')

    def test_positive_temperature(self):
        self.assertLess(temperature(), '0')

if __name__ == '__mani__':
    main()
