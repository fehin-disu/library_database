import sqlite3
from login import login
from datetime import date, timedelta

conn = sqlite3.connect('library.db')
c= conn.cursor()

# Search for books
def search_books(email,keyword, page=1):
    keyword = f"%{keyword}%" # prepares the keyword for use in SQL LIKE clause, allows for partial matching of the keyword

    offset = (page - 1) * 5 # calculates the offset for pagination, first page will be offset 0
    c.execute("""
                   SELECT book_id, title, author, pyear, COALESCE(avg_rating, 0) AS avg_rating, CASE WHEN EXISTS (SELECT 1 FROM borrowings WHERE book_id=b.book_id AND end_date IS NULL) THEN 'On Borrow' ELSE 'Available' END AS status
                   FROM books b
                   LEFT JOIN (
                        SELECT book_id, AVG(rating) AS avg_rating 
                        FROM reviews   
                        GROUP BY book_id
                   ) r ON b.book_id = r.book_id
                   WHERE title LIKE ? OR author LIKE ?  /* filters the books based on the keyword, matching is against the title or author felds /**/
                   ORDER BY  # orders result in following order: 
                        CASE WHEN title LIKE ? THEN 1 ELSE 0 END, # if title matches the keyword, it sorts by the title in ascending order
                        CASE WHEN title LIKE ? THEN title ELSE author END # if author matches the keyword, it sorts by the author's name in ascending order
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
            borrow_book_id(email,int(borrow_book_id))
    elif show_more == '':
        search_books(keyword, page + 1)

# Borrow a book 
def borrow_book_id(email, book_id):
    c.execute("""
                SELECT COUNT(*) FROM borrowings WHERE book_id = ? AND end_date IS NULL""", (book_id,))
    if c.fetchone()[0] > 0:
        print("Book already borrowed.")
        return
    c.execute("""
                INSERT INTO borrowings (email, book_id, start_date) VALUES (?, ?, ?)""", (email, book_id, date.today())
                )
    conn.commit()
    print("Book borrowed successfully.")


