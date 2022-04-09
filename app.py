from flask import Flask
from flask import request
import sqlite3
from colorama import Fore

import utility.table_gener
import bdCreator
#realizations
from realizations.user_exist import user_is_exist
from realizations.affirm_like import add_affirm_to_liked, delete_affirm_from_liked, get_affirm_from_liked
from realizations.authorization import auth_realization
from realizations.taro import taro_realization
from realizations.horoscopes import horoscope_realization
from realizations.pifagorSquare import pifagor_realization
from realizations.affirmations import affirmations_realization
from realizations.registration import register_realization
from realizations.moon_cal import moon_calendar_realization
from parse.horoscope_add_to_bd import update_horoscope_table
from realizations.confirm import code_confirm
from parse.moon_parser import parse_moon_to_bd
from realizations.comp_name import name_comp_realization
from realizations.comp_horo import horo_comp_realization
from realizations.numerology import numerology_realization
from realizations.affirmations import affirmations_not_reg_realization
from realizations.check_confirm import check_confirm
#realizations

bdCreator.tables_check()

app = Flask(__name__)
password = "awd123dSR4rsdf3afds4"

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/updatemoon/', methods=['GET'])
def upd_moon():
    print(Fore.RED + "ОТПРАВЛЕН ЗАПРОС НА ОБНОВЛЕНИЕ ТАБЛИЦЫ С ЛУННЫМ КАЛЕНДАРЕМ!!!")
    if(password == str(request.args.get('pass'))):
        print(Fore.YELLOW + "пароль подтвержден начинаю обновление!")
        parse_moon_to_bd()  # запускать раз в год 30-31дек
        print(Fore.GREEN + "закончил обновление!")
        return 'Success'
    else:
        print(Fore.RED + "пароль не верный!")
        return ':('


@app.route('/updatehoro/', methods=['GET'])
def upd_horo():
    print(Fore.RED + "ОТПРАВЛЕН ЗАПРОС НА ОБНОВЛЕНИЕ ТАБЛИЦЫ С ГОРОСКОПАМИ!!!")
    if(password == str(request.args.get('pass'))):
        print(Fore.YELLOW + "пароль подтвержден начинаю обновление!")
        update_horoscope_table() # поставить задачу на ежедневный парс гороскопов заранее
        print(Fore.GREEN + "закончил обновление!")
        return 'Success'
    else:
        print(Fore.RED + "пароль не верный!")
        return ':('

@app.route('/confirm/', methods=['GET'])
def conf():
    return (code_confirm())

@app.route('/register/', methods=['GET'])
def registr():
    return (register_realization())

@app.route('/auth/', methods=['GET'])
def auth():
    return (auth_realization())

@app.route('/user_exist/', methods=['GET'])
def user_exist():
    return (user_is_exist())

@app.route('/check_confirm/', methods=['GET'])
def check_confirmation():
    return check_confirm()

@app.route('/check_uid/', methods=['GET'])
def check_uniqueID():
    return check_uid()

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
    return (affirmations_realization())

@app.route('/affirmationNotReg/')
def affirm_not_reg():
    return (affirmations_not_reg_realization())

@app.route('/pifagorSquare/', methods=['GET'])
def pifagor():
    return (pifagor_realization())

@app.route('/horoscopes/', methods=['GET'])
def horoscope():
    return (horoscope_realization())


@app.route('/taro/', methods=['GET'])
def taro():
    return (taro_realization())

@app.route('/like_affirm/', methods=['GET'])
def like_affirm():
    return (add_affirm_to_liked())

@app.route('/unlike_affirm/', methods=['GET'])
def unlike_affirm():
    return (delete_affirm_from_liked())

@app.route('/get_liked_affirm/', methods=['GET'])
def get_liked_affirm():
    return (get_affirm_from_liked())

@app.route('/moonCalendar/', methods=['GET'])
def moon():
    return (moon_calendar_realization())

@app.route('/compName/', methods=['GET'])
def comp_name():
    return (name_comp_realization())

@app.route('/compHoro/', methods=['GET'])
def comp_horo():
    return (horo_comp_realization())

@app.route('/numerology/', methods=['GET'])
def numerology():
    return (numerology_realization())

if __name__ == '__main__':
    app.run(host="192.168.1.105", port=5000)
