def menu():
    print("Main menu")
    print("1. Your profile\n2.Return a book\n3.Search for books\n4.Pay a penalty\n5.Log Out\n ")
    while True:
        try:
            function = int(input("Please select a number from given menu: "))
            if function<0 or function>5:
                print("Please enter a valid option from menu")
            break
        except:
            print("Please enter a valid option from menu")
    return function
        