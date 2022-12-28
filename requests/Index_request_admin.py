import sqlite3

def request(id):
    db = sqlite3.connect('./gameWork.db')
    sql = db.cursor()

    sql.execute(f"SELECT admin FROM users WHERE id='{id}'")
    admin = sql.fetchall()
    sql.close()
    db.close()
    print(admin)

    if len(admin) != 0:
        return admin[0][0]
    else:
        return 0