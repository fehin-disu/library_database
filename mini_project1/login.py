def login():
    import sqlite3
    import getpass # to have the password be hidden during input 

    ''' connect to the database
        CHANGE: database name is NOT hardcoded- change later 
    '''
    conn = sqlite3.connect('library.db')

    ''' create a cursor 
        so that we can execute SQLite3 commands
    '''
    c= conn.cursor()

    ''' start of functionality
        - prompt user to login/signup 
    '''
    print("Do you want to login or signup? please enter 1 for login and 2 for new sign in or any other character to exit.")
    try:
        user = int(input())
    except: 
        return -1

    if user == 1:
        email = input ("Please enter your email:\n")
        pwd = getpass.getpass("Please enter your password:\n")
        c.execute("SELECT *FROM members")
        members = c.fetchall()
        login = False
        for items in members: # Checking if credentials are in the members to proceed in the system
            if items[0].lower()== email.lower() and items[1]== pwd:
                print("Login Successsful\n")
                login = True
                return email
        if login == False:
            print("Account not found, do you want to sign up instead? Y/N")
            user1 = input().lower() 
            if user1 != 'y':
                return -1
            user = 2

    if user == 2:
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
            return email
        except:
            print("cannot make an account with given info provided")
            return -1

    else:
        return -1

    conn.commit()
    conn.close()
    return 0
        
