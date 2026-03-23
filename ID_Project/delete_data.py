import sqlite3

conn = sqlite3.connect("student_data.db")

cursor = conn.cursor()

cursor.execute("DELETE FROM students")

conn.commit()

print("All records deleted successfully")

conn.close()