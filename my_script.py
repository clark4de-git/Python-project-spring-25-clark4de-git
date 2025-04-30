import argparse
import sqlite3
import re
import sys
from datetime import datetime

DB_FILE = 'todo.db'

# Creates database and table named todolist if it doesn't exist
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

# This function checks if the due date argument is formatted right
def validate_due_date(date_str):
    if date_str and not re.match('^\d{2}-\d{2}-\d{4}$', date_str):
        print("Error: Due Date must be in DD-MM-YYYY format.")
        sys.exit(1)

# This function is for adding tasks to the todolist which requires a
# task and a due date to be input
def add_task(task, due_date):
    validate_due_date(due_date)
    conn = sqlite3.connect(DB_FILE)
    courier = conn.cursor()
    courier.execute('INSERT INTO todolist (task, due_date) VALUES (?, ?)', (task, due_date))
    conn.commit()
    conn.close()
    print("Task added successfully.")

# This function is for listing out the tasks on the todolist
def list_tasks(due=None, completed=None):
    conn = sqlite3.connect(DB_FILE)
    # This query variable is initialized here so that it can be
    # appended if additional options/args are given in addition to list
    query = 'SELECT * from todolist WHERE 1=1'
    # Variable for appending query
    params = []

    # Optional option due as in due date
    if due:
        validate_due_date(due)
        query += ' AND due_date = ?'
        params.append(due)
    
    # Optional option completed
    if completed is not None:
        query += ' AND completed = ?'
        params.append(int(completed))
    
    # Carries out the execution of the query with or without the optional options
    courier = conn.cursor()
    courier.execute(query, params)
    rows = courier.fetchall()

    # Checks for nothing returned and prints out what is returned based on below format
    if not rows:
        print("No tasks found.")
    for row in rows:
        status = "Completed" if row[3] else " "
        print(f"{row[0]}, [{status}] {row[1]} | Due: {row[2] or 'N/A'} | Created: {row[4]}")
    conn.close()

# This function is for completing task in which the value of
# the completed column becomes 1 rather than 0
def complete_task(task_id):
    conn = sqlite3.connect(DB_FILE)
    courier = conn.cursor()
    courier.execute('UPDATE todolist SET completed = 1 WHERE id ?', (task_id))
    if courier.rowcount == 0:
        print("Error: No task with that ID.")
    else:
        print("Task marked as complete.")
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = sqlite3.connect(DB_FILE)
    courier = conn.cursor()
    courier.execute('DELETE FROM todolist WHERE id = ?', (task_id))
    if courier.rowcount == 0:
        print("Error: No task with that ID.")
    else:
        print("Task deleted.")
    conn.commit()
    conn.close()




def main():

    init_db()


if __name__ == '__main__':
    main()


