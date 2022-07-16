import requests

api_url: str = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

response: list = requests.get(api_url).json()  # Send a request and get response

buy_usd: float = float(response[0]['buy'])  # Price for buy dollar
sale_usd: float = float(response[0]['sale'])  # Price for sale dollar

available_usd: float = 25685.25  # Available USD in cashbox
available_uah: float = 15364.36  # Available UAH in cashbox

while True:
    user_request: list = input(
        "Write one of the commands: 'COURSE USD(UAH)', 'EXCHANGE UAH(USD) 125(amount)' or 'STOP' "
        "for exit write : ").strip().upper().split()

    command_name: str = user_request[0]
    currency_name: str = user_request[1]

    #  Check for valid command from user
    if len(user_request) == 0 or len(user_request) > 3 or command_name not in ('COURSE', 'EXCHANGE', 'STOP') or \
            (command_name == 'STOP' and len(user_request) > 1) or \
            (command_name == 'COURSE' and len(user_request) == 1) or \
            (command_name == 'EXCHANGE' and 1 <= len(user_request) < 3):

        print('INVALID COMMAND')

    elif command_name == 'STOP':
        print('SERVICE STOPPED')
        break

    elif currency_name not in ('USD', 'UAH'):
        print(f'INVALID CURRENCY {currency_name}')

    elif len(user_request) == 2:

        if command_name == 'COURSE' and currency_name == 'USD':
            print(f"RATE {sale_usd}, AVAILABLE {available_usd}")

        elif command_name == 'COURSE' and currency_name == 'UAH':
            print(f"RATE {buy_usd}, AVAILABLE {available_uah}")


    elif len(user_request) == 3:

        amount_currency: str = user_request[2]

        if not amount_currency.isdigit():
            print('INVALID COMMAND')

        elif command_name == 'EXCHANGE' and currency_name == 'USD':

            required_balance: float = float(amount_currency) * buy_usd

            if required_balance > available_uah:
                print(f"UNAVAILABLE, REQUIRED BALANCE UAH {required_balance}, AVAILABLE {available_uah}")

            else:
                available_uah -= required_balance  # Update available balance UAH

                print(f"UAH {round(required_balance, 3)}, RATE {round(buy_usd, 3)}")

        elif command_name == 'EXCHANGE' and currency_name == 'UAH':

            required_balance: float = float(amount_currency) / sale_usd

            if required_balance > available_usd:
                print(f"UNAVAILABLE, REQUIRED BALANCE USD {required_balance}, AVAILABLE {available_usd}")

            else:
                available_usd -= required_balance  # Update available balance UAH

                print(f'USD {round(required_balance, 3)}, RATE {round(required_balance / float(amount_currency), 3)}')
