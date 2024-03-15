
import sqlite3
import getpass # to have the password be hidden during input 
from connect import connect
''' connect to the database
    CHANGE: database name is NOT hardcoded- change later 
'''

    # start of functionality
def login(path_input):
    '''
    Asks user for login or sign up and calls functions accordingly.
    '''
    conn, c = connect(path_input)
    print("Do you want to login or signup? please enter 1 for login and 2 for new sign in or any other character to exit.")
    try:
        user = int(input())
    except: 
        conn.commit()
        conn.close()
        return -1

    if user == 1:
        return login_user(conn,c)
    elif user == 2:
        return sign_up(conn,c)
    else:
        return -1

def login_user(conn,c):
    '''
    Performs and validates the login
    '''
        email = input ("Please enter your email:\n")
        pwd = getpass.getpass("Please enter your password:\n")
        c.execute("SELECT *FROM members")
        members = c.fetchall()
        login = False
        for items in members: # Checking if credentials are in the members to proceed in the system
            if items[0].lower()== email.lower() and items[1]== pwd: 
                print("Login Successsful\n")
                login = True
                conn.commit()
                conn.close()
                return email
            # new code below
            elif items[0].lower()== email.lower():
                attempt = True
                while(attempt):
                    prompt = input("Wrong password. Try again? Type Y for Yes or type any other character to exit.\n")
                    if (prompt.lower() == 'y'):
                        pwd_attempt = getpass.getpass("Please enter your password:\n")
                        if items[1]== pwd_attempt:
                            print("Login Successsful\n")
                            login = True
                            attempt = False
                            conn.commit()
                            conn.close()
                            return email
                    else: # to exit
                        print("Exiting...")
                        conn.commit()
                        conn.close()
                        return -1

                    
        if login == False:
            print("Account not found, do you want to sign up instead? Y/N")
            user1 = input().lower() 
            if user1 != 'y':
                conn.commit()
                conn.close()
                return -1
            sign_up(conn,c)

def sign_up(conn,c):
    '''
    Performs and validates the signup
    '''
        info = [1,2,3,4,5]
        print("Please enter following details:")
        temp = input("Name: ")
        info[2]= temp
        # Possible edge case: year has to be YYYY
        while(True):
            try: 
                temp = int(input("Birth Year: "))
                break
            except: 
                print("Birth year needs to be an integer. Try again.")
                
        info[3]= temp
        temp = input("Faculty: ")
        info[4]= temp
        email= input("Email: ")
        info[0]= email
        temp = getpass.getpass("Password: ")
        info[1]= temp
        info = tuple(info)
        try:
            c.execute("INSERT INTO members VALUES (?,?,?,?,?)",info)
            conn.commit()
            conn.close()
            return email
        except:
            print("cannot make an account with given info provided")
            conn.commit()
            conn.close()
            return -1    
