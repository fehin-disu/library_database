"""
1.     Member profile: The user should be able to view their profile page. In this page, the users can view:

Personal information (such as name, email and birth year).
The number of the books they have borrowed and returned (shown as previous borrowings), the current borrowings which is the number of their unreturned borrowings, and overdue borrowings, which is the number of their current borrowings that are not returned within the deadline. The return deadline is 20 days after the borrowing date.
Penalty information, displaying the number of unpaid penalties (any penalty that is not paid in full), and the user's total debt amount on unpaid penalties.

"""

import sqlite3
from connect import connect

# Get the personal information 

# Define module-level variables
conn, cursor = connect('library.db')

def member_profile(email):
    get_profile(email)
    get_book_info(email)
    

def get_profile(email): 
    """
    Get and display the relevant member info: name, email, byear
    """

    #members (email, passwd, name, byear, faculty)
    profile_query = ''' 
                        SELECT name, email, byear
                        FROM members m 
                        WHERE email = ?;'''

    cursor.execute(profile_query, (email,))
    # cursor stores the values, fetch 
    info = cursor.fetchone()

    if info:
        name, email, byear = info
        print("Name:", name)
        print("Email:", email)
        print("Birth Year:", byear)
    else:
        print("No profile found for the provided email.") # should not be reached. 

def get_book_info(email):
    """
    The number of the books they have borrowed and returned (shown as previous borrowings), 
    the current borrowings which is the number of their unreturned borrowings, 
    and overdue borrowings, which is the number of their current borrowings that are not returned within the deadline. 
    The return deadline is 20 days after the borrowing date.
    """

    # borrowings (bid, member, book_id, start_date, end_date)

    #1) borrowed and returned COUNT IT

    borrow_query = ''' 
                        SELECT COUNT(*)
                        FROM borrowings b  
                        WHERE member = ? AND end_date IS NOT NULL;'''
    
    # Can reduce redundancy below..?
    current_borrow_query = ''' 
                            SELECT COUNT(*)
                            FROM borrowings b  
                            WHERE member = ? AND end_date IS NULL;'''
    
    #ASK TA: NOT COUNTING THE DAYS THAT HAVE NOT BEEN RETURNED??
    
    overdue_query = ''' 
                            SELECT COUNT(*)
                            FROM borrowings b  
                            WHERE member = ? AND julianday(end_date) - julianday(start_date) > 20 AND end_date IS NOT NULL;''' # ASK TA: Assuming this is like May 1 borrowed, May 21 is when it is DUE
    
    try:
        # review the code below
        # could i reduce the code below? 
        cursor.execute(borrow_query, (email,))
        count = cursor.fetchone()
        cursor.execute(current_borrow_query, (email,))
        count2 = cursor.fetchone()
        cursor.execute(overdue_query, (email,))
        count3 = cursor.fetchone()

        print("Previous borrowings:", count[0] if count else 0)
        print("Current borrowings:", count2[0] if count2 else 0)
        print("Overdue borrowings:", count3[0] if count3 else 0)
    except Exception as e:
        print(f"Error: {e}")