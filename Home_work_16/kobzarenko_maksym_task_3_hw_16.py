""" National Bank of Ukraine
Foreign exchange rate to UAH"""

import requests

import datetime

try:
    user_request: list = input(
        "Write currency and date (yyyy.mm.dd., where: y-year, m-month, d-date. Default date = today's date)"
        "\nExample:'USD 2020.04.22' or 'USD' \n").split(' ')

    date_now: datetime.date = datetime.date.today()  # Create variable with today date
    data: str = datetime.date.strftime(date_now, '%Y%m%d')  # Converting date to string
    bank_currencies: list = ['AUD', 'CAD', 'CNY', 'HRK', 'CZK', 'DKK', 'HKD', 'HUF', 'INR', 'IDR', 'ILS', 'JPY', 'KZT',
                             'KRW', 'MXN', 'MDL', 'NZD', 'NOK', 'RUB', 'SGD', 'ZAR', 'SEK', 'CHF', 'EGP', 'GBP', 'USD',
                             'BYN', 'AZN', 'RON', 'TRY', 'XDR', 'BGN', 'EUR', 'PLN', 'DZD', 'BDT', 'AMD', 'DOP', 'IRR',
                             'IQD', 'KGS', 'LBP', 'LYD', 'MYR', 'MAD', 'PKR', 'SAR', 'VND', 'THB', 'AED', 'TND', 'UZS',
                             'TWD', 'TMT', 'RSD', 'TJS', 'GEL',
                             'BRL']  # Create list with currencies which work the bank
    currency: str = user_request[0].upper()  # Write currency which user chose

    if len(user_request) == 2:
        data: str = user_request[1].replace('.', '')

    api_url: str = f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency}&date={data}&json'

    response: list = requests.get(api_url).json()

    if currency not in bank_currencies:
        if currency == '':
            print('Invalid currency name: None')
        else:
            print(f'Invalid currency name: {currency}')

    elif response == list or 'message' in response[0]:
        print(f'Invalid date {user_request[1]}')

    else:
        print(f'''{currency}
    
{response[0]['rate']}''')

except BaseException:
    print('System Error')
