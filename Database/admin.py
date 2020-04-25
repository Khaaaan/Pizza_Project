# import cart
# import login_password
import sqlite3
from Database import cart
from Database import login_password


def createDb():
    try:
        conn = sqlite3.connect('Pizzas.db')
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE  pizzas
            (name text,
            status text,
            price INTEGER)""")
        conn.commit()
        cursor.close()

    except sqlite3.Error as error:
        pass

    finally:
        if (conn):
            conn.close()


createDb()


def search(username):
    user_info = login_password.search(username)
    purchase_info = car.search(username)


def add(name, status, price):
    try:
        conn = sqlite3.connect('Pizzas.db')
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM pizzas WHERE name = ?""", (name,))
        respond = cursor.fetchone()
        if not respond and name != 'Pepperoni' and name != "Margherita":
            insert_query = """INSERT INTO pizzas
                            (name,status,price)
                            VALUES
                            (?,?,?)"""

            cursor.execute(insert_query, (name, status, price))
            conn.commit()
            myfile = open("Database/notifications.txt", "w+")
            myfile.write(f"{name} is now awailable!!!")
            myfile.close()
            return "This pizza added succesfully!"
        else:
            return "This pizza is already exists"
        cursor.close()

    except sqlite3.Error as error:
        print(error)

    finally:
        if(conn):
            conn.close()


def get_one(name):
    try:
        conn = sqlite3.connect("Pizzas.db")
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM pizzas WHERE name = ?""", (name,))
        return cursor.fetchone()

        cursor.close()

    except sqlite3.Error as error:
        print(error)

    finally:
        if (conn):
            conn.close()


# print(get_one("neyse"))

def get_all():
    try:
        conn = sqlite3.connect("Pizzas.db")
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM pizzas """)
        return cursor.fetchall()

        cursor.close()

    except sqlite3.Error as error:
        print(error)

    finally:
        if (conn):
            conn.close()


# print(get_all())
