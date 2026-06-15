import sqlite3

conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

# Create the `users` table if it doesn't already exist
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, user_name TEXT, email TEXT, password TEXT)")

# Insert a record into the `users` table
cursor.execute("INSERT INTO users (id, user_name, email, password) VALUES (?, ?, ?, ?)", (1, "Alex", "AlexMain@gmail.com", "ZXCV2000"))

# Fetch all records where `user_name` is `Alex`
cursor.execute("SELECT * FROM users WHERE user_name = 'Alex'")
data = cursor.fetchall()

print(data)  # print the fetched data

conn.commit()  # commit the changes
conn.close()  # close the connection