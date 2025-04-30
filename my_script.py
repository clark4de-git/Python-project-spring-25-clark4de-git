import argparse
import sqlite3
import re
import sys
from datetime import datetime

DB_FILE = 'todo.db'

def init_db():
    conn = sqlite3.connect(DB_FILE)
    courier = conn.cursor()
    courier.execute('''
        CREATE TABLE IF NOT EXISTS todolist (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            due_date TEXT,
            completed INTEGER DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()



def main():

    init_db()


if __name__ == '__main__':
    main()


