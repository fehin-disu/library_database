import sqlite3
from datetime import datetime, timedelta, date

conn = sqlite3.connect('library.db')
cu = conn.cursor()


def returning_a_book(cursor,member):
    borrow_book(cursor, member)
    
    bid = input("Enter the Borrowing ID of the book you are returning: ")
    return_and_penalty(cursor, bid, member)
    
    book_id = input("Enter the Book ID for which you want to add a review: ")
    add_review(cursor, book_id, member)


def borrow_book(cursor, member):
    cursor.execute("""
                    SELECT borrowings.bid ,books.title, borrowings.start_date, DATE(borrowings.start_date '+20days') AS return_deadline
                    FROM borrowings
                   JOIN books on borrowings.book_id = books.book_id
                   WHERE borrowings.end_date IS NULL                        
                   """,(member))
    borrowings = cursor.fetchall()
    for borrowing in borrowings:
        print(f"Borrowing ID: {borrowing[0]}, Title: {borrowing[1]}, Borrowing Date: {borrowing[2]}, Return Deadline: {borrowing[3]}")

def return_and_penalty(cursor, bid, member):
    current_date = date.today()  # Get the current date in the correct format
    cursor.execute("""
                    SELECT start_date
                    FROM borrowings
                    WHERE bid = ? AND member = ?
                   """, (bid, member))
    conn.commit()
    start_date_val = cursor.fetchone()
    start_date = datetime.strptime(start_date_val[0], '%Y-%m-%d').date()
    return_deadline = start_date + timedelta(days=20)

    overdue_Date = (current_date - return_deadline).days
    if overdue_Date > 0 and overdue_Date <= 25:
        penalty_amount = overdue_Date
    else:
        if overdue_Date>25:
            penalty_amount = overdue_Date+5
    cursor.execute("""
                    INSERT INTO penalties (bid, amount)
                    VALUES (?,?)
                   """),(bid,penalty_amount)
    cursor.execute("""UPDATE borrowings 
                   SET end_date = ? WHERE bid = ? AND member = ?
                   """, (current_date, bid, member))
    conn.commit()



def add_review(cursor, book_id, member):
    ask_review=input("Would you like to write a review and add a rating for this book? ")


    cursor.execute("""
                    SELECT book_id, member
                    FROM borrowings
                    WHERE book_id = ? AND member = ?
                   """, (book_id, member))
    
    if ask_review == 'yes':
        write_review = input("Please add your review here.")
        add_rating = int(input("Please rate the book within 1-5: "))

        review_date= datetime.today()

        cursor.execute("""
                        INSERT INTO reviews (book_id, member, rating, rtext, rdate)
                        VALUES (?, ?, ?, ?, ?)
                        """, (book_id, member, add_rating, write_review, review_date))
        
    conn.commit()

member_email = input("Please enter your email: ")
returning_a_book(member_email)



conn.close()