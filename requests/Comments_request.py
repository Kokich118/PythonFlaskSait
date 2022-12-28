import sqlite3

def request(id_game):
    db = sqlite3.connect('./gameWork.db')
    sql = db.cursor()

    comments = sql.execute(f"SELECT name, text, grade FROM comments WHERE id_game='{id_game}'").fetchall()
    sql.close()
    db.close()

    comments.reverse()
    return comments