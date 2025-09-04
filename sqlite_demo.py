import sqlite3

# Connect to database (creates file if it doesn’t exist)
conn = sqlite3.connect("test.db")

# Create a cursor to execute SQL commands
cursor = conn.cursor()
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
)
"""
)
cursor.execute(
    "INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
    ("Lily", 25, "lily@example.com"),
)

cursor.execute(
    "INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
    ("Love", 30, "love@example.com"),
)

# Commit changes (very important!)
conn.commit()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.execute("UPDATE users SET age = ? WHERE name = ?", (26, "Alice"))
cursor.execute("DELETE FROM users WHERE name = ?", ("Bob",))
conn.commit()

conn.close()
