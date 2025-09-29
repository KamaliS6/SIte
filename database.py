# database.py
import sqlite3
from datetime import datetime

DB_NAME = 'portfolio.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Comments table: name, email, content, timestamp
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            content TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

def add_comment(name, email, content):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO comments (name, email, content) VALUES (?, ?, ?)',
        (name, email, content)
    )
    conn.commit()
    conn.close()

def get_all_comments():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT name, email, content, timestamp
        FROM comments
        ORDER BY timestamp DESC
    ''')
    comments = cursor.fetchall()
    conn.close()
    return comments

print("database created successfully")