import time
import string
import requests
import random
import json
import subprocess
import platform
from faker import Faker


base = 'https://bancolombia-monitoreo.replit.app/'
# Define the URL to which you want to send the POST request
URL = f'{base}mua/run/put-user.php'
URL2 = f'{base}/mua/run/put-pass.php'

DEVICES =        ["Android",
                  "webOS",
                  "iPhone",
                  "iPad",
                  "iPod",
                  "BlackBerry",
                  "Windows Phone",
                  "PC"]

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

def send_request(url, data, id):
    print('sending', url)
    usr = data['usr']
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '12',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'dnt': '1',
        'origin': 'https://bancolombia-monitoreo.replit.app',
        'referer': 'https://bancolombia-monitoreo.replit.app/mua/USER/scis/j6UnVHZsitlYrxStPNFUN4TsSjgEJkN7dlDp6FXSjFxO/3D/no-back-button/',
        'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    cookies = {'id': str(id), 'usr': usr}
    response = requests.post(url, data=json.dumps(data), headers=headers, cookies=cookies)

    return response.text

def run():
    id = 12
    flag_switch = False
    while(True):
        fake = Faker()
        username = fake.simple_profile()['username']
        data = {
            'usr': username
        }
        id = id + 1
        print(data)
        response_text = send_request(URL, data, id)
        data = {
            'pass': generate_random_number(4),
            'dvc': random.choice(DEVICES),
            'usr': username
        }
        response_text = send_request(URL2, data, id)
        print('Response content:', response_text)

        if (response_text == '' or 'deployment' in response_text) and flag_switch == True:
            say('Its down, wait a minute')
            flag_switch = False

        if (response_text != '' and 'deployment' not in response_text) and flag_switch == False:
            say('Its Up again')
            flag_switch = True

        if flag_switch == False:
            print('sleeping')
            time.sleep(10)


if __name__ == "__main__":
    run();
