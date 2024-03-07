from login import login
from menu import menu
import memberprofile
import returningabook
from check_penalty import check_penalty

def main(): 
    success = login()
    if success ==-1:
        exit()
    email = success
    # menu 
    while True:
        user_options = menu()
        if user_options == 5:
            print("Logged out successfully")
            exit()
        else:
            #Can change the if to CASE statements
            if user_options == 1:
                memberprofile()
            if user_options ==2:
                returningabook()
            # if user_options == 3:
            #     searchforbooks()
            if user_options == 4:
                check_penalty(email)
main()
    