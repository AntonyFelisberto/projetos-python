import sqlite3

con = sqlite3.connect("database.db")

cur = con.cursor()

cur.execute("SELECT * FROM 'ips' ORDER BY asn")
print(cur.fetchall())

cur.execute("SELECT address,asn FROM 'ips' ORDER BY asn")
print(cur.fetchall())

cur.execute("SELECT * FROM 'ips' WHERE asn < 300 ORDER BY asn")
print(cur.fetchall())

cur.execute("SELECT * FROM 'ips' WHERE asn = 144 ORDER BY asn")
print(cur.fetchall())

cur.execute("SELECT * FROM 'ips' WHERE asn < 144 AND domain LIKE '%sa' ORDER BY asn")
print(cur.fetchall())

cur.execute("SELECT * FROM 'ips' WHERE asn < 144 AND domain LIKE '%sa' ORDER BY asn")
result = cur.fetchall()
print(result)

result_two = cur.fetchall() #vai retornar vazio pois o cursor esta cansado
print(result_two)

for row in result:
    print(row)