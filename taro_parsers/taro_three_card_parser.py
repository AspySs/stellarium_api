import re
import sqlite3
import time

from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Firefox(executable_path='E:\geckodriver.exe')
conn = sqlite3.connect("/stell.db")
c = conn.cursor()

taro1 = {}
taro2 = {}
taro3 = {}

while len(taro1) < 78 or len(taro2) < 78 or len(taro3) < 78:
    driver.get('https://tragos.ru/taro/three-cards')
    element = driver.find_element_by_css_selector('#setr')
    element.click()
    time.sleep(3)
    card1 = driver.find_element_by_css_selector('#taro-list0')
    card2 = driver.find_element_by_css_selector('#taro-list1')
    card3 = driver.find_element_by_css_selector('#taro-list2')
    card1.click()
    card2.click()
    card3.click()
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    item = soup.find('div', {'id': 'taro_answer'})
    characteristic = item.find_all('td', class_="rgt")
    if characteristic[0].find('b').get_text(strip=True).find('перевернутая') == -1:
        name1 = characteristic[0].find('b').get_text(strip=True)
        text1 = characteristic[0].find('i').get_text(strip=True)
        text1 += '\n\n'
        array1 = characteristic[0].find('p')
        array1.b.decompose()
        array1.i.decompose()
        text1 += array1.get_text(strip=True)
        text1 += '\n'
        taro1[name1] = {
            'text': text1
        }

    if characteristic[1].find('b').get_text(strip=True).find('перевернутая') == -1:
        name2 = characteristic[1].find('b').get_text(strip=True)
        text2 = characteristic[1].find('i').get_text(strip=True)
        text2 += '\n\n'
        array2 = characteristic[1].find('p')
        array2.b.decompose()
        array2.i.decompose()
        text2 += array2.get_text(strip=True)
        text2 += '\n'
        taro2[name2] = {
            'text': text2
        }

    if characteristic[2].find('b').get_text(strip=True).find('перевернутая') == -1:
        name3 = characteristic[2].find('b').get_text(strip=True)
        text3 = characteristic[2].find('i').get_text(strip=True)
        text3 += '\n\n'
        array3 = characteristic[2].find('p')
        array3.b.decompose()
        array3.i.decompose()
        text3 += array3.get_text(strip=True)
        text3 += '\n'
        taro3[name3] = {
            'text': text3
        }
    print(len(taro1))
    print(len(taro2))
    print(len(taro3))
    print('---------')

for item in taro1.keys():
    result = re.sub(r'(?<=[.])(?=[^\s])', r'\n\n', taro1[item].get('text'))
    c.execute("UPDATE taro_cards set desc_first_of_three_cards = ? WHERE name = ?",
              (result, item.capitalize()))
    conn.commit()

for item in taro2.keys():
    result = re.sub(r'(?<=[.])(?=[^\s])', r'\n\n', taro2[item].get('text'))
    c.execute("UPDATE taro_cards set desc_second_of_three_cards = ? WHERE name = ?",
              (result, item.capitalize()))
    conn.commit()

for item in taro3.keys():
    result = re.sub(r'(?<=[.])(?=[^\s])', r'\n\n', taro3[item].get('text'))
    c.execute("UPDATE taro_cards set desc_third_of_three_cards = ? WHERE name = ?",
              (result, item.capitalize()))
    conn.commit()
