from flask import request
import sqlite3

def horoscope_realization():
    sign = int(request.args.get('sign'))
    # подключаемся к БД
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    # подключили
    name = ["NULL", "aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"]
    type = ["love", "common", "health", "business"]
    today = []
    for i in type:
        sql = "SELECT "+ i +" FROM today_horoscopes WHERE id = ?"
        c.execute(sql, (sign, ))
        result = c.fetchone()
        today.append(result[0])
    tomorrow = []
    for i in type:
        sql = "SELECT "+ i +" FROM next_day_horoscopes WHERE id = ?"
        c.execute(sql, (sign, ))
        result = c.fetchone()
        tomorrow.append(result[0])
    week = []
    for i in type:
        sql = "SELECT "+ i +" FROM week_horoscopes WHERE id = ?"
        c.execute(sql, (sign, ))
        result = c.fetchone()
        week.append(result[0])
    month = []
    for i in type:
        sql = "SELECT "+ i +" FROM month_horoscopes WHERE id = ?"
        c.execute(sql, (sign, ))
        result = c.fetchone()
        month.append(result[0])
    year = []
    for i in type:
        sql = "SELECT "+ i +" FROM year_horoscopes WHERE id = ?"
        c.execute(sql, (sign, ))
        result = c.fetchone()
        year.append(result[0])
    type_c = ["description", "charact", "love", "career"]
    character = []
    for i in type_c:
        sql = "SELECT "+ i +" FROM character_horoscopes WHERE id = ?"
        c.execute(sql, (sign, ))
        result = c.fetchone()
        character.append(result[0])

    output = {
        "horoscope": {
            "info": {
                "id": sign,
                "name": name[sign]
            },
            "today": {
               "love": today[0],
               "common": today[1],
               "health": today[2],
               "business": today[3]
            },
            "tomorrow": {
               "love": tomorrow[0],
               "common": tomorrow[1],
               "health": tomorrow[2],
               "business": tomorrow[3]
            },
            "week": {
               "love": week[0],
               "common": week[1],
               "health": week[2],
               "business": week[3]
            },
            "month": {
               "love": month[0],
               "common": month[1],
               "health": month[2],
               "business": month[3]
            },
            "year": {
               "love": year[0],
               "common": year[1],
               "health": year[2],
               "business": year[3]
            },
            "character": {
               "description": character[0],
               "charact": character[1],
               "love": character[2],
               "career": character[3]
            },
        }
    }
    return output