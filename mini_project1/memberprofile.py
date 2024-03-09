"""
1.     Member profile: The user should be able to view their profile page. In this page, the users can view:

Personal information (such as name, email and birth year).
The number of the books they have borrowed and returned (shown as previous borrowings), the current borrowings which is the number of their unreturned borrowings, and overdue borrowings, which is the number of their current borrowings that are not returned within the deadline. The return deadline is 20 days after the borrowing date.
Penalty information, displaying the number of unpaid penalties (any penalty that is not paid in full), and the user's total debt amount on unpaid penalties.

"""

import sqlite3
from connect import connect

# Get the personal information 

def member_profile(email):
    # connect to db
    conn, cursor = connect('library.db')
    
    #members (email, passwd, name, byear, faculty)
    profile_query = ''' 
                        SELECT name, email, byear
                        FROM members m 
                        WHERE email = ?;''', email

    cursor.execute(profile_query)