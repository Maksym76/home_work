import requests

api_url: str = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

response: list = requests.get(api_url).json()

buy_usd: float = float(response[0]['buy'])
sale_usd: float = float(response[0]['sale'])

available_usd: float = 20000.25
available_uah: float = 15364.36

while True:
    user_request: list = input("Write one of the commands 'COURSE USD(UAH)' or 'EXCHANGE UAH(USD) (amount)'.\n"
                               "For exit write 'STOP' : ").strip().upper().split()

    if len(user_request) == 0 or len(user_request) > 3 or user_request[0] not in ('COURSE', 'EXCHANGE', 'STOP') or \
            (user_request[0] == 'STOP' and len(user_request) > 1):
        print('INVALID COMMAND')

    elif user_request[0] == 'STOP':
        print('SERVICE STOPPED')
        break

    elif user_request[1] not in ('USD', 'UAH'):
        print(f'INVALID CURRENCY {user_request[1]}')

    elif len(user_request) == 2:

        if user_request[0] == 'COURSE' and user_request[1] == 'USD':
            print(f"RATE {sale_usd}, AVAILABLE {available_usd}")

        elif user_request[0] == 'COURSE' and user_request[1] == 'UAH':
            print(f"RATE {buy_usd}, AVAILABLE {available_uah}")


    elif len(user_request) == 3:

        if user_request[0] == 'EXCHANGE' and user_request[1] == 'USD':

            req_balance = float(user_request[2]) * buy_usd

            if req_balance > available_uah:
                print(f"UNAVAILABLE, REQUIRED BALANCE UAH {req_balance}, AVAILABLE {available_uah}")

            else:
                available_uah -= req_balance

                print(f"UAH {round(req_balance)}, RATE {buy_usd}")

        elif user_request[0] == 'EXCHANGE' and user_request[1] == 'UAH':

            req_balance = float(user_request[2]) / sale_usd

            if req_balance > available_usd:
                print(f"UNAVAILABLE, REQUIRED BALANCE USD {req_balance}, AVAILABLE {available_usd}")

            else:
                available_usd -= req_balance

                print(f'USD {round(req_balance, 3)}, RATE {round(req_balance / float(user_request[2]), 3)}')

# TODO: разобратьс с 3 аргументом что бы его проверяли состоит он из цифр или нет "elif len(user_request) == 3:"
