from login import login
from menu import menu
import memberprofile
import returningabook
from check_penalty import check_penalty

def main(): 
    success = login()
    if success ==-1:
        print("Exited")
        exit()
    email = success
    # menu 
    while True:
        while True:
            try:
                next_step = int(input("Please enter 1 to see the menu and 2 to log out: "))
                if next_step ==1 or next_step == 2:
                    break   
            except:
                print("Please give a valid input.")
        if next_step ==2:
            print("Logged out successfully")
            exit()
        user_options = menu()

        if user_options == 5:
            print("Logged out successfully")
            exit()
        else:
            #Can change the if to CASE statements
            if user_options == 1:
                memberprofile(email)
            if user_options ==2:
                returningabook(email)
            # if user_options == 3:
            #     searchforbooks(email)
            if user_options == 4:
                check_penalty(email)
main()
    