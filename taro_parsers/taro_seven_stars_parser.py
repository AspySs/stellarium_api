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
taro4 = {}
taro5 = {}
taro6 = {}
taro7 = {}

while len(taro1) < 76 or len(taro2) < 76 or len(taro3) < 76 or len(taro4) < 76 or len(taro5) < 76 or len(taro6) < 76 or len(taro7) < 76:
        driver.get('https://tragos.ru/taro/seven-stars')
        element = driver.find_element_by_css_selector('#setr')
        element.click()
        time.sleep(5)
        card1 = driver.find_element_by_css_selector('#taro-list0')
        card2 = driver.find_element_by_css_selector('#taro-list1')
        card3 = driver.find_element_by_css_selector('#taro-list2')
        card4 = driver.find_element_by_css_selector('#taro-list3')
        card5 = driver.find_element_by_css_selector('#taro-list4')
        card6 = driver.find_element_by_css_selector('#taro-list5')
        card7 = driver.find_element_by_css_selector('#taro-list6')
        card1.click()
        card2.click()
        card3.click()
        card4.click()
        card5.click()
        card6.click()
        card7.click()
        time.sleep(10)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        item = soup.find('div', {'id': 'taro_answer'})
        characteristic = item.find_all('td', class_="rgt")
        if characteristic[0].find('b').get_text(strip=True).find('перевернуто') == -1:
            name1 = characteristic[0].find('b').get_text(strip=True)
            array1 = characteristic[0]
            array1.b.decompose()
            array1.div.decompose()
            array1.h3.decompose()
            array1.br.decompose()
            text1 = array1.get_text(strip=True)
            text1 += '\n'
            taro1[name1] = {
                    'text': text1
                }

        if characteristic[1].find('b').get_text(strip=True).find('перевернуто') == -1:
            name2 = characteristic[1].find('b').get_text(strip=True)
            array2 = characteristic[1]
            array2.b.decompose()
            array2.div.decompose()
            array2.h3.decompose()
            array2.br.decompose()
            text2 = array2.get_text(strip=True)
            text2 += '\n'
            taro2[name2] = {
                    'text': text2
                }

        if characteristic[2].find('b').get_text(strip=True).find('перевернуто') == -1:
            name3 = characteristic[2].find('b').get_text(strip=True)
            array3 = characteristic[2]
            array3.b.decompose()
            array3.div.decompose()
            array3.h3.decompose()
            array3.br.decompose()
            text3 = array3.get_text(strip=True)
            text3 += '\n'
            taro3[name3] = {
                    'text': text3
                }

        if characteristic[3].find('b').get_text(strip=True).find('перевернуто') == -1:
            name4 = characteristic[3].find('b').get_text(strip=True)
            array4 = characteristic[3]
            array4.b.decompose()
            array4.div.decompose()
            array4.h3.decompose()
            array4.br.decompose()
            text4 = array4.get_text(strip=True)
            text4 += '\n'
            taro4[name4] = {
                    'text': text4
                }

        if characteristic[4].find('b').get_text(strip=True).find('перевернуто') == -1:
            name5 = characteristic[4].find('b').get_text(strip=True)
            array5 = characteristic[4]
            array5.b.decompose()
            array5.div.decompose()
            array5.h3.decompose()
            array5.br.decompose()
            text5 = array5.get_text(strip=True)
            text5 += '\n'
            taro5[name5] = {
                    'text': text5
                }

        if characteristic[5].find('b').get_text(strip=True).find('перевернуто') == -1:
            name6 = characteristic[5].find('b').get_text(strip=True)
            array6 = characteristic[5]
            array6.b.decompose()
            array6.div.decompose()
            array6.h3.decompose()
            array6.br.decompose()
            text6 = array6.get_text(strip=True)
            text6 += '\n'
            taro6[name6] = {
                    'text': text6
                }

        if characteristic[6].find('b').get_text(strip=True).find('перевернуто') == -1:
            name7 = characteristic[6].find('b').get_text(strip=True)
            array7 = characteristic[6]
            array7.b.decompose()
            array7.div.decompose()
            array7.h3.decompose()
            array7.br.decompose()
            text7 = array7.get_text(strip=True)
            text7 += '\n'
            taro7[name7] = {
                    'text': text7
                }
        print(len(taro1))
        print(len(taro2))
        print(len(taro3))
        print(len(taro4))
        print(len(taro5))
        print(len(taro6))
        print(len(taro7))
        print('---------')


f1 = open('../taro_txt/seven_stars_your_character.txt', 'w')
f2 = open('../taro_txt/seven_stars_partner_character.txt', 'w')
f3 = open('../taro_txt/seven_stars_partner_behavior.txt', 'w')
f4 = open('../taro_txt/seven_stars_danger.txt', 'w')
f5 = open('../taro_txt/seven_stars_help.txt', 'w')
f6 = open('../taro_txt/seven_stars_secret.txt', 'w')
f7 = open('../taro_txt/seven_stars_perspective.txt', 'w')

for item in taro1.keys():
    c.execute("UPDATE taro_cards set desc_first_of_seven_cards = ? WHERE name = ?",
              (taro1[item].get('text')[:-1], item.capitalize()))
    conn.commit()
    f1.write("%s\n" % item)
    f1.write("\n")
    f1.write("%s\n" % taro1[item].get('text'))
    f1.write("\n")
    f1.write("\n")

for item in taro2.keys():
    c.execute("UPDATE taro_cards set desc_third_of_seven_cards = ? WHERE name = ?",
              (taro2[item].get('text')[:-1], item.capitalize()))
    conn.commit()
    f2.write("%s\n" % item)
    f2.write("\n")
    f2.write("%s\n" % taro2[item].get('text'))
    f2.write("\n")
    f2.write("\n")

for item in taro3.keys():
    c.execute("UPDATE taro_cards set desc_second_of_seven_cards = ? WHERE name = ?",
              (taro3[item].get('text')[:-1], item.capitalize()))
    conn.commit()
    f3.write("%s\n" % item)
    f3.write("\n")
    f3.write("%s\n" % taro3[item].get('text'))
    f3.write("\n")
    f3.write("\n")

for item in taro4.keys():
    c.execute("UPDATE taro_cards set desc_sixth_of_seven_cards = ? WHERE name = ?",
              (taro4[item].get('text')[:-1], item.capitalize()))
    conn.commit()
    f4.write("%s\n" % item)
    f4.write("\n")
    f4.write("%s\n" % taro4[item].get('text'))
    f4.write("\n")
    f4.write("\n")

for item in taro5.keys():
    c.execute("UPDATE taro_cards set desc_seventh_of_seven_cards = ? WHERE name = ?",
              (taro5[item].get('text')[:-1], item.capitalize()))
    conn.commit()
    f5.write("%s\n" % item)
    f5.write("\n")
    f5.write("%s\n" % taro5[item].get('text'))
    f5.write("\n")
    f5.write("\n")

for item in taro6.keys():
    c.execute("UPDATE taro_cards set desc_fifth_of_seven_cards = ? WHERE name = ?",
              (taro6[item].get('text')[:-1], item.capitalize()))
    conn.commit()
    f6.write("%s\n" % item)
    f6.write("\n")
    f6.write("%s\n" % taro6[item].get('text'))
    f6.write("\n")
    f6.write("\n")

for item in taro7.keys():
    c.execute("UPDATE taro_cards set desc_fourth_of_seven_cards = ? WHERE name = ?",
              (taro7[item].get('text')[:-1], item.capitalize()))
    conn.commit()
    f7.write("%s\n" % item)
    f7.write("\n")
    f7.write("%s\n" % taro7[item].get('text'))
    f7.write("\n")
    f7.write("\n")

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()
