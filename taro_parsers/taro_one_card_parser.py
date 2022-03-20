import sqlite3
import time

from selenium import webdriver
from bs4 import BeautifulSoup

name_main = 'ОСНОВНОЕ ЗНАЧЕНИЕ'
name_work = 'РАБОТА'
name_brain = 'СОЗНАНИЕ'
name_love = 'ЛИЧНЫЕ ОТНОШЕНИЯ'

driver = webdriver.Firefox(executable_path='E:\geckodriver.exe')
taro = {}
conn = sqlite3.connect("/stell.db")
c = conn.cursor()

while len(taro) < 78:
    driver.get('https://tragos.ru/taro/one-card')
    element = driver.find_element_by_css_selector('#setr')
    element.click()
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    item = soup.find('div', {'id': 'taro_answer'})
    characteric = item.find_all('p')
    name = item.find('fieldset').find('legend').get_text(strip=True)[17:]
    taro[name] = {
        'main': characteric[0].get_text(strip=True),
        'work': characteric[1].get_text(strip=True),
        'brain': characteric[2].get_text(strip=True),
        'love': characteric[3].get_text(strip=True)
    }
    print(len(taro))

for item in taro.keys():
    data = name_main + '\n\n' + taro[item].get('main') + '\n\n' + name_work + '\n\n' + taro[item].get(
        'work') + '\n\n' + name_brain + '\n\n' + taro[item].get('brain') + '\n\n' + name_love + '\n\n' + taro[item].get(
        'love')
    c.execute("UPDATE taro_cards set desc_one_card = ? WHERE name = ?",
              (data, item.capitalize()))
    conn.commit()
