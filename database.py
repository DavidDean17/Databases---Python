import sqlite3 

# connect to database
conn = sqlite3.connect('customer.db')

# create cursor
c = conn.cursor()

# order by
c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 2")

# print(c.fetchone()[0])
# print(c.fetchmany(3))

items = c.fetchall()

for item in items:
    print(item)

# Types  
    # NULL
    # INTEGER
    # REALS
    # TEXT
    # BLOB


# commit command
conn.commit()

# close connection 
conn.close()
