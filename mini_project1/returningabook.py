import sqlite3
import datetime

conn = sqlite3.connect('library.db')
cu = conn.cursor()

def borrow_book(cursor, user_email):
    cursor.execute("""
                    SELECT borrowings.bid ,books.title, borrowings.start_date, DATE(borrowings.start_date '+20days') AS return_deadline
                    FROM borrowings
                   JOIN books on borrowings.book_id = books.book_id
                   WHERE borrowings.end_date IS NULL                        
                   """,(user_email))
    borrowings = cursor.fetchall()
    for borrowing in borrowings:
        print(f"Borrowing ID: {borrowing[0]}, Title: {borrowing[1]}, Borrowing Date: {borrowing[2]}, Return Deadline: {borrowing[3]}")

def return_book(cursor, bid, user_email):
    current_date = datetime.datetime.now().date()  # Get the current date in the correct format
    cursor.execute("""
                    UPDATE borrowings
                    SET end_date = ?
                    WHERE bid = ? AND member = ?
                   """, (current_date, bid, user_email))
    conn.commit()

    

def add_penalty(cursor,bid,return_date):
    if current_date>return_deadline




##conn.close()
