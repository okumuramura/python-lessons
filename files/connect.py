import sqlite3

db = sqlite3.connect('chinook.db')

cur = db.cursor()

result = cur.execute('select * from tracks;')

for line in result.fetchall()[:10]:
    print(*line)
