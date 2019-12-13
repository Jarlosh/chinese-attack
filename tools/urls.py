from typing import Dict

HTTPS = 'https'
TIMUS_URL = 'timus.online'
ASPX = 'aspx'

class TimusMethods:
    SUBMIT = 'submit'

class UrlMaker:
    @staticmethod
    def make_url(action, params=None, site=TIMUS_URL, protocol=HTTPS, ending='.'+ASPX):
        url = f'{protocol}://{site}/{action}{ending}'
        if params:
            encoded = UrlMaker.url_encode(params)
            url += f'?{encoded}'
        return url

    @staticmethod
    def url_encode(params: Dict):
        encoded = '&'.join((f'{key}={val}' for key, val in params.items()))
        return encoded

# print(UrlMaker.make_url(TimusMethods.SUBMIT, {'honk': 3}))









