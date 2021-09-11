import sqlite3

con = sqlite3.connect('books.db')

cur = con.cursor()

sql = """
CREATE TABLE livros (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL, ano INTEGER NOT NULL, autor TEXT NOT NULL, editora TEXT NOT NULL)
"""

cur.execute(sql)
con.commit()
con.close()

