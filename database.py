import sqlite3
conn=sqlite3.connect("ExpenseTracker.db")

print("opened database successfully!")
try:
    conn.execute("""CREATE TABLE IF NOT EXISTS Expense
    (username CHAR(10)  NOT NULL,
    item CHAR(20) NOT NULL,
    tag TEXT NOT NULL,
    type TEXT NOT NULL,
    amount INT ,
    edate CHAR(10)
    );""")
except:
    print()

print("Table created successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS User
    (
    username CHAR(20) NOT NULL,
    passwrod CHAR(20) NOT NULL,
    budget INT NOT NULL
    );''')
print("Table created successfully")

try:
    conn.execute('''CREATE TABLE IF NOT EXISTS Budget
    (
    username CHAR(20) NOT NULL,
    item CHAR(20) NOT NULL,
    lim INT
    );''')

except:
    print()

print("Table created successfully")


li=[['adi','pizza','others','expense',200,'2021/11/03'],
['adi','movie','entertainment','expense',300,'2021/11/22'],
['adi','old age','pension','income',1000,'2021/11/25'],
['adi','bill','utilities','expense',500,'2021/10/02'],
['adi','diwali','gift income','income',500,'2021/10/02'],
['adi','salary','salary','income',10000,'2021/09/01'],
['adi','child edu','Education','expense',5000,'2021/09/01'],
['adi','bonus','bonus','income',2000,'2021/08/28'],
['adi','other','others','expense',1000,'2021/08/28']]

for i in li:
    conn.execute("""INSERT INTO Expense VALUES(?,?,?,?,?,?);""",i)
print("data entry successful!")
conn.commit()
print("now showing the data: ")

conn.execute("""INSERT INTO User VALUES('adi','123',10000)""")
conn.commit()

conn.execute("INSERT INTO Budget VALUES('adi','movie',1000)")
conn.commit()