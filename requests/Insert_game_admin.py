import sqlite3

def request(name, cost, text, filename):
    db = sqlite3.connect('./gameWork.db')
    sql = db.cursor()
    sql.execute("INSERT INTO games(name, text, cost, photo) VALUES (?, ?, ?, ?)", (name, text, cost, filename))
    db.commit()
    sql.close()
    db.close()