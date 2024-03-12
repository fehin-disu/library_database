from login import login
from menu import menu
from member_profile import member_profile
from connect import connect
from returningabook import returning_a_book 
from check_penalty import check_penalty
from searchbooks import search_books
def main(): 
    """
    Allows all the modules to work with each other for the overall 
    functionality for the program.
    """
    path_input = input("Please provide the path for the database (Form of ./path/databasename.db):")

    #login() returns an email of the user if the login or signup was successful and returns -1 if it was unsuccessful
    success = login()
    if success ==-1:
        print("Exited")
        exit()
    email = success

    # menu 
    while True:
        while True:
            # keeps on asking user for input until they provide a valid input that is 1 to see the menu or 2 to log out
            try:
                next_step = int(input("Please enter 1 to see the menu and 2 to log out: "))
                if next_step ==1 or next_step == 2:
                    break   
            except:
                print("Please give a valid input.")

        # Chose log out
        if next_step ==2:
            #exit the program if the user wants to log out
            print("Logged out successfully")
            exit()

        # Chose menu
        """
        # the function menu shows the menu and ask user to choose one of following options and returns the option chosen by the user:
        1 for profile
        2 to return a book
        3 to search for book
        4 to check the penalty 
        5 to logout
        """
        user_options = menu() # Calls menu, asks for input.

        # Chose log out
        if user_options == 5:
            print("Logged out successfully")
            exit()

        # If the user does not choose to logout calls the function required according to the option chosen
        else:
            #Can change the if to CASE statements
            if user_options == 1:
                member_profile(email,path_input)
            if user_options ==2:
                returningabook(email)
            if user_options == 3:
                keyword = input("Enter the keyword you want to search: ")
                search_books(email,keyword)
            if user_options == 4:
                check_penalty(email)
main()
    
