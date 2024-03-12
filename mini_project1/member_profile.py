

from connect import connect 
from datetime import date # to get current date 


def member_profile(email,path_input):
    """
    This handles the main code of each function in this module
    """
    global connection, cursor # used in all the functions in this module

    connection, cursor = connect(path_input) # NEW CONNECTION, CLOSE!
    get_profile(email)
    get_book_info(email)
    display_penalty(email)
    connection.close()
    
    

def get_profile(email): 
    """
    Get and display the relevant member info: name, email, byear
    """
    global connection, cursor 

    profile_query = ''' 
                        SELECT name, email, byear
                        FROM members m 
                        WHERE email = ?;'''

    cursor.execute(profile_query, (email,))
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
    Gets the following information
    Previous borrowings: books they have borrowed and returned
    Current borrowings: Unreturned
    Overdue borrowings: SUBSET OF CURRENT that are past the deadline, i.e. borrowing date - today
    """
    global connection, cursor
    current_date = date.today() # today's date 

    # Previous borrowings
    borrow_query = ''' 
                        SELECT COUNT(*)
                        FROM borrowings b  
                        WHERE member = ? AND end_date IS NOT NULL;'''
    
    # Current borrowings
    current_borrow_query = ''' 
                            SELECT COUNT(*)
                            FROM borrowings b  
                            WHERE member = ? AND end_date IS NULL;'''
    
    # Overdue borrowings
    overdue_query = ''' 
                            SELECT COUNT(*)
                            FROM borrowings b  
                            WHERE member = ? AND julianday(?) - julianday(start_date) > 20 AND end_date IS NULL''' 
    
    try:
    
        # Talk with SQL
        cursor.execute(borrow_query, (email,))
        count = cursor.fetchone()
        cursor.execute(current_borrow_query, (email,))
        count2 = cursor.fetchone()
        cursor.execute(overdue_query, (email,current_date))
        count3 = cursor.fetchone()

        # Print
        print("Previous borrowings:", count[0] if count else 0)
        print("Current borrowings:", count2[0] if count2 else 0)
        print("Overdue borrowings:", count3[0] if count3 else 0)
    except Exception as e:
        print(f"Error: {e}")

    


def display_penalty(email): 
    """ 
    Responsible for dealing with the penalties
    """

    # Unpaid penalties

    unpaid_query ='''   SELECT COUNT(*)
                        FROM borrowings b  
                        LEFT JOIN penalties p
                        WHERE b.member = ? AND p.bid = b.bid AND p.amount - COALESCE(p.paid_amount,0) > 1;'''
    
    
    
    # Total debt

    total_debt_query = '''SELECT SUM(p.amount -COALESCE(p.paid_amount,0))
                          FROM borrowings b  
                          LEFT JOIN penalties p
                          WHERE b.member = ? AND p.bid = b.bid AND p.amount - COALESCE(p.paid_amount,0) > 1;
                        '''
    
    # Talk with SQL, fetch values
    cursor.execute(unpaid_query, (email,))
    unpaid = cursor.fetchone()
    cursor.execute(total_debt_query, (email,))
    debt = cursor.fetchone()

    # Print
    print("Number of unpaid penalties: ", unpaid[0] if unpaid else 0) # if list is not empty, fetch from the list
    print("Total debt amount of unpaid penalties:", debt[0] if debt else 0)