import random
import sqlite3
from flask import request


def taro_realization():
    count = int(request.args.get('count'))
    if ((count != 0) and (count != 1) and (count != 3) and (count != 4) and (count != 7)):
        return "Invalid count of cards error...."
    # подключаемся к БД
    conn = sqlite3.connect("stell.db")
    c = conn.cursor()
    # подключили
    c.execute(f"SELECT MAX(id) FROM taro_cards")
    max_ = c.fetchone()
    id_list = list(range(1, max_[0] + 1))
    if ((count != 0) and (count != 1)):
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
            "day": {
                "id": id_card,
                "name": names[0],
                "pic_name": pic_names[0],
                "description": descriptions[0]
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
            "one": {
                "id": id_card,
                "name": names[0],
                "pic_name": pic_names[0],
                "description": descriptions[0]
            }
        }
        return output
    elif (count == 3):
        columns_three = ("desc_first_of_three_cards", "desc_second_of_three_cards", "desc_third_of_three_cards")
        j = 0
        for i in columns_three:
            sql = "SELECT " + i + " FROM taro_cards WHERE id = ?"
            c.execute(sql, (cards_id[j],))
            descriptions.append(c.fetchone()[0])
            c.execute(f"SELECT name FROM taro_cards WHERE id=" + str(cards_id[j]))
            names.append(c.fetchone()[0])
            c.execute(f"SELECT pic_name FROM taro_cards WHERE id=" + str(cards_id[j]))
            pic_names.append(c.fetchone()[0])
            j = j + 1

        output = {
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
        return output

    elif (count == 4):
        columns_four = ("desc_first_of_four_cards", "desc_second_of_four_cards", "desc_third_of_four_cards",
                        "desc_fourth_of_four_cards")
        j = 0
        for i in columns_four:
            sql = "SELECT " + i + " FROM taro_cards WHERE id = ?"
            c.execute(sql, (cards_id[j],))
            descriptions.append(c.fetchone()[0])
            c.execute(f"SELECT name FROM taro_cards WHERE id=" + str(cards_id[j]))
            names.append(c.fetchone()[0])
            c.execute(f"SELECT pic_name FROM taro_cards WHERE id=" + str(cards_id[j]))
            pic_names.append(c.fetchone()[0])
            j = j + 1

        output = {
            "four": {
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
        return output
    elif (count == 7):
        columns_seven = ("desc_first_of_seven_cards", "desc_second_of_seven_cards", "desc_third_of_seven_cards",
                         "desc_fourth_of_seven_cards", "desc_fifth_of_seven_cards", "desc_sixth_of_seven_cards",
                         "desc_seventh_of_seven_cards")
        j = 0
        for i in columns_seven:
            sql = "SELECT " + i + " FROM taro_cards WHERE id = ?"
            c.execute(sql, (cards_id[j],))
            descriptions.append(c.fetchone()[0])
            c.execute(f"SELECT name FROM taro_cards WHERE id=" + str(cards_id[j]))
            names.append(c.fetchone()[0])
            c.execute(f"SELECT pic_name FROM taro_cards WHERE id=" + str(cards_id[j]))
            pic_names.append(c.fetchone()[0])
            j = j + 1

        output = {
            "seven": {
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
        return output
