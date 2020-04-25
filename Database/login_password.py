import sqlite3
# import cart
from Database import cart


def create_table():
    try:
        conn = sqlite3.connect("Username_database.db")
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE users
            (username text,
            password text)""")
    except:
        pass


create_table()


def register(username, password):
    try:

        conn = sqlite3.connect("Username_database.db")
        if username == '' or password == '':
            return "Fill the blanks"
        cursor = conn.cursor()

        data_tuple = (username, password)

        select_query = """SELECT * FROM users WHERE username = ?"""
        cursor.execute(select_query, (username, ))
        respond = cursor.fetchone()
        if not respond:
            insert_with_param = """INSERT INTO users
                                (username,password)
                                VALUES
                                (?,?)"""
            cursor.execute(insert_with_param, data_tuple)
            conn.commit()
            cart.create_db_for_user(username)
            return "Registration completed successfully"
        else:
            return "This user is already exist"
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to register th new", error)

    finally:
        if (conn):
            conn.close()


# register('elxan', 'elxasdadasds')


def login(username, password):
    try:

        conn = sqlite3.connect('Username_database.db')
        cursor = conn.cursor()

        data_tuple = (username, password)
        select_query = """SELECT * FROM users WHERE username = ? AND password = ?"""
        cursor.execute(select_query, data_tuple)
        respond = cursor.fetchone()
        cursor.close()

    except sqlite3.Error as error:
        print("Fail in logging ", error)

    finally:
        if (conn):
            conn.close()

    if respond:
        return True
    else:
        return False


# print(login('elxan', 'elxan123565eq'))


def search(username):
    try:
        conn = sqlite3.connect("Username_database.db")
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE username = ?"
        cursor.execute(query, (username,))
        return cursor.fetchone()
        cursor.close()

    except sqlite3.Error as error:
        print(error)

    finally:
        if(conn):
            conn.close()


# print(search("elxan"))
