import sqlite3

# Connecting to the database
conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

# Creating the `articles` table if it doesn't already exist
cursor.execute("CREATE TABLE IF NOT EXISTS articles (id INTEGER PRIMARY KEY, title TEXT, content TEXT, author TEXT)")

# SQL query to insert a record into the `articles` table
insert_query = "INSERT INTO articles (title, content, author) VALUES (?, ?, ?)"

article_data = ("Python Coding", "Python is a high-level, general-purpose programming language.", "John Doe")
# Execute the SQL query with data
cursor.execute(insert_query, article_data)

conn.commit()  # save the changes
conn.close()  # close the connection