import sqlite3


def request(id, name, text, cost, photo):
    db = sqlite3.connect('./gameWork.db')
    sql = db.cursor()
    sql.execute(f"UPDATE games SET name='{name}', text='{text}', cost='{cost}', photo='{photo}' WHERE id='{id}'")
    db.commit()
    sql.close()
    db.close()


def requestNotFile(id, name, text, cost):
    db = sqlite3.connect('./gameWork.db')
    sql = db.cursor()
    sql.execute(f"UPDATE games SET name='{name}', text='{text}', cost='{cost}' WHERE id='{id}'")
    db.commit()
    sql.close()
    db.close()