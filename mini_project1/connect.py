import sqlite3


def connect(path):
    """ 
    This code is based off the lab code provided in eClass
    Returns a connection and a cursor based off the parameter path.
    For testing purposes for now: enter the param as library.db
    """
    global connection, cursor

    connection = sqlite3.connect(path) # connect to path 
    cursor = connection.cursor() # connect the cursor to connection, allowing SQL queries to be able to do. 
    cursor.execute(' PRAGMA forteign_keys=ON; ')
    connection.commit()
    return connection, cursor