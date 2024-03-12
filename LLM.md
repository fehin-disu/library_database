# More detail of any AI tool used, including the name, URL, all the input given and all the output received.  

--- 
## Elykah's use of AI 

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

--- 

## Fehintola's use of AI

--- 
## Samia's use of AI

