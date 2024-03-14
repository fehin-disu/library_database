import sqlite3
from datetime import datetime, timedelta, date
from connect import connect 



def returning_a_book(member,path):
    global connection, cursor
    connection, cursor = connect(path)

    if not borrow_book(member):  
        return
 
        
        
    while True:
        bid = input("Enter the Borrowing ID of the book you are returning: ")
        if return_and_penalty(bid,member):
            break
        else:
            print("Invalid Borrowing ID. Please try again.")


        
    ask_review=input("Would you like to write a review and add a rating for this book? (yes/no) ")
    if ask_review.lower() == "yes":
        while True:
            book_id = input("Enter the Borrowing ID of the book for which you want to add a review: ")
            if add_review(book_id, member):
                break
            else:
                print("Invalid Borrowing ID. Please try again.")

    


def borrow_book(member):
    
    cursor.execute("""
                    SELECT b.bid, bk.title, b.start_date, DATE(b.start_date, '+20 days') AS return_deadline
                    FROM borrowings b
                    JOIN books bk ON b.book_id = bk.book_id
                    WHERE b.member = ? AND b.end_date IS NULL
                    """, (member,))
    borrowings = cursor.fetchall()

    if len(borrowings)==0:  # Checks if the list of borrowings is empty
        print("You have no borrowings currently.")
        return False
    else:
        for borrowing in borrowings:
            print(f"Borrowing ID: {borrowing[0]}, Title: {borrowing[1]}, Borrowing Date: {borrowing[2]}, Return Deadline: {borrowing[3]}")
        return True    

    


def return_and_penalty(bid, member):
    current_date = date.today()  # Get the current date in the correct format
    cursor.execute("""
                    SELECT start_date
                    FROM borrowings
                    WHERE bid = ? AND member = ?
                   """, (bid, member))
    connection.commit()
    start_date_val = cursor.fetchone()

    if start_date_val is None:
        return False
    
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
                   """,(bid,penalty_amount))
    cursor.execute("""UPDATE borrowings 
                   SET end_date = ? WHERE bid = ? AND member = ?
                   """, (current_date, bid, member))
    connection.commit()

    return True

def add_review(bid, member):
    cursor.execute("""
                    SELECT book_id
                    FROM borrowings
                    WHERE bid = ? AND member = ?
                   """, (bid, member))
    
    found_book = cursor.fetchone()
    if not found_book:
        return False
    
    found_book_yes = found_book[0]

    write_review = input("Please add your review here.\n")
    add_rating = int(input("Please rate the book within 1-5: "))
    review_date= datetime.today()

    cursor.execute("""
                    INSERT INTO reviews (book_id, member, rating, rtext, rdate)
                    VALUES (?, ?, ?, ?, ?)
                    """, (found_book_yes, member, add_rating, write_review, review_date))
        
    connection.commit()
    print("Your review has been added successfully")

    return True

