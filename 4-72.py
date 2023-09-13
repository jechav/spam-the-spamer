import time
import string
import requests
import random
import json
import subprocess
import platform
from faker import Faker


URL = "https://4-72.co-serves.cyou/api/address"

def say(text):
    if platform.system() == 'Darwin':
        subprocess.run(['say', text])

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

def send_request(url, data):
    print('sending', url)
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
    response = requests.post(url, data=data, headers=headers)

    return response.text

def run():
    fake = Faker('es_ES')
    while(True):
        full_name = fake.name().split(' ')
        payload = {
          "Appid": generate_random_text(20),
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
        response_text = send_request(URL, json.dumps(payload))

        print(response_text)
        time.sleep(random.choice([1, 2]))

if __name__ == "__main__":
    run();
