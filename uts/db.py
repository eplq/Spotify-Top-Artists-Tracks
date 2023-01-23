import sqlite3
from dotenv import dotenv_values

env = dotenv_values()

connection = sqlite3.connect(env["DATABASE"], check_same_thread=False)

def get_cursor() -> sqlite3.Cursor:
    cursor = connection.cursor()
    cursor.row_factory = sqlite3.Row

    return cursor

def commit():
    connection.commit()

def setup():
    cursor = get_cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, user TEXT, access_token TEXT, expires_in INTEGER, cookie TEXT)""")

    connection.commit()
