import sqlite3
conn = sqlite3.connect('library.db')
c = conn.cursor()
c.execute("PRAGMA foreign_keys = ON")
c.execute('drop table if exists reviews')
c.execute('drop table if exists penalties')
c.execute('drop table if exists borrowings')
c.execute('drop table if exists books')
c.execute('drop table if exists members')

members_query = """CREATE TABLE members (
    email CHAR(100),
    passwd CHAR(100),
    name CHAR(255) NOT NULL,
    byear INTEGER,
    faculty CHAR(100),
    PRIMARY KEY (email)
)"""

c.execute(members_query)


c.execute("""
CREATE TABLE books (
    book_id INTEGER,
    title CHAR(255),
    author CHAR(150),
    pyear INTEGER,
    PRIMARY KEY (book_id)
)""")

c.execute("""

CREATE TABLE borrowings(
    bid INTEGER,
    member CHAR(100) NOT NULL,
    book_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    PRIMARY KEY (bid),
    FOREIGN KEY (member) REFERENCES members(email),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
)""")


c.execute("""
CREATE TABLE penalties(
    pid INTEGER,
    bid INTEGER NOT NULL,
    amount INTEGER NOT NULL,
    paid_amount INTEGER,
    PRIMARY KEY (pid),
    FOREIGN KEY (bid) REFERENCES borrowings(bid)
)""")

c.execute("""
CREATE TABLE reviews(
    rid INTEGER,
    book_id INTEGER NOT NULL,
    member CHAR(100) NOT NULL,
    rating INTEGER NOT NULL,
    rtext CHAR(255),
    rdate DATE,
    PRIMARY KEY (rid),
    FOREIGN KEY (member) REFERENCES members(email),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
)
          """)
books_many = [(1, 'Book 1', 'John', 2002),(2, 'Book 2', 'John', 2022),(3, 'Book 3', 'Marry', 2024),
(4, 'Book 4', 'Mike', 2020),(5, 'Book 5', 'Rejwana', 2017),(6, 'Book 6', 'Marry', 2017)]
members_many = [('dave@ualberta.ca','dave@', 'Dave', 1980, 'CS'),
('john@ualberta.ca','john@', 'John', 1990, 'CS'),
('marry@ualberta.ca', 'marry@','Marry', 1995, 'CS'),
('mike@ualberta.ca', 'mike@','John', 1990, 'Math'),
('sarah@ualberta.ca', 'sarah@','Sarah', 1990, 'Math')]
borrowings_many = [(1, 'dave@ualberta.ca', 1, '2023-11-15',None),
(2, 'dave@ualberta.ca', 1, '2023-11-15',None),
(3, 'dave@ualberta.ca', 2, '2023-11-15',None),
(4, 'dave@ualberta.ca', 2, '2023-10-15', '2023-10-25'),
(5, 'john@ualberta.ca', 3, '2023-10-15', '2023-10-25'),
(6, 'john@ualberta.ca', 3, '2023-10-15', '2023-11-25'),
(7, 'john@ualberta.ca', 3, '2023-10-15', '2023-11-25'),
(8, 'john@ualberta.ca', 3, '2023-10-15', '2023-10-25'),
(9, 'mike@ualberta.ca', 4, '2023-11-15',None),
(10, 'marry@ualberta.ca', 4, '2023-11-15',None),
(11, 'marry@ualberta.ca', 4, '2023-11-15',None),
(12, 'sarah@ualberta.ca', 5, '2023-11-15',None)]

duck_borrowings = [(13,'duck@ualberta.ca',1,'2023-10-15',None), 
                   (14,'duck@ualberta.ca',2,'2023-01-15',None), 
                   (15,'duck@ualberta.ca',3,'2023-10-15','2023-10-25'), 
                   (16,'duck@ualberta.ca',4,'2023-10-15','2023-11-15'),
                   (17,'duck@ualberta.ca',5,'2023-02-12',	None)]

duck_penalties = [(8,13,100,100), (9,14,100,30)]

penalties_many = [(1, 1, 50,None),
(2, 2, 50, 20),
(3, 1, 50, 50),
(4, 3, 60, 60),
(5, 5, 90, 90),
(6, 10, 50,None),
(7, 12, 70, 70)]
reviews_many = [(1, 2, 'dave@ualberta.ca', 4, '','2023-12-15'),
(2, 2, 'marry@ualberta.ca', 3, '','2022-12-15'),
(3, 3, 'dave@ualberta.ca', 4, '','2023-08-15')]
c.executemany("INSERT INTO books VALUES (?,?,?,?)",books_many)
c.executemany("INSERT INTO members VALUES (?,?,?,?,?)",members_many)
c.executemany("INSERT INTO borrowings VALUES (?,?,?,?,?)",borrowings_many)
c.executemany("INSERT INTO penalties VALUES (?,?,?,?)",penalties_many)
c.executemany("INSERT INTO reviews VALUES (?,?,?,?,?,?)",reviews_many)
#DUCK
c.execute("INSERT INTO members VALUES ('duck@ualberta.ca','duck@','duck',2022,'CS')")
c.executemany("INSERT INTO borrowings VALUES (?,?,?,?,?)",duck_borrowings)
c.executemany("INSERT INTO penalties VALUES (?,?,?,?)",duck_penalties)
conn.commit()

#Close our connection
conn.close()
