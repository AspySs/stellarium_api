import sqlite3
import colorama
from colorama import Fore, Back, Style

def gener_info():
    conn = sqlite3.connect('stell.db')
    c = conn.cursor()
    sql = "INSERT INTO pifagor_square (num, num_count, text) VALUES( ?, ?, ?)"
    for i in range(1, 10):
        for j in range(0, 11):
            add = c.execute(sql, (i, j, "XYU"))
            conn.commit()
