import sqlite3

def request(id):
    db = sqlite3.connect('./gameWork.db')
    sql = db.cursor()
    photo = sql.execute(f"SELECT photo FROM games WHERE id='{ id }'").fetchall()
    db.commit()
    sql.execute(f"DELETE FROM games WHERE id='{ id }'")
    db.commit()
    sql.execute(f"DELETE FROM comments WHERE id_game='{ id }'")
    db.commit()
    sql.close()
    db.close()
    return photo