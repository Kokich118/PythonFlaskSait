import sqlite3

def request(login, password, email):
    db = sqlite3.connect('./gameWork.db')
    sql = db.cursor()
    users_login = sql.execute(f"SELECT login FROM users WHERE login='{login}'").fetchall()
    db.commit()
    if len(users_login) == 0:
        sql.execute("INSERT INTO users(login, password, email) VALUES (?, ?, ?)", (login, password, email))
        db.commit()
        sql.close()
        db.close()
        return 1
    else:
        return 0