import sqlite3
import time

class dbConnection:
    def __init__(self):
        self.datatimeFormat = "%04d-%02d-%02d %02d:%02d:%02d"

    def insertIntoFavoriteUpdate(self, name, url):
        with sqlite3.connect("test.db") as conn:
            now = time.localtime()

            s = self.datatimeFormat % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
            print(s)
            cur = conn.cursor()
            # conn.execute('''create table favoriteUpdate(
            #             id integer primary key autoincrement,
            #            name text not null,
            #            url text,
            #            date datetime);''')

            InsertCommand = "INSERT INTO favoriteUpdate values(null, '%s', '%s', '%s')" % (name, url, s)
            print(InsertCommand)
            conn.execute(InsertCommand)
            cur.execute("select * from favoriteUpdate")
            for row in cur.fetchall():
                print(row)
    def printAll(self):
        ret = []
        with sqlite3.connect("test.db") as conn:

            cur = conn.cursor()
            cur.execute("select * from favoriteUpdate;")
            for row in cur.fetchall():
                print(row)
                ret.append(row)
        return ret
    def createTable(self):
        with sqlite3.connect("test.db") as conn:
            conn.execute('''create table favoriteUpdate(
                        id integer primary key autoincrement,
                       name text not null,
                       url text,
                       date datetime);''')
