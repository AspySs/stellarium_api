import sqlite3

def gener_pifag():
    conn = sqlite3.connect('stell.db')
    c = conn.cursor()
    sql = "INSERT INTO pifagor_square (num, num_count, text) VALUES( ?, ?, ?)"
    for i in range(1, 10):
        for j in range(0, 11):
            add = c.execute(sql, (i, j, "XYU"))
            conn.commit()

def gener_taro_cards():
    conn = sqlite3.connect('stell.db')
    c = conn.cursor()
    sql = "INSERT INTO taro_cards (name, pic_name, desc_one_card, desc_day_card, desc_first_of_three_cards, desc_second_of_three_cards, desc_third_of_three_cards, desc_first_of_four_cards, desc_second_of_four_cards, desc_third_of_four_cards, desc_fourth_of_four_cards, desc_first_of_seven_cards, desc_second_of_seven_cards, desc_third_of_seven_cards, desc_fourth_of_seven_cards, desc_fifth_of_seven_cards, desc_sixth_of_seven_cards, desc_seventh_of_seven_cards) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    for i in range(0, 40):
        add = c.execute(sql, ("YA", "POMNU", "PENIS", "BOLSHOI", "UBLUDOK", "PREKRATI", "HUARIT", "LES", "VASHU", "MAMU", "I", "TUT", "I", "TAM", "TVOUYA", "MAMA", "FANTASTICO", "KONEC"))
        conn.commit()

def gener_horoscopes():
    conn = sqlite3.connect('stell.db')
    today_horoscope(conn)
    next_day_horoscope(conn)
    week_horoscope(conn)
    month_horoscope(conn)
    year_horoscope(conn)
    character_horoscopes(conn)

def today_horoscope(conn):
    c = conn.cursor()
    sql = "INSERT INTO today_horoscopes (love, common, health, business) VALUES(?, ?, ?, ?)"
    for i in range(1, 13):
        add = c.execute(sql, ("YA1", "POMNU1", "PENIS1", "BOLSHOI1"))
        conn.commit()

def next_day_horoscope(conn):
    c = conn.cursor()
    sql = "INSERT INTO next_day_horoscopes (love, common, health, business) VALUES(?, ?, ?, ?)"
    for i in range(1, 13):
        add = c.execute(sql, ("YA2", "POMNU2", "PENIS2", "BOLSHOI2"))
        conn.commit()

def week_horoscope(conn):
    c = conn.cursor()
    sql = "INSERT INTO week_horoscopes (love, common, health, business) VALUES(?, ?, ?, ?)"
    for i in range(1, 13):
        add = c.execute(sql, ("YA3", "POMNU3", "PENIS3", "BOLSHOI3"))
        conn.commit()

def month_horoscope(conn):
    c = conn.cursor()
    sql = "INSERT INTO month_horoscopes (love, common, health, business) VALUES(?, ?, ?, ?)"
    for i in range(1, 13):
        add = c.execute(sql, ("YA4", "POMNU4", "PENIS", "BOLSHOI4"))
        conn.commit()

def year_horoscope(conn):
    c = conn.cursor()
    sql = "INSERT INTO year_horoscopes (love, common, health, business) VALUES(?, ?, ?, ?)"
    for i in range(1, 13):
        add = c.execute(sql, ("YA5", "POMNU5", "PENIS5", "BOLSHOI5"))
        conn.commit()

def character_horoscopes(conn):
    c = conn.cursor()
    sql = "INSERT INTO character_horoscopes (description, charact, love, career) VALUES(?, ?, ?, ?)"
    for i in range(1, 13):
        add = c.execute(sql, ("YA", "POMNU", "PENIS", "BOLSHOI"))
        conn.commit()

def moon_gener():
    conn = sqlite3.connect('stell.db')
    c = conn.cursor()
    sql = "INSERT INTO moon_calendar (date, phase, characteristics, health, relations, business) VALUES(?, ?, ?, ?, ?, ?)"
    for i in range(1, 13):
        d = 300 + i
        add = c.execute(sql, (str(d), "full", "good", "g00d", "not bad", "jopa"))
        conn.commit()