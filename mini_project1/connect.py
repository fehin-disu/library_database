import sqlite3

def connect(path_input):
    """ 
    This code is based off the lab code provided in eClass
    Returns a connection and a cursor based off the parameter path.
    For testing purposes for now: enter the param as library.db
    May be temporary.
    """
    connection = sqlite3.connect(path_input) # connect to path 
    cursor = connection.cursor() # connect the cursor to connection, allowing SQL queries to be able to do. 
    cursor.execute(' PRAGMA foreign_keys=ON; ')
    connection.commit()
    return connection, cursor