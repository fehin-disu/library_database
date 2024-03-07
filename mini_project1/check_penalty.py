#When made into functions replace all exit() with return
def check_penalty(email):
    import sqlite3
    conn = sqlite3.connect('library.db')
    c= conn.cursor()
    c.execute("""
    SELECT p.pid, p.paid_amount, p.amount
    FROM penalties AS p
    LEFT JOIN borrowings on p.bid = borrowings.bid
    WHERE borrowings.member =:user_email AND 
    ((p.paid_amount<p.amount) OR (p.paid_amount is NULL))
    """,{"user_email":email})
    penalties = c.fetchall()
    if len(penalties)==0:
        print("You have no penalties.")
        return
    for items in penalties:
        print("Pid: {}, Paid_amount: {}, Total amount:{}".format(items[0],items[1],items[2]))
    user_in = input("Do you want to pay any penalties now? Please enter Y/N.")
    if user_in.lower()!='y':
        return
    else:
        pid_found = False
        while pid_found == False:
            user_pid = int(input("Please enter the pid of the penalty you want to pay from the list shown: "))
            for i in range(len(penalties)):
                items = penalties[i]
                if items[0]==user_pid:
                    pid_found = True
                    while True:
                        try:
                            current_pay = int(input("Please enter the amount you want to pay: "))
                        except:
                            print("Please enter a valid amount to pay.")
                            continue
                        paid_amount = items[1]
                        if paid_amount == None:
                            paid_amount = 0
                        remaining_pay = items[2]-paid_amount
                        if current_pay>remaining_pay:
                            print("You entered the amount greater than due amount.")
                        else:
                            break
                    break
                if pid_found!= True:
                    again_pid = input("Pid not found. Do you want to enter Pid again (Y/N): ")
                    if again_pid.lower()!= 'y':
                        return

        
        c.execute("""UPDATE penalties
                SET paid_amount = (CASE WHEN paid_amount is NOT NULL THEN (:amount + paid_amount) ELSE :amount END)
                WHERE pid = :pid
                """,{"amount":current_pay,"amount":current_pay,"pid":user_pid})
        print("{} dollars paid towards the pid {}".format(current_pay, user_pid))
        
        conn.commit()

    #Close our connection
    conn.close()
