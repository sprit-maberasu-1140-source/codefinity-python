import sqlite3

conn = sqlite3.connect("my_database.db")  # create a new database 
cursor = conn.cursor()  # create a cursor

# Create a table named `articles` with the specified fields
cursor.execute('''
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER,
        title TEXT,
        content TEXT,
        author TEXT
    )
''')
conn.commit()  # save the changes
conn.close()  # close the database connection