import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()
    
# Create the `users` table with fields
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, user_name TEXT, email TEXT, password TEXT)")

# Insert a records into the `users` table
cursor.execute("INSERT INTO users (id, user_name, email, password) VALUES (?, ?, ?, ?)", (1, "Alex", "AlexMain@gmail.com", "ZXCV2000"))
cursor.execute("INSERT INTO users (id, user_name, email, password) VALUES (?, ?, ?, ?)", (2, "Jamie", "Jamie123@gmail.com", "ASDF3000"))

# Delete the record
query = "DELETE FROM users WHERE id = 1"
cursor.execute(query)
    
# Execute select query
select_query = "SELECT * FROM users"
cursor.execute(select_query)
    
# Output
data = cursor.fetchall()
print(data)
    
# Save changes and close the connection
conn.commit()
conn.close()