import sqlite3

def request(id):
    db = sqlite3.connect('./gameWork.db')
    sql = db.cursor()

    sql.execute(f"SELECT login FROM users WHERE id='{id}'")
    login = sql.fetchall()
    sql.close()
    db.close()

    if len(login) != 0:
        return login[0][0]
    else:
        return "ERROR user"