from flask import Flask
from flask import request
import sqlite3
from colorama import Fore

import utility.table_gener
import bdCreator
#realizations
from realizations.authorization import auth_realization
from realizations.taro import taro_realization
from realizations.horoscopes import horoscope_realization
from realizations.pifagorSquare import pifagor_realization
from realizations.affirmations import affirmations_realization
from realizations.registration import register_realization
from realizations.moon_cal import moon_calendar_realization
from parse.horoscope_add_to_bd import update_horoscope_table
from realizations.confirm import code_confirm
#realizations

bdCreator.tables_check()
#table_gener.gener_pifag()
#table_gener.gener_horoscopes()
#table_gener.gener_taro_cards()
#table_gener.moon_gener()
update_horoscope_table()
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/confirm/', methods=['GET'])
def conf():
    return (code_confirm())

@app.route('/register/', methods=['GET'])
def registr():
    return (register_realization())

@app.route('/auth/', methods=['GET'])
def auth():
    return (auth_realization())


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

@app.route('/pifagorSquare/', methods=['GET'])
def pifagor():
    return (pifagor_realization())

@app.route('/horoscopes/', methods=['GET'])
def horoscope():
    return (horoscope_realization())


@app.route('/taro/', methods=['GET'])
def taro():
    return (taro_realization())

@app.route('/moonCalendar/', methods=['GET'])
def moon():
    return (moon_calendar_realization())


if __name__ == '__main__':
    app.run()
