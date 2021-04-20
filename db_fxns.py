import sqlite3

conn = sqlite3.connect("data.db")

c = conn.cursor()


#Database
#Table
#Field/Columns
#DataType

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS tasktable(task TEXT,task_status TEXT,task_due_date DATE)')

def add_data(task,task_status,task_due_date):
    c.execute('INSERT INTO tasktable(task,task_status,task_due_date) VALUES (?,?,?)',(task,task_status,task_due_date))
    conn.commit()

def view_all_data():
    c.execute('SELECT * FROM tasktable')
    data = c.fetchall()
    return data

def view_unique_tasks():
    c.execute('SELECT DISTINCT task FROM tasktable')
    data = c.fetchall()
    return data

def get_task(task):
    c.execute('SELECT * FROM tasktable WHERE task="{}"'.format(task))
    data = c.fetchall()
    return data

