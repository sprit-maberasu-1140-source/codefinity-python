import sqlite3

conn = sqlite3.connect('mydatabase.db')  # create the database 
cursor = conn.cursor()

# Create the `users` table with fields
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, user_name TEXT, email TEXT, password TEXT)")

# Insert a record into the `users` table
cursor.execute(
    "INSERT INTO users (id, user_name, email, password) VALUES (?, ?, ?, ?)",
    (1, "Alex", "AlexMain@gmail.com", "ZXCV2000")
)

# Update the record where email is 'new@gmail.com'
query = "UPDATE users SET id = 1 WHERE email = 'new@gmail.com'"
cursor.execute(query)

# Execute select query to verify update
cursor.execute("SELECT * FROM users")
data = cursor.fetchall()
print(data)

conn.commit()  # save changes 
conn.close()  # close the connection