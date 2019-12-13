import requests
from bs4 import BeautifulSoup as Soup

from tools.files import files_like
from tools.osdir import write
from tools.urls import UrlMaker
import re

FAKE_EMAIL = 'jarl2@bk.ru'
PASSWORD = '123456'
CHINA_CODE = 'CN'

SES_ID = 'ASP.NET_SessionId'
captcha_regex = re.compile(r'\d{6}')

reg_url = UrlMaker.make_url('register')
def extract_captcha(text):
    # assert 'Wrong verification code' in text
    matches = list(captcha_regex.findall(text))
    matches = list(filter(lambda s: s.count('0') != 5, matches))
    if matches:
        return matches[0]

def log_captcha(captcha_url):
    html = f'<img src="{captcha_url}" style="width:300">'
    write('captcha.html', html)

def input_captcha(captcha_num):
    cap_url = UrlMaker.make_url('captcha', {'r': captcha_num})
    log_captcha(cap_url)
    print('wrote, write:')
    return input()


class Register:
    def make_form_data(self, username, captcha, password=PASSWORD, email=FAKE_EMAIL, country=CHINA_CODE):
        form_data = {
            'Action': 'register',
            'Name': username,
            'Password1': password,
            'Password2': password,
            'Email': email,
            'Country': country,
            'Captcha': captcha,
        }
        return form_data

    def make_cookies(self, session_id):
        return {SES_ID: session_id}

    def post(self, name, captcha, session_id):
        files = self.make_form_data(name, captcha)
        cookies = self.make_cookies(session_id)
        return requests.post(reg_url, data=files, cookies=cookies)

    def get_captcha(self, session_id):
        """Getting new captcha, processing it"""
        cookies = {SES_ID: session_id}
        resp = requests.get(reg_url, cookies=cookies)
        captcha_num = extract_captcha(resp.text)
        return input_captcha(captcha_num)

    def is_success(self, resp):
        success = 'Wrong verification code' not in resp.text and 'неверный' not in resp.text
        return success

    def register(self, name, session_id):
        captcha = self.get_captcha(session_id)
        resp = self.post(name, captcha, session_id)
        if self.is_success(resp):
            print('OK,', name)
        else:
            print('BAD,', name)


def make_unit_name(index: int):
    return f'Chinese unit {index}'

ses_id = 'bj0tb4nrzldoywnjavptlb2i'
UNIT = make_unit_name(9)
Register().register(UNIT, ses_id)

# def wonk():
#     ses_id, cap_num  = get()
#     work_cap(resp)
# print(dict(resp.cookies), resp.headers)
# cap = input()
# resp = post(UNIT, cap, SEX)
# honk(resp)
# print(dict(resp.cookies), resp.headers)
# wonk()
