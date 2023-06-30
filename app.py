from os import environ
import requests

url = environ['URL']
email = environ['EMAIL']
password = environ['PASSWORD']
headers = {
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58"
}
r = requests.post(f'{url}/auth/login',
                headers=headers,
                json={
                    'email': email,
                    'passwd': password,
                    'remember_me': True
                })
requests.post(f'{url}/user/checkin', cookies=r.cookies, json="")
