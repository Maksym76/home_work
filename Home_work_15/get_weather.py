import requests

base_url: str = 'http://api.openweathermap.org/data/2.5/weather?'

api_key: str = 'd82759ebf4a4a5ed987117c4027b9dfa'

city_name: str = input('please fill up your city: ')

complete_url: str = base_url + "appid=" + api_key + "&q=" + city_name  # generating URL in which will be take information about weather
response = requests.get(complete_url)  # send a request to the complete URL and get response
r_data: dict = response.json()  # writing the response to the dictionary


def information_about_weather():
    """Showing all information about weather in the city"""

    if r_data["cod"] != "404":
        weather_data: dict = r_data['main']
        current_t: int = round(weather_data['temp'] - 273.15)  # converting temperature from fahrenheit to celsius and round to integer

        current_p: int = weather_data["pressure"]
        weather_description: dict = r_data["weather"]
        weather_description: str = weather_description[0]["description"]
        return f"Weather's data in {city_name.capitalize()}: current temperature {current_t} С, current pressure " \
               f"{current_p} hPa, {weather_description}"

    else:
        return 'city not found'


def pressure():
    """Showing what pressure in the city"""

    weather_pressure: dict = r_data['main']
    current_pressure: int = weather_pressure['pressure']

    return current_pressure


def temperature():
    """Showing what temperature in the city"""

    weather_temperature: dict = r_data['main']
    current_temperature: int = round(weather_temperature['temp'] - 273.15)  # converting temperature from fahrenheit to celsius and round to integer
    return current_temperature


if __name__ == '__main__':
    print(information_about_weather())

"""
1. создать функцию(ии) для определения погоды по данным(Город).
2. Вынести некоторые данные в константу(ы).
3. Для запуска функции использовать if __name__ == '__main__': запуск!
4. Создать модуль test_weather.py внутри создать Класс для тестирования функции, с помощью unittest.
"""
