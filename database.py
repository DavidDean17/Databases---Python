import sqlite3 

# connect to database
conn = sqlite3.connect('customer.db')

# create cursor
c = conn.cursor()

# create table
c.execute("SELECT * FROM customers")

# print(c.fetchone()[0])
# print(c.fetchmany(3))

items = c.fetchall()

print("NAME " + "\tLAST NAME " + "\tEMAIL ")
print("-----" + "\t----------" + "\t----------")
for item in items:
    print(item[0] + "\t" + item[1] + "\t\t" + item[2])
# NULL
# INTEGER
# REALS
# TEXT
# BLOB

print("Command executed successfully...")

# commit command
conn.commit()

# close connection 
conn.close()
