import random
from flask import Flask
from flask import request
import sqlite3
import colorama
from random import randint
from colorama import Fore, Back, Style
import bdCreator
import json
import table_gener

bdCreator.tables_check()
#table_gener.gener_pifag()
#table_gener.gener_horoscopes()
#table_gener.gener_taro_cards()
app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/register/', methods=['GET'])
def register():
    print(Fore.YELLOW + "Start Registration!")
    username = request.args.get('name')
    print(Fore.YELLOW + "Name: " + username)
    date = request.args.get('birth')
    print(Fore.YELLOW + "Birth date: " + date)
    sex = request.args.get('sex')
    print(Fore.YELLOW + "Sex: " + date)
    #подключаемся к БД
    print(Fore.BLUE + "Подключение к БД....")
    conn = sqlite3.connect("stell.db") # или :memory: чтобы сохранить в RAM
    c = conn.cursor()
    print(Fore.BLUE + "Успешно!")
    #подключили
    try:
        print(Fore.GREEN+ "Добавление записи в бд...")
        add = c.execute(f"INSERT INTO Users (sex, user_name, date_of_birth ) VALUES( ?, ?, ?)", (sex, username, date))
        conn.commit()

    except sqlite3.IntegrityError:
        print(Fore.GREEN + "Добавление записи в бд закончено с ошибкой")
        print(Fore.YELLOW + "End Registration!")
        return "Error"
    c.execute(f"SELECT MAX(id) FROM Users")
    id = c.fetchone()
    print(Fore.GREEN + "Добавление записи в бд закончено успешно")
    print(Fore.YELLOW + "End Registration!")
    return str(id[0])

@app.route('/test/', methods=['GET'])
def test():
    id = request.args.get('id')
    #подключаемся к БД
    print(Fore.BLUE + "Подключение к БД....")
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    print(Fore.BLUE + "Успешно!")
    #подключили
    c.execute(f"SELECT user_name FROM Users WHERE id="+id)
    name = c.fetchone()
    c.execute(f"SELECT sex FROM Users WHERE id="+id)
    sex = c.fetchone()
    c.execute(f"SELECT date_of_birth FROM Users WHERE id="+id)
    date_of_birth = c.fetchone()
    output = {
        "user": {
            "id": str(id),
            "name": str(name[0]),
            "sex": str(sex[0]),
            "date_of_birth": str(date_of_birth[0])
        }
    }
    print(Fore.GREEN + "Вывод данных о юзере закончен успешно")
    return output


@app.route('/affirmation/', methods=['GET'])
def affirm():
    user_id = request.args.get('id')
    #подключаемся к БД
    print(Fore.BLUE + "Подключение к БД....")
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    print(Fore.BLUE + "Успешно!")
    #подключили
    c.execute(f"SELECT MAX(id) FROM Affirmations")
    max = c.fetchone()
    c.execute(f"SELECT MAX(affirm_id) FROM Affirmations_shown WHERE user_id="+user_id)
    if (c.fetchone() is None):
        af_id = randint(1, max[0])
    else:
        c.execute(f"SELECT affirm_id FROM Affirmations_shown WHERE user_id="+user_id)
        except_nums = c.fetchall()
        ran_nums = list(range(1, max[0]+1))
        for i in range(0, len(except_nums)):
            ran_nums.remove(except_nums[i][0])
        try:
            af_id = random.choice(ran_nums)
        except IndexError:
            c.execute(f"DELETE FROM Affirmations_shown WHERE user_id="+user_id)
            conn.commit()
            print("Not enough affirmations to show, restart table")
            af_id = randint(1, max[0])
    c.execute(f"SELECT text FROM Affirmations WHERE id=" + str(af_id))
    text = c.fetchone()
    c.execute(f"SELECT picture FROM Affirmations WHERE id=" + str(af_id))
    pic = c.fetchone()
    affirmation = {
        "affirmation": {
            "id": af_id,
            "text": text[0],
            "picture": pic[0]
        }
    }
    c.execute(f"INSERT INTO Affirmations_shown (user_id, affirm_id) VALUES( ?, ?)", (user_id, af_id))
    conn.commit()
    return affirmation

@app.route('/pifagorSquare/', methods=['GET'])
def pifagor():
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

@app.route('/horoscopes/', methods=['GET'])
def horoscope():
    sign = int(request.args.get('sign'))
    #подключаемся к БД
    print(Fore.BLUE + "Подключение к БД....")
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    print(Fore.BLUE + "Успешно!")
    #подключили
    name = ["null", "capricorn", "taurus", "virgo", "aquarius", "gemini", "libra", "pisces", "cancer", "scorpio", "aries", "leo", "sagittarius"]
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


@app.route('/taro/', methods=['GET'])
def taro():
    count = int(request.args.get('count'))
    if((count != 0) and (count != 1) and (count != 3) and (count != 4) and (count != 7)):
        return "Invalid count of cards error...."
    #подключаемся к БД
    print(Fore.BLUE + "Подключение к БД....")
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    print(Fore.BLUE + "Успешно!")
    c.execute(f"SELECT MAX(id) FROM taro_cards")
    max_ = c.fetchone()
    #подключили
    id_list = list(range(1, max_[0]+1))
    if((count!= 0) and (count != 1)):
        cards_id = []
        for i in range(0, count):
            cards_id.append(random.choice(id_list))
            id_list.remove(cards_id[i])
    else:
        id_card = random.choice(id_list)

    descriptions = []
    names = []
    pic_names = []

    if (count == 0):
        c.execute(f"SELECT desc_day_card FROM taro_cards WHERE id=" + str(id_card))
        descriptions.append(c.fetchone()[0])
        c.execute(f"SELECT name FROM taro_cards WHERE id=" + str(id_card))
        names.append(c.fetchone()[0])
        c.execute(f"SELECT pic_name FROM taro_cards WHERE id=" + str(id_card))
        pic_names.append(c.fetchone()[0])
        output = {
            "taro": {
                "day": {
                    "id": id_card,
                    "name": names[0],
                    "pic_name": pic_names[0],
                    "description": descriptions[0]
                }
            }
        }
        return output

    elif (count == 1):
        c.execute(f"SELECT desc_one_card FROM taro_cards WHERE id=" + str(id_card))
        descriptions.append(c.fetchone()[0])
        c.execute(f"SELECT name FROM taro_cards WHERE id=" + str(id_card))
        names.append(c.fetchone()[0])
        c.execute(f"SELECT pic_name FROM taro_cards WHERE id=" + str(id_card))
        pic_names.append(c.fetchone()[0])
        output = {
            "taro": {
                "one": {
                    "id": id_card,
                    "name": names[0],
                    "pic_name": pic_names[0],
                    "description": descriptions[0]
                }
            }
        }
        return output
    elif(count == 3):
        columns_three = ("desc_first_of_three_cards", "desc_second_of_three_cards", "desc_third_of_three_cards")
        j = 0
        for i in columns_three:
            sql = "SELECT " + i + " FROM taro_cards WHERE id = ?"
            c.execute(sql, (cards_id[j], ))
            descriptions.append(c.fetchone()[0])
            c.execute(f"SELECT name FROM taro_cards WHERE id=" + str(cards_id[j]))
            names.append(c.fetchone()[0])
            c.execute(f"SELECT pic_name FROM taro_cards WHERE id=" + str(cards_id[j]))
            pic_names.append(c.fetchone()[0])
            j = j + 1

        output = {
            "taro": {
                "three": {
                    "first": {
                        "id": cards_id[0],
                        "name": names[0],
                        "pic_name": pic_names[0],
                        "description": descriptions[0]
                    },
                    "second": {
                        "id": cards_id[1],
                        "name": names[1],
                        "pic_name": pic_names[1],
                        "description": descriptions[1]
                    },
                    "third": {
                        "id": cards_id[2],
                        "name": names[2],
                        "pic_name": pic_names[2],
                        "description": descriptions[2]
                    }
                }
            }
        }
        return output

    elif(count == 4):
        columns_four = ("desc_first_of_four_cards", "desc_second_of_four_cards", "desc_third_of_four_cards", "desc_fourth_of_four_cards")
        j = 0
        for i in columns_four:
            sql = "SELECT " + i + " FROM taro_cards WHERE id = ?"
            c.execute(sql, (cards_id[j], ))
            descriptions.append(c.fetchone()[0])
            c.execute(f"SELECT name FROM taro_cards WHERE id=" + str(cards_id[j]))
            names.append(c.fetchone()[0])
            c.execute(f"SELECT pic_name FROM taro_cards WHERE id=" + str(cards_id[j]))
            pic_names.append(c.fetchone()[0])
            j = j + 1

        output = {
            "taro": {
                "three": {
                    "first": {
                        "id": cards_id[0],
                        "name": names[0],
                        "pic_name": pic_names[0],
                        "description": descriptions[0]
                    },
                    "second": {
                        "id": cards_id[1],
                        "name": names[1],
                        "pic_name": pic_names[1],
                        "description": descriptions[1]
                    },
                    "third": {
                        "id": cards_id[2],
                        "name": names[2],
                        "pic_name": pic_names[2],
                        "description": descriptions[2]
                    },
                    "fourth": {
                        "id": cards_id[3],
                        "name": names[3],
                        "pic_name": pic_names[3],
                        "description": descriptions[3]
                    }
                }
            }
        }
        return output
    elif(count == 7):
        columns_seven = ("desc_first_of_seven_cards", "desc_second_of_seven_cards", "desc_third_of_seven_cards", "desc_fourth_of_seven_cards", "desc_fifth_of_seven_cards", "desc_sixth_of_seven_cards", "desc_seventh_of_seven_cards")
        j = 0
        for i in columns_seven:
            sql = "SELECT " + i + " FROM taro_cards WHERE id = ?"
            c.execute(sql, (cards_id[j], ))
            descriptions.append(c.fetchone()[0])
            c.execute(f"SELECT name FROM taro_cards WHERE id=" + str(cards_id[j]))
            names.append(c.fetchone()[0])
            c.execute(f"SELECT pic_name FROM taro_cards WHERE id=" + str(cards_id[j]))
            pic_names.append(c.fetchone()[0])
            j = j + 1

        output = {
            "taro": {
                "three": {
                    "first": {
                        "id": cards_id[0],
                        "name": names[0],
                        "pic_name": pic_names[0],
                        "description": descriptions[0]
                    },
                    "second": {
                        "id": cards_id[1],
                        "name": names[1],
                        "pic_name": pic_names[1],
                        "description": descriptions[1]
                    },
                    "third": {
                        "id": cards_id[2],
                        "name": names[2],
                        "pic_name": pic_names[2],
                        "description": descriptions[2]
                    },
                    "fourth": {
                        "id": cards_id[3],
                        "name": names[3],
                        "pic_name": pic_names[3],
                        "description": descriptions[3]
                    },
                    "fifth": {
                        "id": cards_id[4],
                        "name": names[4],
                        "pic_name": pic_names[4],
                        "description": descriptions[4]
                    },
                    "sixth": {
                        "id": cards_id[5],
                        "name": names[5],
                        "pic_name": pic_names[5],
                        "description": descriptions[5]
                    },
                    "seventh": {
                        "id": cards_id[6],
                        "name": names[6],
                        "pic_name": pic_names[6],
                        "description": descriptions[6]
                    }
                }
            }
        }
        return output


if __name__ == '__main__':
    app.run()
