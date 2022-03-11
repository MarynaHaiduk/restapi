import sqlite3 as sql
from sqlite3 import Error
from client import AgifyAPIClient
from initial_data import list_of_names

DATABASE = "persons_table.db"


def connect_to_db():
    try:
        conn = sql.connect(DATABASE)
        print("Connected to DB successfully.")
    except Error as e:
        print("Connection to DB failed. Error: ", e)
    return conn


def create_agify_db_table():
    try:
        conn = connect_to_db()
        conn.execute("""CREATE TABLE if NOT EXISTS persons_records 
        (id INTEGER PRIMARY KEY NOT NULL, name TEXT, age INTEGER, count INTEGER)""")
        conn.commit()
        print("The table created successfully.")
    except Error as e:
        print("The table creation failed. Error: ", e)
    finally:
        conn.close()


def initialize_agify_db():
    try:
        conn = connect_to_db()
        agify_client = AgifyAPIClient()
        for name in list_of_names:
            person = agify_client.fetch(name)
            values = (person.name, person.age, person.count)
            conn.execute("INSERT INTO persons_records (name, age, count) VALUES (?,?,?)", values)
            conn.commit()
    except Error as e:
        print("Failed to add record to database. Error:", e)
    finally:
        conn.close()

