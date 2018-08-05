#pour ouvrir les ficheirs sqlite3 : https://github.com/sqlitebrowser/sqlitebrowser/releases
#Graph from database : https://www.youtube.com/watch?v=pq4nwICEB4U
import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor() #le curseur permet l'execution des commandes SQL


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

def data_static_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1452549219,'2016-01-11 13:53:39','Python',6)")
    conn.commit() #save change

def data_dynamic_entry():
    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
          (unix, date, keyword, value))
    conn.commit() #save change

def read_from_db():
    c.execute("SELECT * FROM stuffToPlot WHERE value = 3 AND unix > 1452554972")
    for row in c.fetchall():
        print(row)

def update():
    c.execute('UPDATE stuffToPlot SET value = 99 WHERE value = 3')
    conn.commit()

def delete():
    c.execute('DELETE FROM stuffToPlot WHERE value = 99')
    conn.commit()

    
c.close()
conn.close()