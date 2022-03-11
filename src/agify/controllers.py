from flask import request
import sqlite3 as sql
from sqlite3 import Error
import db
from client import AgifyAPIClient


def get_persons():
    persons = []
    try:
        conn = db.connect_to_db()
        cur = conn.cursor()
        cur.execute("SELECT DISTINCT(name) FROM persons_records ORDER BY count DESC LIMIT 100")
        all_records = cur.fetchall()
        columns = [column[0] for column in cur.description]
        for row in all_records:
            persons.append(dict(zip(columns, row)))
    except:
        persons = []
    return persons


def get_person_by_name(name):
    person = []
    try:
        conn = db.connect_to_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM persons_records WHERE name=?", (name,))
        row = cur.fetchone()
        columns = [column[0] for column in cur.description]
        person.append(dict(zip(columns, row)))
    except:
        person = []
    return person


def add_person(name, age, count):
    output = []
    try:
        conn = db.connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO persons_records (name, age, count) VALUES (?, ?, ?)", (name, age, count))
        conn.commit()
    except Error as e:
        print("Error: ", e)
    last_row = cur.execute('select * from persons_records').fetchall()[-1]
    return last_row


def update_person(person):
    updated_person = []
    try:
        conn = db.connect_to_db()
        cur = conn.cursor()
        cur.execute("UPDATE persons_records SET name=?, age=?, count=? WHERE name=?", (person[0], person[1], person[2]))
        conn.commit()
        # row = cur.execute("SELECT * FROM persons_records WHERE name=?", (person[0],)).fetchone()
        # columns = [column[0] for column in cur.description]
        # updated_person.append(dict(zip(columns, row)))
    except Error as e:
        print("Error: ", e)
    return updated_person


def delete_person(name):
    try:
        conn = db.connect_to_db()
        conn.execute(" DELETE from persons_records WHERE name=?", (name,))
        conn.commit()
        return "Person deleted successfully."
    except Error as e:
        return ("Cannot delete the person. Error: ", e)
    finally:
        conn.close()


if __name__ == '__main__':
    print(update_person(('qqq', 5, 555)))
