import random
from flask import Flask
from flask import request
import sqlite3
import colorama
from random import randint
from colorama import Fore, Back, Style
import json

def pifagor_realization():
    day = int(request.args.get('day'))
    month = int(request.args.get('month'))
    year = int(request.args.get('year'))

    firstWorkNumber = day//10 + day%10 + month//10 + month%10 + year//1000 + ((year//100)%10) + ((year%100)//10) + (year%10)
    secondWorkNumber =  firstWorkNumber//10 + firstWorkNumber%10
    thirdWorkNumber = (firstWorkNumber - 2)* (day//10)
    fourthWorkNumber = thirdWorkNumber//10 + thirdWorkNumber%10
    resultStr = str(day) + str(month) + str(year) + str(firstWorkNumber) + str(secondWorkNumber) + str(thirdWorkNumber) + str(fourthWorkNumber)
    result = list(range(0,10))
    for i in range(0,len(result)):
        result[i] = resultStr.count(str(i))
    #подключаемся к БД
    print(Fore.BLUE + "Подключение к БД....")
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    print(Fore.BLUE + "Успешно!")
    #подключили
    text = []
    sql = "SELECT text FROM pifagor_square WHERE num = ? AND num_count = ?"
    for i in range(1, 10):
        c.execute(sql, (i, result[i]))
        text0 = c.fetchone()
        text.append(text0[0])
    output = {
        "1": {
            "count": result[1],
            "text": text[0]
        },
        "2": {
            "count": result[2],
            "text": text[1]
        },
        "3": {
            "count": result[3],
            "text": text[2]
        },
        "4": {
            "count": result[4],
            "text": text[3]
        },
        "5": {
            "count": result[5],
            "text": text[4]
        },
        "6": {
            "count": result[6],
            "text": text[5]
        },
        "7": {
            "count": result[7],
            "text": text[6]
        },
        "8": {
            "count": result[8],
            "text": text[7]
        },
        "9": {
            "count": result[9],
            "text": text[8]
        }
    }
    return output