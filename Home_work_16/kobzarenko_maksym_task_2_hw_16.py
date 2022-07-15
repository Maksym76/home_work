"""Script returns city name, country, currency and population"""

import requests

try:

    city_name: str = input("Write city's name: ").capitalize()  # converts the first character of a string to uppercase
    # and all other characters to lowercase

    api_url_city: str = f'https://api.api-ninjas.com/v1/city?name={city_name}'  # To inset city name in api url city

    api_key: str = 'cEVBI1ovwpgTvN5gQyeWrw==XrhtDlSc2JvBAC43'

    # Make a request about information of city and get response
    response_city: list = requests.get(api_url_city, headers={'X-Api-Key': api_key}).json()

    if response_city == list():
        print(f'Invalid city name: {city_name}')
    else:

        city: str = response_city[0]['name']  # From got response about city we  take name city
        country: str = response_city[0]['country']  # From got response about city we  take country abbreviation
        population: int = response_city[0]['population']  # From got response about city we  take population

        api_url_country: str = f'https://api.api-ninjas.com/v1/country?name={country}'  # To inset country abbreviation
        # in api url country

        # Make a request about information of country and get response
        response_country: list = requests.get(api_url_country, headers={'X-Api-Key': api_key}).json()

        currency: str = response_country[0]["currency"]["code"]  # From got response about country we  take currency
        country: str = response_country[0]["name"]  # From got response about country we  take full country name

        print(f'''{city}

{country}
{currency}
{population}''')

except BaseException:
    print('System Error')
