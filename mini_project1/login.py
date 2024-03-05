import sqlite3
import getpass
conn = sqlite3.connect('library.db')
c= conn.cursor()
print("Do you want to login or signup? please enter 1 for login and 2 for new sign in")
user = int(input())
if user == 1:
    email = input ("Please enter your email:\n")
    pwd = getpass.getpass("Please enter your password:\n")
    c.execute("SELECT *FROM members")
    members = c.fetchall()
    login = False
    for items in members:
        if items[0].lower()== email.lower() and items[1]== pwd:
            print("Login Successsful\n")
            login = True
            break
    if login == False:
        print("login unsuccesful")
        exit
elif user == 2:
    info = [1,2,3,4,5]
    print("Please enter following details:")
    temp = input("name: ")
    info[2]= temp
    temp = int(input("Birth Year: "))
    info[3]= temp
    temp = input("Faculty: ")
    info[4]= temp
    temp= input("Email: ")
    info[0]= temp
    temp = getpass.getpass("Password: ")
    info[1]= temp
    info = tuple(info)
    try:
        c.execute("INSERT INTO members VALUES (?,?,?,?,?)",info)
    except:
        print("cannot make an accout with given info provided")
        exit

else:
    exit

conn.commit()

    