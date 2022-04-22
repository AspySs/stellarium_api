import os
import sqlite3
import time
from colorama import Fore
from selenium import webdriver
from bs4 import BeautifulSoup

path = os.path.dirname(os.path.abspath(__file__))+'\\geckodriver.exe'
driver = webdriver.Firefox(executable_path=path)
taro = {}
conn = sqlite3.connect("/stell.db")
c = conn.cursor()
print(Fore.BLUE + "Успешно!")

while len(taro) < 78:
    driver.get('https://tragos.ru/taro/card-of-the-day')
    element = driver.find_element_by_css_selector('#setr')
    element.click()
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    item = soup.find('div', {'id': 'taro_answer'})
    characteric = item.find_all('p')
    name = item.find('h3').get_text(strip=True)[17:]
    text = ''
    for item in characteric:
        text += item.get_text(strip=True)
        text += '\n'
    taro[name] = {
        'text': text,
    }
    print(len(taro))

for item in taro.keys():
    c.execute("UPDATE taro_cards set desc_day_card = ? WHERE name = ?",
              (taro[item].get('text')[1:-1], item[1:-1].capitalize()))
    conn.commit()
