import flask
import sqlite3

conn = sqlite3.connect("test.db", isolation_level=None)

c = conn.cursor()

'''c.execute("CREATE TABLE IF NOT EXISTS table1 \
    (id integer PRIMARY KEY, name text, birthday text)")

c.execute("INSERT INTO table1(id, name, birthday) \
    VALUES(?,?,?)", \
    (2, 'KIM', '1990-00-00')) '''

c.execute("Select * from table1")
print(c.fetchall())

print()

c.execute("Select * from table1")
for row in c.fetchall():
    print(row)