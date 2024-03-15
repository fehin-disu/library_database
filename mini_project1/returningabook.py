import sqlite3
from datetime import datetime, timedelta, date
from connect import connect 



def returning_a_book(member,path):
    global connection, cursor
    connection, cursor = connect(path)

    returned_book = [] #keeps the track of returned books in a list
    
    new_book = borrow_book(member) #list of the borrowed books, mainly the borrow ID
    if not new_book:  
        return

    while True:  
            try: 
                bid = int(input("Enter the Borrowing ID of the book you are returning or a non-number character to exit return a book: ")) #If the borrowing ID is correctly typed and within the unreturned book list
            except:
                return
            if bid in returned_book:
                print("This book has already been returned. Please enter a different Borrowing ID.") #checks if the user typed the borrowing ID for a book that has already been returned
                continue

            if bid in new_book:   
                if return_and_penalty(bid, member): #checks if the borrowing ID is the borrowed book list and if its true it tracks the return and calculates the penalty
                    returned_book.append(bid)

                    while True:
                        ask_review = input("Would you like to write a review and add a rating for this book? (yes/no) ")
                        if ask_review.lower() == "yes":
                            add_review(bid, member)
                            break
                        elif ask_review.lower() != "no":
                            print("Please select the correct option.")
                            continue
                        else:
                            if ask_review.lower() == "no":
                                break
                                
                    if len(returned_book) == len(new_book): #checks if all the books have been returned
                        print("All books have been returned") 
                        break

                    another = input("Do you want to return another book? Type yes to return another book and any other character to exit. ")
                    if another.lower() == "yes":
                        continue    
        
                break
                              
            else:
                print("Invalid Borrowing ID. Please try again.")
                
    connection.close()

    


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
        return None
    else:
        id_values = list()
        for borrowing in borrowings:
            print(f"Borrowing ID: {borrowing[0]}, Title: {borrowing[1]}, Borrowing Date: {borrowing[2]}, Return Deadline: {borrowing[3]}")
            id_values.append(borrowing[0]) #keeps a track of the borrowings iD's
    return id_values


def return_and_penalty(bid, member):
    current_date = date.today()  # Gets the current date in the correct format
    cursor.execute("""
                    SELECT start_date
                    FROM borrowings
                    WHERE bid = ? AND member = ?
                   """, (bid, member))
    
    start_date_val = cursor.fetchone()

    if start_date_val is None: #checks if the list is empty
        return False
    
    start_date = datetime.strptime(start_date_val[0], '%Y-%m-%d').date()
    return_deadline = start_date + timedelta(days=20)

    overdue_Date = (current_date - return_deadline).days
    if 0< overdue_Date <= 25:
        penalty_amount = overdue_Date
    else:
        if overdue_Date>25:
            penalty_amount = overdue_Date+5

    #insert the penalties update
    cursor.execute("""
                    INSERT INTO penalties (bid, amount)
                    VALUES (?,?)
                   """,(bid,penalty_amount))
    
    connection.commit()
    #update the end date with todays date
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
    
    found_book = cursor.fetchone() #to make sure the book id of the borrowing table is the same as reviews table
    if not found_book:
        return False
    
    found_book_yes = found_book[0] #to retrieve the correct book

    write_review = input("Please add your review here.\n")
    

    while True:
        add_rating = int(input("Please rate the book within 1-5: "))
        if 1<=add_rating<=5:
                break
        else:
            print("Invalid rating.")

    print("Your review has been added successfully")
        
        
    review_date= datetime.today()

    #updates the user as a reviewer in the reviews table
    cursor.execute("""
                    INSERT INTO reviews (book_id, member, rating, rtext, rdate) 
                    VALUES (?, ?, ?, ?, ?)
                    """, (found_book_yes, member, add_rating, write_review, review_date))
        
    connection.commit()

    return True
