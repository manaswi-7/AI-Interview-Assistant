import sqlite3

def create_table():

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS interview_results(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        question TEXT,
        score INTEGER,
        feedback TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_result(date, question, score, feedback):

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO interview_results
        (date, question, score, feedback)
        VALUES (?, ?, ?, ?)
        """,
        (date, question, score, feedback)
    )

    conn.commit()
    conn.close()