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

--- 

## Fehintola's use of AI
=======
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
>>>>>>> e704517143eb8cd9021bc3eb37096e1f200a6a28
=======
>>>>>>> e704517143eb8cd9021bc3eb37096e1f200a6a28

--- 
## Samia's use of AI

