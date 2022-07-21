import sqlite3

connection = sqlite3.connect('data.sqlite')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY , username text , password text)"
cursor.execute(create_table)

create_table1 = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
cursor.execute(create_table1)


connection.commit()
connection.close()