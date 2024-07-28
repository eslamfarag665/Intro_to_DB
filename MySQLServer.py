import mysql.connector
from mysql.connector import errorcode

def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
        exit(1)

def main():
    try:
        cnx = mysql.connector.connect(
            user='your_username',  # replace with your MySQL username
            password='your_password',  # replace with your MySQL password
            host='localhost'  # replace with your MySQL server host if different
        )
        cursor = cnx.cursor()
        create_database(cursor)
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursor.close()
        cnx.close()

if __name__ == "__main__":
    main()
