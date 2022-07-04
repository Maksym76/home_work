import requests  # pip install requests

base_url = 'http://api.openweathermap.org/data/2.5/weather?'

api_key = 'd82759ebf4a4a5ed987117c4027b9dfa'  # if api_key not works, generate yours on website


def weather_in_city():
    city_name = input('please fill up your city: ')

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    r_data = response.json()
    if r_data["cod"] != "404":
        weather_data = r_data['main']
        current_t = round(weather_data['temp'] - 273.15)
        current_p = weather_data["pressure"]
        weather_discription = r_data["weather"]
        weather_description = weather_discription[0]["description"]
        return f'Weather data in {city_name.capitalize()}: current temperature {current_t} С, current pressure ' \
               f'{current_p} hPa, {weather_description}'

    else:
        return 'city not found'


if __name__ == '__main__':
    print(weather_in_city())

"""
1. создать функцию(ии) для определения погоды по данным(Город).
2. Вынести некоторые данные в константу(ы).
3. Для запуска функции использовать if __name__ == '__main__': запуск!
4. Создать модуль test_weather.py внутри создать Класс для тестирования функции, с помощью unittest.
"""
