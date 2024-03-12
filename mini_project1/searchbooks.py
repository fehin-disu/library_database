import sqlite3

# Connect to the database
conn = sqlite3.connect('library.db')
# Create a cursor object
cursor = conn.cursor()

# Search for books
def search_books(keyword):
    keyword = f"%{keyword}%" # prepares the keyword for use in SQL LIKE clause, allows for partial matching of the keyword
    cursor.execute("""
                   SELECT book_id, title, author, pyear, COALESCE(avg_rating, 0) AS avg_rating, CASE WHEN EXISTS (SELECT 1 FROM borrowings WHERE book_id=b.book_id AND end_date IS NULL) THEN 'On Borrow' ELSE 'Available' END AS status
                   FROM books b
                   LEFT JOIN (
                        SELECT book_id, AVG(rating) AS avg_rating 
                        FROM reviews   
                        GROUP BY book_id
                   ) r ON b.book_id = r.book_id
                   WHERE title LIKE ? OR author LIKE ?  #filters the books based on the keyword, matching is against the title or author felds 
                   ORDER BY  # orders result in following order: 
                        CASE WHEN title LIKE ? THEN 1 ELSE 0 END, # if title matches the keyword, it sorts by the title in ascending order
                        CASE WHEN title LIKE ? THEN title ELSE author END # if author matches the keyword, it sorts by the author's name in ascending order
                   LIMIT 5;
                   """, (keyword, keyword, keyword, keyword))
    books = cursor.fetchall() # fetches the result of the query
    if not books:
        print("No books found.") # if no books were found 
        return
    print("Search results:")
    for book in books:
        print(f"Book ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}, Average Rating: {book[4]}, Status: {book[5]}")
    
    borrow_book_id = input("Enter book ID to borrow (or press Enter to skip): ")
    if borrow_book_id:
        borrow_book_id(email, int(borrow_book_id))


conn.close()
