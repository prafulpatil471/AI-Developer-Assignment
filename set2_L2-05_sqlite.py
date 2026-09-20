import sqlite3

conn = sqlite3.connect("set2_L2-05.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS TableA (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    info TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS TableB (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    value REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS TableC (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    status TEXT
)
""")

if cursor.execute("SELECT COUNT(*) FROM TableA").fetchone()[0] == 0:
    cursor.execute("INSERT INTO TableA (name, info) VALUES ('Sample A', 'Info A')")

if cursor.execute("SELECT COUNT(*) FROM TableB").fetchone()[0] == 0:
    cursor.execute("INSERT INTO TableB (category, value) VALUES ('Category B', 123.45)")

if cursor.execute("SELECT COUNT(*) FROM TableC").fetchone()[0] == 0:
    cursor.execute("INSERT INTO TableC (description, status) VALUES ('Task C', 'Active')")

conn.commit()

print("All TableA rows:")
for row in cursor.execute("SELECT * FROM TableA"):
    print(row)

print("\nAll TableB rows:")
for row in cursor.execute("SELECT * FROM TableB"):
    print(row)

print("\nAll TableC rows:")
for row in cursor.execute("SELECT * FROM TableC"):
    print(row)

conn.close()

