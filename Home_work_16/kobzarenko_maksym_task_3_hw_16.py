import requests
import datetime

# currency = input('Write currency: ').upper()
#
# api_url = f'https://api.api-ninjas.com/v1/convertcurrency?want=UAH&have={currency}&amount=1'
#
# api_key = 'cEVBI1ovwpgTvN5gQyeWrw==XrhtDlSc2JvBAC43'
#
# response = requests.get(api_url, headers={'X-Api-Key': api_key}).json()
#
# if 'error' in response:
#     print(f'Invalid currency name: {currency}')
# else:
#     print(f'''{currency}
#
# {response['new_amount']}''')
#
#
# print(response)
#
# # {'new_amount': 29.82, 'new_currency': 'UAH', 'old_currency': 'EUR', 'old_amount': 1.0}
#
# # Write currency: rrrr
# # {'error': 'Invalid currencies.'}

try:
    user_request = input('''Write currency and date (yyyy.mm.dd., where: y-year, m-month, d-date. Default date = today's date) 
Example:'USD 2020.04.22' or 'USD' \n ''').split(' ')

    date_now = datetime.date.today()
    data = datetime.date.strftime(date_now, '%Y%m%d')
    bank_currencies = ['AUD', 'CAD', 'CNY', 'HRK', 'CZK', 'DKK', 'HKD', 'HUF', 'INR', 'IDR', 'ILS', 'JPY', 'KZT',
                       'KRW', 'MXN', 'MDL', 'NZD', 'NOK', 'RUB', 'SGD', 'ZAR', 'SEK', 'CHF', 'EGP', 'GBP', 'USD', 'BYN',
                       'AZN', 'RON', 'TRY', 'XDR', 'BGN', 'EUR', 'PLN', 'DZD', 'BDT', 'AMD', 'DOP', 'IRR', 'IQD', 'KGS',
                       'LBP', 'LYD', 'MYR', 'MAD', 'PKR', 'SAR', 'VND', 'THB', 'AED', 'TND', 'UZS', 'TWD', 'TMT', 'RSD',
                       'TJS', 'GEL', 'BRL', 'XAU', 'XAG', 'XPT', 'XPD']
    currency = None

    if len(user_request) < 2:
        currency = user_request[0].upper()

    elif len(user_request) == 2:
        currency = user_request[0].upper()
        data = user_request[1].replace('.', '')
    else:
        print('Invalid request')

    api_url = f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency}&date={data}&json'

    response = requests.get(api_url).json()

    if currency not in bank_currencies:
        print(f'Invalid currency name: {currency}')

    elif response == list or 'message' in response[0]:
        print('Invalid date')

    else:
        print(f'''{currency}
    
{response[0]['rate']}''')

except BaseException:
    print('System Error')
