from login import login
from menu import menu
from member_profile import member_profile
from connect import connect
import returningabook
from check_penalty import check_penalty

def main(): 
    # ask for the db 
    path_input = input("Please provide the path for the database (Form of ./path/databasename.db):")

    # PATH_INPUT MUST BE THROWN AS AN ARGUMENT... Global variables won't work as path is still needed.

    #login() returns an email of the user if the login or signup was successful and returns -1 if it was unsuccessful
    success = login()
    if success ==-1:
        print("Exited")
        exit()
    email = success
    # menu 
    while True:
        while True:
            #keeps on asking user for input until they provide a valid input that is 1 to see the menu or 2 to log out
            try:
                next_step = int(input("Please enter 1 to see the menu and 2 to log out: "))
                if next_step ==1 or next_step == 2:
                    break   
            except:
                print("Please give a valid input.")
        if next_step ==2:
            #exit the program if the user wants to log out
            print("Logged out successfully")
            exit()

        #If not log out then shows the menu
        """
        # the function menu shows the menu and ask user to choose one of following options and returns the option chosen by the user:
        1 for profile
        2 to return a book
        3 to search for book
        4 to check the penalty 
        5 to logout
        """
        user_options = menu()

        if user_options == 5:
            print("Logged out successfully")
            exit()
        #If the user doesnot choose to logout calls the function required according to the option chosen
        else:
            #Can change the if to CASE statements
            if user_options == 1:
                member_profile(email,path_input)
            if user_options ==2:
                returningabook(email)
            # if user_options == 3:
            #     searchforbooks(email)
            if user_options == 4:
                check_penalty(email)
main()
    
