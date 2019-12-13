from io import BytesIO
import requests
from PIL import Image
import pytesseract

from tools.urls import UrlMaker


def cap_url(cap_num):
    return UrlMaker.make_url('captcha', {'r': cap_num})

def get_captcha_page(cap_num):
    return requests.get(cap_url(cap_num), stream=True).raw

class CaptchaSolver:
    def load_img(self, image_url):
        resp = requests.get(image_url)
        image = Image.open(BytesIO(resp.content))
        return image


_cap_num = 835607
_cap_url = cap_url(_cap_num)

cs = CaptchaSolver()
i: Image = cs.load_img(_cap_url)
i.save('original.png')
gray = i.convert('L')
gray.save('gray.png')
bw = gray.point(lambda x: 0 if x < 1 else 255, '1')
bw.save('threshold.png')

pytesseract.image_to_string(gray)
