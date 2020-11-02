# import sqlite3
# arg1 = 'вексор'
# arg2 = 18
# arg3 = 'Corn'
# qwe = [arg1, arg2, arg3]
# conn = sqlite3.connect("data.db")
# cursor = conn.cursor()
# #заполняет таблицу данными
# cursor.execute("""INSERT INTO requests(item, volume, client)
#                     VALUES(?,?,?);""", qwe)
#
# conn.commit()

# cursor.execute('SELECT * from requests where client_id=285056432808919040')
# rows = cursor.fetchall()
# for i in rows:
#     if i[3] == '285056432808919040':
#         print('!!!!!!!!!')
# print(rows)
# cursor.execute('select id from requests where rowid=last_insert_rowid()')
# print(cursor.fetchone()[0])

q = input()
print(q, type(q))
q.split(' ')
print(q)