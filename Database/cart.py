import sqlite3
import datetime


def create_db_for_user(username):
    try:
        conn = sqlite3.connect('Cart.db')

        cursor = conn.cursor()
        create_query = f"CREATE TABLE {username} (pizza text, price REAL, time timestamp)"
        cursor.execute(create_query)
        conn.commit()
        cursor.close()
    except sqlite3.Error as error:
        print(error)

    finally:
        if (conn):
            conn.close()


def confirm(array, price, username):
    string = ''
    for pizza in array:
        string += pizza.get_status() + '\n'
    try:
        conn = sqlite3.connect('Cart.db')
        cursor = conn.cursor()

        insert_query = f"INSERT INTO {username} (pizza,price,time) VALUES (?,?,?)"
        time = datetime.datetime.now()
        cursor.execute(insert_query, (string, price, time))
        conn.commit()
        cursor.close()

    except sqlite3.Error as error:
        print(error)

    finally:
        if (conn):
            conn.close()


def read_all(username):
    try:
        conn = sqlite3.connect('Cart.db')
        cursor = conn.cursor()

        select_query = f"SELECT * FROM {username}"
        cursor.execute(select_query)
        return cursor.fetchall()
        cursor.close()

    except sqlite3.Error as error:
        print(error)

    finally:
        if (conn):
            conn.close()


def search(username):
    try:
        conn = sqlite3.connect("Cart.db")
        cursor = conn.cursor()

        query = f"SELECT * FROM {username}"
        cursor.execute(query)
        return cursor.fetchall()
        cursor.close()

    except sqlite3.Error as error:
        print(error)

    finally:
        if(conn):
            conn.close()


# print(search('ali')[0][0])
