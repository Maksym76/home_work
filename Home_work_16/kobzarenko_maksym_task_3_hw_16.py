import requests
import  datetime
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


currency = input('Write currency: ').upper()
dat = datetime.date.today()
data = datetime.date.strftime(dat, '%Y%m%d')

api_url = f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency}&date={data}&json'

response = requests.get(api_url).json()

if response == list():
    print(f'Invalid currency name: {currency}')
else:
    print(f'''{currency}

{response[0]['rate']}''')
    print(response)
