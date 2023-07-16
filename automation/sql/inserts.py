import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

new_rows = [
    ('100.100.100','a.b.c',100),
    ('100.100.100','f.d.e',200),
]

cur.executemany("INSERT INTO 'ips' VALUES (?,?,?)",new_rows)
con.commit()

cur.execute("SELECT * FROM 'ips'")
print(cur.fetchall())
