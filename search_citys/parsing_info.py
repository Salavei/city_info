import requests
from bs4 import BeautifulSoup

USER_AGENT = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15',
    'Accept-Language': 'ru',
}


def start_parse(name: str) -> dict:
    info_c = requests.get(
        url='https://www.google.com/search?q={}'.format(name),
        headers=USER_AGENT)
    img_c = requests.get(url='https://www.google.com/search?tbm=isch&hl=ru-BY&source=hp&q={}'.format(name),
                         headers=USER_AGENT)
    soup_c = BeautifulSoup(info_c.text, 'lxml')
    place_city = soup_c.find('div', {'class': 'wwUB2c'}).text
    about = soup_c.find('div', {'class': 'kno-rdesc'}).select_one('span').text
    try:
        weather = soup_c.find_all('span', {'class': 'LrzXr'})[0].text
        time = soup_c.find_all('span', {'class': 'LrzXr'})[1].text
    except IndexError:
        time, weather = 'Отсутствует', 'Отсутствует'
    soup_img = BeautifulSoup(img_c.text, 'lxml')
    img1 = soup_img.find_all('a', {'class': 'nfEiy'})
    data = {'place': place_city, 'about': about, 'weather': weather, 'time': time}
    img_list = []
    for i in img1:
        for j in i.find_all('img'):
            if j.get('data-src'):
                img_list.append(j.get('data-src'))

    data['img'] = img_list
    return data
