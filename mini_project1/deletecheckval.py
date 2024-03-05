import sqlite3
conn = sqlite3.connect('library.db')
c= conn.cursor()
c.execute("SELECT * FROM members")
print(c.fetchall())
print("\n")
c.execute("SELECT * FROM borrowings")
print(c.fetchall())
conn.close()