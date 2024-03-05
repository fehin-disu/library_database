import sqlite3
conn = sqlite3.connect('custmer.db')
c= conn.cursor()
c.execute("""
SELECT borrowings.member, p.pid, SUM (CASE WHEN p.paid_amount >= p.amount THEN 1 ELSE 0 END) AS paid_amount, SUM (CASE WHEN p.paid_amount >= p.amount THEN p.paid_amount ELSE 0 END) AS paid_penalties
FROM penalties AS p
WHERE borrowings.member = email AND 
LEFT JOIN borrowings on p.bid = borrowings.bid
GROUP BY borrowings.member;""")