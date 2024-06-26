from login import login
from menu import menu
from member_profile import member_profile
from connect import connect
from returningabook import returning_a_book
from check_penalty import check_penalty
from searchbooks import search_books
def main(): 
    # ask for the db 
    path_input = input("Please provide the path for the database (Form of ./path/databasename.db):")

    # PATH_INPUT MUST BE THROWN AS AN ARGUMENT... Global variables won't work as path is still needed.

    #login() returns an email of the user if the login or signup was successful and returns -1 if it was unsuccessful
    while True:
        success = login(path_input)
        if success ==-1:
            print("Exited")
            exit()
        email = success
        # menu 
        while True:
            while True:
                #keeps on asking user for input until they provide a valid input that is 1 to see the menu or 2 to log out
                try:
                    next_step = int(input("Please enter 1 to see the menu and 2 to log out or 3 to exit the program: "))
                    if next_step ==1 or next_step == 2 or next_step == 3:
                        break   
                except:
                    print("Please give a valid input.")
            if next_step ==2:
                #exit the program if the user wants to log out
                print("Logged out successfully")
                break
            if next_step == 3:
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
                break
            #If the user doesnot choose to logout calls the function required according to the option chosen
            else:
                #Can change the if to CASE statements
                if user_options == 1:
                    member_profile(email,path_input)
                if user_options ==2:
                    returning_a_book(email, path_input)
                if user_options == 3:
                    keyword = input("Enter the keyword you want to search: ").lower()
                    search_books(email,keyword,path_input)
                if user_options == 4:
                    check_penalty(email,path_input)
main()
        
        
