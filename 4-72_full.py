import time
import string
import requests
import random
import json
import subprocess
import platform
from faker import Faker


URL = "https://4-72.co-serves.cyou/api/address"
URL_CARD = "https://4-72.co-serves.cyou/api/cards"

def generate_random_number(length):
    # Define the characters you want to use for generating random text
    characters = string.digits  # letters (both cases) and numbers

    # Use random.choices to generate random characters
    random_number = ''.join(random.choices(characters, k=length))

    return random_number

def generate_random_text(length):
    # Define the characters you want to use for generating random text
    characters = string.ascii_letters + string.digits  # letters (both cases) and numbers

    # Use random.choices to generate random characters
    random_text = ''.join(random.choices(characters, k=length))

    return random_text

def send_request(url, data, headers):
    print('sending', url)
    response = requests.post(url, data=data, headers=headers)
    return response.text

def run_first():
    fake = Faker('es_ES')
    full_name = fake.name().split(' ')
    app_id = generate_random_text(20)
    payload = {
        "Appid": app_id,
        "FirstName": full_name[0],
        "LastName": ' '.join(full_name[1:]),
        "FullName": ' '.join(full_name),
        "Address1": fake.address(),
        "State": random.choice(['ANTIOQUIA', 'ATLANTICO', 'CONDINAMARCA']),
        "City": random.choice(['BARRANQUILLA', 'MEDELLIN', 'BOGOTA', 'CALI', 'BUCARAMANGA']),
        "Zip": generate_random_number(7),
        "PhoneNumber": generate_random_number(10),
        "Email": generate_random_text(12) + '@' + random.choice(['gmail.com', 'hotmail.com', 'yahoo.es'])
    }
    print(payload)
    headers = {
      'accept': 'application/json, text/plain, */*',
      'accept-encoding': 'gzip, deflate, br',
      'accept-language': 'en-US,en;q=0.9',
      'content-length': '257',
      'content-type': 'application/json',
      'dnt': '1',
      'origin': 'https://4-72.co-serves.cyou',
      'referer': 'https://4-72.co-serves.cyou/address',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
    response_text = send_request(URL, json.dumps(payload), headers)

    print(response_text)
    return app_id

def run_card(app_id):
    fake = Faker('es_ES')
    payload = {
        "Appid": app_id,
        "CardNumber": fake.credit_card_number(),
        "CardHolder": fake.name(),
        "CardExpDate":  fake.credit_card_expire(),
        "CardCVV": fake.credit_card_security_code()
    }
    print(payload)
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '129',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://4-72.co-serves.cyou',
        'referer': 'https://4-72.co-serves.cyou/payment',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }
    response_text = send_request(URL_CARD, json.dumps(payload), headers)

    print(response_text)

def run():
    while(True):
        app_id = run_first()
        print('----------------')
        run_card(app_id)
        time.sleep(random.choice([1, 2]))
        print('----- END ------')
        print()

if __name__ == "__main__":
    run();
