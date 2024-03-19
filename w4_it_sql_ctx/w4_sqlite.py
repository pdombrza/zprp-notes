import sqlite3

conn = sqlite3.connect("demo.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Charlie", 22))
conn.commit()
conn.close()

with sqlite3.connect("demo.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")


# baza danych w pamięci

con = sqlite3.connect(":memory")
cur = con.execute("CREATE TABLE lang(name, first_appeared)")

data = (
    {"name": "C", "year": 1972},
    {"name": "Fortran", "year": 1957}
)