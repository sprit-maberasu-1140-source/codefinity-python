import sqlite3

conn = sqlite3.connect("cars_info.db")
cursor = conn.cursor()
    
# Create a table named `cars` with the specified fields and data types
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cars (
        id INTEGER PRIMARY KEY,
        brand TEXT,
        engine_capacity REAL,
        video_presentation BLOB
    )
''')
conn.commit()  # save the changes
conn.close()  # close the database connection