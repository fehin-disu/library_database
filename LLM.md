# More detail of any AI tool used, including the name, URL, all the input given and all the output received.  

--- 
## Elykah's use of AI 

Elykah only used ChatGPT, https://chat.openai.com/, for the AI tool.

[AI Prompt 1] INPUT: are docstrings before or after the def function() declaration 

OUTPUT: In Python, docstrings are usually placed immediately after the function, class, or module declaration. A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition and is used to document the purpose and usage of the code.

Here's an example with a function:

python
```python
def my_function():
    """
    This is a docstring that provides information about the function.
    
    More details and usage information can be included here.
    """
    # Function code goes here
    pass
```
It's important to note that the triple double-quotes (""") or triple single-quotes (''') are used to denote docstrings in Python. The docstring convention helps in documenting code and can be accessed using tools like help() or docstring parsing tools.

--- 
[AI Prompt 2] INPUT: say file foo has def foo(): uses boo() and loo() and another file main(), in the same folder, uses foo() from foo. would i import boo and loo too? 

Yes, if the foo function in the file named "foo" uses the functions boo() and loo(), and you want to use foo() in another file named "main" in the same folder, you would need to import the boo and loo functions into the "main" file.

Here's a simplified example:

File "foo.py":

```python
# foo.py

def boo():
    print("This is boo")

def loo():
    print("This is loo")

def foo():
    boo()
    loo()
```
File "main.py":

```python
Copy code
# main.py
from foo import foo, boo, loo

# Now you can use foo() in this file
foo()
```
In this example, main.py imports the foo function from the foo.py file, and since foo uses boo() and loo(), you also need to import these functions explicitly in the "main" file. This way, when you run "main.py", it will execute the foo() function along with its dependencies.

---
[AI PROMPT 3] Input: can i do a function in python where it returns a connection that connected to the path and the cursor? 

```python
import sqlite3

def connect_to_database(database_path):
    # Create a connection to the database
    connection = sqlite3.connect(database_path)
    
    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Return the connection and cursor as a tuple
    return connection, cursor

# Example usage:
database_path = "example.db"
db_connection, db_cursor = connect_to_database(database_path)

# Now you can use db_connection and db_cursor to interact with the database
```

In this example, the connect_to_database function takes a database_path as an argument, establishes a connection to the specified database using sqlite3.connect(), and creates a cursor with connection.cursor(). The function then returns both the connection and cursor as a tuple. Keep in mind that this is a simple example using SQLite, and you might need to adjust the code based on the specific database you're working with (e.g., MySQL, PostgreSQL). Each database module in Python may have its own way of establishing connections and creating cursors.

----
[AI PROMPT 4] does julianday in SQLite3 subtract year as well? like 2024-03-25 and 2023-10-25, would that be more than 20 days 

In SQLite, the julianday function calculates the number of days since noon in Greenwich on November 24, 4714 B.C. (Proleptic Gregorian calendar). When you subtract one Julian day value from another, you get the difference in days between the two dates, regardless of the years.

So, if you have dates like 2024-03-25 and 2023-10-25, subtracting their Julian day values will indeed give you the number of days between those two dates. This difference will account for the entire year, month, and day values.

Here's how you can calculate the difference using SQLite:

```sql
SELECT julianday('2024-03-25') - julianday('2023-10-25');
This will return the number of days between March 25, 2024, and October 25, 2023. If the result is more than 20 days, then it will be more than 20 days regardless of the year difference.
```
---
## Sandhya's use of AI 
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

--- 

## Fehintola's use of AI
=======
=======
>>>>>>> e704517143eb8cd9021bc3eb37096e1f200a6a28
=======
>>>>>>> e704517143eb8cd9021bc3eb37096e1f200a6a28
Sandhya did not use any AI tools with her code.
--- 

## Fehintola's use of AI
Fehintola only used ClaudeAI, https://claude.ai/chats, for the AI tool.
[AI Prompt 1] INPUT: how would the pagination work for my search book query is there is more than 5 results?

```python
def search_books(keyword):
    keyword = f"%{keyword}%"
    c.execute("""
        SELECT book_id, title, author, pyear, COALESCE(avg_rating, 0) AS avg_rating, CASE WHEN EXISTS (SELECT 1 FROM borrowings WHERE book_id=b.book_id AND end_date IS NULL) THEN 'On Borrow' ELSE 'Available' END AS status
        FROM books b
        LEFT JOIN (
            SELECT book_id, AVG(rating) AS avg_rating
            FROM reviews
            GROUP BY book_id
        ) r ON b.book_id = r.book_id
        WHERE title LIKE ? OR author LIKE ?
        ORDER BY
            CASE WHEN title LIKE ? THEN 0 ELSE 1 END,
            CASE WHEN title LIKE ? THEN title ELSE author END
        LIMIT 5;
    """, (keyword, keyword, keyword, keyword))
    books = c.fetchall()
    if not books:
        print("No books found.")
        return

    print(f"Search results (Page:")
    for book in books:
        print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}, Avg. Rating: {book[4]}, Status: {book[5]}")

    show_more = input("Press Enter to show more results, or type 'b' to borrow a book: ").lower()
    if show_more == 'b':
        borrow_book_id = input("Enter book ID to borrow: ")
        if borrow_book_id:
            borrow_book(email, int(borrow_book_id))
    elif show_more == '':
        search_books(keyword, page + 1)
```
The provided code handles pagination for the search results by limiting the query to return only 5 books at a time. However, it doesn't include functionality to fetch the next set of results. Here's how you can modify the `search_books` function to handle pagination:

```python
def search_books(keyword, page=1):
    keyword = f"%{keyword}%"
    offset = (page - 1) * 5  # Calculate the offset based on the page number
    c.execute("""
        SELECT book_id, title, author, pyear, COALESCE(avg_rating, 0) AS avg_rating, CASE WHEN EXISTS (SELECT 1 FROM borrowings WHERE book_id=b.book_id AND end_date IS NULL) THEN 'On Borrow' ELSE 'Available' END AS status
        FROM books b
        LEFT JOIN (
            SELECT book_id, AVG(rating) AS avg_rating
            FROM reviews
            GROUP BY book_id
        ) r ON b.book_id = r.book_id
        WHERE title LIKE ? OR author LIKE ?
        ORDER BY
            CASE WHEN title LIKE ? THEN 0 ELSE 1 END,
            CASE WHEN title LIKE ? THEN title ELSE author END
        LIMIT 5 OFFSET ?;
    """, (keyword, keyword, keyword, keyword, offset))
    books = c.fetchall()
    if not books:
        print("No books found.")
        return

    print(f"Search results (Page {page}):")
    for book in books:
        print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}, Avg. Rating: {book[4]}, Status: {book[5]}")

    show_more = input("Press Enter to show more results, or type 'b' to borrow a book: ").lower()
    if show_more == 'b':
        borrow_book_id = input("Enter book ID to borrow: ")
        if borrow_book_id:
            borrow_book(email, int(borrow_book_id))
    elif show_more == '':
        search_books(keyword, page + 1)

```

Here are the changes made to accommodate pagination:
1. The `search_books` function now accepts an optional `page` parameter, which defaults to 1.
2. The `offset` value is calculated based on the current page number: `offset = (page - 1) * 5`. This determines the starting point for the results to be retrieved.
3. The SQL query is modified to include the `OFFSET` clause, which skips the specified number of rows before returning the results: `LIMIT 5 OFFSET ?`.
4. After displaying the search results, the user is prompted to either press Enter to show more results (fetching the next page), or type 'b' to borrow a book from the current page.
5. If the user presses Enter, the `search_books` function is called recursively with the `page` parameter incremented by 1, which will fetch and display the next set of results.
6. If the user types 'b', they are prompted to enter a book ID to borrow, and the `borrow_book` function is called with the provided book ID and the user's email.

With these changes, the `search_books` function can handle pagination by fetching and displaying 5 results at a time. When the user wants to see more results, the function is called recursively with the next page number, and the query will skip the previously shown results and return the next set of 5 books.

Note that this implementation assumes that the user will only proceed to the next page or borrow a book. If you want to provide additional options (e.g., go back to the previous page), you'll need to modify the function accordingly.

[AI Prompt 2] INPUT: i got this error "sqlite3.OperationalError: ambiguous column name: book_id" help fix
The error "sqlite3.OperationalError: ambiguous column name: book_id" occurs because the SQL query is referencing the book_id column without specifying which table it belongs to. This happens when there are multiple tables in the query that have a column with the same name.

In your case, the error is likely caused by the subquery that calculates the average rating for each book. The subquery also has a book_id column, and when the outer query references book_id, SQLite doesn't know which table's book_id column to use.

To fix this issue, you need to qualify the book_id column with the table name or table alias whenever it's referenced in the query. Here's the updated search_books function with the necessary changes:
```python
def search_books(keyword, page=1):
    keyword = f"%{keyword}%"
    offset = (page - 1) * 5
    c.execute("""
        SELECT b.book_id, b.title, b.author, b.pyear, COALESCE(r.avg_rating, 0) AS avg_rating, CASE WHEN EXISTS (SELECT 1 FROM borrowings WHERE book_id=b.book_id AND end_date IS NULL) THEN 'On Borrow' ELSE 'Available' END AS status
        FROM books b
        LEFT JOIN (
            SELECT book_id, AVG(rating) AS avg_rating
            FROM reviews
            GROUP BY book_id
        ) r ON b.book_id = r.book_id
        WHERE b.title LIKE ? OR b.author LIKE ?
        ORDER BY
            CASE WHEN b.title LIKE ? THEN 0 ELSE 1 END,
            CASE WHEN b.title LIKE ? THEN b.title ELSE b.author END
        LIMIT 5 OFFSET ?;
    """, (keyword, keyword, keyword, keyword, offset))
    books = c.fetchall()
    if not books:
        print("No books found.")
        return

    print(f"Search results (Page {page}):")
    for book in books:
        print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}, Avg. Rating: {book[4]}, Status: {book[5]}")

    show_more = input("Press Enter to show more results, or type 'b' to borrow a book: ").lower()
    if show_more == 'b':
        borrow_book_id = input("Enter book ID to borrow: ")
        if borrow_book_id:
            borrow_book(email, int(borrow_book_id))
    elif show_more == '':
        search_books(keyword, page + 1)
```
The changes made are:
In the SELECT clause, b.book_id is used instead of just book_id to specify that it's referring to the book_id column from the books table, aliased as b.
In the CASE statement inside the SELECT clause, b.book_id is used for the same reason.
In the WHERE clause, b.title and b.author are used to qualify the column names with the books table alias.
In the ORDER BY clause, b.title and b.author are used to qualify the column names with the books table alias.
By qualifying the column names with the table alias (b for the books table), SQLite can unambiguously identify which book_id column is being referenced, resolving the ambiguity issue.
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> e704517143eb8cd9021bc3eb37096e1f200a6a28
=======
>>>>>>> e704517143eb8cd9021bc3eb37096e1f200a6a28
=======
>>>>>>> e704517143eb8cd9021bc3eb37096e1f200a6a28

--- 
## Samia's use of AI
Samia only used ChatGPT, https://chat.openai.com/, for the AI tool.

[AI Prompt 1] INPUT: Why do I keep facing a NoneType error as follows in my code: TypeError: 'NoneType' object is not subscriptable
```python
def return_and_penalty(bid, member):
    current_date = date.today()  # Get the current date in the correct format
    cursor.execute("""
                    SELECT start_date
                    FROM borrowings
                    WHERE bid = ? AND member = ?
                   """, (bid, member))
    start_date_val = cursor.fetchone()

    start_date = datetime.strptime(start_date_val[0], '%Y-%m-%d').date()
    ...
    # Rest of your code remains the same
```
And why doesn't it display the borrowed books correctlu?

OUTPUT: The error you're encountering, TypeError: 'NoneType' object is not subscriptable, is likely due to the fetchone() method returning None. This can happen if the SQL query does not match any rows in the database, possibly because there are no borrowings matching the bid and member you provided. When fetchone() returns None, attempting to subscript it with [0] to get start_date_val[0] will lead to this error.

How to Fix the Error
To resolve this issue, you should add a check to see if start_date_val is None before trying to access its elements. Modify the return_and_penalty function as follows:

```python

def return_and_penalty(bid, member):
    current_date = date.today()  # Get the current date in the correct format
    cursor.execute("""
                    SELECT start_date
                    FROM borrowings
                    WHERE bid = ? AND member = ?
                   """, (bid, member))
    start_date_val = cursor.fetchone()

    if start_date_val is None:
        print("No borrowing found for the given BID and member.")
        return  # Exit the function early

    start_date = datetime.strptime(start_date_val[0], '%Y-%m-%d').date()
    ...
    # Rest of your code remains the same
```
Displaying Borrowed Books
Regarding your question about why it doesn't display which books have been borrowed, it's important to ensure that:

Data Exists: Verify that there are rows in the borrowings table where end_date IS NULL and the member matches the input. If there are no such rows, the query will return an empty result, and nothing will be printed.

Correct Member Identifier: Ensure that the member parameter you're using matches exactly with the member values in your database. For example, if member is an email address, it must be case-sensitive and match exactly.

Print Statements Are Reached: Verify that the code that prints the borrowed books (inside borrow_book) is actually being executed. If the query returns no results, the loop for printing will not run. You might add a print statement before the loop to check if the function is being called and whether the query returns any rows:

```python

def borrow_book(member):
    cursor.execute("""
                    ...
                   """, (member,))
    borrowings = cursor.fetchall()
    if not borrowings:
        print("No borrowings found for this member.")
        return
    for borrowing in borrowings:
        ...
```
By ensuring there is data matching your query and adding checks for None results, you should be able to avoid errors and correctly display the information about borrowed books.


[AI Prompt 2] INPUT: Fixing the syntax error encountred The error message sqlite3.OperationalError: near "FROM": syntax error 

```python
    def borrow_book(member):
    cursor.execute("""
                    SELECT borrowings.bid ,books.title, borrowings.start_date, DATE(borrowings.start_date, '+20 days') AS return_deadline
                    FROM borrowings
                   JOIN books on borrowings.book_id = books.book_id
                   WHERE member = ? AND borrowings.end_date IS NULL                        
                   """,(member,))
```
OUTPUT:
fixing the syntax error encountred The error message sqlite3.OperationalError: near "FROM": syntax error suggests that there is a syntax error in your SQL statement. This error is typically due to a typo, missing keyword, or incorrect SQL syntax near the FROM clause of your SQL statement.

The SQL statement itself appears correctly formatted at first glance. However, the error suggests there might be an issue just before the FROM keyword or perhaps due to how the lines are joined in the Python multi-line string. Let's ensure there are no hidden characters or syntax issues.

Try to rewrite the query more compactly to see if the error persists, ensuring no unnecessary spaces or hidden characters.

If the error continues, consider these steps to further diagnose and resolve the issue:

Syntax Check: Double-check for any missing commas or syntax issues within the SQL statement.
SQLite Version: Ensure your SQLite version supports all functions and features you're using. The DATE() function with arithmetic operations (+ '20 days') is standard, but it's good to confirm compatibility.
Execution Environment: Ensure the environment where you're executing the script (e.g., IDE or command line) is correctly set up and using the right Python and SQLite versions.
Direct Testing: Try running the SQL query directly in an SQLite client or through a simple script to confirm it works outside of your main application logic.
Lastly, confirm that the connection to the database is correctly established by connect(path) and that cursor is correctly initialized and operational before the query execution

[AI Prompt 3] INPUT: File "c:\Users\samia\OneDrive\Desktop\CMPUT 291\w24-mp1-primary-keys\mini_project1\returningabook.py", line 84, in add_review
    cursor.execute("""
sqlite3.IntegrityError: FOREIGN KEY constraint failed
why does this happen everytime after i add a rating?

```python
def add_review(book_title, member):
    # First, find the book_id based on the book_title
    cursor.execute("SELECT book_id FROM books WHERE title = ?", (book_title,))
    book_result = cursor.fetchone()

    write_review = input("Please add your review here: ")
    add_rating = int(input("Please rate the book within 1-5: "))
    review_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute("""
        INSERT INTO reviews (book_id, member, rating, rtext, rdate)
        VALUES (?, ?, ?, ?, ?)
        """, (book_id, member, add_rating, write_review, review_date))

    connection.commit()
    print("Your review has been added successfully.")
```


OUTPUT: 
the intention is clear: you wish to enable the user to return a book (identified by a borrowing ID) and optionally write a review for it, identified by the book's title rather than its borrowing ID. This approach adds a layer of user-friendliness by referring to books by their titles, which are more recognizable than numeric IDs. However, there are some adjustments and considerations necessary to ensure the process aligns with database constraints and user expectations.

Step 1: Modify add_review to Use Book Title
Your current add_review function attempts to use book_id directly for inserting a review, which may not work as intended since book_id is expected to be a numerical identifier, but you're planning to input a book title (a string). To bridge this gap, you need to first fetch the book_id based on the provided book title, and then proceed with adding the review using this book_id.

Here's how you can adjust the add_review function to accept a book title and fetch the corresponding book_id:
```python
def add_review(book_title, member):
    # First, find the book_id based on the book_title
    cursor.execute("SELECT book_id FROM books WHERE title = ?", (book_title,))
    book_result = cursor.fetchone()

    if book_result is None:
        print("No book found with the given title.")
        return

    book_id = book_result[0]

    # Then, proceed with the existing process for adding a review
    write_review = input("Please add your review here: ")
    add_rating = int(input("Please rate the book within 1-5: "))
    review_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute("""
        INSERT INTO reviews (book_id, member, rating, rtext, rdate)
        VALUES (?, ?, ?, ?, ?)
        """, (book_id, member, add_rating, write_review, review_date))

    connection.commit()
    print("Your review has been added successfully.")
```

[AI Prompt 4] INPUT:

```python
def returning_a_book(member,path):
    global connection, cursor
    connection, cursor = connect(path)
    borrow_book(member)
    
    bid = input("Enter the Borrowing ID of the book you are returning: ")
    if bid is True:
        return_and_penalty(bid, member)
    else:
        input("Please enter the correct Borrowing ID: ")
        return_and_penalty(bid, member)

        
    ask_review=input("Would you like to write a review and add a rating for this book? (yes/no) ")
    if ask_review.lower() == "yes":
        book_id = input("Enter the Borrowing ID of the book for which you want to add a review: ")
        add_review(book_id, member)
    else:
        return
    
    connection.close()
```

cant i do this in the returning a book funciton?

OUTPUT:
Yes, you can improve your returning_a_book function to repeatedly ask for the correct borrowing ID if the user enters an invalid one, both for returning the book and for adding a review. To accomplish this, you should incorporate loops that will prompt the user again if the borrowing ID is not found.


[AI Prompt 5] INPUT: How can i keep a track of the borrowed id from the borrowed books just to compare it later? It already print out the correct borrowings. I want to ensure that the ID is valid

OUTPUT:
If your borrow_book function already prints out the current borrowings for the user, and you want to ensure that the user enters a valid borrowing ID from that list before proceeding with the return or review, you can modify the process to include validation against the printed list of borrowings.

Since borrow_book prints the borrowing IDs but doesn't return them in a way that can be directly used for validation, you'll need to slightly adjust your approach to collect those IDs into a list for validation. Here's how you can do it:

Modify the borrow_book function to return a list of valid borrowing IDs.
Use this list in your returning_a_book function to validate the user input.



[AI Prompt 6] INPUT:
why does it ask for review even after the book has been returned?

```python
new_book = borrow_book(member)
    if not new_book:  
        return


    while True:
        bid = int(input("Enter the Borrowing ID of the book you are returning: "))
        if bid in new_book:
            if return_and_penalty(bid, member):
                ask_review = input("Would you like to write a review and add a rating for this book? (yes/no) ")
                if ask_review.lower() == "yes":
                    add_review(bid, member)
                # After processing the return and optional review, ask if the user wants to process another book
                    if len(new_book) !=0:
                        another = input("Do you want to return another book? (yes/no) ")
                        if another.lower() != "yes":
                            break  # Exit the loop and function if the user doesn't want to return another book
            else:
                print("Invalid Borrowing ID. Please try again.")
```

OUTPUT:
It appears the program is not tracking which books have been returned within the session, allowing the same borrowing ID to be processed for return more than once. To fix this, you could maintain a list of returned borrowing IDs during the session and check against this list before processing a return. If an ID has already been processed, you should not allow it to be processed again.

```python
new_book = borrow_book(member)
    if not new_book:  
        return

    returned_books = []  # Initialize an empty list to keep track of returned books.

    while True:
        bid = int(input("Enter the Borrowing ID of the book you are returning: "))
        
        # Check if the book has already been returned in this session.
        if bid in returned_books:
            print("This book has already been returned. Please enter a different Borrowing ID.")
            continue  # Skip the rest of the loop and ask for another ID.
```