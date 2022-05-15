import sqlite3
from flask import request


def pifagor_realization():
    day = int(request.args.get('day'))
    month = int(request.args.get('month'))
    year = int(request.args.get('year'))
    firstWorkNumber = 0
    secondWorkNumber = 0
    fourthWorkNumber = 0

    for i in range(0, len(str(day))):
        firstWorkNumber += int(str(day)[i])
    for i in range(0, len(str(month))):
        firstWorkNumber += int(str(month)[i])
    for i in range(0, len(str(year))):
        firstWorkNumber += int(str(year)[i])

    for i in range(0, len(str(firstWorkNumber))):
        secondWorkNumber += int(str(firstWorkNumber)[i])
    thirdWorkNumber = abs(firstWorkNumber - (2 * int(str(day)[0])))

    for i in range(0, len(str(thirdWorkNumber))):
        fourthWorkNumber += int(str(thirdWorkNumber)[i])

    resultStr = str(day) + str(month) + str(year) + str(firstWorkNumber) + str(secondWorkNumber) + str(thirdWorkNumber) + str(fourthWorkNumber)
    result = list(range(0,10))
    for i in range(0,len(result)):
        result[i] = resultStr.count(str(i))
    # подключаемся к БД
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    # подключили
    text = []
    sql = "SELECT text FROM pifagor_square WHERE num = ? AND num_count = ?"
    for i in range(1, 10):
        c.execute(sql, (i, result[i]))
        text0 = c.fetchone()
        text.append(text0[0])
    output = {
        "one": {
            "count": result[1],
            "text": text[0]
        },
        "two": {
            "count": result[2],
            "text": text[1]
        },
        "three": {
            "count": result[3],
            "text": text[2]
        },
        "four": {
            "count": result[4],
            "text": text[3]
        },
        "five": {
            "count": result[5],
            "text": text[4]
        },
        "six": {
            "count": result[6],
            "text": text[5]
        },
        "seven": {
            "count": result[7],
            "text": text[6]
        },
        "eight": {
            "count": result[8],
            "text": text[7]
        },
        "nine": {
            "count": result[9],
            "text": text[8]
        }
    }
    return output