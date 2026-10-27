
import sqlite3
from pathlib import Path

# Connect to the database
connection = sqlite3.connect("student.db")

# Read the SQL file
sql_file = Path(__file__).with_name("student.sql")
sql_code = sql_file.read_text(encoding="utf-8")

# Execute the SQL commands
connection.executescript(sql_code)

# Get student records from the database
cursor = connection.execute("SELECT * FROM students")

# Display the records
print("Student Management System")

for student in cursor.fetchall():
    print(student)

# Close the database connection
connection.close()
