import sqlite3
# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users
(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
# Insert a record
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice',
30))
# Commit the changes
conn.commit()
# Query the database
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
   print(row)

#Error handling
try:
    cursor.execute("SELECT * FROM non_existing_table")
except sqlite3.OperationalError as e:
    print(f"An error occurred: {e}")
  
#using parameters for SQL queries
name = "Bob"
grade = "92.3"
ursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", (name, grade))

rows = cursor.fetchall()
for row in rows:
    print(row)
  
#rollback
try:
     cursor.execute("BEGIN")
     cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ('Bob', 92.0))
     cursor.execute("UPDATE students SET grade = ? WHERE name = ?", (90.0, 'Alice'))
    
     connection.commit()
except sqlite3.Error as e:
     connection.rollback()
     print(f"An error occurred: {e}")
  
#deleting data
name_to_delete = 'Bob'
# Execute the DELETE command using a parameterized query
cursor.execute("DELETE FROM students WHERE name = ?", (name_to_delete,))

# Commit the changes to ensure the deletion is saved
connection.commit()
print(f"Deleted student with name {name_to_delete}")

# Close the connection
conn.close()
