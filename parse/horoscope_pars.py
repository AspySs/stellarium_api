import requests
from bs4 import BeautifulSoup
import os

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
           'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    item = soup.find('div', class_='horoscope_main')
    horoscope = []
    horoscope.append({
        'main': item.find('div', class_='horoscope_text').get_text(strip=True),
        'business': item.find('div', {'id': 'fixed-business'}).find('div', 'horoscope_items').get_text(strip=True),
        'health': item.find('div', {'id': 'fixed-health'}).find('div', 'horoscope_items').get_text(strip=True),
        'love': item.find('div', {'id': 'fixed-love'}).find('div', 'horoscope_items').get_text(strip=True)
    })
    return horoscope


def get_content_character(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('div', class_='horoscope_text').find_all('p')
    description = ''
    charact = ''
    career = ''
    love = ''
    for i in range(0, 16):
        if i != 2 and i != 3 and i != 7 and i != 12:
            charact += items[i].get_text() if charact == '' else '\n' + items[i].get_text()

    for i in range(17, 21):
        description += items[i].get_text() if description == '' else '\n' + items[i].get_text()

    for i in range(21, 26):
        if i != 22:
            career += items[i].get_text() if career == '' else '\n' + items[i].get_text()

    for i in range(27, 42):
        if i != 30 and i != 35:
            love += items[i].get_text() if love == '' else '\n' + items[i].get_text()

    character = []
    character.append({
        'description': description,
        'charact': charact,
        'love': love,
        'career': career
    })

    return character


def parse():
    horoscope_today = []
    horoscope_tomorrow = []
    horoscope_week = []
    horoscope_month = []
    horoscope_year = []
    horoscope_character = []

    for x in range(1, 13):
        url_today = 'https://globalmsk.ru/horoscope/today/{}'.format(x)
        html = get_html(url_today)
        horoscope_today.extend(get_content(html.text))

        url_tomorrow = 'https://globalmsk.ru/horoscope/tomorrow/{}'.format(x)
        html = get_html(url_tomorrow)
        horoscope_tomorrow.extend(get_content(html.text))

        url_week = 'https://globalmsk.ru/horoscope/week/{}'.format(x)
        html = get_html(url_week)
        horoscope_week.extend(get_content(html.text))

        url_month = 'https://globalmsk.ru/horoscope/month/{}'.format(x)
        html = get_html(url_month)
        horoscope_month.extend(get_content(html.text))

        url_year = 'https://globalmsk.ru/horoscope/year/{}'.format(x)
        html = get_html(url_year)
        horoscope_year.extend(get_content(html.text))

        url_character = 'https://globalmsk.ru/sign/{}'.format(x)
        html = get_html(url_character)
        horoscope_character.extend(get_content_character(html.text))

    path = ["horo_txts/classic/", "horo_txts/char/"]
    time = ["today_", "tomorrow_", "week_", "month_", "year_"]
    files = ["main.txt", "business.txt", "health.txt", "love.txt"]
    types = ["main", "business", "health", "love"]
    char_types = ["description", "charact", "love", "career"]
    char_files = ["description.txt", "charact.txt", "love.txt", "career.txt"]
    signs = ["leo/", "virgo/", "aries/", "scorpio/", "taurus/", "libra/", "gemini/", "cancer/", "capricorn/", "aquarius/", "pisces/", "sagittarius/"]
    horoscopes = [horoscope_today, horoscope_tomorrow, horoscope_week, horoscope_month, horoscope_year]
    j = 0
    horo = 0
    signs_arr = 0
    cur_path = os.path.dirname(__file__)
    for s in signs:
        for t in time:
            for i in types:
                if(horo==5):
                    horo = 0
                file = open(cur_path + "/" + path[0] + s + t + files[j],'w')
                file.write(horoscopes[horo][signs_arr][i])
                file.close()
                j = j+1
                if(j == 4):
                    j = 0
            j = 0
            horo = horo+1
        signs_arr = signs_arr+1
    signs_arr = 0
    j = 0
    for s in signs:
        for i in char_types:
            file = open(cur_path + "/" + path[1] + s + char_files[j],'w')
            file.write(horoscope_character[signs_arr][i])
            file.close()
            j = j+1
            if(j == 4):
                j = 0
        j = 0
        signs_arr = signs_arr + 1



parse()