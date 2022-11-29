import sqlite3


def create_connection():
    connection = sqlite3.connect("databases/login.db")

    return connection
