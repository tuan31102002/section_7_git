# from multiprocessing import connection
import sqlite3 

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int , username text , password text)"
cursor.execute(create_table)

user = (1,'admin','tuan123')
insert_query = "INSERT INTO  users VALUES (?,?,?)"

users = [
    (2,'admin2','tuan123'),
    (3,'admin3','tuan123')
]

cursor.executemany(insert_query, users)


cursor.execute(insert_query,user) #chạy lệnh sqlite

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)


connection.commit() #xác nhận

connection.close() # kết thúc