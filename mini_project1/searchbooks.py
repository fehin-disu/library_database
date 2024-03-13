import sqlite3
from login import login
from datetime import date, timedelta
from connect import connect



# Search for books
def search_books(email,keyword,path_input, page=1):
    keyword = f"%{keyword}%" # prepares the keyword for use in SQL LIKE clause, allows for partial matching of the keyword

    conn, c = connect(path_input)

    offset = (page - 1) * 5 # calculates the offset for pagination, first page will be offset 0
    c.execute("""
                   SELECT b.book_id, b.title, b.author, b.pyear, COALESCE(r.avg_rating, 0) AS avg_rating, CASE WHEN EXISTS (SELECT 1 FROM borrowings WHERE book_id=b.book_id AND end_date IS NULL) THEN 'On Borrow' ELSE 'Available' END AS status
                   FROM books b
                   LEFT JOIN (
                        SELECT book_id, AVG(rating) AS avg_rating 
                        FROM reviews   
                        GROUP BY book_id
                   ) r ON b.book_id = r.book_id
                   WHERE b.title LIKE ? OR b.author LIKE ?  /* filters the books based on the keyword, matching is against the title or author felds */
                   ORDER BY  /*orders result in following order: */
                        CASE WHEN b.title LIKE ? THEN 1 ELSE 0 END, /*if title matches the keyword, it sorts by the title in ascending order */
                        CASE WHEN b.title LIKE ? THEN b.title ELSE b.author END /* if author matches the keyword, it sorts by the author's name in ascending order */
                   LIMIT 5 OFFSET ?;
                   """, (keyword, keyword, keyword, keyword, offset))
    books = c.fetchall() # fetches the result of the query
    if not books:
        print("No books found.") # if no books were found 
        return
    print("Search results: (Page {page}): ")
    for book in books:
        print(f"Book ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}, Average Rating: {book[4]}, Status: {book[5]}")
    
    show_more = input("Press Enter to show more results, or type 'b' to borrow a book: ").lower()
    if show_more == 'b':
        borrow_book_id = input("Enter the book ID you want to borrow: ")
        if borrow_book_id:
            borrow_book_id(email,int(borrow_book_id),path_input)
    elif show_more == '':
        search_books(keyword, page + 1)
    
    conn.close()

# Borrow a book 
def borrow_book_id(email, book_id,path_input):
    conn, c = connect(path_input)
    c.execute("""
                SELECT COUNT(*) FROM borrowings WHERE book_id = ? AND end_date IS NULL""", (book_id,))
    if c.fetchone()[0] > 0:
        print("Book already borrowed.")
        return
    c.execute("""
                INSERT INTO borrowings (email, book_id, start_date) VALUES (?, ?, ?)""", (email, book_id, date.today())
                )
    c.commit()
    print("Book borrowed successfully.")


