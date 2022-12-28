import sqlite3

def request(login, password):
    db = sqlite3.connect('./gameWork.db')
    sql = db.cursor()


    users_login = sql.execute("SELECT id, login, password FROM users").fetchall()
    db.commit()
    sql.close()
    db.close()
    def askRequest():
        for value in users_login:
            if (login == value[1]) and (password == value[2]):
                return value[0]
        return 0
    return askRequest()