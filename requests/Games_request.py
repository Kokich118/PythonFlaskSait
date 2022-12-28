import sqlite3

def request():
    db = sqlite3.connect('./gameWork.db')
    sql = db.cursor()

    sql.execute("SELECT id, name, text, cost, photo FROM games")
    games_data = sql.fetchall()
    sql.close()
    db.close()

    return games_data