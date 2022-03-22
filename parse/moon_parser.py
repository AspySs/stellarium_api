import os
import sqlite3

import requests
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver

MAIN_URL = "https://womoon.ru/m/"

HEADERS = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0',
           'accept': '*/*'}

path = os.path.dirname(os.path.abspath(__file__))+'\\chromedriver.exe'
def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html, dat):
    soup = BeautifulSoup(html, 'html.parser')
    items_phase = soup.findAll('div', class_='col-md-12')
    all_tag_p_phase = items_phase[1].find_all('p')
    items_characteristics = soup.findAll('p', class_='moon_day_spec_parag')
    calendar_ex = []
    calendar_ex.append({
        'date': dat,
        'phase': all_tag_p_phase[0].get_text() + ' ' + all_tag_p_phase[1].get_text(),
        'characteristics': items_characteristics[0].get_text(),
        'health': items_characteristics[1].get_text(),
        'relations': items_characteristics[2].get_text(),
        'business': items_characteristics[3].get_text()
    })
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    c.execute("INSERT INTO moon_calendar (date, phase, characteristics, health, relations, business) VALUES(?, ?, ?, ?, ?, ?)", (calendar_ex[0]['date'], calendar_ex[0]['phase'], calendar_ex[0]['characteristics'], calendar_ex[0]['health'], calendar_ex[0]['relations'], calendar_ex[0]['business']))
    conn.commit()


def parse_moon_to_bd():
    year = datetime.datetime.now().year
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    c.execute("DELETE FROM moon_calendar")
    conn.commit()
    # январь
    for i in range(1, 32):

        dat = str(100 + i)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        browser = webdriver.Chrome(path)
        url = MAIN_URL + str(year) + "-january-" + str(i) + ".html"
        browser.get(url)
        generated_html = browser.page_source
        get_content(generated_html, dat)
        browser.quit()

    # февраль
    count_of_day = 28
    if year % 4 == 0:
        count_of_day = 29
    for i in range(1, count_of_day + 1):
        dat = str(200 + i)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        browser = webdriver.Chrome(path)
        url = MAIN_URL + str(year) + "-february-" + str(i) + ".html"
        browser.get(url)
        generated_html = browser.page_source
        get_content(generated_html, dat)
        browser.quit()

    # март
    for i in range(1, 32):
        dat = str(300 + i)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        browser = webdriver.Chrome(path)
        url = MAIN_URL + str(year) + "-march-" + str(i) + ".html"
        browser.get(url)
        generated_html = browser.page_source
        get_content(generated_html, dat)
        browser.quit()

    # апрель
    for i in range(1, 31):
        dat = str(400 + i)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        browser = webdriver.Chrome(path)
        url = MAIN_URL + str(year) + "-april-" + str(i) + ".html"
        browser.get(url)
        generated_html = browser.page_source
        get_content(generated_html, dat)
        browser.quit()

    # май
    for i in range(1, 32):
        dat = str(500 + i)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        browser = webdriver.Chrome(path)
        url = MAIN_URL + str(year) + "-may-" + str(i) + ".html"
        browser.get(url)
        generated_html = browser.page_source
        get_content(generated_html, dat)
        browser.quit()

    # июнь
    for i in range(1, 31):
        dat = str(600 + i)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        browser = webdriver.Chrome(path)
        url = MAIN_URL + str(year) + "-june-" + str(i) + ".html"
        browser.get(url)
        generated_html = browser.page_source
        get_content(generated_html, dat)
        browser.quit()

    # июль
    for i in range(1, 32):
        dat = str(700 + i)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        browser = webdriver.Chrome(path)
        url = MAIN_URL + str(year) + "-july-" + str(i) + ".html"
        browser.get(url)
        generated_html = browser.page_source
        get_content(generated_html, dat)
        browser.quit()

    # август
    for i in range(1, 32):
        dat = str(800 + i)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        browser = webdriver.Chrome(path)
        url = MAIN_URL + str(year) + "-august-" + str(i) + ".html"
        browser.get(url)
        generated_html = browser.page_source
        get_content(generated_html, dat)
        browser.quit()

    # сентябрь
    for i in range(1, 31):
        dat = str(900 + i)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        browser = webdriver.Chrome(path)
        url = MAIN_URL + str(year) + "-september-" + str(i) + ".html"
        browser.get(url)
        generated_html = browser.page_source
        get_content(generated_html, dat)
        browser.quit()
    # октябрь
    for i in range(1, 32):
        dat = str(1000 + i)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        browser = webdriver.Chrome(path)
        url = MAIN_URL + str(year) + "-october-" + str(i) + ".html"
        browser.get(url)
        generated_html = browser.page_source
        get_content(generated_html, dat)
        browser.quit()
    # ноябрь
    for i in range(1, 31):
        dat = str(1100 + i)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        browser = webdriver.Chrome(path)
        url = MAIN_URL + str(year) + "-november-" + str(i) + ".html"
        browser.get(url)
        generated_html = browser.page_source
        get_content(generated_html, dat)
        browser.quit()
    # декабрь
    for i in range(1, 32):
        dat = str(1200 + i)
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        browser = webdriver.Chrome(path)
        url = MAIN_URL + str(year) + "-december-" + str(i) + ".html"
        browser.get(url)
        generated_html = browser.page_source
        get_content(generated_html, dat)
        browser.quit()

