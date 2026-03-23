import sqlite3


def save_to_database(data):

    conn = sqlite3.connect("student_data.db")

    cursor = conn.cursor()


    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        student_name TEXT,

        register_number TEXT UNIQUE,

        batch_number TEXT,

        department TEXT,

        academic_year TEXT,

        college_name TEXT

    )
    """)


    
    cursor.execute(

        "SELECT * FROM students WHERE register_number=?",

        (data["register_number"],)

    )

    existing = cursor.fetchone()


    if existing:

        print("\n⚠ Student already exists in database")

        print("Register Number:", data["register_number"])

        conn.close()

        return False


    
    cursor.execute("""

        INSERT INTO students (

            student_name,

            register_number,

            batch_number,

            department,

            academic_year,

            college_name

        )

        VALUES (?, ?, ?, ?, ?, ?)

    """,

    (

        data["student_name"],

        data["register_number"],

        data["batch_number"],

        data["department"],

        data["academic_year"],

        data["college_name"]

    ))


    conn.commit()

    conn.close()


    print("\n✅ New student saved successfully")

    return True