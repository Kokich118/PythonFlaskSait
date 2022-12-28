import sqlite3

def request(id_game):
    db = sqlite3.connect('./gameWork.db')
    sql = db.cursor()

    sql.execute(f"SELECT id, name, text, cost, photo FROM games WHERE id='{id_game}'")
    games_data = sql.fetchall()
    sql.close()
    db.close()

    return games_data

def photo(id_game):
    db = sqlite3.connect('./gameWork.db')
    sql = db.cursor()

    sql.execute(f"SELECT photo FROM games WHERE id='{id_game}'")
    photo = sql.fetchall()
    sql.close()
    db.close()

    return photo