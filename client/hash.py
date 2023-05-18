import os
import sqlite3 as sql
import hashlib
#import main
con = sql.connect('db/cerber_db.db')
cur = con.cursor()
#cur.execute("CREATE TABLE IF NOT EXISTS secret_files(name, path, hash)")
# path = os.path.abspath('2.txt ')
# name = str('2.txt')
# hash = hashlib.md5(open('2.txt', 'rb').read()).hexdigest()
# cur.execute("INSERT into secret_files (name, path, hash) values('" + name + "', '" + path + "', '" + hash + "')")
#con.commit()
result = cur.execute("SELECT * FROM secret_files").fetchall() #смотрим все записи базы
# print(hash)
print(result)
