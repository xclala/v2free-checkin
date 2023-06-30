from os import environ
import requests

email = environ['EMAIL']
password = environ['PASSWORD']
headers = {
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58"
}
r = requests.post('https://v2free.org/auth/login',
                headers=headers,
                json={
                    'email': email,
                    'passwd': password,
                    'remember_me': True
                })
requests.post('https://v2free.org/user/checkin', cookies=r.cookies, json="")
