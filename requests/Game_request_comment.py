import sqlite3


def request(id_game, id, comment, grade):
    db = sqlite3.connect('./gameWork.db')
    sql = db.cursor()
    login = sql.execute(f"SELECT login FROM users WHERE id='{id}'").fetchall()
    db.commit()
    sql.execute("INSERT INTO comments(id_game, name, text, grade) VALUES (?, ?, ?, ?)", (id_game, login[0][0], comment, grade))
    db.commit()
    sql.close()
    db.close()